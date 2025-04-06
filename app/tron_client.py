from tronpy import Tron
from .models import WalletRequest

client = Tron()


def get_wallet_info(address: str, db):
    account = client.get_account(address)
    balance = client.get_account_balance(address)

    db.add(WalletRequest(address=address))
    db.commit()

    return {
        "address": address,
        "balance": balance,
        "bandwidth": account.get("bandwidth", 0),
        "energy": account.get("energy", 0)
    }