"""Generate data/irons_spellbooks/pe_custom_conversions/irons_spellbooks_emc.json.

Iron's Spells 'n Spellbooks uses fluid-based custom recipes (alchemist_cauldron)
that don't map to item->item conversions, so this just seeds the stateless root
materials and lets ProjectE auto-derive the rest from vanilla recipes (93 shaped,
44 shapeless, 38 smithing, blasting). Stateful gear is intentionally left out.

ProjectE NSS schema (1.21.1): values.before = list of {type,emc_value,id}; tags use
{type:"projecte:item","tag":...}. See PROJECTE_EMC_NOTES.md.
"""

import json
import os

OUT = os.path.join(
    os.path.dirname(__file__),
    "..",
    "src",
    "main",
    "resources",
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
    "raw_mithril": 384,  # mithril ore drop; anchors scrap->ingot->weave chain
    "pyrium_ingot": 65536,  # end-game; blasts into 5 ancient_debris -> must exceed 5x debris (~61k) to block an EMC dupe
    "cinder_essence": 1024,  # fire essence
    "hogskin": 256,  # hide material
    "dragonskin": 4096,  # rare hide
    "divine_pearl": 2048,  # upgraded ender_pearl (1024)
    "divine_soulshard": 4096,
    "energized_core": 2048,
    "permafrost_shard": 1024,
}


def main() -> None:
    doc = {
        "replace": False,
        "comment": (
            "Iron's Spells 'n Spellbooks EMC integration for ProjectE (KURONAMI). "
            "Stateless root materials only; vanilla recipes derive the rest. "
            "Spellbooks/scrolls/weapons/armor/upgrade-orbs/maps intentionally have no EMC. "
            "Fluid-based ink/elixir items are deferred (cauldron recipes are fluid-gated)."
        ),
        "values": {
            "before": [
                {"type": "projecte:item", "emc_value": v, "id": f"irons_spellbooks:{k}"}
                for k, v in BEFORE.items()
            ]
        },
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(doc, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"primitives={len(BEFORE)} -> {os.path.normpath(OUT)}")


if __name__ == "__main__":
    main()
