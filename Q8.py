import numpy as np

class Polynomial:
    def __init__(self, coeffs):
        # coeffs hold the polynomial in descending powers, e.g. [2, 0, –3] ≡ 2x² – 3
        self.coeffs = np.asarray(coeffs, dtype=float)

    def __call__(self, x):
        """Evaluate P(x) with Horner’s rule."""
        y = 0
        for c in self.coeffs:
            y = y * x + c
        return y

    @staticmethod
    def from_roots(*roots):
        """
        Build a Polynomial given any number of roots.
        For roots r₁,r₂,…,rₙ the polynomial is (x – r₁)(x – r₂)…(x – rₙ).
        Returns a *new* Polynomial object whose coefficients have been computed with np.convolve.
        """
        coeffs = np.array([1.0])
        for r in roots:
            coeffs = np.convolve(coeffs, [1, -r])  # multiply by (x – r)
        return Polynomial(coeffs)
