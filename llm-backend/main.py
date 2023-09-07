import os
from dotenv import load_dotenv
from fastapi import FastAPI, status
import uvicorn

from typing import Dict

app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def read_root_endpoint() -> Dict[str, str]:
    """
    Basic root call for API
    """
    return {"message": "Hello from {}".format('llm-backend')}

if __name__ == '__main__':
    load_dotenv()
    host = os.environ['server_host']
    port = os.environ['server_port']
    uvicorn.run(app, host=host, port=port)