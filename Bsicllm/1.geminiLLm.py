from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("GOOGLE_API_KEY"))
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
response = llm.invoke("What is the capital of France?")
print(response.content[0:19] )