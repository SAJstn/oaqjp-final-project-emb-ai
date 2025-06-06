import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json = myobj, headers = header)
    
    #If the response status code is 200
    if response.status_code == 200:
        #Parse the response from the API
        formatted_response = json.loads(response.text)['emotionPredictions'][0]['emotion']
        #Extract all required values from the response
        anger_score = formatted_response['anger']
        disgust_score = formatted_response['disgust']
        fear_score = formatted_response['fear']
        joy_score = formatted_response['joy']
        sadness_score = formatted_response['sadness']
        dominant_emotion = max(formatted_response, key=formatted_response.get)

    # If the response status code is 400, set all values to None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        formatted_response = None
        dominant_emotion = None

    # If the response status code is 500, set all values to None
    elif response.status_code == 500:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        formatted_response = None
        dominant_emotion = None

    # Return the all values in a dictionary
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}
