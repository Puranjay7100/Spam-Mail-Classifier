📧 Spam Mail Classifier
Welcome to the Spam Mail Classifier, a machine learning-based web application designed to detect whether an email message is Spam or Ham (legitimate). This project leverages natural language processing techniques and logistic regression for accurate, real-time predictions — all accessible via an interactive web interface powered by Streamlit.

🌐 Live Demo
🔗 

📌 Overview
Email spam is a common problem that affects communication and cybersecurity. Detecting spam automatically helps prevent phishing attacks and improves productivity by filtering out irrelevant messages.

This project demonstrates how simple yet effective a machine learning pipeline can be in solving such a problem. With the help of the TfidfVectorizer, we convert raw email text into meaningful numerical features, which are then classified using a Logistic Regression model.

🎯 Objectives
Build a spam classifier using a traditional ML pipeline.

Visualize dataset characteristics and evaluate model performance.

Save the trained model and vectorizer using pickle for future use.

Build a user-friendly frontend using Streamlit for predictions.

Deploy the app online for easy accessibility.

🧠 Machine Learning Stack
Component         	  Technology Used
Language	            Python
Text Preprocessing	  TF-IDF Vectorization
Classification Model	Logistic Regression
Model Persistence	    Pickle
Frontend Web App	    Streamlit
Data Handling       	Pandas, NumPy
Visualization       	Matplotlib, Seaborn

📊 Dataset
The dataset used is a CSV file containing labeled emails marked as Spam or Ham. The key columns include:

Category: The label (spam or ham)

Message: The content of the email/message

We use LabelEncoder to convert the labels into binary values and then apply TfidfVectorizer for converting text data into numerical features suitable for model training.

💻 How It Works
Preprocessing
Emails are cleaned and transformed using the TfidfVectorizer which removes stop words and encodes each message into a numeric vector.

Model Training
A LogisticRegression model is trained on 80% of the dataset using the TF-IDF features and evaluated on the remaining 20%.

Model Evaluation
Metrics such as accuracy, confusion matrix, and classification report are generated to assess the performance.

Web App Interface
A clean and intuitive interface built with Streamlit allows users to input an email message and get instant classification.

Prediction
The app loads the pickled model and vectorizer, transforms the user input, and displays whether it’s Spam or Ham.

🚀 Future Improvements
Add support for multiple ML models (SVM, Naive Bayes, etc.) for comparison.

Include visualization of prediction confidence.

Implement email header analysis for better spam detection.

Deploy the app with user authentication for personal use.
