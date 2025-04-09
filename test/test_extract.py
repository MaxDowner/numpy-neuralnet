# check number of rows, number of columns, whether first row follows appropriate pattern, check type(s) 
from src.extract import extract
import pytest
import pandas as pd

# put tests in a class

@pytest.mark.skip(reason="extract takes a long time")
def test_extract():
    # arrange
    # act
    result = extract()
    # assert
    assert (isinstance(result[0], pd.DataFrame) & isinstance(result[1], pd.DataFrame))