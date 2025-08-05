import gradio as gr
from transformers import pipeline

# মডেল লোড করো
emotion_classifier = pipeline(
    "text-classification",
    model="Toshifumi/bert-base-multilingual-cased-finetuned-emotion"
)

# Human-friendly emotion mapping
humanized_map = {
    "label_0": "😠 রাগ (Anger)",
    "label_1": "😢 দুঃখ (Sadness)",
    "label_2": "😊 আনন্দিত (Joy)",
    "label_3": "❤️ ভালোবাসা (Love)",
    "label_4": "😨 ভয় (Fear)",
    "label_5": "😲 বিস্ময় (Surprise)",
    "label_6": "😐 নিরপেক্ষ (Neutral)",

    "LABEL_0": "😠 রাগ (Anger)",
    "LABEL_1": "😢 দুঃখ (Sadness)",
    "LABEL_2": "😊 আনন্দিত (Joy)",
    "LABEL_3": "❤️ ভালোবাসা (Love)",
    "LABEL_4": "😨 ভয় (Fear)",
    "LABEL_5": "😲 বিস্ময় (Surprise)",
    "LABEL_6": "😐 নিরপেক্ষ (Neutral)",

    "Anger": "😠 রাগ (Anger)",
    "Sadness": "😢 দুঃখ (Sadness)",
    "Joy": "😊 আনন্দিত (Joy)",
    "Love": "❤️ ভালোবাসা (Love)",
    "Fear": "😨 ভয় (Fear)",
    "Surprise": "😲 বিস্ময় (Surprise)",
    "Neutral": "😐 নিরপেক্ষ (Neutral)"
}

# Emotion detect function
def detect_emotion(text):
    if not text.strip():
        return "⚠️ অনুগ্রহ করে একটি বার্তা লিখুন।"
    try:
        result = emotion_classifier(text)[0]
        label = result["label"]
        score = round(result["score"] * 100, 2)
        emotion = humanized_map.get(label)
        if emotion:
            return f"{emotion} (score: {score}%)"
        else:
            return f"🤔 অজানা (Unknown) — মডেল লেবেল: {label} (score: {score}%)"
    except Exception as e:
        return f"❌ সমস্যা হয়েছে: {str(e)}"

# Interface
interface = gr.Interface(
    fn=detect_emotion,
    inputs=gr.Textbox(label="✍️ মেসেজ লিখুন (বাংলা / English)", placeholder="আমি আজ অনেক খুশি..."),
    outputs=gr.Textbox(label="🧠 সনাক্তকৃত অনুভূতি"),
    title="🌐 Bilingual Emotion Detector",
    description="এই AI টুলটি বাংলা ও ইংরেজি টেক্সট থেকে মানুষের আবেগ শনাক্ত করে (যেমন: 😊 আনন্দ, 😢 দুঃখ, 😠 রাগ)।"
)

interface.launch()
