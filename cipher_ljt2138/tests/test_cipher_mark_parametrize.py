from cipher_ljt2138 import cipher_ljt2138
import pytest

# Testing using a single test function
@pytest.mark.parametrize("eg_text, eg_shift, expected", [
    ('Single', 3, 'Vlqjoh'),
    ('lower', 4, 'psAiv'),
    ('UPPER', 6, 'aVVKX'),
    ('A sentence with spaces', 10, 'K CoxDoxmo GsDr CzkmoC')
])
def test_cipher_multi(eg_text, eg_shift, expected):
    result = cipher_ljt2138.cipher(eg_text, eg_shift)
    assert result == expected