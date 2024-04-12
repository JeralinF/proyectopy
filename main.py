from fastapi import FastAPI, status
import uuid
from fastapi.responses import JSONResponse


app= FastAPI(
    title="Obesity_data_set",
    version= "0.0.1"
)
user = {}

@app.post("/api/v1/user/")
async def create_user(username: str, name: str):
    user_ID= str(uuid.uuid4())
    user[user_ID] = {"username": username, "name": name}
    return {"username": username,
            "name": name,
            "ID": user_ID,
            "message": "Registro exitoso",
            "status_code":201}


@app.get("/api/v1/user/{user_id}")
async def get_user_info(user_id:str):
    user = {
        "ID5524":{
            "username": "Juan1",
            "name": "Juan"
        },
        "ID5525":{
            "username": "Pedro1",
             "name": "Pedro"


         }
    }

    if user_id in user:
        user=[user_id]

        return JSONResponse(
            status_code= status.HTTP_200_OK ,
            content= user
        )
    else:
        return JSONResponse(
            content= "No existe el usuario",
            status_code= status.HTTP_404_NOT_FOUND
        )
