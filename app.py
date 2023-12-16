from flask import Flask, request, send_file
from transformers import pipeline
import torch
from datasets import load_dataset
import soundfile as sf
from io import BytesIO

app = Flask(__name__)

@app.route('/convert-to-speech', methods=['POST'])
def convert_to_speech():
    data = request.json
    text = data['text']

    # Seu código Python para conversão de texto em fala
    synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    speech = synthesiser(text, forward_params={"speaker_embeddings": speaker_embedding})

    # Salvando o áudio em um buffer de memória
    buffer = BytesIO()
    sf.write(buffer, speech["audio"], samplerate=speech["sampling_rate"], format='WAV')
    buffer.seek(0)

    return send_file(buffer, mimetype='audio/wav')

if __name__ == '__main__':
    app.run(debug=True)
