import os
import glob
import subprocess
import requests

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

export_script = os.path.join(current_dir, "export-modpack.py")  # packwiz

def find_modpack_file(search_dir, prefix):
    """Find the first file in the directory that starts with the given prefix."""
    pattern = os.path.join(search_dir, f"{prefix}*")
    files = glob.glob(pattern)
    return files[0] if files else None

def upload_modpack_curseforge(api_key, project_id, modpack_path, changelog, release_type, game_versions):
    url = f"https://minecraft.curseforge.com/api/projects/{project_id}/upload-file"
    headers = {
        "X-Api-Token": api_key
    }
    metadata = {
        "changelog": changelog,
        "releaseType": release_type,  # e.g., "release", "beta", or "alpha"
        "gameVersions": game_versions
    }

    with open(modpack_path, "rb") as modpack_file:
        files = {
            "file": modpack_file,
            "metadata": (None, str(metadata))
        }

        response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        print("Modpack uploaded successfully to CurseForge!")
        print(response.json())  # Display response details
    else:
        print(f"Failed to upload modpack to CurseForge. Status code: {response.status_code}")
        print(response.text)


def upload_modpack_modrinth(api_key, project_id, modpack_path, changelog, release_type, game_versions):
    url = f"https://api.modrinth.com/v2/projects/{project_id}/versions"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    # Construct the JSON payload
    payload = {
        "loaders": game_versions,  # Example: [ "minecraft" ] or [ "fabric", "forge" ]
        "changelog": changelog,
        "version_type": release_type,  # e.g., "release", "beta", or "alpha"
        "files": [
            {
                "file": open(modpack_path, "rb"),
                "filename": os.path.basename(modpack_path)
            }
        ]
    }

    files = {
        "file": payload["files"][0]["file"]
    }

    response = requests.post(url, headers=headers, files=files, data=json.dumps(payload))

    if response.status_code == 201:
        print("Modpack uploaded successfully to Modrinth!")
        print(response.json())  # Display response details
    else:
        print(f"Failed to upload modpack to Modrinth. Status code: {response.status_code}")
        print(response.text)

def get_changelog():
    print("Enter the changelog for this version. Press Enter on an empty line to finish.")
    changelog_lines = []
    while True:
        line = input("> ").strip()  # Collect each line of the changelog
        if line == "":  # Stop when an empty line is entered
            break
        changelog_lines.append(line)  # Add the line to the list
    return "\n".join(changelog_lines)  # Join all lines with a newline character



if __name__ == "__main__":
    subprocess.run(["python", export_script], check=True)
    
    API_KEY_CURSEFORGE = "ddfb7261-68d5-499f-9098-c2411434e731"
    PROJECT_ID_CURSEFORGE = "1183185"

    # Search for the modpack file
    SEARCH_DIR = input("Enter the directory to search for the modpack: ").strip()

    MODRINTH_PREFIX = "Optimum-Modrinth"
    CURSEFORGE_PREFIX = "Optimum-CurseForge"

    MODRINTH_PATH = find_modpack_file(SEARCH_DIR, MODRINTH_PREFIX)
    CURSEFORGE_PATH = find_modpack_file(SEARCH_DIR, CURSEFORGE_PREFIX)

    if not MODRINTH_PATH:
        print(f"No file starting with '{MODRINTH_PREFIX}' found in the directory '{SEARCH_DIR}'.")
        exit(1)  # Exit the program if no file is found

    if not CURSEFORGE_PATH:
        print(f"No file starting with '{CURSEFORGE_PREFIX}' found in the directory '{SEARCH_DIR}'.")
        exit(1)  # Exit the program if no file is found

    print(f"Found modpack: {MODRINTH_PATH}")
    print(f"Found modpack: {CURSEFORGE_PATH}")

    CHANGELOG = get_changelog()

    GAME_VERSIONS = [7498, 6756]  # forge + 1.12.2 (in id form)

    RELEASE_TYPE_OPTIONS = ["release", "beta", "alpha"]
    RELEASE_TYPE = input(f"Enter the release type ({', '.join(RELEASE_TYPE_OPTIONS)}): ").strip().lower()
    while RELEASE_TYPE not in RELEASE_TYPE_OPTIONS:
        print("Invalid release type. Please choose one of: release, beta, alpha.")
        RELEASE_TYPE = input(f"Enter the release type ({', '.join(RELEASE_TYPE_OPTIONS)}): ").strip().lower()

    upload_modpack_modrinth(API_KEY, PROJECT_ID, MODRINTH_PATH, CHANGELOG, RELEASE_TYPE, GAME_VERSIONS)
    upload_modpack_curseforge(API_KEY, PROJECT_ID, CURSEFORGE_PATH, CHANGELOG, RELEASE_TYPE, GAME_VERSIONS)
