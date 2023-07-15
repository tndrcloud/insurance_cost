from typing import List, Dict



@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )


@app.get("/users/get_user/{id}", response_model=List[User])
async def get_user(user_id: int) -> List[User]:
    return [user for user in db.users if user.get("id") == user_id]
