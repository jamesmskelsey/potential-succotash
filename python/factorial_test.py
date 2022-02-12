from factorial import factorial

def test_normal_factorial():
    assert factorial(8) == 40320
    assert factorial(18) == 6402373705728000
    assert factorial(
        45) == 119622220865480194561963161495657715064383733760000000000

def test_negative_factorial():
    assert factorial(-8) == 1

def test_factorial_zero():
    assert factorial(0) == 1