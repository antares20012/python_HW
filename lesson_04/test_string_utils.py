import pytest

from string_utils import StringUtils

string_utils = StringUtils()

# 🟩 POSITIVE TESTS

@pytest.mark.positive
@pytest.mark.parametrize('input_text, expected_text',
                         [
                             ("python", "Python"),
                             ("englisH", "English"),
                             ("my English is so bad", "My English is so bad")
                             #(3, None)

                         ])
def test_capitalize_positive(input_text: str, expected_text: str):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_text) == expected_text

@pytest.mark.parametrize('input_text, expected_text',
                         [
                             ("    School", "School"),
                             ("    Slow down", "Slow down"),
                             ("____    ____", "____    ____"),
                             ("a", "a")

                          ])
def test_trim_positive(input_text: str, expected_text: str):
    string_utils = StringUtils()
    assert string_utils.trim(input_text) == expected_text

@pytest.mark.parametrize('string, symbol, expected',
                         [
                             ("slow down", "n", True),
                             ("3", "3", True),
                             (" ", " ", True),
                             ("slow down", "z", False),
                             ("slow down", "s", True),
                             ("asddgljhv@mili.sdg", "@", True)
                         ])
def test_contains_positive(string: str, symbol: str, expected: bool):
    string_utils = StringUtils()
    assert string_utils.contains(string, symbol) == expected



@pytest.mark.parametrize('string, symbol, result',
                         [
                             ("Butterfly", "t", "Buerfly"),
                             ("The 1st of July", "t", "he 1s of July"),
                             ("123", "1", "23"),
                         ])
def test_delete_symbol_positive(string: str, symbol: str, result: str):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(string, symbol) == result



# 🟥 NEGATIVE TESTS
@pytest.mark.negative
@pytest.mark.parametrize('input_text, expected_text',
                         [
                             ("", ""),
                             ("12354wasd", "12354wasd"),
                             ("    ", "    "),
                             ("SDFGLJKHLK", "SDFGLJKHLK"),
                             (". ", ". "),
                             (" hello"," Hello")

                         ])
def test_capitalize_positive(input_text: str, expected_text: str):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_text) == expected_text

@pytest.mark.parametrize('input_text, expected_text',
                         [
                             ("", ""),
                             ("    ", ""),
                             ("\t\n    \r", ""),
                         ])
def test_trim_negative(input_text: str, expected_text: str):
    string_utils = StringUtils()
    assert string_utils.trim(input_text) == expected_text

@pytest.mark.parametrize('string, symbol, expected',
                         [
                             ("school", "t", False),
                             (None, None, False),
                             ("", "", False),
                             ("school", "S", False),
                             (" ", "S", False)
                         ])
def test_contains_negative(string: str, symbol: str, expected:bool):
    result = StringUtils()
    assert result.contains(string, symbol) == expected


@pytest.mark.parametrize('string, symbol, result',
                         [
                             ("Butterfly", "Z", "Butterfly"),
                             ("The 1st of July", "t", "The 1s of July"),
                             ("", "A", ""),
                         ])
def test_delete_symbol_negative(string: str, symbol: str, result: str):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(string, symbol) == result
