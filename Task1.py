# Task 1: Text Summarization Tool
# Objective: Summarize lengthy articles using BART from Hugging Face

import sys
import os

# Print environment details for debugging
print("Python version:", sys.version)
print("Python executable:", sys.executable)

try:
    from transformers import BartForConditionalGeneration, BartTokenizer
except ModuleNotFoundError:
    print("Error: 'transformers' module not found. Run: pip install transformers")
    sys.exit(1)

# Initialize BART model and tokenizer
model_name = "facebook/bart-large-cnn"
try:
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
except Exception as e:
    print(f"Error loading model: {e}")
    sys.exit(1)

# Function to summarize text
def summarize_text(input_text, max_length=150, min_length=60):
    """
    Summarizes input text using BART model.
    Args:
        input_text (str): Text to summarize
        max_length (int): Maximum length of summary (in tokens)
        min_length (int): Minimum length of summary (in tokens)
    Returns:
        str: Summary of the input text or None if an error occurs
    """
    if not input_text or len(input_text.strip()) < 50:
        print("Error: Input text is empty or too short for summarization.")
        return None
    
    try:
        inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=max_length,
            min_length=min_length,
            length_penalty=2.0,  # Increased to encourage longer, detailed summaries
            num_beams=16,        # Higher beams for better quality
            early_stopping=True,
            no_repeat_ngram_size=3  # Prevent repetition
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return None

# Example article (hardcoded for testing)
article = """
In recent years, remote work has transitioned from a niche employment model to a mainstream practice embraced by companies and employees around the world. Initially accelerated by the global COVID-19 pandemic, the shift to working from home proved that many jobs do not require a traditional office setting to be performed effectively. Today, remote work continues to reshape how we think about employment, productivity, and work-life balance.

One of the major benefits of remote work is flexibility. Employees can tailor their schedules to better align with personal responsibilities, resulting in improved mental health and job satisfaction. Additionally, companies are no longer restricted by geographic boundaries when hiring, giving them access to a broader and more diverse talent pool. This model also reduces overhead costs, as businesses can downsize or eliminate physical office spaces.

However, remote work comes with its own set of challenges. Communication can become fragmented without regular in-person interaction, leading to misunderstandings or reduced collaboration. Team building and company culture may suffer if not intentionally cultivated through virtual means. Moreover, some employees struggle with maintaining a clear boundary between work and home life, leading to burnout or decreased productivity.

Technological advancements have played a key role in supporting remote work. Video conferencing tools, cloud-based collaboration platforms, and project management software have made it easier than ever to stay connected and organized from anywhere. As these tools become more sophisticated, the remote work experience continues to improve.

Looking forward, the future of work is likely to be hybrid — blending in-office and remote options to accommodate diverse needs and preferences. Organizations that adapt to this new reality by fostering trust, flexibility, and strong digital infrastructure will be best positioned for long-term success. Remote work is not just a temporary trend; it represents a fundamental shift in how work is conceptualized and executed in the 21st century.
"""

# Summarize the example article
print("\nSummarizing hardcoded example article...")
summary = summarize_text(article)
if summary:
    print("Original Text:", article)
    print("\nSummary:", summary)
else:
    print("Summarization of example article failed.")

# Save summary to file
output_path = "Task1/summary_output.txt"
try:
    os.makedirs("Task1", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("Example Article:\n" + article + "\n\nExample Summary:\n" + (summary or "Summarization failed."))
    print(f"Summary saved to {output_path}")
except Exception as e:
    print(f"Error saving summary: {e}")

