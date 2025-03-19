import json
import re

def replace_requirements_data():
    # Read the requirements.json file
    with open('data/requirements.json', 'r') as json_file:
        json_data = json_file.read()

    # Read the index.html file
    with open('index.html', 'r') as html_file:
        html_content = html_file.read()

    # Create the replacement string
    replacement = f"const requirementsData = {json_data};"

    # Define the pattern to match the existing requirementsData declaration
    pattern = r'const\s+requirementsData\s*=\s*{[\s\S]*?};'

    # Replace the matched content with the new data
    new_content = re.sub(pattern, replacement, html_content)

    # Write the modified content back to index.html
    with open('index.html', 'w') as html_file:
        html_file.write(new_content)

if __name__ == "__main__":
    try:
        replace_requirements_data()
        print("Successfully replaced requirementsData in index.html")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
