import streamlit as st
import pandas as pd
import os

from dotenv import load_dotenv
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import StreamlitCallbackHandler

def main():
    load_dotenv()

    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(page_title="Talk CSV to me")
    st.header("Agent Panda 🕵🐼️")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")

    if csv_file is not None:

        df = pd.read_csv(csv_file)