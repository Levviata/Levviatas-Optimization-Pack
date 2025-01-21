import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the variables
token = os.getenv('MODRINTH_TOKEN')
project_id = os.getenv('MODRINTH_PROJECT_ID')

# API URL (use the staging URL for testing)
API_URL = f"https://api.modrinth.com/v2/project/{project_id}"

summary_path = "SUMMARY.md"
description_path = "README.md"


def read_markdown_file(file_path):
    """
    Reads the contents of a Markdown file.

    Args:
        file_path (str): The path to the Markdown file.

    Returns:
        str: The contents of the file if read successfully.
        None: If the file cannot be read.

    Raises:
        FileNotFoundError: If the file does not exist.
        Exception: For other errors during file reading.
    """
    try:
        # Open the file in read mode
        with open(file_path, "r", encoding="utf-8") as file:
            # Read and return the contents of the file
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


summary = read_markdown_file(summary_path)
description = read_markdown_file(description_path)

# Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Request body (modify the fields as needed)
payload = {
    "description": summary,
    "body": "test"
}

# Make the PATCH request
response = requests.patch(API_URL, json=payload, headers=HEADERS)

# Check response
if response.status_code == 204:
    print("Project modified successfully!")
elif response.status_code == 401:
    print("Authentication Error: Invalid Authentication Credentials")
    print("Response:", response.json())
elif response.status_code == 404:
    print("Error: Project not found or no authorization to access it.")
    print("Response:", response.json())
else:
    print(f"Unexpected status code: {response.status_code}")
    print("Response:", response.text)
