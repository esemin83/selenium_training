

class Countries:
    def __init__(self, id=None, name=None, geo_zones=None):
        self.id = id
        self.name = name
        self.geo_zones = geo_zones

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.geo_zones)
