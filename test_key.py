from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  # reads GROQ_API_KEY from .env

llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)
response = llm.invoke("Say hello in German in one short sentence.")
print(response.content)