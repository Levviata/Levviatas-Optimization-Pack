# Levviata's Optimization Pack (Optimum)
_A Forge 1.12.2 only modpack with pure optimizations and nothing else._

A Forge/~~Cleanroom~~ ([Cleanroom](https://discord.com/invite/f2K4aSpG4F) support is planned) modpack
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

## Links
Modrinth: https://modrinth.com/modpack/levviatas-optimization-pack

CurseForge: https://www.curseforge.com/minecraft/modpacks/levviatas-optimization-pack

GitHub: https://github.com/Levviata/Levviatas-Optimization-Pack (source)

## Performance Comparisons
_These are rough comparisons and not 100% correct or absolute, depending on hardware; performance can be worse, better, or even neither, take these comparisons with a grain of salt._

### Setup

<details>
<summary>Hardware/Specs</summary>

```
OS Name	Microsoft Windows 10 Pro
Version	10.0.19045 Build 19045

Processor AMD Ryzen 5 3600 6-Core Processor, 3600 Mhz, 6 Core(s), 12 Logical Processor(s)

Gpu Name NVIDIA GeForce GTX 1650

Installed Physical Memory (RAM)	16.0 GB
Total Physical Memory 15.9 GB

Storage Model KINGSTON SA400S37240G
```

</details>

<details>
<summary>Game Specs</summary>

Forge Mod Loader version 14.23.5.2860 for Minecraft 1.12.2 (Latest Forge version for Minecraft 1.12.2)

Java: jdk-8.0.442.6-hotspot (Adoptium Java 8)

Java Arguments:
[-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump, -Xms512m, -Xmx4096m, -Duser.language=en]

(
```
Minimum memory allocation: 512 mb of ram
Maximum memory allocation: 4096 mb of ram
```

We are using 4GBs of ram to run the game basically.

)

Game Launcher: PolyMC v6.1

Mods:

```
!configanytime-3.0.jar
!mixinbooter-10.4.jar
!mod-director-launchwrapper-1.8.3.jar
!Red-Core-MC-1.7-1.12-0.5.1.jar
Alfheim-1.4.jar
betterbiomeblend-1.12.2-1.1.7-forge.jar
censoredasm5.21.jar
Clumps-3.1.2.jar
EntityCulling-1.12.2-6.4.3.jar
MultithreadedNoise-1.12.2-0.0.2.jar
naughthirium-1.0.2.jar
Nothirium-1.12.2-0.3.4-beta.jar
particleculling-1.12.2-v1.4.3.jar
RenderLib-1.12.2-1.3.5.jar
Sledgehammer-1.12.2-2.0.26.jar
StellarCore-1.5.21.jar
vintagefix-0.5.1.jar

# Profiling mod added to, well, profile performance (CPU, GPU, ram, FPS, TPS, etc.)
flare-0.2.1.jar
```

_(my mod list was scraped off/extracted/got
using a Python script! This is probably not the proper way to do it, but you can find the script here!)_

</details>

<details>
<summary>Game configuration</summary>

```
version:1343
invertYMouse:false
mouseSensitivity:0.5
fov:1.0
gamma:0.0
saturation:0.0
renderDistance:16
guiScale:3
particles:1
bobView:true
anaglyph3d:false
maxFps:260
fboEnable:true
difficulty:2
fancyGraphics:false
ao:2
renderClouds:fast
resourcePacks:[]
incompatibleResourcePacks:[]
lastServer:
lang:en_us
chatVisibility:0
chatColors:true
chatLinks:true
chatLinksPrompt:true
chatOpacity:1.0
snooperEnabled:true
fullscreen:true
enableVsync:false
useVbo:true
hideServerAddress:false
advancedItemTooltips:false
pauseOnLostFocus:true
touchscreen:false
overrideWidth:0
overrideHeight:0
heldItemTooltips:true
chatHeightFocused:1.0
chatHeightUnfocused:0.44366196
chatScale:1.0
chatWidth:1.0
mipmapLevels:4
forceUnicodeFont:false
reducedDebugInfo:false
useNativeTransport:true
entityShadows:true
mainHand:right
attackIndicator:1
showSubtitles:false
realmsNotifications:true
enableWeakAttacks:false
autoJump:true
narrator:0
tutorialStep:none
key_key.attack:-100
key_key.use:-99
key_key.forward:17
key_key.left:30
key_key.back:31
key_key.right:32
key_key.jump:57
key_key.sneak:42
key_key.sprint:29
key_key.drop:16
key_key.inventory:18
key_key.chat:20
key_key.playerlist:15
key_key.pickItem:-98
key_key.command:53
key_key.screenshot:60
key_key.togglePerspective:63
key_key.smoothCamera:0
key_key.fullscreen:87
key_key.spectatorOutlines:0
key_key.swapHands:33
key_key.saveToolbarActivator:46
key_key.loadToolbarActivator:45
key_key.advancements:38
key_key.hotbar.1:2
key_key.hotbar.2:3
key_key.hotbar.3:4
key_key.hotbar.4:5
key_key.hotbar.5:6
key_key.hotbar.6:7
key_key.hotbar.7:8
key_key.hotbar.8:9
key_key.hotbar.9:10
soundCategory_master:0.5
soundCategory_music:1.0
soundCategory_record:1.0
soundCategory_weather:1.0
soundCategory_block:1.0
soundCategory_hostile:1.0
soundCategory_neutral:1.0
soundCategory_player:1.0
soundCategory_ambient:1.0
soundCategory_voice:1.0
modelPart_cape:true
modelPart_jacket:true
modelPart_left_sleeve:true
modelPart_right_sleeve:true
modelPart_left_pants_leg:true
modelPart_right_pants_leg:true
modelPart_hat:true
```

</details>

_(Note: FOV matters! The higher your FOV is, the more chunks on your screen that then need to be rendered!)_


## License

TLDR: Distribution and modification is allowed, but you can't use "Levviata's Optimization Pack" as your own trademark
("Optimum" is NOT trademarked as it is a common English word.)

That is a short summary of what is most important, please read the full license below:

License: https://github.com/Levviata/Levviatas-Optimization-Pack/blob/main/LICENSE.txt