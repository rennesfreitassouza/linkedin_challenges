import pytest


@pytest.fixture(params=[-6, 0, 1, 2, 13, 630])
def value(request):
    return request.param

def test_prime_values(value):
    from ans import FindPrimeFactors

    retorno = FindPrimeFactors.findAllPrimeFactors(value)
    result = 1
    for primeValue in retorno:
        result *= primeValue
    print(result)
    assert value == result if value >= 2 else retorno == [], print(retorno)
