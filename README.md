# Sprout Techical Exam - Employee Management App

Employee Management CRUD built with Vue3 and FastAPI

##TODO:
1. Finish Backend
2. Finish Frontend
3. Dockerize the project (because i'd rather make the thing first then worry about that later)
4. Add test cases / make the website look nicer

## How to install the project
these steps assume you have both pipenv and pnpm installed (though npm can be used instead of pnpm)

### Python Commands (for backend)
```bash
pipenv --python 3.12
pipenv shell
pipenv install python-dotenv uvicorn fastapi sqlmodel pydantic-settings
```

### PNPM Commands (for frontend)
```bash
pnpm create vue@latest
pnpm install tailwindcss 
pnpm install -D prettier prettier-plugin-tailwindcss
```

### Command for starting backend server
```bash
uvicorn main:app --reload --host localhost --port 5000```
