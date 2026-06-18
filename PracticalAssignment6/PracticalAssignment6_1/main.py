import PracticalAssignment6.PracticalAssignment6_1.io_utils as io_utils
import PracticalAssignment6.PracticalAssignment6_1.analysis as analysis

def main():
    file_path = "PracticalAssignment6_1/input.txt"

    data = io_utils.read_numbers(file_path)
    
    if not data:
        print(f"Файл '{file_path}' порожній або відсутній.")
        return

    stats = analysis.get_stats(data)
    
    if not stats:
        print("Помилка при аналізі даних.")
        return

    result_text = (
        f"Статистика по файлу:\n"
        f"Середнє значення: {stats['mean']:.2f}\n"
        f"Мінімум: {stats['min']}\n"
        f"Максимум: {stats['max']}\n"
        f"Стандартне відхилення: {stats['std']:.2f}"
    )
    
    print(result_text)

    io_utils.save_results("PracticalAssignment6_1/results.txt", result_text)
    print("\nРезультати збережено")

if __name__ == "__main__":
    main()