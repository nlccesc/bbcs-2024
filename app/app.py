import streamlit as st 
import query_responder 
from threading import Thread
from middleware import start_metrics_server

# Start the metrics server in a background thread
Thread(target=start_metrics_server, daemon=True).start()

# backend 
q = "" 

def eval_query(query): 
    if query == "": 
        return 
    st.text("Response:")
    st.text(query_responder.respond(query))

# frontend 
st.title("Query")
q = st.text_input("Query", key='query_input')
if st.button("Ask"):
    eval_query(q)
