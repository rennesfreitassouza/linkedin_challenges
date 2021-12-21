import pytest

@pytest.fixture(params=["level", "race car", "Go hang a salami - I'm a lasagna hog", "@@", "", "@race car_", "renneR", "+oo"])
def palindrome_string(request):
    return request.param

@pytest.fixture(params=["hello world", "rennes", "poo"])
def not_a_palindrome_string(request):
    return request.param    

def test_prime_values(palindrome_string):
    from ans import IdentifyaPalindrome

    retorno = IdentifyaPalindrome.isaPalindrome(palindrome_string)
    
    assert retorno is True, print(retorno)

def test_prime_values_not_p(not_a_palindrome_string):
    from ans import IdentifyaPalindrome

    retorno = IdentifyaPalindrome.isaPalindrome(not_a_palindrome_string)
    
    assert retorno is False, print(retorno)