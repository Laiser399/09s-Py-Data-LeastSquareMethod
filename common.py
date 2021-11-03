import numpy as np

left, right = 1, 6
poly_degrees = [1, 2, 3, 4, 5]


def build_poly(coefficients):
    def poly(arg):
        poly_sum = np.zeros(arg.shape if type(arg) is np.ndarray else 1)
        arg_degree = np.ones(arg.shape if type(arg) is np.ndarray else 1)
        for c in coefficients:
            poly_sum += c * arg_degree
            arg_degree *= arg
        return poly_sum

    return poly
