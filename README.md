# Levviata's Optimization Pack
A Forge/~~Cleanroom~~ (Cleanroom support is planned) modpack that optimizes Minecraft 1.12.2
(no other versions) while adding no other gameplay, QoL, etc. features

Intended to use in new singleplayer playthroughs as a standalone

BUT

Definitely works in existing modpacks (e.i: Drag and drop this pack's mods and configs into yours)

AND existing singleplayer playthroughs (MIGHT corrupt your world, usually should not)

BUT I have not tested or released instructions for that so don't come at me with pitchforks and torches
(kindly [open an issue on the GitHub issue tracker](<https://github.com/Levviata/Levviatas-Optimization-Pack/issues>) though)

(the modpack name on the web (modrinth, CurseForge, and GitHub) is "Levviata's Optimization Pack" for visibility,
the pack is named "Optimum" internally)

## Features
**Mods included in the modpack are the following (embedded and external):**
- **Core:**
  - [Alfheim](https://modrinth.com/mod/alfheim-lighting-engine) (lighting engine)
    - Completely reworks and optimizes the lighting engine
  - [Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium) + [Naughtirium](https://modrinth.com/mod/naughthirium) (render engine) -> _NOTE: Naughtirium adds compatibility with CensoredASM and Nothirium, it is needed._
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
    - Moves, downloads, and handles files for the modpack
  - [ConfigAnyTime](https://www.curseforge.com/minecraft/mc-mods/configanytime) (library)
  - [RedCore](https://www.curseforge.com/minecraft/mc-mods/red-core) (library)
  - [RenderLib](https://www.curseforge.com/minecraft/mc-mods/renderlib) (library)

### Notes:

**Universal Tweaks:**
- Changes the way auto jumping works. If auto jumping is enabled, it makes you automatically step up a whole block (like if you were riding a horse) instead of jumping near a block. To disable -> B:"Auto Jump Replacement"=false (Tweaks.cfg)
- There is also a bunch of other similar changes, edit the config as you wish (this will be removed from the modpack soon)

## External Mods / CurseForge Mods
This modpack uses [File Director](https://modrinth.com/mod/filedirector) to download these mods from CurseForge:
- [Entity Culling](https://www.curseforge.com/minecraft/mc-mods/entity-culling)
- [Fast Furnace](https://www.curseforge.com/minecraft/mc-mods/fastfurnace)
- [Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium)
- [RenderLib](https://www.curseforge.com/minecraft/mc-mods/renderlib)
- [Fixeroo](https://www.curseforge.com/minecraft/mc-mods/xp-orb-clump)
These mods were redistributed/bundled with the modpack for convenience (see "Copyright" section for more information):
- [Censored ASM](https://www.curseforge.com/minecraft/mc-mods/lolasm)

### NOTE: When you first download these mods your game WILL crash, simply reboot your game and no more errors/crashes should appear ([issue on GitHub](https://github.com/TerraFirmaCraft-The-Final-Frontier/FileDirector/issues/31) + [reason why this unavoidably happens](https://github.com/Levviata/Levviatas-Optimization-Pack-public/blob/72e72c417410e9ee3f867704bf0cac6d576c6bf1/Misc/filedirectorissue.png)).

## Performance Comparison
TODO: add images for comparison (against vanilla, etc.)
also check how Entity Cull (current) differs from the other Entity Cull (by tr7zw)

## Known Issues
**VintageFix:**
- [Error accessing resource pack on classpath](https://github.com/embeddedt/VintageFix/issues/117) (can be safely ignored)

## Other Mods / Useful Resources
<sub>_Other useful mods that aren't essential and the resources/lists used to make this modpack._</sub>

### **Performance**
- **Performance mod lists used/referenced:**
  - [UtilMods](https://github.com/TheUsefulLists/UsefulMods/)
  - [Radk6's Performance Mod List](https://github.com/Radk6/MC-Optimization-Guide)

**Java Arguments**:
- [DataDalton's Arguments](https://github.com/DataDalton/Minecraft-Performance-Guide/blob/fe8d8fbfebe129a38a67c56d5452e871e48580bc/Java%20Arguments/README.md)

**Non-essential Performance Mods**:
- [Entity Distance](https://www.curseforge.com/minecraft/mc-mods/entity-distance-1-12-2):
  - Adds a configuration for reducing how far your client renders and tracks certain entities (similar to "Simulation Distance" Minecraft configuration in modern versions)

### **Quality of Life or Gameplay**
**Quality of Life Mods:**
- **[Raw Mouse Input](https://modrinth.com/mod/raw-mouse-input-blessed-edition):**
  - Make Minecraft use your mouse's raw input to fix sensitivity on higher DPI. You can also adjust the mouse sensitive through Minecraft to around half (50%), and it will be about the same.
- **[Had Enough Items](https://www.curseforge.com/minecraft/mc-mods/had-enough-items):**
  - Just Enough Items but for 1.12.2. Optimizes memory usage, load time, and how the GUI is rendered, mod is also actively maintained.
 
### **Utility**
**Modpack utils:**
- **[Multiblocked](https://www.curseforge.com/minecraft/mc-mods/multiblocked):**
  - Multiblock tweaker and library. Looks amazing for multiblock machines/structures/etc.


## Links
Modrinth: https://modrinth.com/modpack/levviatas-optimization-pack

CurseForge: https://legacy.curseforge.com/minecraft/modpacks/levviatas-optimization-pack

## Credits / Copyright Notice

[CensoredASM](https://github.com/LoliKingdom/LoliASM) (by [Rongmario](https://github.com/Rongmario)),
which is licensed with [LGPL](https://github.com/LoliKingdom/LoliASM/blob/master/LICENSE),
comes bundled with the pack for convenience 
(click blue texts/links for more info)

Credits to every mod's author included (or were included) in the pack for their amazing optimizations.

## License
This project is licensed with [BSD-3-Clause license](https://github.com/Levviata/Levviatas-Optimization-Pack-public?tab=BSD-3-Clause-1-ov-file#readme).
