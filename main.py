from fastapi import FastAPI
from apps.todo_app.views import router as todo_router
from apps.user_app.views import router as user_router
from fastapi_pagination import add_pagination


app = FastAPI(debug=True)
app.include_router(todo_router)
app.include_router(user_router)

# Adding pagination for the app
add_pagination(app)