import datetime
import re

def extract_problem_name(url):
    # Extracts the problem title from the URL
    match = re.search(r'problems/([^/]+)/', url)
    if match:
        return match.group(1).replace('-', ' ').title()
    return "Unknown Problem"

def log_problem_to_readme(url):
    # Extract problem name and time of entry
    problem_name = extract_problem_name(url)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Format the entry for README.md
    entry = f"- [{problem_name}]({url}) - Completed on {timestamp}\n"

    # Append the entry to README.md
    with open("README.md", "a") as f:
        f.write(entry)

    print(f"Logged: {problem_name}")

if __name__ == "__main__":
    # Input from the user
    url = input("Enter LeetCode problem URL: ").strip()

    if "leetcode.com/problems" in url:
        log_problem_to_readme(url)
    else:
        print("Invalid URL. Please provide a valid LeetCode problem link.")
