from fastapi.routing import APIRouter

router = APIRouter(tags=['Products'])


@router.get('/')
def get_products():
    return {}
