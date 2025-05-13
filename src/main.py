from fastapi import FastAPI
from pydantic import BaseModel
from src.retriever import search_cloudsearch, build_prompt_with_context
from src.bedrock_integration import generate_titan_text

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: QueryRequest):
    docs = search_cloudsearch(query.question)
    prompt = build_prompt_with_context(docs, query.question)
    answer = generate_titan_text(prompt)
    return {"answer": answer}
