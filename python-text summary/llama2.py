from langchain.llms import Ollama
from langchain_community.llms import Ollama
# Function to generate a summary using Ollama model
def generate_summary(text):
    # Initialize the Ollama model (make sure the base_url and model name are correct)
    ollama = Ollama(base_url='http://localhost:11434', model='phi')
    
    # Prompt to ask the model for a summary of the input text
    prompt = f"Please provide a professional and detailed summary inclusing all the points of the following text:\n{text}"
    
    # Get the response from the model
    summary = ollama(prompt)
    
    # Return the generated summary
    return summary