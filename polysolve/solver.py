from cmath import sqrt
import math
from typing import Tuple

from cowsay import cow

CBRT_UNITY_IM = sqrt(3)/2 * 1j

def quadratic(a: float, b: float, c: float) -> Tuple[complex, complex]:
    """
Parameters
    ----------
    a
       :math:`x^2` coefficient.
    b
       :math:`x` coefficient.
    c
       Constant value.

    Returns
    -------
    tuple[float, float]
        Positive and negative roots of quadratic.

    Raises
    ------
    ValueError
        Discriminant < 0 implying imaginary root.

    Notes
    -----
    Equation of the form:

    .. math::

        ax^{2} + bx + c

    Examples
    --------
    >>> quadratic(1, 2, 0)
    (0j, (-2+0j))
    >>> quadratic(3., 0., -1.)
    ((0.5773502691896257+0j), (-0.5773502691896257+0j))

    """

    det = b**2 - (4*a*c)

    if math.isclose(det, 0):
        cow("Degenerate MOOoo-ts")

    return ((-b + sqrt(det)) / (2*a), (-b - sqrt(det)) / (2*a))

def cubic(a, b, c, d):
    q = (3*a*c - b**2) / (9*a**2)
    r = (9*a*b*c - 27*a**2*d - 2*b**3) / (54*a**3)

    s = (r + sqrt(q**3 + r**2))**(1/3)
    t = (r - sqrt(q**3 + r**2))**(1/3)

    x1 = s + t - (b/3*a)
    x2 = -(s + t)/2 - (b/3*a) + CBRT_UNITY_IM * (s - t)
    x3 = -(s + t)/2 - (b/3*a) - CBRT_UNITY_IM * (s - t)

    if any(x == x1 for x in (x2, x3)):
        cow("Degenerate MOOoo-ts")

    return (x1, x2, x3)
