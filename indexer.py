import re
from collections import defaultdict

def tokenize(text: str) -> list[str]:
    #Convert text to lowercase and extract words using regex
    return re.findall(text.lower())

def build_index(files: list[str]) -> dict[str, dict[str, int]]:
    index = defaultdict(lambda: defaultdict(int)) # Initialize a nested defaultdict for the index

    for file in files: # Iterate over each file in the list of files
        try:
            with open(file, "r", encoding="utf-8") as f:
                text = f.read() # Read the entire content of the file into a string                

        except (FileNotFoundError, UnicodeDecodeError) as e:
            print(f"Error al leer el archivo {file}: {e}") # Print an error message if a file is not found
            continue # Skip to the next file if the current file is not found

        # Tokenize the text and update the index with word counts for the current file
        for word in tokenize(text):
            index[word][file] += 1 # Increment the count of the word in the current file
        
        return {word: dict(counts) for word, counts in index.items()} # Return the constructed index dictionary
    
    

