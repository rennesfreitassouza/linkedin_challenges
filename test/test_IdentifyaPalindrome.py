import pytest

@pytest.fixture(params=["level", "race car", "Go hang a salami - I'm a lasagna hog", "@@", "", "@race car_", "renneR", "+oo",'sagas', 'Radar', 'Was it a cat I saw?', 'Eva, can I see bees in a cave?', 'Red rum, sir, is MURDER!!'])
def palindrome_string(request):
    return request.param

@pytest.fixture(params=["hello world", "rennes", "poo", "This should not not work", 'radars'])
def not_a_palindrome_string(request):
    return request.param    

def test_identify_palindrome_values(palindrome_string):
    from Files_Python_Code_Challenges import IdentifyaPalindrome

    retorno = IdentifyaPalindrome.isaPalindrome(palindrome_string)
    
    assert retorno is True, print(retorno)

def test_identify_palindrome_not_p(not_a_palindrome_string):
    from Files_Python_Code_Challenges import IdentifyaPalindrome

    retorno = IdentifyaPalindrome.isaPalindrome(not_a_palindrome_string)
    
    assert retorno is False, print(retorno)