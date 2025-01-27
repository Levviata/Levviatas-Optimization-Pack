# Incompatibilities
## Optifine

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

<sub>TODO: Make a full and comprehensive list of alternatives to Optifine's Quality of Life [QoL]
(as telling people to ditch all of it in favor of only a better render engine is stupid.)</sub>

## Optimization mod Incompatibility 101

[Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium) and [Vintagium](https://github.com/Asek3/sodium-1.12) rework the rendering system heavily,
making some mod's rendering to straight out not work.

([Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium) has been reported to have better mod support than [Vintagium](https://github.com/Asek3/sodium-1.12) in the [Cleanroom Discord](https://discord.com/invite/f2K4aSpG4F) server,
but that is my personal insight.)

Some of the current incompatibilities:

_NOTE: This list might be out of date as it was made on 1/24/2025!
This list also doesn't include all the incompatibilities neither might it be 100% correct,
take this information with a grain of salt.
Please check the respective mod's issue tracker for up-to-date information._

- **[Nothirium](https://www.curseforge.com/minecraft/mc-mods/nothirium):** ([see all incompatibilities here](https://github.com/Meldexun/Nothirium/issues?q=is%3Aissue%20state%3Aopen%20label%3Aconfirmed))
    - [Little Tiles](https://github.com/Meldexun/Nothirium/issues/9)
    - ~~[VanillaFix (but also CensoredASM)](https://github.com/Meldexun/Nothirium/issues/24)~~ (fixed by [Naughthirium](https://modrinth.com/mod/naughthirium))
    - [iChun's Portal Guns portals rendering wrong](https://github.com/Meldexun/Nothirium/issues/50)
    - [Multiblock broken textures](https://github.com/Meldexun/Nothirium/issues/82)
    - [ChunkAnimator chunks not animating sometimes](https://github.com/Meldexun/Nothirium/issues/93)
    - [ReplayMod rendering breaks](https://github.com/Meldexun/Nothirium/issues/94)
    - Optifine:
        - [Custom block layers](https://github.com/Meldexun/Nothirium/issues/36)
        - [Texture animation errors](https://github.com/Meldexun/Nothirium/issues/40)



- **[Vintagium](https://github.com/Asek3/sodium-1.12):** ([see the complete issue list, these might not be incompatibilities, neither have they been confirmed nor dismissed, see at your own discretion](https://github.com/Asek3/sodium-1.12/issues))
    - [daizu-007's Vintagium Compatibility List](https://github.com/daizu-007/Vintagium-Compatibility-List) (this is both a compatibility and incompatibility list)
    - [Little Tiles](https://github.com/Asek3/sodium-1.12/issues/8)
    - [ArchitectureCraft](https://github.com/Asek3/sodium-1.12/issues/9)
    - [Wrong render of ImmersiveEngineering wires](https://github.com/Asek3/sodium-1.12/issues/13)
    - [Tweakeroo crash](https://github.com/Asek3/sodium-1.12/issues/20)
    - [Valkyrien Skies](https://github.com/Asek3/sodium-1.12/issues/28)
    - [Chisel & Bits crash](https://github.com/Asek3/sodium-1.12/issues/64)
    - [Multiblocks not rendering](https://github.com/Asek3/sodium-1.12/issues/39)



## Other Misc Incompatibilities

### [NoiseThreader](https://www.curseforge.com/minecraft/mc-mods/noisethreader)

Replaced by its "better"
uncle [Multithreaded Noise,](https://www.curseforge.com/minecraft/mc-mods/multithreaded-noise)
which also does not add another (possibly) redundant dependency.

<---------->

For further information
about integrating this modpack's optimizations into your already existing modpack,
please see [Modpack Specific Optimizations](https://github.com/Radk6/MC-Optimization-Guide/blob/main/modpack-specific/modpack-instructions.md) by [Radk6](https://github.com/Radk6),
it is not a directly useful guide, but it will help you a ton.
