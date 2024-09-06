"""

chatbot_free:
Demonstrates the use of opwn source LLMs to create a simple chatbot
using langchain framework and enables execution using streamlit

"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit
import os
from dotenv import load_dotenv


def init():
    load_dotenv()

    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


def chatbot_free():
    # User prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system","You are an assistant. Please response to the user queries"),
            ("user","Question:{question}")
        ]
    )

    # streamlit framework
    streamlit.title('AI_Chatbot!')
    input_text = streamlit.text_input("Type in your question here.")

    # Ollama interface to run LLMs
    llm=Ollama(model="llama3.1")
    output_parser=StrOutputParser()

    chain=prompt|llm|output_parser

    if input_text:
        streamlit.write(chain.invoke({"question": input_text}))


if __name__ == "__main__":
    init()
    chatbot_free()
