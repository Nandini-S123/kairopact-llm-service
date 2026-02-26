# Async FastAPI LLM Service – Schema Validated JSON

**Overview**
This project is a production-style FastAPI service that calls an LLM and returns
strictly schema-validated structured JSON using Pydantic.

It is designed with clean separation of concerns, environment-based configuration,
retry handling, and domain-aware prompt construction to ensure deterministic outputs.

**Features**
- Async FastAPI endpoint
- Pydantic request/response validation
- LLM provider abstraction (configurable via environment variables)
- Retry with exponential backoff (Tenacity)
- Domain-aware prompt builder to remove acronym ambiguity
- Health check endpoint
- Graceful fallback when LLM is unavailable
**Project Structure**
app/
├── api/        # Route definitions
├── core/       # Config and LLM service layer
├── schemas/    # Pydantic models
└── main.py     # FastAPI entry point

**Execution Steps**

pip install -r requirements.txt
GROQ_API_KEY=your_api_key
MODEL_NAME=llama-3.1-8b-instant

uvicorn app.main:app --reload
