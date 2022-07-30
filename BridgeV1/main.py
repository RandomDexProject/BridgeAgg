import uvicorn
import os
from dotenv import load_dotenv

from Configs import fastapi_config


try:
    load_dotenv(os.path.dirname(os.path.realpath(__file__)) + "/.env")
except Exception as e:
    print(e)
    import sys
    sys.dont_write_bytecode = True
    load_dotenv(".env")


DOMAIN = os.getenv("DOMAIN") or "http://localhost:8000" 
URL_PREFIX = os.getenv("URL_PREFIX") or ""

app = fastapi_config.config(DOMAIN, URL_PREFIX)


@app.on_event("startup")
async def app_boot():
    ...
    


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
