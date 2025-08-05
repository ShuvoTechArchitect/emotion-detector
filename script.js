async function analyzeEmotion() {
  const postText = document.getElementById('postInput').value;

  const response = await fetch("https://shuvo100-emotion-detector-api.hf.space/run/predict", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ data: [postText] })
  });

  const result = await response.json();

  try {
    const emotion = Array.isArray(result.data) ? result.data[0] : "Unknown";
    document.getElementById('result').innerText = `Emotion: ${emotion}`;
  } catch (error) {
    document.getElementById('result').innerText = "Emotion detection failed.";
    console.error("Error parsing API response:", result);
  }
}
