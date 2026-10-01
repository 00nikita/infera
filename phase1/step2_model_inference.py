import torch 
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "sshleifer/tiny-gpt2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

model.eval()

text = "I love building AI"

inputs = tokenizer(text, return_tensors="pt")
print(inputs)

with torch.inference_mode():
    outputs = model(**inputs)
print(outputs)

# Generate new tokens
with torch.inference_mode():
    output_ids = model.generate(
        **inputs,
        max_new_tokens=20
    )

# Token IDs → text
generated_text = tokenizer.decode(output_ids[0])

print("\nGenerated text:")
print(generated_text)
