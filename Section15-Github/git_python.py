import git

repo_url = "https://github.com/rodosilva/pythonForDevOps.git"
clone_dir = "/home/rodrigo/pythonForDevOps/Section15-Github/test-repo-clone"

# Cloning using gitPython Library
try:
    output = git.Repo.clone_from(repo_url, clone_dir)
    print(output)
except git.GitError as e:
    print(f"Error cloning the repo: {e}")





