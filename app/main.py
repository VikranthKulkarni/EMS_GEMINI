from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.ai_engine import generate_sql
from app.query_executor import execute_sql_query
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()  # auto-create tables if not exist

@app.post("/ai/command")
async def handle_command(request: Request):
    print(await request.body()) # <-- Debug line
    # data = await request.json()
    # user_input = data.get("input", "")
    # if not user_input:
    #     return {"error": "Missing input"}

    # sql = generate_sql(user_input)
    # print("Generated SQL:", sql)
    # result = execute_sql_query(sql)
    # return {"sql": sql, "result": result}
    try:
        content_type = request.headers.get("Content-Type", "")
        if "application/json" in content_type:
            data = await request.json()
            user_input = data.get("input", "")
        else:
            user_input = (await request.body()).decode("utf-8").strip()
        
        sql = generate_sql(user_input)  # Use the imported generate_sql function

        result = execute_sql_query(sql)  # Use the imported execute_sql_query function

        return JSONResponse(content={"sql": sql, "result": result})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    

