Emotion-Based Music Recommendation System

Introduction
In our quest to blend the art of music with the subtleties of human emotions, we, Leslie Konlack and Eileen Blessing, have architected an Emotion-Based Music Recommendation System. This project encapsulates the power of artificial intelligence to not just understand but also respond to human emotions by curating a personalized music experience that resonates with the user's current emotional state.


About the Project
Our application operates at the intersection of technology and empathy. It employs a sophisticated facial emotion recognition model to interpret a user's expressions in real-time. Leveraging the depth of TensorFlow and Keras, the model captures the nuances of human emotion, which in turn, guides the music recommendation engine to suggest tracks that reflect the user's mood.


At the heart of the project is a database that meticulously categorizes music tracks based on their emotional tone. This database is not static; it's designed to expand, learning and evolving as new tracks are classified by our music emotion classification model. This ensures a fresh and diverse music selection with each recommendation.


Repository Composition
Here's how the repository is structured, with each file playing a pivotal role in the application's functionality:

graphql
Copy code
.
├── templates/
│   └── capture.html                # The frontend HTML interface capturing user emotions
├── app.py                          # The core Flask application for server-side logic
├── best_model.h5                   # The pre-trained TensorFlow model for facial emotion recognition
├── music_db_revised_setup.sql      # SQL script for setting up the MySQL database schema
├── requirements.txt                # Project dependencies for replication and deployment
|__ my_keras_model.joblib           # The pre-trained  model for music emotion classification
└── Procfile                        # Heroku deployment configurations


Core Features
Facial Emotion Detection: Utilizing real-time video data, the pre-trained TensorFlow model detects the user's current emotional state with precision.
Emotion-Based Music Selection: A sophisticated algorithm correlates the detected emotion with a database of songs, each tagged with an emotional signature.
Interactive Interface: Designed for simplicity and ease of use, the interface invites users to capture their emotion and receive music recommendations instantly.
Dynamic Music Database: The MySQL database is continuously updated with new tracks, enriching the recommendation engine.
Accessibility and Deployment: Hosted on Heroku, the application is universally accessible, with the deployment process refined for consistency.


Technologies Employed
This application is a confluence of various technologies, each chosen for its efficacy and compatibility with the overall system:

Frontend: HTML5, CSS3, JavaScript
Backend: Flask (Python 3.8+)
AI & Machine Learning: TensorFlow 2.x, Keras, scikit-learn
Database Management: MySQL
Cloud Hosting and Deployment: Heroku, GitHub


Detailed Usage Guide

Interaction Flow
The user is welcomed by the application and prompted to allow webcam access.
Once the "Capture Image" button is clicked, the model evaluates the user's facial expression.
The detected emotion triggers a database query, fetching a song that embodies the user's emotional state.
The user is presented with the song through an embedded music player with options to play and download.

Behind the Scenes
The facial recognition model processes incoming visual data, translating pixels into emotions.
The music classification model, trained on a dataset from the Emotify Music Project, interprets the emotional content of songs, which have been converted from file paths to accessible URLs.
The Flask backend orchestrates the interaction between the frontend, models, and database, ensuring a smooth and responsive user experience.

Deployment and Live Access
The system is deployed on Heroku, available for public access here: [MusicRecommendationApp](https://musicrecommendationapp-328d0564fd7b.herokuapp.com/). This cloud platform was chosen for its robustness and ease of use, allowing us to focus on user experience and system reliability.

How to Contribute
Your contributions and suggestions are heartily welcomed. If you'd like to contribute to the project, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

Licensing
This project is released under the Ashesi University Introduction to artificial intelligence course 

The Creators
-
-Leslie Konlack  
-Eileen Blessing 
-Group20FinalAIPROJECT
-
We celebrate the contributions of the Emotify Music Project for providing the dataset that informed our music classification model, a testament to the collaborative nature of the scientific community.

Experience the harmonious blend of emotion and music with our live application, where each recommendation is a note in the melody of your mood.

GoogleColablinks:https://colab.research.google.com/drive/1Aq7UT28LHaqOQP23Jxv3i5tHIpXhRf9R#scrollTo=dqKQkjB6n1wd
