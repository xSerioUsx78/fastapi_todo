from fastapi import FastAPI
from apps.todo_app.views import router as todo_router


app = FastAPI(debug=True)
app.include_router(todo_router)