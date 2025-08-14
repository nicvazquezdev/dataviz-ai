import os
from openai import OpenAI
from dotenv import load_dotenv
from app.utils import is_valid_question
import random
from datetime import datetime, timedelta

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_dummy_data(question: str) -> dict:
    """Generate dummy data based on the question"""
    question_lower = question.lower()
    
    # Determine what type of visualization to generate based on the question
    if any(word in question_lower for word in ["top", "best", "selling", "products", "product"]):
        # Top products visualization
        products = [
            "Alfajor Super DDL x un",
            "Alfajor Sin Azucar Suelto", 
            "Conito choc caja x12un",
            "Alfajor Sin Azucar x9 Un",
            "Alfajor 70 cacao caja x9un",
            "Alf. 150 aniv. X 8 unidades",
            "Alfajor mixto caja x6un",
            "Alfajor 70 cacao x un"
        ]
        
        # Generate top 5-8 products with sales data
        num_products = min(len(products), random.randint(5, 8))
        selected_products = random.sample(products, num_products)
        
        dummy_data = []
        for product in selected_products:
            dummy_data.append({
                "product": product,
                "sales": random.randint(10000, 500000)
            })
        
        # Sort by sales descending
        dummy_data.sort(key=lambda x: x["sales"], reverse=True)
        
        dummy_sql = f"-- Dummy SQL for: {question}\nSELECT product_name, SUM(total) as sales FROM sales_data GROUP BY product_name ORDER BY sales DESC LIMIT {num_products}"
        
    elif any(word in question_lower for word in ["date", "time", "trend", "over time", "daily", "monthly"]):
        # Time series visualization
        dates = []
        sales = []
        
        # Generate last 7-14 days of data
        num_days = random.randint(7, 14)
        end_date = datetime.now()
        
        for i in range(num_days):
            date = end_date - timedelta(days=num_days - i - 1)
            dates.append(date.strftime("%m/%d/%Y"))
            sales.append(random.randint(50000, 200000))
        
        dummy_data = []
        for i in range(len(dates)):
            dummy_data.append({
                "date": dates[i],
                "sales": sales[i]
            })
        
        dummy_sql = f"-- Dummy SQL for: {question}\nSELECT date, SUM(total) as sales FROM sales_data GROUP BY date ORDER BY date LIMIT {num_days}"
        
    elif any(word in question_lower for word in ["waiter", "employee", "staff", "server"]):
        # Waiter performance visualization
        waiters = [0, 51, 23, 45, 12, 67, 89, 34]
        num_waiters = random.randint(4, len(waiters))
        selected_waiters = random.sample(waiters, num_waiters)
        
        dummy_data = []
        for waiter in selected_waiters:
            dummy_data.append({
                "waiter": f"Waiter {waiter}",
                "sales": random.randint(20000, 300000)
            })
        
        # Sort by sales descending
        dummy_data.sort(key=lambda x: x["sales"], reverse=True)
        
        dummy_sql = f"-- Dummy SQL for: {question}\nSELECT waiter, SUM(total) as sales FROM sales_data GROUP BY waiter ORDER BY sales DESC LIMIT {num_waiters}"
        
    elif any(word in question_lower for word in ["revenue", "total", "sum", "amount"]):
        # Revenue summary visualization
        categories = ["Alfajores", "Conitos", "Special Products", "Bulk Items"]
        num_categories = random.randint(3, len(categories))
        selected_categories = random.sample(categories, num_categories)
        
        dummy_data = []
        for category in selected_categories:
            dummy_data.append({
                "category": category,
                "revenue": random.randint(100000, 800000)
            })
        
        dummy_sql = f"-- Dummy SQL for: {question}\nSELECT product_category, SUM(total) as revenue FROM sales_data GROUP BY product_category ORDER BY revenue DESC"
        
    elif any(word in question_lower for word in ["quantity", "units", "count"]):
        # Quantity analysis visualization
        products = [
            "Alfajor Super DDL x un",
            "Alfajor Sin Azucar Suelto", 
            "Conito choc caja x12un",
            "Alfajor Sin Azucar x9 Un"
        ]
        num_products = random.randint(3, len(products))
        selected_products = random.sample(products, num_products)
        
        dummy_data = []
        for product in selected_products:
            dummy_data.append({
                "product": product,
                "quantity": random.randint(50, 500)
            })
        
        # Sort by quantity descending
        dummy_data.sort(key=lambda x: x["quantity"], reverse=True)
        
        dummy_sql = f"-- Dummy SQL for: {question}\nSELECT product_name, SUM(quantity) as total_quantity FROM sales_data GROUP BY product_name ORDER BY total_quantity DESC LIMIT {num_products}"
        
    else:
        # Default: generic sales data
        products = [
            "Alfajor Super DDL x un",
            "Alfajor Sin Azucar Suelto", 
            "Conito choc caja x12un",
            "Alfajor Sin Azucar x9 Un",
            "Alfajor 70 cacao caja x9un"
        ]
        num_products = random.randint(3, len(products))
        selected_products = random.sample(products, num_products)
        
        dummy_data = []
        for product in selected_products:
            dummy_data.append({
                "product": product,
                "value": random.randint(10000, 200000)
            })
        
        dummy_sql = f"-- Dummy SQL for: {question}\nSELECT product_name, SUM(total) as value FROM sales_data GROUP BY product_name ORDER BY value DESC LIMIT {num_products}"
    
    return {
        "sql": dummy_sql,
        "data": dummy_data,
        "is_dummy": True
    }

def generate_sql(question: str, schema_description: str) -> str:
    # First validate if the question makes sense
    if not is_valid_question(question):
        raise ValueError("Invalid question: The question doesn't appear to be a valid data query.")
    
    # Check if API key is available
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key.strip() == "":
        raise ValueError("API_KEY_MISSING: No OpenAI API key configured")
    
    system_prompt = (
        "You are a data analyst. Your job is to translate natural language questions "
        "into clean, executable SQL queries based on the provided schema. "
        "IMPORTANT: If the question is nonsensical, contains only gibberish, or cannot be "
        "reasonably translated into a meaningful SQL query, respond with 'INVALID_QUESTION'. "
        "Otherwise, return only the raw SQL. Do not include explanations, markdown formatting, or code blocks. "
        "Do not prefix your response with 'sql' or anything else. Output only the SQL query."
    )

    user_prompt = f"Schema:\n{schema_description}\n\nQuestion: {question}\nSQL:"

    try:
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
        
    except Exception as e:
        # Check if it's an API key related error
        error_str = str(e).lower()
        if any(keyword in error_str for keyword in ["api_key", "authentication", "invalid_api_key", "unauthorized"]):
            raise ValueError("API_KEY_ERROR: OpenAI API key is invalid or not working")
        else:
            # Re-raise other errors
            raise e
