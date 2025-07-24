import os
from openai import OpenAI
from dotenv import load_dotenv
from app.utils import is_valid_question

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
