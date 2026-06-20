from app.services.gemini_service import ask_gemini

def answer_question(question, chunks):

    context = "\n\n".join(chunks[:5])

    prompt = f"""
    Answer the question using ONLY the provided paper context.

    Context:
    {context}

    Question:
    {question}
    """

    return ask_gemini(prompt)