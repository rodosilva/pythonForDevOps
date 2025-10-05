# Import the Github class from the PyGithub library
import os
from github import Github
from github import Auth

# Provide the Github Personal Access Token
# using an access token
personal_token = os.getenv("GITHUB_TOKEN")
auth = Auth.Token(personal_token)

# First create a Github instance:
g = Github(auth=auth)

# We will Fetch the USER information from the Github Account
# Print the authenticated User
user = g.get_user()
print(f"Authenticated as: {user.login}")

# View the Number of Public Repositories
print(f"Public Repos: {user.public_repos}")

# List of followers
print(f"Followers: {user.followers}")

# List of Repositories
for repo in user.get_repos():
    print(f"Repo Name: {repo.name}")

#Create a new repository
repo_name = "new_repo_from_pygithub"
repo = user.create_repo(repo_name)

print(f"Creating repository: {repo.name}")






