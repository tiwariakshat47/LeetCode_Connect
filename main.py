import datetime
import re
import subprocess

def extract_problem_name(url):
    match = re.search(r'problems/([^/]+)/', url)
    if match:
        return match.group(1).replace('-', ' ').title()
    return "Unknown Problem"

def log_problem_to_readme(url):
    problem_name = extract_problem_name(url)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    entry = f"- [{problem_name}]({url}) - Completed on {timestamp}\n"

    with open("README.md", "a") as f:
        f.write(entry)

    print(f"Logged: {problem_name}")

def git_commit():
    try:
        subprocess.run(["git", "add", "README.md"], check=True)
        
        commit_message = "Update LeetCode Tracker"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        print("Changes committed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Git operation: {e}")

if __name__ == "__main__":
    while True:
        url = input("Enter LeetCode problem URL: ").strip()

        if "leetcode.com/problems" in url:
            log_problem_to_readme(url)
        else:
            print("Invalid URL. Please provide a valid LeetCode problem link.")

        more = input("Do you have more problems to log? (Y/N): ").strip().lower()

        if more != 'y':
            print("Exiting LeetCode Tracker.")
            git_commit()
            break
