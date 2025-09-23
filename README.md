# Phishing Detector

A simple Python script that uses machine learning to detect phishing attempts in SMS or email text.

## Features

- Uses RoBERTa-based spam detection model
- Command-line interface
- Interactive mode for testing multiple messages

## Requirements

- Python 3.x
- transformers library
- torch (automatically installed with transformers)

Install dependencies:
```bash
pip install transformers
```

## Usage

### Command Line
```bash
python ia_or_true.py "Your suspicious message here"
```

### Interactive Mode
```bash
python ia_or_true.py
```
Then paste messages one by one. Press Enter on empty line to exit.

## Model

Uses the `mshenoda/roberta-spam` model from Hugging Face, fine-tuned for spam/phishing detection.

## Output

- 🟢 LEGÍTIMO: Legitimate message
- 🔴 PHISHING: Phishing attempt detected

## Disclaimer

This is a demo script. For production use, consider additional security measures and model validation.

## About the Author

Check out my book "Programming with Artificial Intelligence" available on [Amazon](https://www.amazon.com/dp/B0FQ4ZFTSN).

Made with ❤️ by [JokiRuiz](https://jokiruiz.com)
