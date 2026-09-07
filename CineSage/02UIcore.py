# #structured output

# import streamlit as st
# from dotenv import load_dotenv

# load_dotenv()

# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from langchain_core.prompts import ChatPromptTemplate # to use prompt template
# from pydantic import BaseModel;
# from typing import List,Optional;
# from langchain_core.output_parsers import PydanticOutputParser



# llm = HuggingFaceEndpoint (
#     repo_id = "deepseek-ai/DeepSeek-V4-Flash-0731",
#     max_new_tokens=2048
  
# )

# model = ChatHuggingFace(llm = llm)


# #schema
# class Movie (BaseModel):
#     title: str
#     release_year: Optional[int]
#     genre: List[str]
#     director: Optional[str]
#     cast: List[str]
#     rating: Optional[float]
#     summary: str

# parser = PydanticOutputParser(pydantic_object=Movie) 


# prompt = ChatPromptTemplate.from_messages(
#          [
#              ('system', """
#              Extract movie information from the paragraph
#              {format_instructions}
#              """),
#              ("human","{paragraph}")
#          ]
# )

# st.title("Movie Info Extractor")

# para = st.text_area("Enter your paragraph:")

# if st.button("Extract"):
#     if para.strip() == "":
#         st.warning("Please enter a paragraph.")
#     else:
#         with st.spinner("Extracting..."):
#             final_prompt = prompt.invoke(
#                 { "paragraph":para,
#                    "format_instructions":parser.get_format_instructions()
#                  }
#                 )

#             response = model.invoke(final_prompt)

#             st.write(response.content)

#structured output


# ------------------------------------------------------------------------------------------------------------


import json
import re

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate # to use prompt template
from pydantic import BaseModel;
from typing import List,Optional;
from langchain_core.output_parsers import PydanticOutputParser


st.set_page_config(page_title="Reel Extract", page_icon="🎞️", layout="centered")

llm = HuggingFaceEndpoint (
    repo_id = "deepseek-ai/DeepSeek-V4-Flash-0731",
    max_new_tokens=2048
  
)

model = ChatHuggingFace(llm = llm)


#schema
class Movie (BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie) 


prompt = ChatPromptTemplate.from_messages(
         [
             ('system', """
             Extract movie information from the paragraph
             {format_instructions}
             """),
             ("human","{paragraph}")
         ]
)

# ---------- styling ----------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600&display=swap');

:root {
    --ink: #EDE6D6;
    --ink-dim: #A79E8C;
    --marquee: #D4A24E;
    --stage: #14171C;
    --stage-raised: #1C2028;
    --rule: #33383F;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: var(--stage);
    color: var(--ink);
}

/* hide default streamlit chrome */
#MainMenu, header, footer { visibility: hidden; }

.reel-header {
    text-align: center;
    padding: 2.2rem 0 1.6rem 0;
    border-bottom: 1px solid var(--rule);
    margin-bottom: 2rem;
}

.reel-eyebrow {
    font-size: 0.78rem;
    letter-spacing: 0.14em;
    color: var(--marquee);
    margin-bottom: 0.4rem;
}

.reel-title {
    font-family: 'Fraunces', serif;
    font-weight: 600;
    font-size: 2.6rem;
    color: var(--ink);
    margin: 0;
}

.reel-sub {
    color: var(--ink-dim);
    font-size: 0.95rem;
    margin-top: 0.5rem;
}

.stTextArea textarea {
    background: var(--stage-raised) !important;
    color: var(--ink) !important;
    border: 1px solid var(--rule) !important;
    border-radius: 4px !important;
    font-size: 0.98rem !important;
}

.stTextArea textarea:focus {
    border-color: var(--marquee) !important;
    box-shadow: 0 0 0 1px var(--marquee) !important;
}

.stTextArea label {
    color: var(--ink-dim) !important;
    font-size: 0.85rem !important;
}

.stButton button {
    background: var(--marquee) !important;
    color: #1C1204 !important;
    border: none !important;
    border-radius: 3px !important;
    font-weight: 600 !important;
    letter-spacing: 0.03em;
    padding: 0.55rem 1.6rem !important;
}

.stButton button:hover {
    background: #E3B564 !important;
    color: #1C1204 !important;
}

.card {
    background: var(--stage-raised);
    border: 1px solid var(--rule);
    border-radius: 4px;
    padding: 1.6rem 1.8rem;
    margin-top: 1.4rem;
}

.card-title {
    font-family: 'Fraunces', serif;
    font-size: 1.7rem;
    font-weight: 600;
    color: var(--ink);
    margin: 0;
}

.card-year {
    color: var(--marquee);
    font-size: 1rem;
    font-weight: 500;
}

.card-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 0.9rem;
}

.chip-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin: 0.6rem 0 1.1rem 0;
}

.chip {
    border: 1px solid var(--marquee);
    color: var(--marquee);
    font-size: 0.76rem;
    padding: 0.18rem 0.6rem;
    border-radius: 20px;
}

.field-label {
    color: var(--ink-dim);
    font-size: 0.76rem;
    letter-spacing: 0.06em;
    margin-bottom: 0.15rem;
}

.field-value {
    color: var(--ink);
    font-size: 0.95rem;
    margin-bottom: 1rem;
    line-height: 1.5;
}

.rating-value {
    color: var(--marquee);
    font-family: 'Fraunces', serif;
    font-size: 1.1rem;
}

hr.thin {
    border: none;
    border-top: 1px solid var(--rule);
    margin: 1.1rem 0;
}
</style>

<div class="reel-header">
    <div class="reel-eyebrow">STRUCTURED OUTPUT</div>
    <p class="reel-title">Reel Extract</p>
    <p class="reel-sub">Paste a paragraph about a film. Get back a clean record.</p>
</div>
""", unsafe_allow_html=True)

# ---------- app logic ----------

para = st.text_area("Paragraph", height=180, placeholder="e.g. Christopher Nolan's Inception (2010) follows Dom Cobb, played by Leonardo DiCaprio...")

if st.button("Extract"):
    if para.strip() == "":
        st.warning("Please enter a paragraph.")
    else:
        with st.spinner("Extracting..."):
            final_prompt = prompt.invoke(
                { "paragraph":para,
                   "format_instructions":parser.get_format_instructions()
                 }
                )

            response = model.invoke(final_prompt)

        content = response.content

        movie = None
        try:
            movie = parser.parse(content)
        except Exception:
            match = re.search(r"\{.*\}", content, re.DOTALL)
            if match:
                try:
                    movie = Movie(**json.loads(match.group(0)))
                except Exception:
                    movie = None

        st.markdown('<div class="field-label" style="margin-top:1.2rem;">RAW MODEL OUTPUT</div>', unsafe_allow_html=True)
        st.code(content, language="json")

        if movie:
            genre_chips = "".join(f'<span class="chip">{g}</span>' for g in movie.genre)
            cast_list = ", ".join(movie.cast) if movie.cast else "—"
            rating_html = f'<span class="rating-value">{movie.rating}</span> / 10' if movie.rating is not None else "—"

            st.markdown('<div class="field-label" style="margin-top:0.6rem;">STRUCTURED OUTPUT</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="card">
                <div class="card-row">
                    <p class="card-title">{movie.title}</p>
                    <span class="card-year">{movie.release_year or "—"}</span>
                </div>
                <div class="chip-row">{genre_chips}</div>
                <div class="field-label">DIRECTOR</div>
                <div class="field-value">{movie.director or "—"}</div>
                <div class="field-label">CAST</div>
                <div class="field-value">{cast_list}</div>
                <div class="field-label">RATING</div>
                <div class="field-value">{rating_html}</div>
                <hr class="thin">
                <div class="field-label">SUMMARY</div>
                <div class="field-value">{movie.summary}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Could not parse the raw output into the Movie schema.")