# check number of rows, number of columns, whether first row follows appropriate pattern, check type(s) 
from src.extract import extract
import pytest
import pandas as pd

# put tests in a class

@pytest.mark.skip
def test_extract_object_type():
    # arrange
    # act
    result = extract()
    # assert
    assert (isinstance(result[0], pd.DataFrame) & isinstance(result[1], pd.DataFrame))


def test_extract_shape():
    # arrange
    # act
    result = extract()
    # assert
    assert (result[0].shape == (10000, 785)) & (result[1].shape == (60000, 785))