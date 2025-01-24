# Levviata's Optimization Pack
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

### Notes:

**Universal Tweaks:**
- Changes the way auto jumping works. If auto jumping is enabled, it makes you automatically step up a whole block (like if you were riding a horse) instead of jumping near a block. To disable -> B:"Auto Jump Replacement"=false (Tweaks.cfg)
- There is also a bunch of other similar changes, edit the config as you wish (this will be removed from the modpack soon)

## Performance Comparison
TODO: add images for comparison (against vanilla, etc.)
also check how Entity Cull (current) differs from the other Entity Cull (by tr7zw)

## Known Issues
**VintageFix:**
- [Error accessing resource pack on classpath](https://github.com/embeddedt/VintageFix/issues/117) (can be safely ignored)

## Other Mods / Useful Resources
_Other useful mods that aren't essential and the resources/lists used to make this modpack._

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

GitHub: https://github.com/Levviata/Levviatas-Optimization-Pack (source)

CurseForge: https://www.curseforge.com/minecraft/modpacks/levviatas-optimization-pack (you are here)


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
