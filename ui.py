import streamlit as st
from youtube_analyser import youtube_agent
st.set_page_config(
    page_title="Youtube analyser",
    layout="centered"
)
st.title("AI YOUTUBE VIDEO ANALYSER")

@st.cache_resource
def get_agent():
    return youtube_agent()

agent = get_agent()

#input box
video_url = st.text_input("Enter or paste Youtube Video URL/Link") #IN STR
button = st.button("Analyze video") #TRUE / FALSE
print(video_url , button)

if video_url and button:
    with st.spinner("Analysing video....."):
        response = agent.run(
            f"Analyze this video : {video_url}"
        )
    st.markdown(f"Analysis Report of Video : {video_url}")
    st.markdown(response.content)