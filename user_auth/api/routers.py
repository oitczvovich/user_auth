from fastapi import APIRouter

from user_auth.api.endpoints import 

router = APIRouter()


@router.get('/hello')
def read_root():
    return {'Hello': 'FastApi'}