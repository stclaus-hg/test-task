from core.api.dtos import UserCreateModel, UserModel, UserUpdateModel
from core.impl.rest_controller import RestController

from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/v1")
rest_controller = RestController()


@router.get("/")
async def users():
    return await rest_controller.users_list()


@router.post("/user")
async def create_user(payload: UserCreateModel):
    user = await rest_controller.create_user(payload)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(user))


@router.put("/user/{id}")
async def update_user(id: str, payload: UserUpdateModel):
    res = await rest_controller.update_user(id, payload)
    if res:
        return res
    raise HTTPException(status_code=404, detail=f"User {id} not found")


@router.delete("/user/{id}")
async def delete_user(id: str):
    deleted_count = await rest_controller.delete_user(id)

    if deleted_count == 1:
        return {"message": "User was deleted"}

    raise HTTPException(status_code=404, detail=f"User {id} not found")



# 2. Define and implement validation strategy for each one of given fields.
# 4. Implement a simple authentication middleware.
# 5. Create a route restricted only for user's with admin roles which allow to change by oid(ObjectId) other user's attributes except `hashed_pass`.
# 6. Create a docker-compose file to deploy the app.
# 7. Upload the solution to github and send the link.
