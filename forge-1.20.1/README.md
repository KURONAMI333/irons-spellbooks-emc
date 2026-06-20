# Iron's Spellbooks ProjectE EMC — Forge 1.20.1

The Minecraft **1.20.1 Forge** build of the EMC addon (the repo root is the 1.21.1 NeoForge build).

Same EMC content as the 1.21.1 sibling, re-emitted in ProjectE 1.20.1 (PE1.0.1)'s
`values.before` **map** shape and shipped as a **lowcodefml** data jar (no compilation).
Targets Iron's Spells 'n Spellbooks 1.20.1 (all 11 seeded items present as of 3.16.1).

## Build (no Gradle / JDK)

```bash
python tools/generate_emc.py   # regenerate src/data/.../irons_spellbooks_emc.json
python tools/build_jar.py       # -> build/irons_spellbooks_emc-0.1.0-forge-1.20.1.jar
```

## Verify (parse-0 gate)

Drop the jar + `ProjectE-1.20.1-PE1.0.1` + Iron's Spellbooks (+ its deps) into a Forge
1.20.1 server's `mods/`, launch headless (JDK17), confirm in the log:
`mo.pr.PECore` logs `Considering file irons_spellbooks:pe_custom_conversions/...`
then `Registered N EMC values` with no PECore parse error. (Format/canon: see
`kuronami-mods/knowledge/PROJECTE_EMC_NOTES.md` → 1.20.1 Forge 展開.)

Status: v0.1.0 — built; ProjectE 1.20.1 parse verified (0 errors) on a Forge 1.20.1 server.
