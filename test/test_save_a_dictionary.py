import pytest

@pytest.fixture(params=[dict(a=1, b=2, c=(1,9)), {0:{}, '1': ['1', 2]}, [9,6,2]])
def dictionary(request):
    return request.param

def test_save_a_dictionary(dictionary):
    from ans import SaveADictionary

    retorno = SaveADictionary.main("fileName", dictionary)
    
    assert retorno == dictionary, print(retorno)
