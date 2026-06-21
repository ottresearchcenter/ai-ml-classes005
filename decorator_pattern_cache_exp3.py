from functools import wraps


def cache_result(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key in cache:
            print("[CACHE] hit")
            return cache[key]

        print("[CACHE] miss")
        result = func(*args, **kwargs)
        cache[key] = result

        return result

    return wrapper

"""
@cache_result
def generate_embedding(text: str) -> list[float]:
    print("[EMBEDDING] expensive embedding call")
    return [len(text) * 0.1, len(text) * 0.2]


print(generate_embedding("policy document"))
print(generate_embedding("policy document"))"""

@cache_result
def search_data_for_user_profile(user_id: str) -> list[str]:
    print(f"[SEARCH] searching data for user_id={user_id}")
    return "data from postgresql db for user_id: " + user_id

search_data_for_user_profile("123")
search_data_for_user_profile("123")
search_data_for_user_profile("456")