import os
import requests
from dotenv import load_dotenv
from pathlib import Path
import json
import toml

# Load environment variables from the .env file
load_dotenv()

# Access the variables
token = os.getenv('MODRINTH_TOKEN')
project_id = os.getenv('MODRINTH_PROJECT_ID')

def run():
    try:
        # Check if run, true = prompt user to check files
        with open("../data/has_run.json", "r") as file:
            hasRunData = json.load(file)

        hasRunModrinth = hasRunData["hasRunModrinth"]
        if hasRunModrinth:
            os.chdir('..')

            file_to_upload = None

            for filename in os.listdir(os.getcwd()):
                if filename.startswith("Optimum"):
                    file_to_upload = filename
                    break

            if not file_to_upload:
                print("No file starting with 'Optimum' found.")
                exit()

            # Load data from pack.toml
            with open("../Modrinth/pack.toml", 'r') as file:
                modrinth_project_data = toml.load(file)


            with open("../data/dependencies_modrinth.json", "r") as file:
                data = json.load(file)

            # Extract data from the TOML file
            name = modrinth_project_data['name']
            version = modrinth_project_data['version']
            minecraft_version = modrinth_project_data['versions']['minecraft']

            # Step 4: Create the data for the request using the extracted information
            data = {
                "name": name + " v" + version,  # Name of the version
                "version_number": version,  # Version number
                "changelog": f"- Changelog is on [GitHub](https://github.com/Levviata/Levviatas-Optimization-Pack/releases/latest)",  # Change log
                "dependencies": data,  # Optional dependencies, if any
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
