import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate # to use prompt template

llm = HuggingFaceEndpoint (
    repo_id = "deepseek-ai/DeepSeek-V4-Flash-0731",
    max_new_tokens=2048
  
)

model = ChatHuggingFace(llm = llm)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an expert information extraction assistant.

Extract useful information from the given movie description.

Identify:
- Movie Name
- Release Year
- Genre
- Director
- Cast
- Main Characters
- Plot
- Setting
- Main Themes
- Important Facts
- Quick Summary

Instructions:
- Extract only information that is present in the text.
- Do not make up missing information.
- If information is not available, mention "Not mentioned".
- Keep each point concise and easy to understand.
- The Quick Summary should be 2–3 sentences.
- Organize the response using clear headings."""
    ),
    (
        "human",
        """Movie Description:

{paragraph}"""
    )
])

st.title("Movie Description Information Extractor")

para = st.text_area("Enter your paragraph:")

if st.button("Submit"):

    final_prompt = prompt.invoke(
        { "paragraph": para }
        )

    response = model.invoke(final_prompt)

    st.write(response.content)