from langchain_groq import ChatGroq
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)
response = llm.invoke("What is the capital of France?")
print(response.content)


