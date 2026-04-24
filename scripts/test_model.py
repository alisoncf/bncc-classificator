import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from src.models.load_model import load_model
from src.models.predict import predict

def run_test():
    model, tokenizer, mlb = load_model()

    textos_teste = [
        "O aluno deve interpretar diferentes tipos de texto.",
        "Produção de texto com coesão e coerência.",
        "Analisar elementos gramaticais em frases."
    ]

    for texto in textos_teste:
        resultado = predict(texto, model, tokenizer, mlb)

        print("\nTexto:", texto)
        print("Predição:", resultado)


if __name__ == "__main__":
    run_test()