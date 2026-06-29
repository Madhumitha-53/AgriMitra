import os
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_nvidia_ai_endpoints import ChatNVIDIA

from ai.prompt import prompt


def get_secret(key):
    return st.secrets.get(key, os.getenv(key))


nvidia = ChatNVIDIA(
    api_key=get_secret("NVIDIA_API_KEY"),
    model="meta/llama-3.1-8b-instruct"
)


openai = ChatOpenAI(
    api_key=get_secret("OPENAI_API_KEY"),
    model="gpt-4o-mini"
)


groq = ChatGroq(
    api_key=get_secret("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)


llm = nvidia.with_fallbacks(
    [
        openai,
        groq
    ]
)


def get_response(question):

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question
        }
    )

    return response.content
