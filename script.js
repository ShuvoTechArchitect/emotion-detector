async function analyzeEmotion() {
  const postText = document.getElementById('postInput').value;

  const response = await fetch("https://shuvo100-emotion-detector-api.hf.space/run/predict", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ data: [postText] })  // ✅ Correct format for Hugging Face API
  });

  const result = await response.json();
  
  try {
    const emotion = result.data[0].label || result.data[0];  // ✅ Safe extraction
    document.getElementById('result').innerText = `Emotion: ${emotion}`;
  } catch (error) {
    document.getElementById('result').innerText = "Emotion detection failed.";
    console.error("Error parsing API response:", result);
  }
}
