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
