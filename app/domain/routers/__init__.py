from fastapi import (
    APIRouter, 
    Response
)

from starlette.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)

class BaseRouter(APIRouter):
  
    def post(self, *args, **kwargs):
        if not "status_code" in kwargs:
            kwargs["status_code"] = HTTP_201_CREATED
        return super().post(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if not "status_code" in kwargs:
            kwargs["status_code"] = HTTP_204_NO_CONTENT
        if not "response_class" in kwargs:
            kwargs["response_class"] = Response
        return super().delete(*args, **kwargs)
