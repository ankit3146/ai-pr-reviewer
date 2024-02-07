import subprocess

def get_repo_info():
    # Get the URL of the remote repository
    remote_url = subprocess.check_output(['git', 'remote', 'get-url', 'origin']).decode('utf-8').strip()
    # Extract the repository name from the URL
    repo_name = remote_url.split('/')[-1].replace('.git', '')

    # Get the name of the current branch
    current_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode('utf-8').strip()

    return repo_name, current_branch

def fetch_and_checkout_branch(branch_name):
    # Fetch the latest changes from the specified branch
    subprocess.run(['git', 'fetch', 'origin', branch_name])

    # Checkout the specified branch
    subprocess.run(['git', 'checkout', branch_name])

def get_changes(branch_name):
    # Get the changes between the specified branch and main
    output = subprocess.check_output(['git', 'diff', f'main..{branch_name}']).decode('utf-8')
    return output

if __name__ == "__main__":
    repo_name, current_branch = get_repo_info()
    print(f"Repository: {repo_name}")
    print(f"Current Branch: {current_branch}")

    fetch_and_checkout_branch(current_branch)
    changes = get_changes(current_branch)

    print("Changes:")
    print(changes)
