import unittest
import math
import sys

# Setting the path to the module to be tested
sys.path.append('../PiCalculator')
from PiCalculator import PiCalculator

class TestPiCalculator(unittest.TestCase):

    def test_leibniz_series(self):
        calculator = PiCalculator()
        pi_approx = calculator.calculate_pi_leibniz(20000)
        self.assertAlmostEqual(pi_approx, math.pi, places=4)

    def test_nilakantha_series(self):
        calculator = PiCalculator()
        pi_approx = calculator.calculate_pi_nilakantha(1000)
        self.assertAlmostEqual(pi_approx, math.pi, places=4)

    def test_monte_carlo_method(self):
        # Due to the randomness of Monte Carlo, we can't expect exact results
        calculator = PiCalculator()
        pi_approx = calculator.calculate_pi_monte_carlo(100000)
        self.assertAlmostEqual(pi_approx, math.pi, places=1)

    def test_machin_formula(self):
        calculator = PiCalculator()
        pi_approx = calculator.calculate_pi_machin()
        self.assertAlmostEqual(pi_approx, math.pi, places=15)

if __name__ == '__main__':
    unittest.main()

