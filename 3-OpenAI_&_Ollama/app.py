import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# LanSmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="True"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")\


## prompt templet
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please resapond to the question asked"),
        ("user","Question:{question}")
    ]
)

## Streamlite framework
st.title("Langchain Demo with gemma:2b")
input_text=st.text_input("what question you have in mind")


## Ollama(Gemma:2b)
llm = Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))