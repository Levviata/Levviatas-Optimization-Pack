import subprocess
import json

update_info_path = "update-info.py"

set_metadata_path = "set-metadata-all.py"

get_modrinth_dependencies_path = "../Modrinth/get-modrinth-dependencies.py"

export_all_path = "export-all.py"

release_modrinth_path = "../Modrinth/release-modrinth.py"
release_curseforge_path = "CurseForge/release-curseforge.py"


def run_script(script_path):
    """
    Runs a Python script using the subprocess module.

    Args:
        script_path (str): Path to the Python script to be run.

    Returns:
        int: The exit code of the script.
    """
    try:
        result = subprocess.run(["python", script_path], check=True)
        print(f"Script '{script_path}' executed successfully.")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Script execution failed with error: {e}")
        return e.returncode

# Step 1: Update summary and description of our project in the website
run_script(update_info_path)

# Step 2: Set inherited metadata
run_script(set_metadata_path)

# Step 3: Get dependencies
run_script(get_modrinth_dependencies_path)

# Step 4: Export
run_script(export_all_path)

# Check if run, true = prompt user to check files
with open("../data/has_run.json", "r") as file:
    hasRunData = json.load(file)

hasRunModrinth = hasRunData["hasRunModrinth"]


# Step 5: Release
run_script(release_modrinth_path)
