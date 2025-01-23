import os
import subprocess
import json

update_info_path = "../Modrinth/scripts/update-modrinth-info.py"

set_metadata_path = "../scripts/set-metadata-all.py"

get_modrinth_dependencies_path = "../Modrinth/scripts/get-modrinth-dependencies.py"
get_curseforge_dependencies_path = "../CurseForge/scripts/get-curseforge-dependencies.py"

export_modrinth_path = "../Modrinth/scripts/export-modrinth.py"
export_curseforge_path = "../CurseForge/scripts/export-curseforge.py"

release_modrinth_path = "../Modrinth/scripts/release-modrinth.py"
release_curseforge_path = "../CurseForge/scripts/release-curseforge.py"

clean_data_path = "../scripts/clean-data.py"


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

# Step 1: Update summary and description of our project in modrinth (cant on curseforge for now)
print("Starting Phase 1")
run_script(update_info_path)

# Step 2: Set inherited metadata
print("Starting Phase 2")
run_script(set_metadata_path)

# Step 3: Get dependencies
print("Starting Phase 3")
run_script(get_modrinth_dependencies_path)
run_script(get_curseforge_dependencies_path)

# Step 4: Export
print("Starting Phase 4")
run_script(export_modrinth_path)
run_script(export_curseforge_path)

# Check if run, true = prompt user to check files
with open("../data/has_run_modrinth.json", "r") as file:
    hasRunModrinthData = json.load(file)

with open("../data/has_run_curseforge.json", "r") as file:
    hasRunCurseForgeData = json.load(file)

hasRunModrinth = hasRunModrinthData["hasRunModrinth"]
hasRunCurseForgeData = hasRunCurseForgeData["hasRunCurseForge"]

if not hasRunModrinth:
    run_script(clean_data_path)
    exit()
if not hasRunModrinth:
    run_script(clean_data_path)
    exit()

# Step 5: Release
print("Starting Phase 5")
run_script(release_modrinth_path)
run_script(release_curseforge_path)

# Step 6: Clean data (to avoid using it in case we error out)
print("Starting Phase 6")
run_script(clean_data_path)

print("End of script")
