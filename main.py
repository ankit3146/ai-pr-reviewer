import requests
from urllib.parse import urlparse

def fetch_pull_request_files(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split("/")
    owner = path_parts[1]
    repo = path_parts[2]
    pull_number = path_parts[4]
    
    api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"
    
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch pull request files. Status code: {response.status_code}")
        return None

def main():
    pr_url = input("Enter the GitHub pull request URL: ")

    files = fetch_pull_request_files(pr_url)
    if files:
        print("Files in the pull request:")
        for file in files:
            print(file["filename"])
    else:
        print("Failed to fetch pull request files.")

if __name__ == "__main__":
    main()
