from fastapi import FastAPI, UploadFile, File, Body
import os

from app.services.pdf_service import extract_pdf_text
from app.services.metadata_service import extract_metadata
from app.services.chunking_service import create_chunks
from app.services.rag_service import answer_question

app = FastAPI(title="ResearchMind AI")

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

# Store latest uploaded paper chunks
LATEST_CHUNKS = []


@app.get("/")
def home():
    return {"message": "ResearchMind AI Backend Running"}


@app.post("/upload-paper")
async def upload_paper(file: UploadFile = File(...)):

    global LATEST_CHUNKS

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_pdf_text(file_path)

    metadata = extract_metadata(extracted_text)

    chunks = create_chunks(extracted_text)

    # Save chunks for question answering
    LATEST_CHUNKS = chunks

    return {
        "message": "Paper uploaded successfully",
        "filename": file.filename,
        "metadata": metadata,
        "total_chunks": len(chunks),
        "first_chunk": chunks[0][:1000] if chunks else ""
    }


@app.post("/ask-paper")
async def ask_paper(data: dict = Body(...)):

    question = data.get("question", "")

    if not LATEST_CHUNKS:
        return {
            "error": "Please upload a paper first."
        }

    answer = answer_question(
        question,
        LATEST_CHUNKS
    )

    return {
        "question": question,
        "answer": answer
    }