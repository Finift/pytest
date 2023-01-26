def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42

def test_comparison(fix_data):
    assert 'BBG000B9Y9C7' in fix_data, "Item wasn't added"

