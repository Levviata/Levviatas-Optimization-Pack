import toml
import os
from dotenv import load_dotenv
from github import Github

load_dotenv()
# Authentication
token = os.getenv('GITHUB_TOKEN')

# Authenticate with your GitHub token
g = Github(token)

# Get the repository object
repo = g.get_repo(f"Levviata/Levviatas-Optimization-Pack")

with open("../inherited_metadata.toml", 'r') as file:
    metadata = toml.load(file)

# Get the list of draft releases
draft_releases = [release for release in repo.get_releases() if release.tag_name == "v" + metadata["version"]]

for release in draft_releases:
    print(f"Draft Release: {release.title} (Tag: {release.tag_name})")



print("End of release github script.")