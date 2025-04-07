import streamlit as st
import pickle

# Load the saved model and vectorizer
with open('spam_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('feature_extraction.pkl', 'rb') as f:
    feature_extraction = pickle.load(f)

st.set_page_config(page_title="Spam Mail Classifier", layout="centered")
st.title("📧 Spam Mail Classifier")

st.markdown("Enter the email text below to classify it as **Ham** or **Spam**.")

user_input = st.text_area("✉️ Email Text", height=150)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message before prediction.")
    else:
        input_features = feature_extraction.transform([user_input])
        prediction = model.predict(input_features)

        if prediction[0] == 0:
            st.success("✅ This is a **Ham (Not Spam)** mail.")
        else:
            st.error("🚫 This is a **Spam** mail.")
