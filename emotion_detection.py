import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)['emotionPredictions']
    
    anger_score = formatted_response[0]['emotion']['anger']
    disgust_score = formatted_response[0]['emotion']['disgust']
    fear_score = formatted_response[0]['emotion']['fear']
    joy_score = formatted_response[0]['emotion']['joy']
    sadness_score = formatted_response[0]['emotion']['sadness']
    emotion_values = formatted_response[0]['emotion']
    dominant_emotion = max(emotion_values, key=emotion_values.get)
    
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sad': sadness_score, 'dominant_emotion': dominant_emotion}
