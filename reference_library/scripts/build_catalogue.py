#!/usr/bin/env python3
"""Build a source-page catalogue. Does not mark scraped images as accepted."""
import csv, json, re, time
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "catalog"
OUT.mkdir(parents=True, exist_ok=True)
BASES = {
    "monsters": "https://classicconqueronline.net/monsters/",
    "npcs": "https://classicconqueronline.net/npcs/",
    "items": "https://classicconqueronline.net/items/",
}
S = requests.Session()
S.headers.update({"User-Agent": "ConquerReferenceLibraryResearch/1.0 (public catalog indexing)"})

def get(url):
    r = S.get(url, timeout=30)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")

def scrape_index(kind, url):
    soup = get(url)
    records = []
    for a in soup.select("a[href]"):
        href = urljoin(url, a.get("href", ""))
        name = " ".join(a.get_text(" ", strip=True).split())
        if not name or urlparse(href).netloc != urlparse(url).netloc:
            continue
        if kind == "monsters" and "/monsters/" in urlparse(href).path and href.rstrip("/") != url.rstrip("/"):
            records.append({"category":kind,"name":name,"detail_url":href,"source_index":url,"status":"catalogued"})
        elif kind == "npcs" and "/npcs/" in urlparse(href).path and href.rstrip("/") != url.rstrip("/"):
            records.append({"category":kind,"name":name,"detail_url":href,"source_index":url,"status":"catalogued"})
        elif kind == "items" and "/items/" in urlparse(href).path and href.rstrip("/") != url.rstrip("/"):
            records.append({"category":"item_category","name":name,"detail_url":href,"source_index":url,"status":"catalogued"})
    # Deduplicate without losing order.
    seen=set(); out=[]
    for x in records:
        k=(x["category"],x["name"],x["detail_url"])
        if k not in seen: seen.add(k); out.append(x)
    return out

all_records=[]
for kind,url in BASES.items():
    try:
        rows=scrape_index(kind,url)
        all_records.extend(rows)
        print(f"{kind}: {len(rows)} linked records")
    except Exception as e:
        print(f"WARNING {kind}: {e}")

with (OUT/"source_page_catalog.csv").open("w",newline="",encoding="utf-8-sig") as f:
    fields=["category","name","detail_url","source_index","status"]
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(all_records)

(OUT/"source_page_catalog.json").write_text(json.dumps(all_records,ensure_ascii=False,indent=2),encoding="utf-8")
summary={"records":len(all_records),"categories":{},"policy":"catalogue only; no image accepted without visual review"}
for r in all_records: summary["categories"][r["category"]]=summary["categories"].get(r["category"],0)+1
(OUT/"summary.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(summary,ensure_ascii=False))
