import os
import toml
import json

# Directory where your mods are located
mods_directory = "../CurseForge/mods"

# List to hold dependencies
dependencies = []

# Loop through all TOML files in the 'mods' folder
for mod in os.listdir(mods_directory):
    if mod.endswith(".pw.toml"):  # Look for files with the .pw.toml extension
        mod_file_path = os.path.join(mods_directory, mod)

        # Load the TOML file
        with open(mod_file_path, 'r') as toml_file:
            mod_data = toml.load(toml_file)

        # Remove `.pw.toml` from the filename to get the slug
        mod_name = mod.replace(".pw.toml", "")

        dependencies.append({
            "slug": mod_name,
            "type": "embeddedLibrary"
         })
# Save to a file
with open("../data/dependencies_curseforge.json", "w") as file:
    json.dump(dependencies, file)