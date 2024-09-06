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

# Local imports
import CONSTANTS

def init():
    try:
        load_dotenv(CONSTANTS.ENV_PATH)

        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        #os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
        os.environ["LANGCHAIN_API_KEY"] = streamlit.secrets["LANGCHAIN_API_KEY"]
    except Exception as err:
        raise Exception("Failed to load environment variables")


def chatbot_free():
    try:
        # User prompt
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system","You are an assistant. Please response to the user queries"),
                ("user","Question:{question}")
            ]
        )
    except Exception as err:
        raise Exception("Failed to initiate prompt field")

    try:
        # streamlit framework
        streamlit.title('AI_Chatbot!')
        input_text = streamlit.text_input("Type in your question here.")
    except Exception as err:
        raise Exception("Failed to initiate streamlit")

    try:
        # Ollama interface to run LLMs
        llm=Ollama(model="llama3.1")
        output_parser=StrOutputParser()
    except Exception as err:
        raise Exception("Failed to initiate LLM")

    try:
        chain=prompt|llm|output_parser
        if input_text:
            streamlit.write(chain.invoke({"question": input_text}))
    except Exception as err:
        raise Exception("Failed to run chatbot model")



if __name__ == "__main__":
    try:
        init()
        chatbot_free()
    except Exception as err:
        raise Exception("Error: Failed to trigger Chatbot")
