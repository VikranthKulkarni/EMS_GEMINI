from app.database import engine
from sqlalchemy import text

def execute_sql_query(sql: str):
    try:
        with engine.connect() as connection:
            # Begin a transaction
            transaction = connection.begin()
            try:
                result = connection.execute(text(sql))
                transaction.commit()  # Commit the transaction
                if result.returns_rows:
                    return [dict(row._mapping) for row in result]
                return {"status": "success"}
            except Exception as e:
                transaction.rollback()  # Rollback the transaction on error
                raise e
    except Exception as e:
        return {"error": str(e)}
