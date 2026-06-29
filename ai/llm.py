import os

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_nvidia_ai_endpoints import ChatNVIDIA

from ai.prompt import prompt



nvidia = ChatNVIDIA(
    api_key=os.getenv("NVIDIA_API_KEY"),
    model="meta/llama-3.1-8b-instruct"
)



openai = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4o-mini"
)



groq = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
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
            "question":question
        }
    )


    return response.content