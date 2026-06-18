def read_logs(path: str) -> list[str]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Помилка: Файл {path} не знайдено.")
        return []