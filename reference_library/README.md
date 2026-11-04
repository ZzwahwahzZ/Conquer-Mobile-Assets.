# Conquer reference library

This library is a research and quality-control workspace for building a large, individually indexed visual reference set for 3D reconstruction.

## Non-negotiable acceptance rules

- One asset per image. No inventory screens, collages, banners, UI screenshots, or tiny icons as accepted 3D inputs.
- Keep the exact source URL and the game's version/variant when known.
- Record image dimensions, background/occlusion, full-object visibility, view angle, and visual quality.
- Status values: `catalogued`, `candidate`, `needs_review`, `accepted_3d_input`, `rejected`.
- A catalog entry is not an image, and a page containing a 3D viewer is not automatically a downloadable model.
- Do not mix classic PC assets with Conquer Online Mobile assets without an explicit visual-match check.
- Preserve the original 42-image set unchanged as historical input.

## Planned folders

- `catalog/`: names and source records for every known character, NPC, monster, boss, weapon, armor, accessory, mount, map and environment prop.
- `images/characters/`
- `images/npcs/`
- `images/monsters/`
- `images/bosses/`
- `images/weapons/`
- `images/armor/`
- `images/accessories/`
- `images/mounts/`
- `images/maps/`
- `images/environment/`
- `previews/`: contact sheets and image-quality reports.

## Initial research sources (community / archive; not the official game site)

1. Classic Conquer community database — 177 monster records: https://classicconqueronline.net/monsters/
2. Classic Conquer community database — 167 NPC records: https://classicconqueronline.net/npcs/
3. Classic Conquer community item index: https://classicconqueronline.net/items/
4. Conquer Online Development Wiki — documents client data formats including Monster.dat, Npc.ini, ItemType.dat, mounttype.dat and GameMap.dat: https://conquer-online.github.io/wiki/files/content/itemtype.dat.html
5. TQ Digital Games Archive — historical client/patch preservation index: https://tqarchive.org/
6. Nox community project — modern 3D Conquer-style monsters, NPCs, mounts and garments; use only as visual comparison, not assumed to match Mobile: https://noxconquest.com/

## Important scope note

The current sources provide useful catalogues and some 3D-viewer pages, but they do not prove that every Conquer Online Mobile asset has an individually downloadable, clean, high-resolution image. Items must remain marked as candidates until the actual image is inspected. No fabricated "complete" count is allowed.
