def count_words(input_text):
    # Remove leading and trailing whitespace
    input_text = input_text.strip()
    # Split the input text into words based on whitespace
    if input_text == "":
        return 0  # If input is empty, return 0
    words = input_text.split()
    # Return the number of words
    return len(words)
def main():
    # User prompt for input
    print("Welcome to the Word Counter program!")
    print("Please enter a sentence or paragraph:")
    # Read user input
    input_text = input()
    # Call function to count words
    word_count = count_words(input_text)
    # Display the word count
    print(f"Word count: {word_count}")
main()