import streamlit as st

name = st.text_input("Enter your Name")
fname = st.text_input("Enter your Father Name")
sname = st.text_input("Enter your Surname")

adr = st.text_area("Enter your Address")

python_level_data = st.selectbox(
    "Enter your Level of python:",
    (1, 2, 3, 4, 5)
)

button = st.button("Done")

if button:
    st.success("Form Submitted Successfully!")

    st.markdown(f"""
    **Name:** {name}

    **Father Name:** {fname}

    **Surname:** {sname}

    **Address:** {adr}

    **Level:** {python_level_data}
    """)
