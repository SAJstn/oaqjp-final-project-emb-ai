"""
This is a server.py for final project.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")

def sent_analyzer():
    """
    Receive the user input to the emotion detector
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyzer = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyzer)

    # Extract the label and score from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the anger_score is None, indicating an error or invalid input
    if anger_score is None:
        return " Invalid text! Please try again!."

    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear':{fear_score}, 'joy': {joy_score}, and 'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index_page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
