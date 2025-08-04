async function analyzeEmotion() {
  const postText = document.getElementById('postInput').value;

  const response = await fetch('https://huggingface.co/spaces/YOUR_USERNAME/YOUR_MODEL/api/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: postText })
  });

  const data = await response.json();
  document.getElementById('result').innerText = `Emotion: ${data.label || data}`;
}
