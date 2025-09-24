"""Command-line helper to flag phishing messages using a RoBERTa spam model."""

from transformers import pipeline
import sys

MODEL = "mshenoda/roberta-spam"
# Build the Hugging Face pipeline once so repeated classifications stay fast. [SF][RP]
det = pipeline("text-classification", model=MODEL)


def classify(text):
    """Print the phishing verdict for the provided message text."""

    # The pipeline returns a list of predictions; take the top one. [RP]
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
        print("Pega SMS/Email (intro vacío para salir):")
        while True:
            s = input("> ").strip()
            if not s:
                break  # Empty input ends the interactive session. [RP]
            classify(s)
