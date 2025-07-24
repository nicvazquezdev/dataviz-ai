from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import text, inspect
from app.db import SessionLocal, engine
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

def get_table_schema():
    """Get schema from the actual database table"""
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    if not tables:
        return "No tables found. Please load a CSV file first."
    
    table_name = tables[0]
    columns = inspector.get_columns(table_name)
    
    schema_lines = [f"Table: {table_name}", "Columns:"]
    
    for column in columns:
        col_name = column['name']
        col_type = str(column['type']).lower()
        
        if 'varchar' in col_type or 'text' in col_type:
            type_desc = "string"
        elif 'integer' in col_type:
            type_desc = "integer"
        elif 'float' in col_type or 'numeric' in col_type:
            type_desc = "float"
        else:
            type_desc = "string"
        
        schema_lines.append(f"- {col_name}: {type_desc}")
    
    schema = "\n".join(schema_lines)

    if any(col['name'] == 'date' for col in columns):
        schema += (
            "\n\nNote: The 'date' column is a string in M/D/YYYY format, not ISO format. "
            "Queries must use dates like '10/10/2024' instead of '2024-10-10'."
        )

    return schema

@app.post("/ask")
def ask_question(request: QuestionRequest):
    session = SessionLocal()
    try:
        schema_description = get_table_schema()
        sql = generate_sql(request.question, schema_description)
        query = text(sql)
        result = session.execute(query)
        rows = [dict(row._mapping) for row in result]
        return {"sql": sql, "data": rows}
    except ValueError as e:
        # Handle invalid questions specifically
        if "Invalid question" in str(e):
            return {"error": str(e), "type": "invalid_question"}
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Database error: {str(e)}"}
    finally:
        session.close()
