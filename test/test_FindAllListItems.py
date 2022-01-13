import pytest

@pytest.fixture(params=[ [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]] ])
def l_request(request):
    return request.param

@pytest.fixture(params=[2, 1, 3])
def item(request):
    return request.param

def test_index_all(l_request, item):
    from Files_Python_Code_Challenges import FindAllListItems

    retorno = FindAllListItems.index_all(l_request, item)
    if (item == 2):
        assert retorno == [[0, 0, 1], [0, 1], [1, 1]], print(retorno)
    if (item == 1):
        assert retorno == [[0, 0, 0], [0, 2, 0], [1, 0]], print(retorno)
    if (item == 3):
        assert retorno == [[0, 0, 2], [0, 2, 1], [1, 2]], print(retorno)
