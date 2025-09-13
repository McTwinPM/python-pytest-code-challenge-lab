
from lib.palindrome import longest_palindromic_substring

def test_is_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("ab") == "a"
    assert longest_palindromic_substring("aba") == "aba"
    assert longest_palindromic_substring("abc") == "a"
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"