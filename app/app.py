import streamlit as st 
import query_responder 


# backend 

q = "" 

def eval_query(query): 
    if query == "": return 
    st.text("Response:")
    st.text(query_responder.respond(query))





# frontend 


st.title("Query")

q = st.text_input("Query")

st.button("Ask", on_click=eval_query(q))

