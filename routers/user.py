from fastapi import APIRouter

router = APIRouter()

@router.get('/user')
async def get_user():
    return {"message": "hello world"}