
from google.cloud import speech

def run_quickstart() -> speech.RecognizeResponse:
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")
        
        
        
# import whisper
# model = whisper.load_model("base")
# result = model.transcribe("audio.file")  #need to change later to file name

# transcribed_text = result["text"]

# # print(transcribed_text)

# with open("transcription.text" "w") as text_file:
#     text_file.write(result["text"])
# # a file in Backend called transcription.text will be created with the transcribed text inside

    
    

# Imports the Google Cloud client library