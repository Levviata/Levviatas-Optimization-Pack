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

### Notes:

**Universal Tweaks:**
- Changes the way auto jumping works. If auto jumping is enabled, it makes you automatically step up a whole block (like if you were riding a horse) instead of jumping near a block. To disable -> B:"Auto Jump Replacement"=false (Tweaks.cfg)
- There is also a bunch of other similar changes, edit the config as you wish (this will be removed from the modpack soon)

## Performance Comparison
TODO: add images for comparison (against vanilla, etc.)
also check how Entity Cull (current) differs from the other Entity Cull (by tr7zw)

## Known Issues / Known Incompatibilities
### Incompatibilities
**Optifine:**

No, thanks. Why not? See below.

["This](https://www.reddit.com/r/Minecraft/comments/1bjc5mc/is_there_a_reason_why_people_still_use_optifine/)
[topic](https://www.reddit.com/r/Minecraft/comments/17qij4g/is_optifine_that_bad_nowadays/) 
[has](https://www.reddit.com/r/feedthebeast/comments/187djkg/what_is_up_with_optifine_and_why_does_it_get_so/) 
[been](https://web.archive.org/web/20201029070752/https://gist.github.com/jellysquid3/e46882e37907dfbb3d03d26f589b1c6a/) 
[beaten](https://www.youtube.com/watch?v=wqXF4GgP9e0) 
[to](https://www.reddit.com/r/feedthebeast/comments/wyyymx/stop_using_optifine_goddamit/)
[death"](https://www.reddit.com/r/feedthebeast/comments/12qpidr/is_optifine_that_bad/) -> _NOTE:
Kindly taken from [Opti Not So Fine](https://github.com/Radk6/MC-Optimization-Guide/blob/85fe6cf2c438b2c2ecc6c9cd103d064db3a06186/mods-n-stuff/opti-not-so-fine.md) by [Radk6](https://github.com/Radk6)_

Small, digestible, list here:

- It does not mix well with mods that try to do the same ([Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium), [Vintagium](https://github.com/Asek3/sodium-1.12), etc.)
- It tends to increase loading times, especially in bigger modpacks
- Some of its features can break other mods (for example, Fast Math or Smooth World options)
- Most likely lags behind performance compared to other optimization mods (which are also actively maintained in comparison)
- Not nice to work with due to restrictive license, and developers already have to be careful enough with Minecraft's own license. _Don't add another rooster to a chicken pen, one is enough._

TLDR²:
Optifine is a good general purpose optimization mod,
but for our application, it's not enough and actually makes optimization lag behind (literally).

**Optimization mod Incompatibility 101:**

[Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium) and [Vintagium](https://github.com/Asek3/sodium-1.12) rework the rendering system heavily,
making some mod's rendering to straight out not work.

([Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium) has been reported to have better mod support than [Vintagium](https://github.com/Asek3/sodium-1.12) in the [Cleanroom Discord](https://discord.com/invite/f2K4aSpG4F) server,
but that is my personal insight.)

Some of the current incompatibilities:

_NOTE: This list might be out of date as it was made on 1/24/2025!
This list also doesn't include all the incompatibilities neither might it be 100% correct,
take this information with a grain of salt.
Please check the respective mod's issue tracker for up-to-date information and/or._

- **[Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium):** ([see all incompatibilities here](https://github.com/Meldexun/Nothirium/issues?q=is%3Aissue%20state%3Aopen%20label%3Aconfirmed))
  - [Little Tiles](https://github.com/Meldexun/Nothirium/issues/9) 
  - ~~[VanillaFix (but also CensoredASM)](https://github.com/Meldexun/Nothirium/issues/24)~~ (fixed by Naughtirium)
  - [iChun's Portal Guns portals rendering wrong](https://github.com/Meldexun/Nothirium/issues/50)
  - [Multiblock broken textures](https://github.com/Meldexun/Nothirium/issues/82)
  - [ChunkAnimator chunks not animating sometimes](https://github.com/Meldexun/Nothirium/issues/93)
  - [ReplayMod rendering breaks](https://github.com/Meldexun/Nothirium/issues/94)
  - Optifine:
    - [Custom block layers](https://github.com/Meldexun/Nothirium/issues/36)
    - [Texture animation errors](https://github.com/Meldexun/Nothirium/issues/40)
  
- **[Vintagium](https://github.com/Asek3/sodium-1.12):** ([see the complete issue list, these might not be incompatibilities, neither have they been confirmed nor dismissed, see at your own discretion](https://github.com/Asek3/sodium-1.12/issues))
  - [daizu-007's Vintagium Compatibility List](https://github.com/daizu-007/Vintagium-Compatibility-List)
  - [Little Tiles](https://github.com/Asek3/sodium-1.12/issues/8)
  - [ArchitectureCraft](https://github.com/Asek3/sodium-1.12/issues/9)
  - [Wrong render of ImmersiveEngineering wires](https://github.com/Asek3/sodium-1.12/issues/13)
  - [Tweakeroo crash](https://github.com/Asek3/sodium-1.12/issues/20)
  - [Valkyrien Skies](https://github.com/Asek3/sodium-1.12/issues/28)
  - [Chisel & Bits crash](https://github.com/Asek3/sodium-1.12/issues/64)
  - [Multiblocks not rendering](https://github.com/Asek3/sodium-1.12/issues/39)

For further information about integrating this modpack's mods into your already existing modpack,
please see [Modpack Specific Optimizations](https://github.com/Radk6/MC-Optimization-Guide/blob/main/modpack-specific/modpack-instructions.md) by [Radk6](https://github.com/Radk6),
it is not a directly useful guide, but it will help you a ton.

### Issues:

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

Credits to [Radk6](https://github.com/Radk6) for their [optimization list](https://github.com/Radk6/MC-Optimization-Guide).

Credits to [TheUsefulLists](https://github.com/TheUsefulLists) for their [useful mod list](https://github.com/TheUsefulLists/UsefulMods/).

## License
TLDR: Distribution and modification is allowed, but you can't use "Levviata's Optimization Pack" as your own trademark
("Optimum" is NOT trademarked as it is a common English word.)

That is a short summary of what is most important, please read the full license below:

License: https://github.com/Levviata/Levviatas-Optimization-Pack/blob/ac9718cc0c63fb7ebc53c753f284dac3bae2421c/LICENSE.md
