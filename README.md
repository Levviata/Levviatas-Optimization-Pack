# Levviata's Optimization Pack
A Forge/~~Cleanroom~~ (Cleanroom support is planned) modpack that optimizes Minecraft 1.12.2 (no other versions) while adding no other gameplay or QoL features.

Feel free to add more mods when playing standalone (you can also add this modpack's config and mods into existing modpacks or playthroughs but it MIGHT cause issues, if you find any please [open an issue on the tracker](https://github.com/Levviata/Levviatas-Optimization-Pack/issues)).

(the modpack name on the webs (modrinth, CurseForge, and GitHub) is "Levviata's Optimization Pack" for simplicity and visibility, the pack is named "Optimum" internally)

## Features
**Mods added are the following (embedded and external):**
- **Core:**
  - Alfheim (lighting engine)
    - Completely reworks and optimizes the lighting engine 
  - Nothirium + Naughtirium (render engine) -> _NOTE: Naughtirium enables compat with CensoredASM and Nothirium, hence why it's here_
    - Reworks chunk rendering
  - CensoredASM (optimizes ram, fixes crashes, and optimizes code in general)
    - Reworks and optimizes a lot of Minecraft's code with positive results
  - Entity Culling (1.12.2-only maintained entity culling)
    - Hides entities that aren't visible on you screen
  - Universal Tweaks (general tweaks/bugfixes)
    - A LOT of bugfixes and tweaks, positive results overall
  - VintageFix (FoamFix replacer)
    - Replaces foamfix, improves memory usage and load times
  - Particle Culling (less particle lag)
    - Hides particles that aren't visible on your screen
  - Mixin Booter + Mixin Bootstrap (core library)
    - Handles code injection + a lot of other nerdy things
- **Minor Fixes:**
  - Better Biome Blend (biome color blender optimizer)
  - Fixeroo (Clumps replacer)
    - Replaces Clumps, doesnt add a new entity like Clumps does along other general misc optimizations
- **Utility or Library:**
  - File director (utility)
    - Moves, downloads, and handles files for the modpack
  - ConfigAnyTime (library)
  - RedCore (library)
  - RenderLib (library)

### Notes:

**Universal Tweaks:**
- Changes the way auto jumping works. If auto jumping is enabled, it makes you automatically step up a whole block (like if you were riding a horse) instead of jumping near a block. To disable -> B:"Auto Jump Replacement"=false (Tweaks.cfg)
- There is also a bunch of other similar changes, edit the config as you wish.

## External Mods / CurseForge Mods
This modpack uses [File Director](https://modrinth.com/mod/filedirector) to download these mods from CurseForge:
- [Mixin 0.7-0.8 Compatibility](https://www.curseforge.com/minecraft/mc-mods/mixin-0-7-0-8-compatibility) (optional, is helpful only on specific occasions)
- [Censored ASM](https://www.curseforge.com/minecraft/mc-mods/lolasm)
- [Entity Culling](https://www.curseforge.com/minecraft/mc-mods/entity-culling)
- [Fast Furnace](https://www.curseforge.com/minecraft/mc-mods/fastfurnace)
- [Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium)
- [RenderLib](https://www.curseforge.com/minecraft/mc-mods/renderlib)

### NOTE: When you first download these mods your game WILL crash, simply reboot your game and no more errors/crashes should appear ([issue on GitHub](https://github.com/TerraFirmaCraft-The-Final-Frontier/FileDirector/issues/31) + [reason why this unavoidably happens](https://github.com/Levviata/Levviatas-Optimization-Pack-public/blob/72e72c417410e9ee3f867704bf0cac6d576c6bf1/Misc/filedirectorissue.png)).

## Performance Comparation
TODO: add images for comparation (against vanilla,etc.)
also check how Entity Cull (arr) differs from other entity cull (tr7zw)

## Issues
**VintageFix:**
- [Error accessing resource pack on classpath](https://github.com/embeddedt/VintageFix/issues/117) (can be safely ignored)

## Other Mods / Useful Resources
<sub>_Other useful mods that aren't extremely important in general and the resources/lists used to make this modpack._</sub>

**Peformance mod lists used/referenced:**
- [UtilMods](https://github.com/TheUsefulLists/UsefulMods/)
- [Radk6's Peformance Mod List](https://github.com/Radk6/MC-Optimization-Guide)

**Java Arguments:
- [DataDalton's Arguments](https://github.com/DataDalton/Minecraft-Performance-Guide/blob/fe8d8fbfebe129a38a67c56d5452e871e48580bc/Java%20Arguments/README.md)

**Quality of Life Mods:**
- **Raw Mouse Input:**
  - Makes Minecraft use your mouse's raw input. This might be a problem if your mouse is old, an office mouse, low dpi, etc. Remove mod or adjust mouse sensitivity in options if this is an issue to you.
- **[Had Enough Items](https://www.curseforge.com/minecraft/mc-mods/had-enough-items):**
  - Just Enough Items but for 1.12.2,
 
**Non-essential Performance Mods**:
- [Entity Distance](https://www.curseforge.com/minecraft/mc-mods/entity-distance-1-12-2):
  - Adds a configurable

**

## Links
Modrinth: https://modrinth.com/modpack/levviatas-optimization-pack (unlisted visibility)

CurseForge: https://legacy.curseforge.com/minecraft/modpacks/levviatas-optimization-pack (not listed)

## Credits
Credits to every mod author included (or were included) in the pack for their amazing optimizations.

## License
This project is licensed with [BSD-3-Clause license](https://github.com/Levviata/Levviatas-Optimization-Pack-public?tab=BSD-3-Clause-1-ov-file#readme).
