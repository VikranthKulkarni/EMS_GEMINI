import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
    "temperature": 0.2,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 256,
}

# List available models to verify the correct model name and attributes
try:
    available_models = list(genai.list_models())  # Convert generator to list
    for model in available_models:
        print(f"Model Name: {model.name}")
        print(f"Model Attributes: {model.__dict__}")  # Print all attributes of the model
except Exception as e:
    print(f"Error listing models: {e}")

# Use the correct model name
model = genai.GenerativeModel("models/gemini-2.0-flash-001", generation_config=generation_config)

def generate_sql(prompt: str) -> str:
    try:
        query_prompt = f"""
        You are a helpful AI assistant. Convert the following plain English instruction or JSON into a SQL query (MySQL format) for the 'employees' table:
        {prompt}

        Important rules:
        - The table name is "employees"
        - Columns: id, firstname, lastname, department, salary
        - Return only the SQL query, nothing else.
        """
        response = model.generate_content(query_prompt)
        sql_query = response.text.strip()

        # Remove Markdown formatting if present
        if sql_query.startswith("```") and sql_query.endswith("```"):
            sql_query = sql_query.strip("```").strip("sql").strip()

        return sql_query
    except Exception as e:
        raise RuntimeError(f"Error generating SQL: {str(e)}")
