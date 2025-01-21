import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Authentication
token = os.getenv('GITHUB_TOKEN')
headers = {"Authorization": f"token {token}"}

# Step 1: Create a release
release_url = "https://api.github.com/repos/Levviata/Levviatas-Optimization-Pack/releases"
release_data = {
    "tag_name": "v1.0.0",
    "target_commitish": "main",
    "name": "v1.0.0",
    "body": "Release notes for v1.0.0",
    "draft": False,
    "prerelease": False,
}
response = requests.post(release_url, json=release_data, headers=headers)
response.raise_for_status()
release_id = response.json()["id"]

# Step 2: Upload the asset
upload_url = f"https://uploads.github.com/repos/Levviata/Levviatas-Optimization-Pack/releases/{release_id}/assets?name={file_to_upload_modrinth}"
with open(file_to_upload_modrinth, "rb") as file:
    headers["Content-Type"] = "application/octet-stream"
    upload_response = requests.post(upload_url, headers=headers, data=file)
    upload_response.raise_for_status()



print("End of release github script.")