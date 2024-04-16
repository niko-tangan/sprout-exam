# Sprout Techical Exam - Employee Management App

Employee Management CRUD built with Vue3 and FastAPI

## How to install the project (without using docker)

these steps assume you have both pipenv and pnpm installed (though npm can be used instead of pnpm)

### Python Commands (for backend)

```bash
pipenv --python 3.12
pipenv shell
pipenv install python-dotenv uvicorn fastapi sqlmodel pydantic-settings
cp .env.example .env
```

### PNPM Commands (for frontend)

```bash
pnpm create vue@latest
pnpm install tailwindcss
pnpm install -D prettier prettier-plugin-tailwindcss
```

### Command for starting backend server

```bash
uvicorn main:app --reload --host localhost --port 5000
```

### Command for starting frontend server

```bash
pnpm run dev
```
