import pytest
from project import cal_PMT, calculate_amortization, format

@pytest.fixture
def example_input():
    return {'pv': 1000, 'i': 0.1, 'n': 5, 'pmt': 263.80}

@pytest.fixture
def amortization_schedule():
    data = [{'Year': 1, 'Beginning Balance': 1000, 'Payment': 263.79748079474524, 'Interest Paid': 100.0, 'Principal Paid': 163.79748079474524, 'Ending Balance': 836.2025192052547},
                           {'Year': 2, 'Beginning Balance': 836.2025192052547, 'Payment': 263.79748079474524, 'Interest Paid': 83.62025192052548, 'Principal Paid': 180.17722887421976, 'Ending Balance': 656.025290331035},
                           {'Year': 3, 'Beginning Balance': 656.025290331035, 'Payment': 263.79748079474524, 'Interest Paid': 65.6025290331035, 'Principal Paid': 198.19495176164173, 'Ending Balance': 457.83033856939323},
                           {'Year': 4, 'Beginning Balance': 457.83033856939323, 'Payment': 263.79748079474524, 'Interest Paid': 45.783033856939326, 'Principal Paid': 218.01444693780593, 'Ending Balance': 239.8158916315873},
                           {'Year': 5, 'Beginning Balance': 239.8158916315873, 'Payment': 263.79748079474524, 'Interest Paid': 23.98158916315873, 'Principal Paid': 239.8158916315865, 'Ending Balance': 7.958078640513122e-13}]

    return data

def test_cal_PMT(example_input):
    pmt = cal_PMT(example_input['pv'], example_input['i'], example_input['n'])
    assert round(pmt, 2) == 263.80

def test_calculate_amortization(example_input):
    amortization_schedule = calculate_amortization(example_input['pv'], example_input['i'], 1288.37, example_input['n'])
    assert len(amortization_schedule) == example_input['n']

def test_format(amortization_schedule):
    expected_result = [
        ['Year', 'Beginning Balance', 'Payment', 'Interest Paid', 'Principal Paid', 'Ending Balance'],
        [1, 1000, 263.79748079474524, 100.0, 163.79748079474524, 836.2025192052547],
        [2, 836.2025192052547, 263.79748079474524, 83.62025192052548, 180.17722887421976, 656.025290331035],
        [3, 656.025290331035, 263.79748079474524, 65.6025290331035, 198.19495176164173, 457.83033856939323],
        [4, 457.83033856939323, 263.79748079474524, 45.783033856939326, 218.01444693780593, 239.8158916315873],
        [5, 239.8158916315873, 263.79748079474524, 23.98158916315873, 239.8158916315865, 7.958078640513122e-13]
    ]
    result = format(amortization_schedule)
    assert result == expected_result
