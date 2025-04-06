from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from .db import get_db
from .models import AddressInput, WalletInfo, WalletRequest
from .tron_client import get_wallet_info as tron_info

app = FastAPI()


@app.get("/")
async def root():
    return JSONResponse(content={"message": "Здравствуйте, товарищ работодатель!"}, media_type="application/json; charset=utf-8")


@app.post("/wallet", response_model=WalletInfo)
def get_wallet_info(data: AddressInput, db=Depends(get_db)):
    return tron_info(data.address, db)


@app.get("/requests")
def get_requests(skip: int = 0, limit: int = 10, db=Depends(get_db)):
    return db.query(WalletRequest).offset(skip).limit(limit).all()
