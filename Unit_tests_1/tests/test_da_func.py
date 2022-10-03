from testing_products.data_analysts import *
import numpy as np
import pytest


@pytest.mark.parametrize("data, expected_result", [(np.zeros(10), 0),
                                                   (np.ones(10), 1),
                                                   ([1, 2, 3, 4, 5], 3),
                                                   ([-5, 5, -5, 5], 0)])
def test_mean_positive(data, expected_result):
    assert mean(data) == expected_result


@pytest.mark.parametrize("data, expected_result", [(np.zeros(10), 0),
                                                   (np.ones(10), 0),
                                                   ([1, -1, 1, -1, 1], 1.2),
                                                   ([2, 2, 4, 8], 8)])
def test_variance_positive(data, expected_result):
    assert variance(data) == expected_result


@pytest.mark.parametrize("expected_exeption, data", [(TypeError, ['a', 'q']),
                                                     (TypeError, 2)])
def test_variance_error(expected_exeption, data):
    with pytest.raises(expected_exeption):
        variance(data)


@pytest.mark.parametrize("expected_exeption, data", [(TypeError, ['a', 'q']),
                                                     (TypeError, 2)])
def test_mean_error(expected_exeption, data):
    with pytest.raises(expected_exeption):
        mean(data)
