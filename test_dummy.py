#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.llm import generate_dummy_data

def test_dummy_data():
    test_questions = [
        "What are the top 5 selling products?",
        "Show me sales by date",
        "Which waiter had the most sales?",
        "What's the total revenue?",
        "Show me product quantities",
        "Random question about data"
    ]
    
    for question in test_questions:
        print(f"\n📝 Question: {question}")
        result = generate_dummy_data(question)
        
        print(f"✅ SQL: {result['sql']}")
        print(f"✅ Records: {len(result['data'])}")
        print(f"✅ Structure: {list(result['data'][0].keys()) if result['data'] else 'No data'}")
        print(f"✅ Sample: {result['data'][0] if result['data'] else 'No data'}")
        print(f"✅ Can visualize: {len(result['data'][0].keys()) == 2 if result['data'] else False}")

if __name__ == "__main__":
    test_dummy_data()
