# 🚀 EMS Gemini API

Welcome to **EMS Gemini API**, a FastAPI-based application that leverages **Google Generative AI** to transform natural language instructions into SQL queries for seamless interaction with an employee database. 🌟

---

## ✨ Features

- 🤖 **AI-Powered SQL Generation**: Converts plain English instructions into SQL queries using Google's Generative AI.
- 🗄️ **Database Integration**: Executes SQL queries on a MySQL database.
- ⚡ **FastAPI Framework**: Provides a fast and scalable REST API.
- 🌐 **CORS Support**: Enables cross-origin requests for frontend integration.
- 🔒 **Environment Configuration**: Securely manage sensitive data with `.env` files.

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://gitlab.com/gen_ai_applications/ems_gemini_api.git
   cd ems_gemini_api
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the root directory and add the following:
   ```env
   GEMINI_API_KEY=your-google-api-key
   MYSQL_URI=mysql+pymysql://username:password@localhost:3306/employee_db
   ```

5. **Initialize the database**:
   ```bash
   python -c "from app.database import init_db; init_db()"
   ```

---

## 🚀 Usage

1. **Start the server**:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Send a request**:
   Use the `/ai/command` endpoint to generate and execute SQL queries:
   - **Request**:
     ```json
     {
       "input": "Get all employees in the IT department"
     }
     ```
   - **Response**:
     ```json
     {
       "sql": "SELECT * FROM employees WHERE department = 'IT';",
       "result": [
         {
           "id": 1,
           "firstname": "John",
           "lastname": "Doe",
           "department": "IT",
           "salary": "5000"
         }
       ]
     }
     ```

---

## 📂 Project Structure

```
ems_gemini_api/
├── app/
│   ├── ai_engine.py       # AI-based SQL generation
│   ├── database.py        # Database connection and initialization
│   ├── main.py            # FastAPI application entry point
│   ├── models.py          # SQLAlchemy models
│   ├── query_executor.py  # SQL query execution
├── .env                   # Environment variables
├── requirements.txt       # Dependencies
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

---

## 🧰 Dependencies

- **FastAPI**: Web framework
- **Uvicorn**: ASGI server
- **SQLAlchemy**: ORM for database management
- **PyMySQL**: MySQL driver
- **Google Generative AI**: AI-powered SQL generation
- **python-dotenv**: Environment variable management

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## 🌟 Environment Variables

| Variable         | Description                          |
|-------------------|--------------------------------------|
| `GEMINI_API_KEY` | Your Google Generative AI API key    |
| `MYSQL_URI`      | MySQL database connection string     |

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request. Let's build something amazing together! 💡

---

## 🙏 Acknowledgments

- **Google Generative AI** for powering SQL generation.
- **FastAPI** for the robust web framework.
- **SQLAlchemy** for database management.

---

🎉 **Thank you for checking out EMS Gemini API!** If you have any questions or suggestions, feel free to reach out. Happy coding! 💻