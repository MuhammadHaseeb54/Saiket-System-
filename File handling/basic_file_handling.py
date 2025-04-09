# Task 03
# Basic File Handling

import os
def file_handling(filepath, finding_word, replacement_of_word):
    try:
        # Check if file exists
        if not os.path.exists(filepath):
            raise FileNotFoundError("Error! The file does not exist.")
        # Read the file
        with open(filepath, 'r') as file:
            content = file.read()
        # Replace the word
        modified_content = content.replace(finding_word, replacement_word)   
        # Write back to the file
        with open(filepath, 'w') as file:
            file.write(modified_content)
        print("Word replacement successful!")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError:
        print("Error: Unable to read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filepath = "sample.txt"  
finding_word = "combined"   
replacement_word = "system"  

file_handling(filepath, finding_word, replacement_word)




