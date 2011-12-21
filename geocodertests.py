import nominatim
import unittest



class GeocoderTestCase(unittest.TestCase):

    def test_geocode_city(self):
        client = nominatim.Geocoder()
        response = client.geocode('Hays, Kansas')
        self.assertIsNotNone(response)

    def test_geocode_invalid_city(self):
        client = nominatim.Geocoder()
        response = client.geocode('Hiawatha, Kansas')
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
