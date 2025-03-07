import redis
import json
from typing import Optional, Dict

class RedisCache:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0):
        # Connect to Redis server
        self.cache = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)

    def get(self, key: str) -> Optional[Dict]:
        """Retrieve cached data from Redis if available."""
        cached_data = self.cache.get(key)
        if cached_data:
            return json.loads(cached_data)  # Convert the cached string back to a dict
        return None

    def set(self, key: str, value: Dict, ttl: int = 3600):
        """Store the final response data (products data) in Redis with an optional TTL."""
        self.cache.setex(key, ttl, json.dumps(value))  # Set data with expiration time (TTL in seconds)

    def clear(self):
        """Clear the cache in Redis."""
        self.cache.flushdb()  # Clear the entire Redis database (caution)
    