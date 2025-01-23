import os
import toml
import json

# Directory where your mods are located
mods_directory = "../Modrinth/mods"

# List to hold dependencies
dependencies = []

# We can actually skip dependencies to package so that's nice
skip_list = ["flare.pw.toml",
             "raw-mouse-input-blessed-edition.pw.toml"
             ]

# Loop through all TOML files in the 'mods' folder
for mod in os.listdir(mods_directory):
    if mod.endswith(".pw.toml"):  # Look for files with the .pw.toml extension
        mod_file_path = os.path.join(mods_directory, mod)

        if mod in skip_list:
            print(f"Skipping {mod}!")
            continue  # Skip this file and move to the next iteration

        if not skip_list:
            print("Skipped all mods!")

        # Load the TOML file
        with open(mod_file_path, 'r') as toml_file:
            mod_data = toml.load(toml_file)

        # Extract the mod ID and version from the '[update.modrinth]' section
        if "update" in mod_data and "modrinth" in mod_data["update"]:
            mod_id = mod_data["update"]["modrinth"].get("mod-id")
            mod_version = mod_data["update"]["modrinth"].get("version")

            if mod_id and mod_version:
                # Add the dependency to the list
                dependencies.append({
                    "project_id": mod_id,
                    "version_id": mod_version,
                    "dependency_type": "required"
                })
# Save to a file
with open("../data/dependencies_modrinth.json", "w") as file:
    json.dump(dependencies, file)