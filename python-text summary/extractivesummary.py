from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
import nltk

# Download the Punkt tokenizer models for sentence splitting
nltk.download('punkt')

def extractive_summary_textrank(text, num_sentences=3):
    # Tokenize the text using nltk
    sentences = nltk.tokenize.sent_tokenize(text)
    
    # Parse the input text with the tokenized sentences
    parser = PlaintextParser.from_string(' '.join(sentences), nltk.tokenize.sent_tokenize)
    
    # Initialize the TextRank summarizer
    summarizer = TextRankSummarizer()
    
    # Get the summary
    summary = summarizer(parser.document, num_sentences)
    
    # Combine the summary sentences into one string
    return ' '.join([str(sentence) for sentence in summary])