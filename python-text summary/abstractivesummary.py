from transformers import pipeline

# Initialize the Hugging Face summarization pipeline with the T5 model (t5-small)
summarizer = pipeline("summarization", model="t5-small")

def abstractive_summary(text, max_length=200, min_length=50, truncation=True):
    summary = summarizer(text, max_length=max_length, min_length=min_length, truncation=truncation, do_sample=False)
    return summary[0]['summary_text']
