# Levviata's Optimization Pack
A Forge/~~Cleanroom~~ ([Cleanroom](discord.gg/f2K4aSpG4F) support is planned) modpack
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

## License
TLDR: Distribution and modification is allowed, but you can't use "Levviata's Optimization Pack" as your own trademark.

That is a short summary of what is most important, please read the full license below:

License: https://github.com/Levviata/Levviatas-Optimization-Pack/blob/ac9718cc0c63fb7ebc53c753f284dac3bae2421c/LICENSE.md
