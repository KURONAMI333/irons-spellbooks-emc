<!-- Modrinth/CurseForge description source of truth. Paste verbatim into Modrinth;
     paste into CurseForge in MARKDOWN mode. Title/summary below are the search-indexed fields. -->

<!-- TITLE (<=64 chars): Iron's Spellbooks ProjectE EMC -->
<!-- SUMMARY (search-indexed, plain text): ProjectE EMC for Iron's Spells 'n Spellbooks: adds EMC to its arcane essence, mithril, pyrium and other materials so you can transmute them. -->

# Iron's Spellbooks ProjectE EMC

Play [Iron's Spells 'n Spellbooks](https://modrinth.com/mod/irons-spellbooks) with [ProjectE](https://modrinth.com/mod/projecte) and notice its materials have no EMC value? This add-on fixes that.

## What it does

A small, **data-only** add-on that teaches ProjectE about Iron's Spellbooks:

- **Hand-tuned EMC** for the mod's core materials — Arcane Essence, raw Mithril, Pyrium, Cinder Essence, Hogskin, Dragonskin, Divine Pearl and friends.
- Most crafted content (ingots, runes, the smithing-upgraded gear chains) **derives its EMC automatically** from the mod's vanilla-style recipes once the base materials are valued.
- **Pyrium is priced high on purpose** — it converts into ancient debris, so a low value would create an EMC duplication exploit. Mining stays the real path.
- **Stateful items have no EMC by design**: spellbooks, scrolls, weapons, staves, armor and upgrade orbs all carry stored spells / durability / upgrade data that ProjectE shouldn't price.

It adds **no items, blocks or recipes** — only EMC data.

## Compatibility

| | 1.21.1 |
|---|---|
| NeoForge | ✅ |

Requires **ProjectE** and **Iron's Spells 'n Spellbooks** (NeoForge 1.21.1).

## Install

Drop the jar into your `mods` folder alongside ProjectE and Iron's Spellbooks. EMC values apply on world load — open a Transmutation Table to see them.

## Dependencies

- **ProjectE** — required
- **Iron's Spells 'n Spellbooks** — required

## Scope & limitations

- NeoForge 1.21.1 only.
- EMC values are a considered first pass; balance feedback is welcome via the issue tracker.
- The fluid-based ink and elixir items (made in the Alchemist Cauldron) are not valued in this first version.
- Spellbooks, scrolls, weapons, armor and upgrade orbs intentionally carry no EMC (see above).

## License & credits

MIT. Iron's Spells 'n Spellbooks is by Iron431 & Lab3; ProjectE by sinkillerj & contributors. This add-on is an independent integration and is not affiliated with either.
