import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def is_valid_question(question: str) -> bool:
    """Check if the question is a valid data query"""
    question = question.strip().lower()
    
    # Check if question is too short or just gibberish
    if len(question) < 3:
        return False
    
    # Check if question contains mostly non-alphabetic characters
    alpha_chars = sum(1 for c in question if c.isalpha())
    total_chars = len(question.replace(' ', ''))
    if total_chars > 0 and alpha_chars / total_chars < 0.3:
        return False
    
    # Check if question contains common query words
    query_indicators = [
        'what', 'how', 'when', 'where', 'who', 'which', 'show', 'get', 'find',
        'list', 'count', 'sum', 'total', 'average', 'max', 'min', 'top', 'bottom',
        'sales', 'product', 'customer', 'order', 'date', 'price', 'quantity'
    ]
    
    has_query_indicator = any(indicator in question for indicator in query_indicators)
    
    return has_query_indicator

def generate_sql(question: str, schema_description: str) -> str:
    # First validate if the question makes sense
    if not is_valid_question(question):
        raise ValueError("Invalid question: The question doesn't appear to be a valid data query.")
    
    system_prompt = (
        "You are a data analyst. Your job is to translate natural language questions "
        "into clean, executable SQL queries based on the provided schema. "
        "IMPORTANT: If the question is nonsensical, contains only gibberish, or cannot be "
        "reasonably translated into a meaningful SQL query, respond with 'INVALID_QUESTION'. "
        "Otherwise, return only the raw SQL. Do not include explanations, markdown formatting, or code blocks. "
        "Do not prefix your response with 'sql' or anything else. Output only the SQL query."
    )

    user_prompt = f"Schema:\n{schema_description}\n\nQuestion: {question}\nSQL:"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )

    sql_response = response.choices[0].message.content.strip().strip("`")
    
    # Check if the AI detected an invalid question
    if sql_response.strip() == "INVALID_QUESTION":
        raise ValueError("Invalid question: The question cannot be translated into a meaningful SQL query.")
    
    return sql_response
