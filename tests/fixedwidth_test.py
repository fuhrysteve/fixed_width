import os
from fixed_width import FixedWidth

example_file_path = os.path.join(
    os.path.dirname(__file__), 'examples/example1.txt')
example_fieldnames = [
    'Account',
    'LastName',
    'FirstName',
    'Balance',
    'CreditLimit',
    'AccountCreated',
    'Rating',
]


def test_can_parse_ordereddict():
    with open(example_file_path, 'rb') as file:
        next(file)
        fw = FixedWidth(file, format='8s16s16s12s14s16s7s',
                        fieldnames=example_fieldnames)
        rows = list(fw)
    assert rows[0]['Account'] == '101'
    assert rows[0]['LastName'] == 'Reeves'
    assert rows[0]['FirstName'] == 'Keanu'
    assert rows[0]['Balance'] == '9315.45'
    assert rows[0]['CreditLimit'] == '10000.00'
    assert rows[0]['AccountCreated'] == '1/17/1998'
    assert rows[0]['Rating'] == 'A'
