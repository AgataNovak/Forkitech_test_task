from app.db import engine, Session
from app.models import WalletRequest


def test_db_write():
    db = Session(engine)
    request = WalletRequest(address="TEST_ADDRESS")
    db.add(request)
    db.commit()
    assert db.query(WalletRequest).filter_by(address="TEST_ADDRESS").first()
