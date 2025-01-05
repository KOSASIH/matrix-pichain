import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, requests_per_minute=60):
        self.requests_per_minute = requests_per_minute
        self.user_requests = defaultdict(list)

    def limit_requests(self, func):
        def wrapper(*args, **kwargs):
            user_id = kwargs.get('user_id')
            current_time = time.time()
            self.user_requests[user_id] = [req for req in self.user_requests[user_id] if req > current_time - 60]

            if len(self.user_requests[user_id]) >= self.requests_per_minute:
                return {"status": "error", "message": "Rate limit exceeded."}, 429

            self.user_requests[user_id].append(current_time)
            return func(*args, **kwargs)
        return wrapper

    def __repr__(self):
        return f"RateLimiter(requests_per_minute={self.requests_per_minute})"
