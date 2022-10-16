from fastapi import FastAPI
from apps.todo_app.views import router as todo_router
from apps.user_app.views import router as user_router


app = FastAPI(debug=True)
app.include_router(todo_router)
app.include_router(user_router)