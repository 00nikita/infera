from transformers import AutoTokenizer, AutoModelForCausalLM

class ModelManager:
    def __init__(self, model_name):
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
    def load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self.model.eval()