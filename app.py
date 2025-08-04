import gradio as gr
from transformers import pipeline

# Load sentiment analysis pipeline that supports English and Bengali
emotion_classifier = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

def detect_emotion(text):
    results = emotion_classifier(text)
    if not results or not results[0]:
        return "No emotion detected"
    
    # Get the emotion with the highest score
    best = max(results[0], key=lambda x: x['score'])
    return f"Emotion: {best['label']} (Confidence: {best['score']:.2f})"

iface = gr.Interface(
    fn=detect_emotion,
    inputs=gr.Textbox(lines=5, placeholder="Enter social media post (English/Bangla)..."),
    outputs="text",
    title="Emotion Detection from Social Media Posts",
    description="Detect emotions like joy, anger, sadness, etc. from English or Bengali social media texts.",
)

if __name__ == "__main__":
    iface.launch()
