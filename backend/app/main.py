from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import text
from app.db import SessionLocal
from app.llm import generate_sql

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

SCHEMA_DESCRIPTION = """
Table: sales
Columns:
- date: string (format: M/D/YYYY)
- week_day: string
- hour: string
- ticket_number: string
- waiter: integer
- product_name: string
- quantity: float
- unitary_price: integer
- total: integer

Note: The "date" column is a string in M/D/YYYY format, not ISO format. Queries must use dates like '10/10/2024' instead of '2024-10-10'.
"""

@app.post("/ask")
def ask_question(request: QuestionRequest):
    session = SessionLocal()
    try:
        sql = generate_sql(request.question, SCHEMA_DESCRIPTION)
        query = text(sql)
        result = session.execute(query)
        rows = [dict(row._mapping) for row in result]
        return {"sql": sql, "data": rows}
    except Exception as e:
        return {"error": str(e)}
    finally:
        session.close()
