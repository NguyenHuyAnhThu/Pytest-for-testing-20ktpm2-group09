import pytest
from wallet import Wallet, InsufficientAmount, NegativeMoney


def test_TC001_default_zero_initial_amount():
    wallet = Wallet(0)
    assert wallet.balance == 0


def test_TC002_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100


def test_TC003_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0


def test_TC004_setting_initial_negative_amount():
    with pytest.raises(NegativeMoney):
        wallet = Wallet(-100)


def test_TC005_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100


def test_TC006_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(2)
    assert wallet.balance == 12


def test_TC007_wallet_add_negative_cash():
    wallet = Wallet(10)
    with pytest.raises(NegativeMoney):
        wallet.add_cash(-90)
    assert wallet.balance == 10


# def test_TC008_wallet_spend_cash_raises_exception_on_insufficient_amount():
#     wallet = Wallet(50)
#     with pytest.raises(InsufficientAmount):
#         wallet.spend_cash(100)
#     assert wallet.balance == 50


def test_TC009_wallet_spend_negative_cash():
    wallet = Wallet(90)
    with pytest.raises(NegativeMoney):
        wallet.spend_cash(-10)
    assert wallet.balance == 90


# def test_TC010_wallet_spend_cash():
#     wallet = Wallet(90)
#     wallet.spend_cash(10)
#     assert wallet.balance == 80
