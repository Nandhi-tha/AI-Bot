import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains.llm import LLMChain

class Chatbot:
    def __init__(self):
        load_dotenv()
        GOOGLE_API_KEY = os.getenv("GOOGLE_KEY")
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5, api_key=GOOGLE_API_KEY)

        # template = """The assistant is polite, helpful, and knowledgeable. 
        # It provides clear and concise answers, explains concepts in simple terms, and offers helpful suggestions when appropriate. \n
        # Conversation history: {history}\n
        # User: {input}\n
        # Assistant:
        # """

        template = """The assistant is a professional and empathetic call center agent, trained to handle customer queries effectively. 
It actively listens to the user's concerns, identifies their needs, and provides clear and concise resolutions. 
The assistant ensures all responses are polite, helpful, and action-oriented, aiming to resolve the user's issues efficiently while maintaining a friendly tone. 
If additional information or context is needed, the assistant will ask clarifying questions.

Conversation guidelines:
- Acknowledge the user's concerns with empathy.
- Provide actionable and relevant solutions promptly.
- Use a professional yet friendly tone.
- Confirm that the user is satisfied before concluding the interaction.

Conversation history: 
{history}

User: {input}
Assistant:
"""

        prompt_template = PromptTemplate(
            input_variables=["history", "input"],
            template=template
        )

        self.memory = ConversationBufferMemory()
        self.chain = LLMChain(
            llm=self.llm,
            verbose=False,
            memory=self.memory,
            prompt=prompt_template
        )

    def chat(self, user_input: str) -> str:
        try:
            response = self.chain.invoke(input=user_input)
            return response["text"]
        except Exception as error:
            return f"Error: {error}"

    def get_history(self):
        return self.memory.load_memory_variables({})
    
