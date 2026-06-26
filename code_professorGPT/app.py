import os

from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

# 2 chatgpt apps : 1) code explainer(professor)

load_dotenv()
user = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
gptmodel = "gpt-4o-mini"
userrole = "user"  # 3roles : user, assistant, system

preprompt = "teach me the following code in simple terms and explain it to me like I am a 5 year old. Also provide me with a real life example of the code. Here is the code: "

response = ""

st.title("Code ProfessorGPT App")
st.divider()
prompt = st.text_input("Enter your code here:", "")
gptbutton = st.button("Explain Code")
st.caption("This app uses OpenAI's GPT-4o-mini model to explain code in simple terms.")
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