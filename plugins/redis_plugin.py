
from . import ContainerPlugin
import redis

class RedisContainer(redis.StrictRedis, ContainerPlugin):
    """ Implementing a dictionary-like interface for Redis key-value pairs
        Probably an alternative implementation:
        https://github.com/wehlutyk/webquotes/blob/master/datainterface/redistools.py
        And more inspiration:
        https://github.com/gumuz/redisobj/blob/master/redisobj/redis_db.py
    """
    encoding = 'utf-8'
    # http://docs.python.org/3.3/reference/datamodel.html#sequence-types
    def __len__(self):
        return self.dbsize()
    def __getitem__(self, key):
        value = self.get(key)
        if value: return value.decode(self.encoding)
    def __setitem__(self, key, value):
        self.set(key, value)
    def __delitem__(self, key):
        self.delete(key)
    def keys(self):
        return [key.decode('utf-8') for key in super().keys('*')]
    def __iter__(self):
        for key in self.keys():
            yield key
    def iterkeys(self):
        for key in self.keys():
            yield key
    def __contains__(self, key):
        return self.exists(key)
