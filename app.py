from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import base64
import mysql

app = Flask(__name__)

model_path ='best_model.h5'

model = tf.keras.models.load_model(model_path)

# Define the list of class labels
class_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

@app.route('/')
def index():
    # Render the HTML page which will capture the image
    return render_template('capture.html')

@app.route('/predict-emotion', methods=['POST'])
def predict_emotion():
    # Receive the image data from the POST request
    image_data = request.json['image_data']

    # Decode the image data
    header, encoded = image_data.split(",", 1)
    image_bytes = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(image_bytes)).convert('L')  # Convert to grayscale if your model expects that

    # Preprocess the image to fit the model's input requirements
    image = image.resize((48, 48))
    image_array = np.array(image)
    image_array = image_array / 255.0  # Rescale pixel values
    image_array = np.expand_dims(image_array, axis=-1)  # Add channel dimension if needed
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Make prediction
    predictions = model.predict(image_array)
    emotion_index = np.argmax(predictions)
    predicted_emotion = class_labels[emotion_index]

    # Make sure you're getting the prediction
    print(f"Predicted emotion: {predicted_emotion}")

    # Query the music database for a random URL of a song matching the predicted emotion
    cursor = mysql.connection.cursor()
    query = """
    SELECT file_path FROM track_emotions 
    JOIN tracks ON track_emotions.track_id = tracks.track_id 
    JOIN emotions ON track_emotions.emotion_id = emotions.emotion_id 
    WHERE emotion_name = %s ORDER BY RAND() LIMIT 1
    """
    print(f"Executing query: {query}")  # Debugging print
    cursor.execute(query, (predicted_emotion,))
    track_url = cursor.fetchone()  # Fetch a single result
    cursor.close()

    # If track_url is None, no tracks were found
    if not track_url:
        print("No track found for this emotion.")  # Debugging print
        return jsonify({'error': 'No track found for this emotion.'}), 404

    # Format the URL for JSON response
    formatted_url = track_url[0]

    # Return the result as a JSON response
    return jsonify({
        'emotion': predicted_emotion,
        'track_url': formatted_url  # Single track URL
    })
if __name__ == '__main__':
    app.run(debug=True)
