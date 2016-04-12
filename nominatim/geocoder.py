import urllib
import urllib2
import simplejson


class GeocoderError(Exception): pass


class GeocoderResultError(Exception): pass


class Geocoder(object):
    base_url = "http://open.mapquestapi.com/nominatim/v1/search?format=json&%s"

    def __init__(self, app_name, key=None):
        self.app_name = app_name
        self.key = key

    def geocode(self, q, addressdetails=False, limit=None,
                 countrycodes='', viewbox=(), exclude_place_ids=[],
                 bounded=False, routewidth=None, osm_type='', osm_id=None):

        params = {}

        if self.key:
            params['key'] = self.key

        q = unicode(q).encode('utf-8')
        params['q'] = q
        params['addressdetails'] = addressdetails

        if limit is not None:
            params['limit'] = limit

        if countrycodes:
            params['countrycodes'] = countrycodes

        if routewidth:
            params['routewidth'] = routewidth

        if osm_type:
            params['osm_type'] = osm_type

        if osm_id:
            params['osm_id'] = osm_id

        url = self.base_url % urllib.urlencode(params)

        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', self.app_name)]
        data = opener.open(url)
        response = data.read()
        
        return self.parse_json(response)

    def parse_json(self, data):
        try:
            data = simplejson.loads(data)
        except simplejson.JSONDecodeError:
            data = []
        
        return data
