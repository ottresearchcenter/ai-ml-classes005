import time
from functools import wraps


def measure_latency(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        latency_ms = (time.time() - start_time) * 1000
        print(f"[METRIC] {func.__name__} latency={latency_ms:.2f} ms")

        return result

    return wrapper


@measure_latency
def run_inference(prompt: str) -> str:
    time.sleep(0.2)
    return f"Answer for: {prompt}"


print(run_inference("Explain transformer architecture"))