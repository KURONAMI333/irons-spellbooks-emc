"""Generate data/irons_spellbooks/pe_custom_conversions/irons_spellbooks_emc.json
for ProjectE on Minecraft 1.20.1 (PE1.0.1).

Same EMC content as the 1.21.1 sibling except for arcane_salvage, which 1.20.1 registers
and 1.21.1 does not (1.21.1 ships the assets but not the registration, so a value there only
produces a load error). ProjectE 1.20.1's CustomConversionFile
reads `values.before` as a MAP ({id: emc}), not the array-of-objects form used by
ProjectE 1.21.1 (PE1.1.0). This generator emits the 1.20.1 map shape, grounded on
ProjectE-1.20.1-PE1.0.1.jar's own bundled defaults.json / metals.json.

All ids below were confirmed present in irons_spellbooks-1.20.1 (lang en_us.json).

Usage: python tools/generate_emc.py
"""

import json
import os

OUT = os.path.join(
    os.path.dirname(__file__),
    "..",
    "src",
    "data",
    "irons_spellbooks",
    "pe_custom_conversions",
    "irons_spellbooks_emc.json",
)

# Hand-set EMC for stateless root materials (P2; anchored on ProjectE scale:
# iron 256, gold 2048, diamond 8192, ender_pearl 1024, netherite_scrap 12288).
BEFORE = {
    "arcane_essence": 256,  # central crafting essence (loot/mob); many recipes consume it
    "arcane_salvage": 512,  # rarer salvage material
    # raw_mithril is in the raw_materials tag, which ProjectE forces to 0, so the
    # chain is anchored one step downstream instead (blasting is 1:1, same value).
    "mithril_scrap": 384,  # anchors scrap->ingot->weave; rings/talismans consume it directly
    "pyrium_ingot": 65536,  # end-game; blasts into 5 ancient_debris -> must exceed 5x debris (~61k) to block an EMC dupe
    "cinder_essence": 1024,  # fire essence
    "hogskin": 256,  # hide material
    "dragonskin": 4096,  # rare hide
    "divine_pearl": 2048,  # upgraded ender_pearl (1024)
    "divine_soulshard": 4096,
    "energized_core": 2048,
    "permafrost_shard": 1024,
    "common_ink": 64,  # loot-only root (chest loot / wandering traders); no recipe
    "uncommon_ink": 256,  # cauldron ladder tier 1, fixed 4:1 above common; bottle return factored in
    "rare_ink": 1024,  # cauldron ladder tier 2, fixed 4:1 above uncommon; bottle return factored in
    "epic_ink": 4096,  # cauldron ladder tier 3, fixed 4:1 above rare; bottle return factored in
    "legendary_ink": 16384,  # cauldron ladder tier 4, fixed 4:1 above epic; bottle return factored in
}


def main() -> None:
    doc = {
        "comment": (
            "Iron's Spells 'n Spellbooks EMC integration for ProjectE (KURONAMI). "
            "Stateless root materials only; vanilla recipes derive the rest. "
            "Spellbooks/scrolls/weapons/armor/upgrade-orbs/maps intentionally have no EMC. "
            "All five ink tiers are valued: common ink has no recipe (chest loot and wandering "
            "traders only), and the alchemist cauldron ladder above it is a fixed four-to-one per "
            "tier, so the tiers are set by hand with the emptied bottles accounted for. Elixirs "
            "stay unvalued: their base fluids are component-carrying potions, "
            "irons_spellbooks:blood has no item source, and the brew ratios differ per recipe."
        ),
        "values": {
            "before": {f"irons_spellbooks:{k}": v for k, v in BEFORE.items()},
        },
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    print(f"primitives={len(BEFORE)} -> {os.path.normpath(OUT)}")


if __name__ == "__main__":
    main()
