from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class WalletRequest(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True)
    address = Column(String)


class AddressInput(BaseModel):
    address: str


class WalletInfo(BaseModel):
    address: str
    balance: float
    bandwidth: int
    energy: int
