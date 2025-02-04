<div align="center">

# Backend

</div>

---

## 📦 Requirements  

To run the backend, you will need the following dependencies installed:  

- **Python 3.12+**: Core language for the backend.  
- **Package Manager**: [**uv**](https://github.com/astral-sh/uv), an extremely fast Python package and project manager, written in Rust.s.

---

## 📦 Key Dependencies  

The backend uses the following libraries to ensure seamless functionality and robust performance:  

| Dependency                 | Version     | Purpose                                                                 |
|----------------------------|-------------|-------------------------------------------------------------------------|
| **aiosqlite**              | `>=0.20.0`  | Async driver for SQLite, used in debug mode.                           |
| **alembic**                | `>=1.14.1`  | Database migrations and version control.                               |
| **asyncpg**                | `>=0.30.0`  | High-performance async PostgreSQL driver.                              |
| **fastapi[standard]**      | `>=0.115.8` | Web framework for building REST APIs.                                  |
| **greenlet**               | `>=3.1.1`   | Concurrency support for SQLAlchemy.                                    |
| **psycopg2-binary**        | `>=2.9.10`  | PostgreSQL database adapter for production.                            |
| **python-dotenv**          | `>=1.0.1`   | Environment variable management.                                       |
| **sqlalchemy**             | `>=2.0.37`  | ORM and SQL toolkit for database interactions.                         |
| **sqlmodel**               | `>=0.0.22`  | A layer on top of SQLAlchemy for defining database models.             |
| **uuid**                   | `>=1.30`    | Universally unique identifier generation.                              |
| **uvicorn**                | `>=0.34.0`  | ASGI server for running FastAPI applications.                          |  

These dependencies are automatically installed with the `uv install` command as specified in the `uv.lock` file.  

---

## 🛠 General Workflow  

### 1. **Setup Environment**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/haxgun/Valory.git
   cd backend
   ```
2. Install dependencies:
    ```bash
    uv init
    ```
   
3. Create a .env file to configure environment variables. Example:
    ```env
   PROJECT_NAME=""
   PROJECT_DESCRIPTION=""
   VERSION=""
   DEBUG=True
   
   TWITCH_CLIENT_ID=""
   TWITCH_CLIENT_SECRET=""
   
   DATABASE_LOGIN=""
   DATABASE_PASSWORD=""
   DATABASE_IP=""
   DATABASE_PORT=5432
   DATABASE_NAME=""
    ```

4. Run the Application
    ```bash
   uv run main.py
   ```

---

## 🛡 API Documentation  

The backend provides an auto-generated, interactive API documentation accessible at:  
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)  

Explore endpoints, test requests, and understand API details conveniently!