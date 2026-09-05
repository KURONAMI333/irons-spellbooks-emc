# Changelog

## v0.2.0

- Added EMC for all five alchemist ink tiers (common through legendary).
- Common ink is a root value (no recipe; chest loot and wandering traders only); the four tiers above it follow the cauldron's fixed four-to-one ladder.
- Bottle returns from the cauldron recipes are factored in, so each tier stays EMC-neutral or below.
- Elixirs remain unvalued (component-carrying potion bases, no item source for blood, and per-recipe brew ratios).
- Moved the mithril anchor from Raw Mithril to Mithril Scrap. ProjectE forces every item in the raw-materials tag to zero, so the old value never applied and the mithril chain went unpriced on 1.21.1. Smelting is one-to-one, so the value is unchanged.
- Dropped the Arcane Salvage value from the 1.21.1 build. Iron's Spellbooks 1.21.1 ships the item's assets but never registers it, so the entry only produced a load error. The Forge 1.20.1 build, where the item does exist, keeps it.

## v0.1.0

Initial release.

- ProjectE EMC integration for Iron's Spells 'n Spellbooks (NeoForge 1.21.1).
- Hand-set EMC for core stateless materials (arcane essence, raw mithril, pyrium, cinder essence, hides, divine pearl/soulshard, energized core, permafrost shard); vanilla recipes derive the rest.
- Pyrium priced high to keep mining preferable to transmutation (it converts to ancient debris).
- Spellbooks / scrolls / weapons / armor / upgrade orbs intentionally left without EMC (stored state).
- Data-only: adds no items, blocks or recipes. Fluid-based ink/elixir items deferred to a later pass.
