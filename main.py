from src.models.train import train_model
from src.data.load_data import load_json

data = load_json("src/data/labeled/sample.json")

textos = [d["texto"] for d in data]
labels = [d["labels"] for d in data]

model, tokenizer, mlb = train_model(textos, labels)

print("Treinamento concluído!")