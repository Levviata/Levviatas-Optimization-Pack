# Levviata's Optimization Pack

### NOTE: To download Vintagium latest release, please join [Cleanroom's Discord server](https://discord.com/invite/f2K4aSpG4F) and check the [# 🌟 information channel](https://discord.com/channels/926486493562814515/1185366081133617293/1259432738843398265), you will see the latest release there.


### OPTIFINE IS NOT SUPPORTED 
_(see more on "Known Issues / Known Incompatibilities" section)_

A Forge/~~Cleanroom~~ ([Cleanroom](discord.gg/f2K4aSpG4F) support is planned) modpack
that uses the latest optimization mods for Minecraft 1.12.2 while adding no other gameplay,
QoL, etc. features.

Intended to use in new singleplayer playthroughs as a standalone,
but I will eventually release server-only instances and instructions for integration in existing modpacks.

(there is not enough testing,
but please try it
and [open an issue in the tracker](https://github.com/Levviata/Levviatas-Optimization-Pack/issues)
if you have any problem.)

(the modpack name on the web (modrinth, CurseForge, and GitHub) is "Levviata's Optimization Pack" for visibility,
the pack is named "Optimum" internally)

## Features
**Mods included in the modpack are the following (embedded and external):**
- **Core:**
  - [Alfheim](https://modrinth.com/mod/alfheim-lighting-engine) (lighting engine)
    - A lighting engine. Completely reworks and optimizes the lighting engine
  - [Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium) + [Naughtirium](https://modrinth.com/mod/naughthirium) (render engine) -> _NOTE: Naughtirium adds compatibility with CensoredASM and Nothirium, it is needed._
    - A chunk render engine. Reworks and (hopefully) optimizes chunk rendering
  - [CensoredASM](https://www.curseforge.com/minecraft/mc-mods/lolasm) (optimizes ram, fixes crashes, and optimizes code in general)
    - ~~Agnostic Super Mod~~ Minecraft code patcher via magic hackery. Reworks and optimizes a lot of Minecraft's code with positive results
  - [Entity Culling](https://www.curseforge.com/minecraft/mc-mods/entity-culling) (1.12.2-only maintained entity culling)
    - A entity culling render system. Hides entities that aren't visible on your screen
  - [Universal Tweaks](https://www.curseforge.com/minecraft/mc-mods/universal-tweaks) (general tweaks/bugfixes)
    - Packs a lot of minor changes into one big mod. A LOT of bugfixes and tweaks
  - [VintageFix](https://modrinth.com/mod/vintagefix) (FoamFix replacer)
    - Blockstate/model optimizations. Improves memory usage and load times
  - [Particle Culling](https://www.curseforge.com/minecraft/mc-mods/particle-culling) (less particle lag)
    - A particle culling render system. Hides particles that aren't visible on your screen
  - [MixinBooter](https://modrinth.com/mod/mixinbooter) (core library)
    - Mixin 101. Handles code injection and a lot of other nerdy things
- **Minor Fixes:**
  - [Better Biome Blend](https://www.curseforge.com/minecraft/mc-mods/better-biome-blend) (biome color blender optimizer)
    - Better-looking biome blending and optimizes the biome blend algorithm
  - [Fixeroo](https://www.curseforge.com/minecraft/mc-mods/xp-orb-clump) (Clumps replacer)
    - Clumps experience into one and adds minor optimizations. Doesn't add a new entity like Clumps does
- **Utility or Library:**
  - [ConfigAnyTime](https://www.curseforge.com/minecraft/mc-mods/configanytime) (library)
    - Lets config be edited at any time 
  - [RedCore](https://www.curseforge.com/minecraft/mc-mods/red-core) (library)
    - Amazing library for developers
  - [RenderLib](https://www.curseforge.com/minecraft/mc-mods/renderlib) (library)
    - A rendering library

## Performance Comparison
TODO: add images for comparison (against vanilla, etc.)
also check how Entity Cull (current) differs from the other Entity Cull (by tr7zw)

## Known Issues / Known Incompatibilities
Please see [Known Issues](https://github.com/Levviata/Levviatas-Optimization-Pack/blob/main/Documentation/KNOWN_ISSUES.md)
and [Incompatibilities](https://github.com/Levviata/Levviatas-Optimization-Pack/blob/main/Documentation/INCOMPATIBILITIES.md).

## Other Mods / Useful Resources
<sub>_Other useful mods that aren't essential and the resources/lists used to make this modpack._</sub>

Please see [Other Mods and Useful Resources](https://github.com/Levviata/Levviatas-Optimization-Pack/blob/main/Documentation/RESOURCES.md).

## Credits / Copyright Notice
Please see [Credits and Copyright](https://github.com/Levviata/Levviatas-Optimization-Pack/blob/main/Documentation/CREDITS.md).

## Links

CurseForge: https://www.curseforge.com/minecraft/modpacks/levviatas-optimization-pack (you are here)

Modrinth: https://modrinth.com/modpack/levviatas-optimization-pack

GitHub: https://github.com/Levviata/Levviatas-Optimization-Pack (source)

## License
TLDR: Distribution and modification is allowed, but you can't use "Levviata's Optimization Pack" as your own trademark
("Optimum" is NOT trademarked as it is a common English word.)

That is a short summary of what is most important, please read the full license below:

License: https://github.com/Levviata/Levviatas-Optimization-Pack/blob/main/LICENSE.txt
