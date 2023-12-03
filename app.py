from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import base64

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'grp6m5lz95d9exiz.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'yb1kzgj064vmir99'
app.config['MYSQL_PASSWORD'] = 'u4aorhbaziyr6i1b'
app.config['MYSQL_DB'] = 'm2p8uekpnqas4rst'

mysql = MySQL(app)


model_path ='best_model.h5'

model = tf.keras.models.load_model(model_path)

# Define the list of class labels
class_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

@app.route('/')
def index():
    return render_template('capture.html')

@app.route('/predict-emotion', methods=['POST'])
def predict_emotion_route():
    image_data = request.json['image_data']
    header, encoded = image_data.split(",", 1)
    image_bytes = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(image_bytes)).convert('L')

    image = image.resize((48, 48))
    image_array = np.array(image)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=-1)
    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array)
    emotion_index = np.argmax(predictions)
    predicted_emotion = class_labels[emotion_index]

    cursor = mysql.connection.cursor()
    query = """
    SELECT file_path FROM track_emotions 
    JOIN tracks ON track_emotions.track_id = tracks.track_id 
    JOIN emotions ON track_emotions.emotion_id = emotions.emotion_id 
    WHERE emotion_name = %s ORDER BY RAND() LIMIT 1
    """
    cursor.execute(query, (predicted_emotion,))
    track_url = cursor.fetchone()
    cursor.close()
    if not track_url:
        return jsonify({'error': 'No track found for this emotion.'}), 404

    return jsonify({
        'emotion': predicted_emotion,
        'track_url': track_url[0]
    })
if __name__ == '__main__':
    app.run(debug=True)
