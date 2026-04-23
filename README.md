# Classificador BNCC

Projeto para classificar textos educacionais nas habilidades da BNCC usando NLP.

## Objetivo
Classificar dissertações e materiais didáticos em habilidades BNCC.

## Stack
- Python
- Transformers (BERTimbau)
- Scikit-learn

## Estrutura
(descrição das pastas)

## Como rodar
Projeto de classificação de textos educacionais segundo a BNCC usando BERTimbau.

## Como usar
1. Prepare seus dados em JSON
2. Rode treinamento em src/models/train.py
3. Use predict.py para inferência

# ---------- exemplo dataset (data/labeled/sample.json) ----------
[
  {
    "texto": "Este texto trabalha interpretação de leitura...",
    "labels": ["EF15LP05"]
  }
]