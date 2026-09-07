import pytest
from financial import financial_info

def test_1():
  result = financial_info("MSFT", "Total Revenue")
  assert len(result) > 0
  assert result[0] == 'Total Revenue'

def test_2():
  result = financial_info("AAPL","Total Revenue")
  assert isinstance(result,tuple)

def test_3():
  with pytest.raises(Exception):
    financial_info("ASKJN", "Total Revenue")

if __name__ == '__main__':
  test_1()
  test_2()
  test_3()
