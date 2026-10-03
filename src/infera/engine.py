from transformers import AutoTokenizer
import torch

class InferenceEngine:
    def __init__(self, manager):
        self.manager = manager
    def tokenize(self, text):
        return self.manager.tokenizer(text, return_tensors="pt")
    def generate(self, inputs):
        with torch.inference_mode():
            output_ids = self.manager.model.generate(
                **inputs, 
                max_new_tokens=20
            )
        return output_ids
    def decode(self, output_ids):
        return self.manager.tokenizer.decode(output_ids[0], skip_special_tokens=True)
    def infer(self, text):   
       inputs = self.tokenize(text)
       output_ids = self.generate(inputs)
       return self.decode(output_ids)