# EMC for Iron's Spellbooks

Play [Iron's Spells 'n Spellbooks](https://modrinth.com/mod/irons-spellbooks) with [ProjectE](https://modrinth.com/mod/projecte) and its materials have no EMC value. This data-only add-on fixes that.

- **Hand-tuned EMC** for the core materials — Arcane Essence, Mithril Scrap, Pyrium, Cinder Essence, Hogskin, Dragonskin, Divine Pearl, and the rest.
- Most crafted content (ingots, runes, the smithing-upgrade gear chains) **derives its EMC automatically** from the mod's vanilla-style recipes once the base materials are valued.
- **Pyrium is priced high on purpose** — it converts into ancient debris, so a low value would be an EMC duplication exploit. Mining stays the real path.
- **All five ink tiers are valued** — Common through Legendary. Common Ink has no recipe at all, so it carries a hand-set value; the Alchemist Cauldron ladder above it is a fixed four-to-one per tier, priced so that brewing upward is never an EMC gain.
- **Stateful items carry no EMC by design**: spellbooks, scrolls, weapons, staves, armor, and upgrade orbs all hold stored spells, durability, or upgrade data that ProjectE shouldn't price.

It adds no items, blocks, or recipes — only EMC data. Values apply on world load; open a Transmutation Table to see them.

**Dependencies**

- [ProjectE](https://modrinth.com/mod/projecte) — required
- [Iron's Spells 'n Spellbooks](https://modrinth.com/mod/irons-spellbooks) — required
- NeoForge 1.21.1, or Forge 1.20.1

The elixirs and the other Alchemist Cauldron fluids stay unvalued: their base fluids are potions that carry data, blood has no item form to price, and the brew ratios differ from recipe to recipe. EMC values are a considered pass; balance feedback is welcome.

Bugs and questions: comment on the CurseForge page, or DM @kuronami333 on X.

All Rights Reserved (free to put in any modpack, no permission or credit needed). Iron's Spells 'n Spellbooks is by Iron431 & Lab3; ProjectE by sinkillerj & contributors. Independent integration, not affiliated with either. Source: https://github.com/KURONAMI333/irons-spellbooks-emc
