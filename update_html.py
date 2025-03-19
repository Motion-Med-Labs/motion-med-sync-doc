import re
import subprocess

def replace_markdown_data():
    # Read the data_fields.MD file
    with open('data/data_fields.MD', 'r') as md_file:
        md_data = md_file.read()

    # Use the markdown content directly without modifications
    processed_md = md_data

    # Read the data_fields.html file
    with open('data_fields.html', 'r') as html_file:
        html_content = html_file.read()

    # Create the replacement string with the processed markdown content
    replacement = f"const markdownContent = `{processed_md}`;"

    # Define the pattern to match the existing markdownContent declaration
    pattern = r'const\s+markdownContent\s*=\s*`[\s\S]*?`;'

    # Replace the matched content with the new data
    new_content = re.sub(pattern, replacement, html_content)

    # Write the modified content back to data_fields.html
    with open('data_fields.html', 'w') as html_file:
        html_file.write(new_content)

    # Run Prettier on the updated file
    try:
        subprocess.run(['npx', 'prettier', '--write', 'data_fields.html'], check=True)
        print("Successfully formatted data_fields.html with Prettier")
    except subprocess.CalledProcessError as e:
        print(f"Error running Prettier: {str(e)}")

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

    # Run Prettier on the updated file
    try:
        subprocess.run(['npx', 'prettier', '--write', 'index.html'], check=True)
        print("Successfully formatted index.html with Prettier")
    except subprocess.CalledProcessError as e:
        print(f"Error running Prettier: {str(e)}")

if __name__ == "__main__":
    try:
        replace_requirements_data()
        print("Successfully replaced requirementsData in index.html")
        replace_markdown_data()
        print("Successfully replaced markdownContent in data_fields.html")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
