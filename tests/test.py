from mypackage import mymodule

def top_n():
    """
    This is to make sure top_n works correctly
    """

    assert mymodule.top_n([8,7,3,4,2], 3) == [8,7,4], 'Incorrect'
    assert mymodule.top_n([8,7,3,4,2], 2) == [8,7], 'Incorrect'
    assert mymodule.top_n([5,7,3,4,2], 4) == [8,7,4, 3], 'Incorrect'