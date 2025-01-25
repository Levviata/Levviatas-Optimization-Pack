# Levviata's Optimization Pack
A Forge/~~Cleanroom~~ ([Cleanroom](https://discord.com/invite/f2K4aSpG4F) support is planned) modpack
that uses the latest optimization mods for Minecraft 1.12.2 while adding no other gameplay,
QoL, etc. features.

Intended to use in new singleplayer playthroughs as a standalone,
but I will eventually release server and instructions for integration in existing modpacks.

(there is not enough testing,
but please try it
and [open an issue in the tracker](https://github.com/Levviata/Levviatas-Optimization-Pack/issues)
if you have any problem.)

(the modpack name on the web (modrinth, CurseForge, and GitHub) is "Levviata's Optimization Pack" for visibility,
the pack is named "Optimum" internally)

## Download
Choose CurseForge for your preferred website to download as it is the easiest to use:

**CurseForge:** 
- https://www.curseforge.com/minecraft/modpacks/levviatas-optimization-pack

**Modrinth:**
- https://modrinth.com/modpack/levviatas-optimization-pack

Uploaded versions on CurseForge and Modrinth have no differences. You don't have to care about it.

<details>
  <summary>But if you do care, here's an explanation</summary>

The only difference that "matters"
is that the modpack version on Modrinth uses [File Director](https://modrinth.com/mod/filedirector) to download these mods:

- [Entity Culling](https://www.curseforge.com/minecraft/mc-mods/entity-culling)
- [Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium)
- [RenderLib](https://www.curseforge.com/minecraft/mc-mods/renderlib)

There is currently no other way to bundle those mods with the modpack.

This is because of:

- Mods might not be on CurseForge or Modrinth or vice versa.
- Distribution permissions are different from CurseForge to Modrinth and vice versa.
- Some mods have restrictive licenses which do not allow distribution.


</details>

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

## Credits / Copyright Notice

[CensoredASM](https://github.com/LoliKingdom/LoliASM) (by [Rongmario](https://github.com/Rongmario)),
which is licensed with [LGPL](https://github.com/LoliKingdom/LoliASM/blob/master/LICENSE),
comes bundled with the Modrinth modpack for convenience
(click blue texts/links for more info)

[Fixeroo](https://www.curseforge.com/minecraft/mc-mods/xp-orb-clump) by [CaliforniaDemise](https://github.com/CaliforniaDemise),
which is licensed with [MIT](https://github.com/CaliforniaDemise/Fixeroo/blob/main/LICENSE),
comes bundled with the Modrinth modpack for convenience
(click blue texts/links for more info)

Credits to every mod's author included (or were included) in the modpack for their amazing optimizations.

Credits to [Radk6](https://github.com/Radk6) for their [optimization list](https://github.com/Radk6/MC-Optimization-Guide).

Credits to [TheUsefulLists](https://github.com/TheUsefulLists) for their [useful mod list](https://github.com/TheUsefulLists/UsefulMods/).

## License
TLDR: Distribution and modification is allowed, but you can't use "Levviata's Optimization Pack" as your own trademark.

That is a short summary of what is most important, please read the full license below:

License: https://github.com/Levviata/Levviatas-Optimization-Pack/blob/ac9718cc0c63fb7ebc53c753f284dac3bae2421c/LICENSE.md
