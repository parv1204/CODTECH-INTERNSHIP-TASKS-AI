# Task 4: Generative Text

- **Objective**: Generate creative and coherent text for given prompts using a pre-trained GPT-2 model from Hugging Face.
- **Deliverables**:
  - Python script: `Task4_AI.py` (contains the code to generate text using the GPT-2 model).
  - Output file: `generated_text.txt` (contains the generated text for three prompts).
- **How to Run**:
  1. Install the required dependencies by running:
  2. Place `Task4_AI.py` in the `Task4/` directory.
  3. Run the script using Python:
  4. Check the `generated_text.txt` file in the `Task4/` directory for the generated text outputs.
- **Notes**:
- The script uses the GPT-2 Medium model (`gpt2-medium`) from Hugging Face for text generation.
- Required dependencies: `torch`, `transformers` (listed in `requirements.txt`).
- System requirements: At least 8 GB RAM or 1 GB GPU memory to run the script efficiently.
- Due to script limitations, the final outputs in `generated_text.txt` were manually curated to ensure coherence and relevance, as the model struggled with generating consistent results.
