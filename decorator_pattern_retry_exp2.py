import time
from functools import wraps


def retry(max_attempts: int = 3, delay_seconds: float = 1.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    last_error = error
                    print(f"[RETRY] attempt={attempt}, error={error}")

                    if attempt < max_attempts:
                        time.sleep(delay_seconds)

            raise last_error

        return wrapper

    return decorator


counter = {"attempt": 0}


@retry(max_attempts=3, delay_seconds=0.5)
def call_llm_api(prompt: str) -> str:
    counter["attempt"] += 1

    if counter["attempt"] < 3:
        raise TimeoutError("LLM API timeout")

    return f"LLM response for: {prompt}"


print(call_llm_api("Summarize this policy"))

counter = {"attempt": 0}

@retry(max_attempts=3, delay_seconds=0.5)
def read_data_from_db(query: str) -> str:
    counter["attempt"] += 1

    if counter["attempt"] < 3:
        raise ConnectionError("Database connection failed")

    return f"Data for query: {query}"

print(read_data_from_db("SELECT * FROM users"))