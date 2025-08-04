async function analyzeEmotion() {
  const postText = document.getElementById('postInput').value;

  const response = await fetch("https://shuvo100-emotion-detector-api.hf.space/run/predict", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: postText })
  });

  const data = await response.json();
  document.getElementById('result').innerText = `Emotion: ${data.label || data}`;
}
