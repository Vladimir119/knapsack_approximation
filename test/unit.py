import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from approximation_knapsack.approximated_knapsack import knapsack_with_scaling
from base_knapsack.np_knapsack import knapsack

class TestKnapsack(unittest.TestCase):
    
    def test_exact_solution_simple(self):
        weights = [2, 3, 4]
        values = [3, 4, 5]
        W = 5
        expected_value = 7
        result_value, result_items = knapsack(weights, values, W)
        self.assertEqual(result_value, expected_value)

    def test_exact_solution_all_fit(self):
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        W = 30
        expected_value = 300
        result_value, result_items = knapsack(weights, values, W)
        self.assertEqual(result_value, expected_value)

    def test_exact_solution_no_fit(self):
        weights = [5, 6, 7, 8, 9, 10]
        values = [10, 20, 30, 40, 50, 60]
        W = 4
        expected_value = 0
        result_value, result_items = knapsack(weights, values, W)
        self.assertEqual(result_value, expected_value)

    def test_exact_solution_one_item(self):
        weights = [10]
        values = [50]
        W = 10
        expected_value = 50
        result_value, result_items = knapsack(weights, values, W)
        self.assertEqual(result_value, expected_value)

    def test_exact_solution_multiple_solutions(self):
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        values = [10, 15, 40, 50, 30, 20, 10, 60, 90, 80]
        W = 30
        expected_value = 285
        result_value, result_items = knapsack(weights, values, W)
        self.assertEqual(result_value, expected_value)

    def test_exact_solution_large_capacity(self):
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        values = [10, 15, 40, 50, 30, 20, 10, 60, 90, 80]
        W = 100
        expected_value = 405
        result_value, result_items = knapsack(weights, values, W)
        self.assertEqual(result_value, expected_value)

class TestKnapsackApproximation(unittest.TestCase):

    def test_approx_solution_simple(self):
        weights = [2, 3, 4]
        values = [3, 4, 5]
        W = 5
        epsilon = 0.1
        exact_value, _ = knapsack(weights, values, W)
        approx_value = knapsack_with_scaling(weights, values, W, epsilon)
        self.assertTrue(float(exact_value) <= approx_value * (1 + epsilon))

    def test_approx_solution_large_epsilon(self):
        weights = [1, 3, 4, 5]
        values = [15, 20, 30, 40]
        W = 7
        epsilon = 0.5
        exact_value, _ = knapsack(weights, values, W)
        approx_value = knapsack_with_scaling(weights, values, W, epsilon)
        self.assertTrue(exact_value <= approx_value * (1 + epsilon))
        
    def test_approx_solution_high_epsilon(self):
        weights = [2, 2, 4, 6]
        values = [10, 20, 30, 40]
        W = 8
        epsilon = 0.3
        exact_value, _ = knapsack(weights, values, W)
        approx_value = knapsack_with_scaling(weights, values, W, epsilon)
        self.assertTrue(exact_value <= approx_value * (1 + epsilon))

    def test_approx_solution_one_item(self):
        weights = [5]
        values = [100]
        W = 5
        epsilon = 0.1
        exact_value, _ = knapsack(weights, values, W)
        approx_value = knapsack_with_scaling(weights, values, W, epsilon)
        self.assertEqual(exact_value, approx_value)

    def test_approx_solution_large_test(self):
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        values = [10, 15, 40, 50, 30, 20, 10, 60, 90, 80]
        W = 30
        epsilon = 0.2
        exact_value, _ = knapsack(weights, values, W)
        approx_value = knapsack_with_scaling(weights, values, W, epsilon)
        self.assertTrue(exact_value <= approx_value * (1 + epsilon))
        W = 7
        epsilon = 0.5
        exact_value, _ = knapsack(weights, values, W)
        approx_value = knapsack_with_scaling(weights, values, W, epsilon)
        self.assertTrue(exact_value <= approx_value * (1 + epsilon))

class TestKnapsackComparison(unittest.TestCase):
    def test_exact_vs_approx_error(self):
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        values = [10, 15, 40, 50, 30, 20, 10, 60, 90, 80]
        W = 30
        epsilon = 0.2
        exact_value, _ = knapsack(weights, values, W)
        approx_value = knapsack_with_scaling(weights, values, W, epsilon)
        error = abs(exact_value - approx_value) / exact_value
        self.assertTrue(error <= epsilon)

if __name__ == "__main__":
    unittest.main()
