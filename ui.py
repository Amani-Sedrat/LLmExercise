import gradio as gr
import requests

def chat_interface(query_text):
    response = requests.post("http://127.0.0.1:5000/query", json={"query_text": query_text})
    response_text = response.json()["response_text"]
    return response_text

# Create the Gradio interface
gr.Interface(fn=chat_interface, inputs="text", outputs="text", title="Q&A interface").launch()
