from fastapi import FastAPI
from infera.manager import ModelManager
from infera.engine import InferenceEngine

app = FastAPI(title="Inferra")

model_manager = ModelManager("sshleifer/tiny-gpt2")
model_manager.load_model()

inference_engine = InferenceEngine(model_manager)

# output_ids = inference_engine.generate({"input_ids": model_manager.tokenizer.encode("Hello, how are you?", return_tensors="pt")})

# output = model_manager.decode(output_ids)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/models")
def list_models():
    return {"models": [{"id":"Qwen/Qwen3.8-27B","name":"Qwen3.8 27B"}]}

@app.get("/generate")
def generate():
    output = inference_engine.infer("Hello, how are you?")
    return {"output": output}
