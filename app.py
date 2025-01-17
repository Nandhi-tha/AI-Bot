import io
import streamlit as st
from bot import Chatbot
import speech_recognition as sr
from gtts import gTTS

chatbot = Chatbot()

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🗪",
    layout="centered"
)

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "current_page" not in st.session_state:
        st.session_state.current_page = "chat"
    if "enable_voice_response" not in st.session_state:
        st.session_state.enable_voice_response = False

def play_text_to_speech_streamlit(text):
    tts = gTTS(text)
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    st.audio(audio_fp, format="audio/mp3")

def chat_page():
    st.title("AI Chatbot 🗪")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type here"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Response from chatbot
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                response = chatbot.chat(prompt)
                if response:
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})

                    # Check if voice response is enabled
                    if st.session_state.enable_voice_response:
                        play_text_to_speech_streamlit(response)

def voice_conversation_page():
    st.title("Voice Chat 🗣")
    st.write("Click the button below and start speaking.")

    recognizer = sr.Recognizer()
    
    # Placeholder for status
    status_placeholder = st.empty()
    if st.button("Start Recording"):
        listening_message = status_placeholder.info("Listening...")
        
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=10)
                listening_message.empty()
                
                try:
                    query = recognizer.recognize_google(audio)
                    
                    st.chat_message("user").markdown(query)
                    st.session_state.messages.append({"role": "user", "content": query})
                    
                    with st.chat_message("assistant"):
                        with st.spinner("Generating response..."):
                            response = chatbot.chat(query)
                            if response:
                                st.markdown(response)
                                st.session_state.messages.append({"role": "assistant", "content": response})

                                # Check if voice response is enabled
                                if st.session_state.enable_voice_response:
                                    play_text_to_speech_streamlit(response)
                
                except sr.UnknownValueError:
                    status_placeholder.error("Sorry, I could not understand the audio.")
                except sr.RequestError as e:
                    status_placeholder.error(f"Error with speech recognition service: {e}")
                
        except Exception as e:
            status_placeholder.error(f"An error occurred: {str(e)}")
                                
def main():
    initialize_session_state()

    # Sidebar
    with st.sidebar:
        st.title("Chat Options")

        if st.button("Text Chat"):
            st.session_state.current_page = "chat"
            st.rerun()
        
        if st.button("Voice Chat"):
            st.session_state.current_page = "voice"
            st.rerun()

        st.session_state.enable_voice_response = st.checkbox("Enable voice response", value=st.session_state.enable_voice_response)
        
        if st.button("Clear Conversation"):
            st.session_state.messages = []
            st.rerun()
    
    # Main content
    if st.session_state.current_page == "voice":
        voice_conversation_page()
    else:
        chat_page()

if __name__ == "__main__":
    main()
