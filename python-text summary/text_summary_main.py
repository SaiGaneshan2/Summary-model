from text_extract import text_extractor
from text_extract import text_preprocessing
from breakparagraph import create_chunks
from breakparagraph import count_words
from abstractivesummary import abstractive_summary
from llama2 import generate_summary
def generate_pdf_summary(file_path):

    
    # Extract and preprocess text from the PDF
    complete_text = text_extractor(file_path)
    clean_text = text_preprocessing(complete_text)

    # Break the clean text into chunks
    paragraph = create_chunks(clean_text, 750)

    # Count total words before summarization
    total_word_count = sum(count_words(chunk) for chunk in paragraph)
    print(f"Total word count before summary: {total_word_count}\n")

    # Initialize an empty string to store the combined summary
    summary = ""

    # Generate summaries for each chunk
    for i in range(0, len(paragraph)):  # Loop through all the chunks
        summary += abstractive_summary(paragraph[i])

    # Count total words after summarization
    total_word_count_after_summary = count_words(summary)

    # Final summary generation
    final_summary = generate_summary(summary)

    return final_summary

# Example usage:
file_path = "/home/sg-ubuntu/Downloads/examplechemistrychapter1.pdf"
final_summary = generate_pdf_summary(file_path)
print(f"The final summary is \n{final_summary}")

