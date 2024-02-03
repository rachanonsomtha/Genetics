import unittest

from chromosome import generate_solution, generate_hub_cities

class TestHubLocationProblem(unittest.TestCase):
    def setUp(self):
        # Set up any common variables or configurations needed for the tests
        pass

    def test_generate_solution(self):
        # Test the generate_solution function
        n = 6
        p = 2
        solution = generate_solution()
        
        # Check if the length of the solution is correct
        self.assertEqual(len(solution), (n - p) * p)

        # Check if each non-hub city is connected to exactly one hub city
        non_hub_cities_count = n - p
        for i in range(0, non_hub_cities_count, p):
            connected_count = sum(solution[i:i + p])
            self.assertEqual(connected_count, 1)

    def test_generate_hub_cities(self):
        # Test the generate_hub_cities function
        n = 6
        p = 2
        hub_cities = generate_hub_cities()

        # Check if the length of the hub_cities is correct
        self.assertEqual(len(hub_cities), p)

        # Check if all hub cities are unique
        self.assertEqual(len(set(hub_cities)), p)

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()
