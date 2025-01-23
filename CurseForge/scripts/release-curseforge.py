import os
import requests
from dotenv import load_dotenv
from pathlib import Path
import json
import toml

# Load environment variables from the .env file
load_dotenv()

# Access the variables
api_key = os.getenv('CURSEFORGE_TOKEN')
project_id = os.getenv('CURSEFORGE_PROJECT_ID')  # CurseForge project ID

# Set the base URL for CurseForge API
BASE_URL = "https://minecraft.curseforge.com"

def run():
    try:
        # Check if the script should run (like in your Modrinth script)
        with open("../data/has_run_curseforge.json", "r") as file:
            hasRunData = json.load(file)

        hasRunCurseForge = hasRunData["hasRunCurseForge"]
        if hasRunCurseForge:
            os.chdir('../CurseForge')

            file_to_upload = None
            for filename in os.listdir(os.getcwd()):
                if filename.startswith("Optimum"):
                    file_to_upload = filename
                    break

            if not file_to_upload:
                print("No file starting with 'Optimum' found.")
                exit()

            # Load metadata from pack.toml
            with open("../CurseForge/pack.toml", 'r') as file:
                curseforge_project_data = toml.load(file)

            # Extract data
            name = curseforge_project_data['name']
            version = curseforge_project_data['version']
            minecraft_version = curseforge_project_data['versions']['minecraft']

            # Prepare the data payload
            data = {
                "changelog": "Changelog available on [GitHub](https://github.com/Levviata/Levviatas-Optimization-Pack/releases/latest)",
                "changelogType": "markdown",
                "releaseType": "beta",  # Can be 'release', 'beta', or 'alpha'
                "gameVersions": [6756],
                "displayName": f"{name} v{version}",  # Version display name
            }

            print(f"Request data: {data}")

            url = f"{BASE_URL}/api/projects/{project_id}/upload-file"
            headers = {
                'X-Api-Token': api_key  # CurseForge API key
            }

            with open(file_to_upload, 'rb') as file:
                files = {
                    'metadata': (None, json.dumps(data), 'application/json'),
                    'file': (Path(file_to_upload).name, file)
                }
                response = requests.post(url, headers=headers, files=files)

            print(f"Response code: {response.status_code}")
            if response.status_code == 200:
                print("Success!")
                print(f"Response body:\n{response.text}")
            else:
                print(f"{response.status_code}: {response.reason}\nResponse body:\n{response.text}\nRequest data:\n{data}")
                return
    except Exception as e:
        print(e)
        raise


if __name__ == '__main__':
    run()
