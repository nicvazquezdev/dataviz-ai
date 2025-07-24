import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_sql(question: str, schema_description: str) -> str:
    system_prompt = (
        "You are a data analyst. Your job is to translate natural language questions "
        "into clean, executable SQL queries based on the provided schema. "
        "Return only the raw SQL. Do not include explanations, markdown formatting, or code blocks. "
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

    return response.choices[0].message.content.strip().strip("`")
