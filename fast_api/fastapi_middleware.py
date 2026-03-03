# at the import level
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

app = FastAPI()

# after the `app` variable
@app.middleware("http")
async def modify_request_response_middleware(request: Request, call_next):
    # Intercept and modify the incoming request
    request.scope["path"] = str(request.url.path).replace("api", "apiv2")
    # Process the modified request
    response = await call_next(request)
    # Transform the outgoing response
    if isinstance(response, StreamingResponse):
        response.headers["X-Custom-Header"] = "Modified"
    return response