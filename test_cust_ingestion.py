from cust_ingestion_1 import calculate_bonus

def test_bonus_calculation():
    assert calculate_bonus(50000) == 5000
def test_zero_salary():
    assert calculate_bonus(0) == 0
def test_small_salary():
    assert calculate_bonus(10000) == 1000
