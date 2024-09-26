#!/usr/bin/env python
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes
from langserve import RemoteRunnable

# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]="pr-sparkling-talent-8"


# Create prompt template
system_template = "Translate the following into {lang}"
prompt_template = ChatPromptTemplate([
    ("system", system_template),
    ("user","{text}")
])

# Create model
model = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-4o"
)

# Create output parser

parser = StrOutputParser()

# Create chain

chain = prompt_template | model | parser

# Create FastAPI app

app = FastAPI(
    title="LangChain Server",
    version="0.1.0",
    description="A server for LangChain",
)

# Add chain route

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)