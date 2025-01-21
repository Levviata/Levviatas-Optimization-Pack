import subprocess
import json
import os

def run_export():
    """
    Executes the Modrinth export command using packwiz.exe and checks its success.

    Returns:
        bool: True if the command runs successfully, False otherwise.
    """
    command_modrinth = ["packwiz.exe", "modrinth", "export"]

    try:
        # Execute the command and check if it runs successfully
        result = subprocess.run(command_modrinth, check=True)
        print("Command executed successfully!")
        return True  # Success
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        print(f"Error output: {e}")
        return False  # Failure
    except FileNotFoundError:
        print("Error: packwiz.exe not found. Please ensure it's in your PATH or the correct directory.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

os.chdir('../Modrinth')

# Step 1: Execute the Modrinth export command
hasRun = run_export()

if hasRun:
    # Pause execution and wait for user input
    input("Exported modrinth modpack, please check the contents. Run enter when finished to upload.")
if not hasRun:
    print("Did not export modrinth modpack.")