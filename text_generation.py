

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load pre-trained model and tokenizer
model = AutoModelForCausalLM.from_pretrained("distilgpt2")
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")

# Create text generation pipeline
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Define input prompt
prompt = "Once upon a time when life"

# Generate text
output = pipe(prompt, max_new_tokens=78, do_sample=True, temperature=0.7)

# Print generated text
print(output[0]['generated_text'])
