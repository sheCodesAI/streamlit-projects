import os

from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

# 2nd chatgpt app : 1) translator(professor)

load_dotenv()
user = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
gptmodel = "gpt-4o-mini"
userrole = "user"  # 3roles : user, assistant, system

preprompt = "translate the following code into a different programming language. Here is the code: "

response = ""

st.title("Translator-GPT App")
st.divider()
prompt = st.text_input("Enter your code here:", "")
gptbutton = st.button("Translate Code")
st.caption("Paste your code to translate it into different programming languages.")
st.caption("Ex: def add(a, b): return a + b")
st.divider()

if gptbutton:

    if prompt.strip() == "":
        st.warning("⚠️ Please enter some code first.")
    else:
        with st.spinner("Generating response..."):
            response = user.chat.completions.create(
                model=gptmodel,
                messages=[
                    {
                        "role": userrole,
                        "content": preprompt + prompt
                    }
                ]
            )

        st.success("✅ Response generated successfully!")
        st.snow()
        st.write(response.choices[0].message.content)