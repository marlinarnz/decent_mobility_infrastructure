import unittest

from persona import Persona
from alternative import Alternative

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.trips_data = {"work": 1, "home": 4, "grocery_store": 1, "leisure": 2}
        self.persona = Persona("John", 30.5, self.trips_data)
        self.alternatives = [Alternative(dest, mode, 1.5, 10, energy)
                             for dest in self.trips_data.keys()
                             for mode, energy in {'car': 1, 'bicycle': 0, 'bus': 0.2}.items()]

    def test_get_name(self):
        self.assertEqual(self.persona.get_name(), "John")

    def test_get_typ_travel_time(self):
        self.assertEqual(self.persona.get_typ_travel_time(), 30.5)

    def test_get_demand(self):
        self.assertEqual(self.persona.get_demand(), self.trips_data)
    
    def test_compute_trips_random(self):
        self.persona.compute_trips_random(self.alternatives)
        trips = self.persona.get_trips()
        for dest, count in self.trips_data.items():
            self.assertEqual(len(trips[dest]), count, dest)
            for alt in trips[dest]:
                self.assertEqual(alt.destination, dest, alt)
    
    def test_compute_trips_random_car_unavailable(self):
        self.persona.compute_trips_random(self.alternatives, ['car'])
        trips = self.persona.get_trips()
        for dest, count in self.trips_data.items():
            self.assertEqual(len(trips[dest]), count, dest)
            for alt in trips[dest]:
                self.assertEqual(alt.destination, dest, alt)
    
    def test_compute_trips_random_all_unavailable(self):
        with self.assertRaises(ValueError):
            self.persona.compute_trips_random(self.alternatives, ['car', 'bicycle', 'bus'])

if __name__ == "__main__":
    unittest.main()