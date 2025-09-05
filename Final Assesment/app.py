import gradio as gr
from transformers import pipeline

# Load fine-tuned model
classifier = pipeline("text-classification", model="./sms_spam_model", tokenizer="./sms_spam_model")

def predict_spam(text):
    result = classifier(text)[0]
    label = " 🚫 Spam 🚫 " if result['label'] == "LABEL_1" else " ✅ Not a spam ✅ "
    return f"Prediction: {label}\nConfidence: {result['score']:.2f}"

demo = gr.Interface(
    fn=predict_spam,
    inputs=gr.Textbox(label="Enter your SMS here", placeholder="Type or paste an SMS message..."),
    outputs=gr.Textbox(label="Prediction"),
    title="SMS Spam Classifier",
    description="Type/Paste an SMS message to check if it's spam or not."
)

demo.launch(share = False)
