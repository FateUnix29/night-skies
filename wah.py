import os
import fileinput
from pathlib import Path

def replace_in_files(directory):
    # Walk through all files and directories
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            # Skip .git directory and binary files
            if '.git' in root or any(file.endswith(ext) for ext in ['.pyc', '.pyo', '.so', '.dll']):
                continue
                
            filepath = Path(root) / file

            if filepath.name == 'wah.py':
                continue # This file should not be overwritten
            
            try:
                # Try to read the file as text
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # If the file contains the target string
                find_list = ['open-webui', 'open_webui', 'OpenWebUI', 'openwebui']
                if any(find_str in content.lower() for find_str in find_list):
                    print(f"Processing: {filepath}")
                    
                    # Perform replacements
                    new_content = content.replace('open-webui', 'night-skies')
                    new_content = new_content.replace('open_webui', 'night_skies')
                    new_content = new_content.replace('OpenWebUI', 'NightSkies')
                    new_content = new_content.replace('openwebui', 'nightskies')
                    
                    # Write the changes back
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                # If the file/dir name itself contains open-webui or openwebui or whatever
                find_list2 = ['open-webui', 'open_webui', 'OpenWebUI', 'openwebui']

                if any(find_str in filepath.name.lower() for find_str in find_list2):
                    new_name = filepath.name.replace('open-webui', 'night-skies')
                    new_name = new_name.replace('open_webui', 'night_skies')
                    new_name = new_name.replace('OpenWebUI', 'NightSkies')
                    new_name = new_name.replace('openwebui', 'nightskies')
                    new_filepath = filepath.with_name(new_name)
                    filepath.rename(new_filepath)
                        
            except UnicodeDecodeError:
                # Skip files that can't be read as text
                continue
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    # Get the current directory
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Ask for confirmation
    print(f"This will replace all instances of 'open-webui' with 'night-skies' in {current_dir}")
    response = input("Do you want to continue? (y/N): ")
    
    if response.lower() == 'y':
        replace_in_files(current_dir)
        print("Replacement complete!")
    else:
        print("Operation cancelled.")