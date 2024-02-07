import subprocess

def fetch_and_checkout_branch(repo_name, branch_name):
    # Fetch the latest changes from the specified branch
    subprocess.run(['git', 'fetch', repo_name, branch_name])

    # Checkout the specified branch
    subprocess.run(['git', 'checkout', branch_name])

def print_changes(repo_name, branch_name):
    # Print the changes between the specified branch and master
    print("\n===== Code Changes =====\n")
    subprocess.run(['git', 'diff', f'master..{branch_name}'])

    print("\n===== Commit History =====\n")
    subprocess.run(['git', 'log', '--oneline', f'master..{branch_name}'])

if __name__ == "__main__":
    repo_name = input("Enter the name of the repository: ")
    branch_name = input("Enter the name of the branch you want to compare with master: ")

    fetch_and_checkout_branch(repo_name, branch_name)
    print_changes(repo_name, branch_name)
