
from dicount_function import calculate_discount

def test_dicount_20_or_more():
    """Does a discount of 20 or more work"""
    result = calculate_discount(100, 25)
    assert result == "Amount to pay is KSH 75.00"

def test_dicount_less_than_20():
    """Does discount less than 20 work"""
    result = calculate_discount(100, 10)
    assert result == "Amount to pay is KSH 100.00"

def test_zero_dicount():
    """Does dicount equal zero work"""
    result = calculate_discount(100, 0)
    assert result == "Amount to pay is KSH 100.00"

def test_100_percent_dicount():
    """Does dicount equal 100 work"""
    result = calculate_discount(100,100)
    assert result == "Amount to pay is KSH 0.00"

def test_large_price():
    """Does larger prices work"""
    result = calculate_discount(1000000,30)
    assert result == "Amount to pay is KSH 700000.00"

def test_negative_dicount():
    """Does negative dicount value work"""
    result = calculate_discount(100, -10)
    assert result == "Amount to pay is KSH 100.00"

def test_edge_case_zero_price():
    """Does price equal zero work"""
    result = calculate_discount(0, 25)
    assert result == "Amount to pay is KSH 0.00"