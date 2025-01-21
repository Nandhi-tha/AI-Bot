# AI Call Center

AI Call Center is an interactive and professional call center application designed to handle customer queries effectively. It features both text-based and voice-based interactions, leveraging AI-powered conversational capabilities to deliver efficient and empathetic responses.

## Features

- **Text Chat Interface**: Seamlessly interact with the chatbot through a text-based interface.
- **Voice Chat Functionality**: Enable voice-based conversations for a more natural communication experience.
- **Memory-Powered Conversations**: Retain conversation history to provide contextually relevant and continuous interactions.
- **Text-to-Speech (TTS)**: Optional feature to convert chatbot responses to audio for enhanced accessibility.
- **Streamlit-Powered UI**: Clean and intuitive user interface built with Streamlit.
- **LangSmith Integration**: Monitor and trace AI interactions using LangSmith for enhanced observability.
- **Deployed on Streamlit**: The application is hosted and accessible via Streamlit for ease of use.

## Tech Stack

- **Backend**: Python
  - [LangChain](https://www.langchain.com/) for managing the conversational AI logic.
  - [Google Generative AI](https://cloud.google.com/generative-ai) for advanced natural language processing.
  - [LangSmith](https://smith.langchain.com/) for AI tracing and observability.
  - [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for voice input handling.
  - [gTTS](https://pypi.org/project/gTTS/) for converting text responses to speech.
  - [dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables securely.
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Environment**: Docker-compatible, lightweight runtime.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Nandhi-tha/AI-Bot.git
   cd AI-Bot
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory with the following content:
   ```env
   GOOGLE_KEY=your_google_api_key
   LANGSMITH_TRACING_V2=true
   LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
   LANGSMITH_API_KEY="your-api-key"
   LANGSMITH_PROJECT="AI-Bot"
   ```
   Replace `your_google_api_key` and `your-api-key` with the appropriate keys.

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## Usage

### Text Chat
- Start the application and navigate to the **Text Chat** option from the sidebar.
- Type your queries in the input box, and the chatbot will respond in real-time.

### Voice Chat
- Select the **Voice Chat** option from the sidebar.
- Click the "Start Recording" button and speak into your microphone.
- The chatbot will process your query and provide a response. Optionally, enable the **Voice Response** checkbox for audio feedback.

### Additional Options
- Use the **Clear Conversation** button in the sidebar to reset the chat history.

## File Structure

```plaintext
.
├── app.py             # Streamlit app entry point
├── bot.py             # Chatbot logic and AI integration
├── requirements.txt   # Python dependencies
├── .env               # Example environment variable file
└── README.md          # Project documentation
```

## Dependencies

- Python 3.8+
- [LangChain](https://www.langchain.com/)
- [Google Generative AI](https://cloud.google.com/generative-ai)
- [Streamlit](https://streamlit.io/)
- [LangSmith](https://smith.langchain.com/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS](https://pypi.org/project/gTTS/)

## Future Enhancements

- Add multi-language support for a wider audience.
- Implement user authentication and role-based access control.
- Integrate analytics to track user interactions and chatbot performance.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to the project by submitting issues or pull requests. Happy coding!
