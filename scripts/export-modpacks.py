import os
import glob
import subprocess
import re
import time  # Import time for sleep

commandModrinth = ["packwiz.exe", "modrinth", "export"]  # Export Modrinth
commandCurseForge = ["packwiz.exe", "curseforge", "export"]  # Export CurseForge

def find_modpack_file(search_dir, prefix):
    pattern = os.path.join(search_dir, f"{prefix}*")
    files = glob.glob(pattern)
    return files[0] if files else None

def delete_old_files(search_dir, prefix):
    pattern = os.path.join(search_dir, f"{prefix}*")
    old_files = glob.glob(pattern)
    
    for old_file in old_files:
        try:
            os.remove(old_file)
            print(f"Deleted old file: {old_file}")
        except Exception as e:
            print(f"Error deleting file {old_file}: {e}")

def extract_version(text):
    # Regular expression pattern to match a version like "0.0.0"
    version_pattern = r"\b\d+\.\d+\.\d+\b"
    
    # Search for the pattern in the given text
    match = re.search(version_pattern, text)
    
    # If a match is found, return the version, else return None
    return match.group(0) if match else None

if __name__ == "__main__":
    shouldRetry = True
    max_retries = 5  # Set the maximum number of retries
    retry_count = 0  # Initialize the retry counter

    # Get the current script directory and go one level behind
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    
    # Change the working directory to the parent directory
    os.chdir(parent_dir)

    delete_old_files(parent_dir, "Optimum")

    # Export Modrinth
    while shouldRetry:
        # Run the Modrinth export command and capture the result
        result = subprocess.run(commandModrinth, check=False)  # check=False so we can handle errors manually

        if result.returncode == 0:
            shouldRetry = False  # Stop retrying if the command is successful

            # Ensure the file is generated before renaming
            print(f"Current directory is now: {os.getcwd()}")
            FILE = find_modpack_file(parent_dir, "Optimum")

            if FILE:
                version = extract_version(FILE)
                # Rename the file for Modrinth with .mrpack
                new_file_modrinth = os.path.join(parent_dir, f"Optimum-Modrinth-{version}.mrpack")
                os.rename(FILE, new_file_modrinth)
                print(f"Modrinth file renamed to {new_file_modrinth}")
            else:
                print("No file found to rename for Modrinth.")
        else:
            retry_count += 1
            print(f"Modrinth command failed. Retry {retry_count}/{max_retries}...")

            if retry_count >= max_retries:
                print("Max retries reached for Modrinth. Exiting.")
                break  # Exit the loop if the retry limit is reached
            else:
                time.sleep(2)  # Sleep for 2 seconds before retrying

    # Reset retry logic for CurseForge export
    shouldRetry = True
    retry_count = 0

    # Export CurseForge
    while shouldRetry:
        # Run the CurseForge export command and capture the result
        result = subprocess.run(commandCurseForge, check=False)  # check=False so we can handle errors manually

        if result.returncode == 0:
            shouldRetry = False  # Stop retrying if the command is successful

            # Ensure the file is generated before renaming
            print(f"Current directory is now: {os.getcwd()}")
            FILE = find_modpack_file(parent_dir, "Optimum")

            if FILE:
                version = extract_version(FILE)
                # Rename the file for CurseForge with .zip
                new_file_curseforge = os.path.join(parent_dir, f"Optimum-CurseForge-{version}.zip")
                os.rename(FILE, new_file_curseforge)
                print(f"CurseForge file renamed to {new_file_curseforge}")
            else:
                print("No file found to rename for CurseForge.")
        else:
            retry_count += 1
            print(f"CurseForge command failed. Retry {retry_count}/{max_retries}...")

            if retry_count >= max_retries:
                print("Max retries reached for CurseForge. Exiting.")
                break  # Exit the loop if the retry limit is reached
            else:
                time.sleep(2)  # Sleep for 2 seconds before retrying
