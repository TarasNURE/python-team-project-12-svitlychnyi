def read_numbers(path: str) -> list[float]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [float(line.strip()) for line in f if line.strip()]
    except (FileNotFoundError, ValueError):
        return []

def save_results(path: str, data: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)