# Levviata's Optimization Pack
A Forge/~~Cleanroom~~ (Cleanroom support is planned) mod pack that optimizes Minecraft 1.12.2
(no other versions) while adding no other gameplay or QoL features.

Feel free to add more mods when playing standalone.
(You can also add this mod pack's config and mods into existing mod packs or playthroughs,
but it MIGHT cause issues if you find any,
please [open an issue on the tracker.)](https://github.com/Levviata/Levviatas-Optimization-Pack/issues))

(the mod pack name on the web (modrinth, CurseForge, and GitHub) is "Levviata's Optimization Pack"
for simplicity and visibility,
the pack is named "Optimum" internally)

## Features
**Mods included in the mod pack are the following (embedded and external):**
- **Core:**
  - [Alfheim (lighting engine)](https://modrinth.com/mod/alfheim-lighting-engine)
    - Completely reworks and optimizes the lighting engine
  - [Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium) + [Naughtirium](https://modrinth.com/mod/naughthirium) (render engine) -> _NOTE: Naughtirium enables compat with CensoredASM and Nothirium, hence why it's here_
    - Reworks and (hopefully) optimizes chunk rendering
  - [CensoredASM](https://www.curseforge.com/minecraft/mc-mods/lolasm) (optimizes ram, fixes crashes, and optimizes code in general)
    - Reworks and optimizes a lot of Minecraft's code with positive results
  - [Entity Culling](https://www.curseforge.com/minecraft/mc-mods/entity-culling) (1.12.2-only maintained entity culling)
    - Hides entities that aren't visible on your screen
  - [Universal Tweaks](https://www.curseforge.com/minecraft/mc-mods/universal-tweaks) (general tweaks/bugfixes)
    - A LOT of bugfixes and tweaks, positive results overall
  - [VintageFix](https://modrinth.com/mod/vintagefix) (FoamFix replacer)
    - Replaces and improves upon FoamFix. Improves memory usage and load times
  - [Particle Culling](https://www.curseforge.com/minecraft/mc-mods/particle-culling) (less particle lag)
    - Hides particles that aren't visible on your screen
  - [MixinBooter](https://modrinth.com/mod/mixinbooter) + [MixinBootstrap](https://modrinth.com/mod/mixinbootstrap) (core library)
    - Handles code injection and a lot of other nerdy things
- **Minor Fixes:**
  - [Better Biome Blend](https://www.curseforge.com/minecraft/mc-mods/better-biome-blend) (biome color blender optimizer)
    - Optimizes biome color blending code
  - [Fixeroo](https://www.curseforge.com/minecraft/mc-mods/xp-orb-clump) (Clumps replacer)
    - Replaces Clumps. Doesn't add a new entity like Clumps does, apart from that it adds a bunch of random optimizations
- **Utility or Library:**
  - [File director](https://modrinth.com/mod/filedirector) (utility)
    - Moves, downloads, and handles files for the mod pack
  - [ConfigAnyTime](https://www.curseforge.com/minecraft/mc-mods/configanytime) (library)
  - [RedCore](https://www.curseforge.com/minecraft/mc-mods/red-core) (library)
  - [RenderLib](https://www.curseforge.com/minecraft/mc-mods/renderlib) (library)

### Notes:

**Universal Tweaks:**
- Changes the way auto jumping works. If auto jumping is enabled, it makes you automatically step up a whole block (like if you were riding a horse) instead of jumping near a block. To disable -> B:"Auto Jump Replacement"=false (Tweaks.cfg)
- There is also a bunch of other similar changes, edit the config as you wish.

## External Mods / CurseForge Mods
This mod pack uses [File Director](https://modrinth.com/mod/filedirector) to download these mods from CurseForge:
- [Mixin 0.7-0.8 Compatibility](https://www.curseforge.com/minecraft/mc-mods/mixin-0-7-0-8-compatibility) (optional, is helpful only on specific occasions)
- [Censored ASM](https://www.curseforge.com/minecraft/mc-mods/lolasm)
- [Entity Culling](https://www.curseforge.com/minecraft/mc-mods/entity-culling)
- [Fast Furnace](https://www.curseforge.com/minecraft/mc-mods/fastfurnace)
- [Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium)
- [RenderLib](https://www.curseforge.com/minecraft/mc-mods/renderlib)
- [Fixeroo](https://www.curseforge.com/minecraft/mc-mods/xp-orb-clump)

### NOTE: When you first download these mods your game WILL crash, simply reboot your game and no more errors/crashes should appear ([issue on GitHub](https://github.com/TerraFirmaCraft-The-Final-Frontier/FileDirector/issues/31) + [reason why this unavoidably happens](https://github.com/Levviata/Levviatas-Optimization-Pack-public/blob/72e72c417410e9ee3f867704bf0cac6d576c6bf1/Misc/filedirectorissue.png)).

## Performance Comparison
TODO: add images for comparison (against vanilla, etc.)
also check how Entity Cull (arr) differs from another entity cull (tr7zw)

## Known Issues
**VintageFix:**
- [Error accessing resource pack on classpath](https://github.com/embeddedt/VintageFix/issues/117) (can be safely ignored)

## Other Mods / Useful Resources
<sub>_Other useful mods that aren't essential and the resources/lists used to make this mod pack._</sub>

### **Performance**
- **Performance mod lists used/referenced:**
  - [UtilMods](https://github.com/TheUsefulLists/UsefulMods/)
  - [Radk6's Performance Mod List](https://github.com/Radk6/MC-Optimization-Guide)

**Java Arguments**:
- [DataDalton's Arguments](https://github.com/DataDalton/Minecraft-Performance-Guide/blob/fe8d8fbfebe129a38a67c56d5452e871e48580bc/Java%20Arguments/README.md)

**Non-essential Performance Mods**:
- [Entity Distance](https://www.curseforge.com/minecraft/mc-mods/entity-distance-1-12-2):
  - Adds a configurable

### **Quality of Life or Gameplay**
**Quality of Life Mods:**
- **[Raw Mouse Input](https://modrinth.com/mod/raw-mouse-input-blessed-edition):**
  - Make Minecraft use your mouse's raw input. This might be a problem if your mouse is old, an office mouse, low dpi, etc. You can also adjust the mouse sensitive through Minecraft to around half (50%), and it will be about the same.
- **[Had Enough Items](https://www.curseforge.com/minecraft/mc-mods/had-enough-items):**
  - Just Enough Items but for 1.12.2. Optimizes memory usage, load time, and how the GUI is rendered, mod is also actively maintained.
 
### **Utility**
**Mod pack utils:**
- **[Multiblocked](https://www.curseforge.com/minecraft/mc-mods/multiblocked):**
  - Multiblock tweaker and library. Looks amazing for multiblock machines/structures/etc.


## Links
Modrinth: https://modrinth.com/modpack/levviatas-optimization-pack (unlisted visibility)

CurseForge: https://legacy.curseforge.com/minecraft/modpacks/levviatas-optimization-pack (not listed)

## Credits
Credits to every mod's author included (or were included) in the pack for their amazing optimizations.

## License
This project is licensed with [BSD-3-Clause license](https://github.com/Levviata/Levviatas-Optimization-Pack-public?tab=BSD-3-Clause-1-ov-file#readme).
