import subprocess

# Define the URL
repo_url = "https://github.com/rodosilva/pythonForDevOps.git"

# Define the directory to clone into
clone_dir = "/home/rodrigo/pythonForDevOps/Section15-Github/test-repo-clone"

# Run the git clone command
subprocess.run(["git", "clone", repo_url, clone_dir])


