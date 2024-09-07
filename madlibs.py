# Attempt to open and read the file, handling potential file access errors
try:
    with open("story.txt", "r") as f:
        story = f.read()
except FileNotFoundError:
    print("Error: The file 'story.txt' was not found.")
    exit()  # Exit the program if the file cannot be opened
except IOError:
    print("Error: An issue occurred while reading 'story.txt'.")
    exit()  # Exit the program if an IO error occurs

# Initialize an empty set to store unique placeholder words
words = set()

# Variable to track the start index of a placeholder word
start_of_word = -1

# Define the characters marking the start and end of placeholder words
target_start = "<"
target_end = ">"

# Loop through each character in the story to find placeholders
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i  # Mark the start of a placeholder word
    if char == target_end and start_of_word != -1:
        # Extract the placeholder word (including the '<' and '>')
        word = story[start_of_word : i + 1]
        words.add(word)  # Add the placeholder to the set
        start_of_word = -1  # Reset the start index after finding a placeholder

# Dictionary to store user inputs for each placeholder word
answers = {}

# Check if any placeholders were found
if not words:
    print("Error: No placeholders found in the story.")
    exit()  # Exit if no placeholders are found

# For each unique placeholder word, prompt the user for a replacement
for word in words:
    while True:
        answer = input(f"Enter a word for {word}: ").strip()

        # Error handling for empty inputs
        if not answer:
            print(f"Error: No input provided for {word}. Please enter a valid word.")
        else:
            answers[word] = answer  # Store valid replacement
            break  # Exit the loop when a valid input is provided

# Replace each placeholder in the story with the corresponding user-provided word
for word in words:
    story = story.replace(word, answers[word])
