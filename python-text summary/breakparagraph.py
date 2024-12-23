
# Function to count words in a text
def count_words(text):
    words = text.split()  # Split text by spaces
    return len(words)  # Return the number of words

# Function to break text into chunks based on a max word count per chunk
def create_chunks(text, max_words_per_chunk):
    words = text.split()  # Split the text into words
    chunks = []  # To store the resulting chunks
    current_chunk = []  # Temporary list for accumulating words

    for word in words:
        current_chunk.append(word)  # Add word to the current chunk
        
        # If the current chunk exceeds the max word count, finalize the chunk
        if len(current_chunk) >= max_words_per_chunk:
            chunks.append(" ".join(current_chunk))  # Join words into a chunk
            current_chunk = []  # Reset the current chunk for the next part
    
    # If there are remaining words, add them as the last chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks