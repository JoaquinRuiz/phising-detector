from transformers import pipeline
import sys

MODEL = "mshenoda/roberta-spam"
det = pipeline("text-classification", model=MODEL)

def classify(text):
    o = det(text)[0]
    lab = o["label"].lower()
    if lab not in ("spam","label_1","spam messages","spam_messages"): 
        print("🟢 LEGÍTIMO")
    else:
        print("🔴 PHISHING")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        classify(" ".join(sys.argv[1:]))
    else:
        print("Pega SMS/Email (vacío para salir):")
        while True:
            s = input("> ").strip()
            if not s: break
            classify(s)
