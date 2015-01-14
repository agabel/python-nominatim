# -*- coding: utf-8 -*-
import city_list
import nominatim
import unittest



class GeocoderTestCase(unittest.TestCase):

    def test_geocode_city(self):
        client = nominatim.Geocoder()
        response = client.geocode(city_list.us)
        self.assertEquals(response[0]['lon'], '-99.3267702')
        self.assertEquals(response[0]['lat'], '38.8791783')

    def test_get_location_by_city_invalid_chars(self):
        client = nominatim.Geocoder()
        # we need to test that the value is unicode and properly converted to a string when it is processed
        response = client.geocode(unicode(city_list.intl, 'utf-8'))
        self.assertEquals(response[0]['lon'], '-3.9868641')
        self.assertEquals(response[0]['lat'], '48.6849601')


if __name__ == "__main__":
    unittest.main()
