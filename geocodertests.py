# -*- coding: utf-8 -*-
import city_list
import nominatim
import unittest



class GeocoderTestCase(unittest.TestCase):

    def test_geocode_city(self):
        client = nominatim.Geocoder()
        response = client.geocode(city_list.us)
        self.assertIsNotNone(response)

    def test_get_location_by_city_invalid_chars(self):
        client = nominatim.Geocoder()
        response = client.geocode(unicode(city_list.intl, 'utf-8'))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
