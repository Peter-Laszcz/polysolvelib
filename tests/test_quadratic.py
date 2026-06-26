import cmath
import pytest

from polysolve.solver import quadratic

def quad(a, b, c, x):
    return a * x ** 2 + b * x + c

@pytest.mark.parametrize('params, expected', [
    ([1.0, 0.0, 0.0], [0.0, 0.0]),
    ([1.0, 14.0, 49.0], [-7.0, -7.0]),
    ([3.0, 2.0, -1.0], [(1/3), -1.0])
    ],
)
def test_roots(params, expected):
    roots = quadratic(*params)
    assert all(map(cmath.isclose, roots, expected))
    assert all(cmath.isclose(quad(*params, root), 0.0) for root in roots)

@pytest.mark.skip(reason="Not implemented")
def tests_fails():
    with pytest.raises(ZeroDivisionError):
        quadratic(0, 0, 0)

