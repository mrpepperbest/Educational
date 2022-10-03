from testing_products.funcs import brightness_contrast
import pytest
import numpy as np


@pytest.mark.parametrize("img, a, b, expected_result", [(np.eye(2, 2), 0, 255, np.array([[255, 255],
                                                                                        [255, 255]])),
                                                        (np.eye(2, 2), 255, 0, np.array([[255, 0],
                                                                                        [0, 255]])),
                                                        (np.ones(2), 255, 0, np.array([255, 255])),
                                                        (np.ones((3, 3)), 2, 2, np.array([[4, 4, 4],
                                                                                          [4, 4, 4],
                                                                                          [4, 4, 4]])),
                                                        (np.ones(1), 0, 1, np.array([1]))])
def test_calculus(img, a, b, expected_result):
    assert np.array_equal(brightness_contrast(img, a, b), expected_result)


@pytest.mark.parametrize("expected_exeption, img, a, b", [(TypeError, np.ones(2), "15", 50),
                                                          (TypeError, np.ones(2), 15, "50"),
                                                          (TypeError, "2", 15, 50),
                                                          (AttributeError, 0, 0, 0)])
def test_bc_with_error(expected_exeption, img, a, b):
    with pytest.raises(expected_exeption):
        brightness_contrast(img, a, b)

