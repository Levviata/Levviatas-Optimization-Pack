# Levviata's Optimization Pack

## NOTE:

When you first run the modpack, your game WILL crash; this is expected, however.

Reboot your game and you will be totally fine.


([issue on GitHub](https://github.com/TerraFirmaCraft-The-Final-Frontier/FileDirector/issues/31) + [reason why this unavoidably happens](https://github.com/Levviata/Levviatas-Optimization-Pack-public/blob/72e72c417410e9ee3f867704bf0cac6d576c6bf1/Misc/filedirectorissue.png)).

To download Vintagium latest release,
please join [Cleanroom's Discord server](https://discord.com/invite/f2K4aSpG4F)
and check the [# 🌟 information channel](https://discord.com/channels/926486493562814515/1185366081133617293/1259432738843398265),
you will see the latest release there.

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
  - [Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium) + [Naughthirium](https://modrinth.com/mod/naughthirium) (render engine) -> _NOTE: Naughthirium adds compatibility with CensoredASM and Nothirium, it is needed._
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
  - [File director](https://modrinth.com/mod/filedirector) (utility)
    - Moves, downloads, and handles files for the modpack
  - [ConfigAnyTime](https://www.curseforge.com/minecraft/mc-mods/configanytime) (library)
    - Lets config be edited at any time
  - [RedCore](https://www.curseforge.com/minecraft/mc-mods/red-core) (library)
    - Amazing library for developers
  - [RenderLib](https://www.curseforge.com/minecraft/mc-mods/renderlib) (library)
    - A rendering library

## External Mods / Bundled Mods
This modpack uses [File Director](https://modrinth.com/mod/filedirector) to download these mods from CurseForge:
- [Entity Culling](https://www.curseforge.com/minecraft/mc-mods/entity-culling)
- [Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium)
- [RenderLib](https://www.curseforge.com/minecraft/mc-mods/renderlib)
- [MultiThreadNoise](https://www.curseforge.com/minecraft/mc-mods/multithreaded-noise)

These mods were redistributed/bundled with the modpack for convenience (see "Credits / Copyright Notice" section for more information):
- [Censored ASM](https://www.curseforge.com/minecraft/mc-mods/lolasm)
- [Fixeroo](https://www.curseforge.com/minecraft/mc-mods/xp-orb-clump)


## Performance Comparison
TODO: add images for comparison (against vanilla, etc.)
also check how Entity Cull (current) differs from the other Entity Cull (by tr7zw)

## Known Issues / Known Incompatibilities


## Other Mods / Useful Resources
<sub>_Other useful mods that aren't essential and the resources/lists used to make this modpack._</sub>

## Links

CurseForge: https://www.curseforge.com/minecraft/modpacks/levviatas-optimization-pack

Modrinth: https://modrinth.com/modpack/levviatas-optimization-pack (you are here)

GitHub: https://github.com/Levviata/Levviatas-Optimization-Pack (source)

## Credits / Copyright Notice

[CensoredASM](https://github.com/LoliKingdom/LoliASM) (by [Rongmario](https://github.com/Rongmario)),
which is licensed with [LGPL](https://github.com/LoliKingdom/LoliASM/blob/master/LICENSE),
comes bundled with the pack for convenience
(click blue texts/links for more info)

[Fixeroo](https://www.curseforge.com/minecraft/mc-mods/xp-orb-clump) by [CaliforniaDemise](https://github.com/CaliforniaDemise),
which is licensed with [MIT](https://github.com/CaliforniaDemise/Fixeroo/blob/main/LICENSE),
comes bundled with the pack for convenience
(click blue texts/links for more info)

Credits to every mod's author included (or were included) in the pack for their amazing optimizations.

## License
TLDR: Distribution and modification is allowed, but you can't use "Levviata's Optimization Pack" as your own trademark
("Optimum" is NOT trademarked as it is a common English word.)

That is a short summary of what is most important, please read the full license below:

License: https://github.com/Levviata/Levviatas-Optimization-Pack/blob/ac9718cc0c63fb7ebc53c753f284dac3bae2421c/LICENSE.md