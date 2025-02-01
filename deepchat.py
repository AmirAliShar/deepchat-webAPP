import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate
import  re

with st.sidebar:
    st.title("🤍 Deep Chat")
    st.caption(f"**🚀 A Streamlit AI Assistant powered by Deepseek-r1")
    options=st.selectbox("Choose a option",["Chat","user_history"],key="options")
    st.caption("Amir's Chatbot")

if options=="Chat":
     llm=OllamaLLM(model="deepseek-r1")
if options=="user_history":
    for i in st.session_state.messages:
        st.write(i)
# prompt=ChatPromptTemplate.from_template("""
# Answer the question based on correct knowledge.
# Please provide the most accurate response based on the question
# and do not try the incorrect answer, If you do not know then simply say I do not know.
# Question:{input}
# """)
#
prompt = ChatPromptTemplate.from_template("""You are are helpful assistant.
                                          Please provide a concise and correct answer to the question.
Question:{input}
""")


query=st.chat_input("Please enter the question here")

#Store LLM generate respose
if "messages" not in st.session_state:
    st.session_state.messages = []

if query:
    st.write(query)
    chain=prompt|llm
    response=chain.invoke({"input":query})
    #Remove the text between the think
    cleaned_response = re.sub(r"<think>.*?</think>", " ", response, flags=re.DOTALL).strip()
    st.write(cleaned_response)
    st.session_state.messages.append(f"**User Question**: {query}")
    st.session_state.messages.append(f"**Response** :{cleaned_response}")

