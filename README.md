# 🧠 ResearchMindAI

AI-Powered Research Assistant for Scientific Literature Analysis

ResearchMindAI is a full-stack AI platform that helps researchers, students, and academics analyze scientific papers using Retrieval-Augmented Generation (RAG), semantic search, vector embeddings, and Generative AI.

---

## 🚀 Features

### 📄 Research Paper Upload
- Upload PDF research papers
- Automatic text extraction
- Metadata extraction
- Intelligent chunking
- Embedding generation

### 🤖 Ask Paper
- Ask questions about uploaded papers
- Context-aware answers using RAG
- Semantic retrieval of relevant sections

### 📚 Literature Review
- Generate structured literature reviews
- Analyze multiple papers together
- Identify key methodologies and trends

### 🎯 Research Gap Analysis
- Existing challenges
- Current limitations
- Unexplored opportunities
- Future research directions
- Novel project ideas

### 📄 Research Proposal Generator
Generates:
- Abstract
- Problem Statement
- Research Gap
- Objectives
- Methodology
- Expected Results
- References

### ⚖️ Compare Papers
- Compare methodologies
- Compare results
- Identify strengths and weaknesses
- Recommend best approaches

### 📊 Research Score
Evaluates:
- Novelty
- Technical Depth
- Feasibility
- Impact
- Publication Potential

### 📝 IEEE Reviewer Mode
Generates:
- Strengths
- Weaknesses
- Technical Review
- Publication Recommendation

---

## 🏗 Architecture

```text
PDF Upload
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embedding Generation
    ↓
Vector Search (RAG)
    ↓
Gemini AI
    ↓
Research Analysis Modules
🛠 Tech Stack
Frontend
Next.js
React
TypeScript
Tailwind CSS
Axios
Backend
FastAPI
Python
AI / ML
Gemini API
RAG
Semantic Search
Vector Embeddings
NLP
Document Processing
PDF Extraction
Metadata Analysis
Text Chunking
📡 API Endpoints
Endpoint	Description
POST /upload-paper	Upload Research Paper
POST /ask-paper	Ask Questions
POST /literature-review	Generate Literature Review
POST /research-gaps	Generate Research Gaps
POST /research-proposal	Generate Research Proposal
POST /compare-papers	Compare Papers
POST /research-score	Research Evaluation
POST /reviewer-mode	IEEE Reviewer Analysis
