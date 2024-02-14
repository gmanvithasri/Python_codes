import requests

def count_files_in_repo(repo_url):
    response = requests.get(repo_url)
    if response.status_code != 200:
        print(f"Failed to retrieve repository data: {response.status_code}")
        return 0

    repo_content = response.json()
    return sum(1 for item in repo_content if item['type'] == 'file')

def main():
    user = input("Enter the GitHub username: ")
    repo = input("Enter the repository name: ")
    api_url = f"https://api.github.com/repos/{user}/{repo}/contents"

    file_count = count_files_in_repo(api_url)
    print(f"The total number of files in the repository '{repo}' is: {file_count}")

if __name__ == "__main__":
    main()
