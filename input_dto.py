from typing import Optional
from pydantic import BaseModel

class InputRequest(BaseModel):
    page_count: Optional[int] = 1
    proxy_string: Optional[str] = None