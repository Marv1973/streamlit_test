# 

from pandas import from_dummies
import streamlit as st


from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import numpy as np


st.title("ARC Challenge")

#st.chat_input(placeholder="Hi you")#, *, key=None, max_chars=None, disabled=False, on_submit=None, args=None, kwargs=None)



user_prompt=st.chat_input(placeholder="Hi you 1" , key=None, max_chars=None, disabled=False, on_submit=None, args=None, kwargs=None)

print(user_prompt)

# %% 
if user_prompt:
    message = st.chat_message("assistant")
    message.write("Hello human")
    message.bar_chart(np.random.randn(30, 3))


# %%
@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"