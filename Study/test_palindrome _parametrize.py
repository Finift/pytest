import pytest
# def test_is_palindrome_empty_string():
#     assert is_palindrome("")
#
# def test_is_palindrome_single_character():
#     assert is_palindrome("a")
#
# def test_is_palindrome_mixed_casing():
#     assert is_palindrome("Bob")
#
# def test_is_palindrome_with_spaces():
#     assert is_palindrome("Never odd or even")
#
# def test_is_palindrome_with_punctuation():
#     assert is_palindrome("Do geese see God?")
#
# def test_is_palindrome_not_palindrome():
#     assert not is_palindrome("abc")
#
# def test_is_palindrome_not_quite():
#     assert not is_palindrome("abab")

# теперь сделаю все эти тесты через параметрайз:
# @pytest.mark.parametrize("palindrome", [
#     "",
#     "a",
#     "Bob",
#     "Never odd or even",
#     "Do geese see God",
# ])
# def test_is_palindrome(palindrome):
#     data = palindrome.lower().replace(" ", "")
#     data_reverse = data[::-1]
#     assert data == data_reverse, "It's not a palindrome"
#
# @pytest.mark.parametrize("non_palindrome", [
#     "abc",
#     "abab",
# ])
# def test_is_palindrome_not_palindrome(non_palindrome):
#     data = non_palindrome.lower().replace(" ", "")
#     data_reverse = data[::-1]
#     assert not data == data_reverse, "It's a palindrome"

#или ещё удобнее:
@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God", True),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    data = maybe_palindrome.lower().replace(" ", "")
    data_reverse = data[::-1]
    if data == data_reverse:
        result = True
    else:
        result = False
    assert result == expected_result