from collections import Counter
import heapq
from itertools import count

_counter = count()

class LogStatistics:

    def __init__(self):
        self.total_requests = 0
        self.methods = Counter()
        self.ip_counter = Counter()
        self.longest = []

    def update(self, data):
        self.total_requests += 1
        self.methods[data["method"]] += 1
        self.ip_counter[data["ip"]] += 1

        duration = int(data["duration"])

        request = {
            "method": data["method"],
            "url": data["url"],
            "ip": data["ip"],
            "duration": duration,
            "datetime": data["time"],
        }

        if len(self.longest) < 3:
            heapq.heappush(self.longest, (duration, next(_counter), request))
        else:
            heapq.heappushpop(self.longest, (duration, next(_counter), request))

    def to_dict(self):
        top_requests = sorted(
            self.longest,
            key=lambda x: x[0],
            reverse=True
        )

        return {
            "total_requests": self.total_requests,
            "methods": dict(self.methods),
            "top_ips": self.ip_counter.most_common(3),
            "top_longest_requests": [
                item[2] for item in top_requests
            ],
        }