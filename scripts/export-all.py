import subprocess

export_modrinth_path = "../Modrinth/scripts/export-modrinth.py"

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

run_script(export_modrinth_path)