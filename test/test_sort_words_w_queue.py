import pytest


@pytest.fixture(params=["orange ORANGE", "ORANGE orange", "banana ORANGE apple", "0A 0a", "0a 0A", "00A 00a", "00a 10A"])
def string(request):
    return request.param

def test_sort_a_str(string):
    from Files_Python_Code_Challenges import SortAString

    retorno = SortAString.sort_words_w_queue(string)
    
    assert retorno == SortAString.sort_words_linkedin(string), print(retorno)
