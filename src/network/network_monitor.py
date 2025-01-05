import time
import random

class NetworkMonitor:
    def __init__(self):
        self.metrics = []

    def collect_metrics(self):
        # Simulate collecting metrics
        while True:
            metric = {
                "timestamp": time.time(),
                "latency": random.uniform(10, 100), "throughput": random.uniform(100, 1000)
            }
            self.metrics.append(metric)
            print(f"Collected metrics: {metric}")
            time.sleep(5)  # Collect metrics every 5 seconds

    def get_metrics(self):
        return self.metrics

    def __repr__(self):
        return f"NetworkMonitor(metrics_count={len(self.metrics)})"

# To run the network monitor
if __name__ == "__main__":
    monitor = NetworkMonitor()
    monitor.collect_metrics()
