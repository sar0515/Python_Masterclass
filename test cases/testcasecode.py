from testcase import divide
#here we import that divide from testcase.py file to test .
def test_divide_regular():
    assert divide(6 , 2) == 3.0

test_divide_regular()