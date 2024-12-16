from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()
some_file_path = "./cat.png"

@router.get("/cat")
def cat_route():
    def iterfile():
        with open(some_file_path, mode="rb") as file_like:
            yield from file_like

    return StreamingResponse(iterfile(), media_type="image/png")
