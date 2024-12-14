from fastapi import APIRouter

router = APIRouter()

@router.get('/advertisement')
async def get_advertisements():
    return {"message": "hello world"}