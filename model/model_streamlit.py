import streamlit as st
import pickle

def load_model():
    with open('AITA.pkl','rb') as pickle_in:
        the_model = pickle.load(pickle_in)
    return the_model
    
model = load_model()

st.title("Where should you post this?")

your_text = st.text_input("Enter your post:", max_chars=10_000)

if st.button('AITA?'):
    if len(your_text) >= 10:
        pred = model.predict([your_text])[0] # predictions
        probs = list(model.predict_proba([your_text])[0]) #predicted probabilities
        prob = probs[0] if pred == 'AmItheAsshole?' else probs[1]
        st.write(f"This should go in {pred}.")
        st.metric("Probability", f"{100*round(prob, 2)}%")
    else:
        st.write("Too short. Write more.")
