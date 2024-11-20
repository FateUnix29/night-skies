import os
import fileinput
from pathlib import Path

def replace_in_files(directory):
    # Walk through all files and directories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Skip .git directory and binary files
            if '.git' in root or any(file.endswith(ext) for ext in ['.pyc', '.pyo', '.so', '.dll']):
                continue
                
            filepath = Path(root) / file
            try:
                # Try to read the file as text
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # If the file contains the target string
                if 'night-skies' in content.lower() or 'night_skies' in content.lower():
                    print(f"Processing: {filepath}")
                    
                    # Perform replacements
                    new_content = content.replace('night-skies', 'night-skies')
                    new_content = new_content.replace('night_skies', 'night_skies')
                    new_content = new_content.replace('NightSkies', 'NightSkies')
                    
                    # Write the changes back
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                        
            except UnicodeDecodeError:
                # Skip files that can't be read as text
                continue
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    # Get the current directory
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Ask for confirmation
    print(f"This will replace all instances of 'night-skies' with 'night-skies' in {current_dir}")
    response = input("Do you want to continue? (y/N): ")
    
    if response.lower() == 'y':
        replace_in_files(current_dir)
        print("Replacement complete!")
    else:
        print("Operation cancelled.")