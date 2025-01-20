import subprocess
import os
import requests
from dotenv import load_dotenv
import toml
from pathlib import Path
import json

API_URL = 'https://api.modrinth.com/v2'

def run():
    try:
        # Load environment variables from the .env file
        load_dotenv()

        # Access the variables
        token = os.getenv('MODRINTH_TOKEN')
        project_id = os.getenv('MODRINTH_PROJECT_ID')

        # Directory where your mods are located
        mods_directory = "./mods"

        # List to hold dependencies
        dependencies = []

        skip_list = []

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
                            "dependency_type": "required"  # You can modify this depending on the mod's usage
                        })

        # Step 1: Execute the Modrinth export command
        commandModrinth = ["packwiz.exe", "modrinth", "export"]
        subprocess.run(commandModrinth, check=True)

        # Pause execution and wait for user input
        response = input("Exported modrinth modpack, please check the contents. Run enter when finished to upload.")

        # Step 2: Search for the output file starting with "Optimum"
        output_dir = "./" # same folder
        file_to_upload = None

        for filename in os.listdir(output_dir):
            if filename.startswith("Optimum"):
                file_to_upload = filename
                break

        if not file_to_upload:
            print("No file starting with 'Optimum' found.")
            exit()

        # Step 3: Read project data from the TOML file (pack.toml)
        toml_file_path = "pack.toml"  # The TOML file is in the same folder as the script

        # Load the TOML file
        with open(toml_file_path, 'r') as toml_file:
            project_data = toml.load(toml_file)

        # Extract data from the TOML file
        name = project_data['name']
        version = project_data['version']
        minecraft_version = project_data['versions']['minecraft']

        # Step 4: Create the data for the request using the extracted information
        data = {
            "name": name + " v" + version,  # Name of the version
            "version_number": version,  # Version number
            "changelog": f"- Changelog is on [GitHub](https://github.com/Levviata/Levviatas-Optimization-Pack/releases/latest)",  # Change log
            "dependencies": dependencies,  # Optional dependencies, if any
            "game_versions": [minecraft_version],  # Supported game versions (Minecraft version from TOML)
            "version_type": "beta",  # Release type (e.g., 'release', 'beta')
            "loaders": ["forge"],  # Mod loader
            "featured": True,  # Whether it's featured or not
            "status": "listed",  # Status (e.g., 'listed', 'unlisted')
            "requested_status": "listed",
            "project_id": project_id,  # Project ID
            'file_parts': [Path(file_to_upload).name]
        }

        print(f"Request body: {data}")
        url = "https://api.modrinth.com/v2/version"
        headers = {
            'Authorization': token
        }

        with open(file_to_upload, 'rb') as file:
            files = {
                'data': (None, json.dumps(data), 'application/json'),
                'file': (Path(file_to_upload).name, file)
            }
            response = requests.post(url, headers=headers, files=files)

        print(f"Response code: {response.status_code}")
        if response.status_code == 200:
            print("Success!")
            print(f"Response body:\n{response.text}")
        else:
            print(f"{response.status_code}: {response.reason}\nResponse body:\n{response.text}\nRequest body:\n{data}")
            return
    except Exception as e:
        print(e)
        raise


if __name__ == '__main__':
    run()
