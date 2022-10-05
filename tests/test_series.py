import pytest

from math_series.series import fibonacci

'''Here is the testing part for fibonacci'''

def test_fibozero():
    actual=fibonacci(0)
    expected=0
    assert actual == expected

def test_fiboone():
    actual=fibonacci(1)
    expected=1
    assert actual == expected

def test_fibotwo():
    actual=fibonacci(2)
    expected=1
    assert actual == expected

def test_fibothree():
   actual=fibonacci(3)
   expected=2
   assert actual == expected 

def test_fibofour():
   actual=fibonacci(4)
   expected=3
   assert actual == expected 

def test_fibofive():
    actual=fibonacci(5)
    expected=5
    assert actual == expected 

def test_fiboerror():
    actual=fibonacci('hi')
    expected="Please enter an integer"
    assert actual == expected 

def test_fibominus():
    actual=fibonacci(-1)
    expected="please enter a positive integer!!"
    assert actual == expected 


#===================================================================================

from math_series.series import lucas

'''Here is the testing part for lucas'''

def test_lucaszero():
    actual=lucas(0)
    expected=2
    assert actual == expected

def test_lucasone():
    actual=lucas(1)
    expected=1
    assert actual == expected

def test_lucastwo():
    actual=lucas(2)
    expected=3
    assert actual == expected

def test_lucasthree():
   actual=lucas(3)
   expected=4
   assert actual == expected 

def test_lucasfour():
   actual=lucas(4)
   expected=7
   assert actual == expected 

def test_lucasfive():
    actual=lucas(5)
    expected=11
    assert actual == expected 

def test_lucaserror():
    actual=lucas('hi')
    expected="Please enter an integer"
    assert actual == expected 

def test_lucasminus():
    actual=lucas(-1)
    expected="please enter a positive integer!!"
    assert actual == expected 



#===============================================================================

from math_series.series import sum

'''Here is the testing part for SUM'''

def test_sumfibo():
    actual=sum(9)
    expected=34
    assert actual == expected

def test_sumlucas():
    actual=sum(9,2,1)
    expected=76
    assert actual == expected

def test_sumrand():
    actual=sum(5,4,5)
    expected=37
    assert actual == expected

def test_sumweird():
   actual=sum(6,6,6)
   expected=78
   assert actual == expected 

def test_sumzero():
   actual=sum(0)
   expected=0
   assert actual == expected 

def test_sumten():
    actual=sum(10)
    expected=55
    assert actual == expected 

def test_sumerror():
    actual=sum('hi')
    expected="Please enter an integer"
    assert actual == expected 

def test_summinus():
    actual=sum(-1)
    expected="please enter a positive integer!!"
    assert actual == expected 