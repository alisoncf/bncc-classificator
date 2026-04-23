from src.models.predict import predict

def run_test(model, tokenizer, mlb):
    textos_teste = [
        "O aluno deve interpretar diferentes tipos de texto.",
        "Produção de texto com coesão e coerência.",
        "Analisar elementos gramaticais em frases."
    ]

    for texto in textos_teste:
        resultado = predict(texto, model, tokenizer, mlb)

        print("\nTexto:", texto)
        print("Predição:", resultado)