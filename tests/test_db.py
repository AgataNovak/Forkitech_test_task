from app.db import engine, Session
from app.models import WalletRequest

# тесты взамодействия с базой данных

def test_db_write():
    db = Session(engine)
    request = WalletRequest(address="TEST_ADDRESS")
    db.add(request)
    db.commit()
    assert db.query(WalletRequest).filter_by(address="TEST_ADDRESS").first()
