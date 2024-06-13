
import streamlit as st
import query_responder
from threading import Thread
from middleware import start_metrics_server
import time
import requests

Thread(target=start_metrics_server, daemon=True).start()
API_ENDPOINT = "http://your-api-endpoint.com/predict"

if 'responses' not in st.session_state:
    st.session_state.responses = []

if 'q' not in st.session_state:
    st.session_state.q = ""

if 'responder' not in st.session_state:
    st.session_state.responder = None 

def get_prediction(prompt):
    response = requests.post(API_ENDPOINT, json={"prompt": prompt})
    if response.ok:
        return response.json()["predicted_text"]
    else:
        return "Error fetching prediction."

def add_response(query, response_text):
    # Generating ID for respecive response
    response_id = len(st.session_state.responses) + 1
    st.session_state.responses.insert(0,(response_id, query, response_text))


def display_responses():
    for response_id, query, response_text in st.session_state.responses:
        # Emphasize important points using bold text
        emphasized_points = "**Important Point:**"
        # Insert the emphasized points into the response text
        modified_response_text = response_text.replace("Important Point:", emphasized_points)
        
        st.markdown(f"### {query}...")
        st.caption(modified_response_text)


def reset_responder():
    st.session_state.responder = None
    st.session_state.responder = query_responder.Responder() 

st.title("Legal Adviser ")
q = st.text_input("Your Legal Query", key='query_input')

if st.button("Ask Away"):
    # Initialize the progress bar
    progress_bar = st.progress(0)
    
    # Simulate waiting for the AI response
    for i in range(10):
        # Update the progress bar
        progress_bar.progress(i / 10)
        time.sleep(0.5)  # Wait for half a second
    response_text = query_responder.respond(q)
    add_response(q,response_text)
    st.session_state.q = q
    display_responses()
    progress_bar.empty()

