import math

def get_stats(data: list[float]) -> dict:
    if not data:
        return {}
    return {
        "mean": sum(data) / len(data),
        "min": min(data),
        "max": max(data),
        "std": math.sqrt(sum((x - sum(data)/len(data))**2 for x in data) / len(data))
    }