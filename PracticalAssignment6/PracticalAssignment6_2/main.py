import PracticalAssignment6.PracticalAssignment6_2.io_utils as io_utils
import PracticalAssignment6.PracticalAssignment6_2.analysis as analysis

def main():
    file_path = "PracticalAssignment6_2/logs.txt"
    
    logs = io_utils.read_logs(file_path)
    
    if not logs:
        print("Немає даних для аналізу.")
        return
    
    stats = analysis.analyze_logs(logs)

    report = (
        f"Звіт аналізатора логів\n"
        f"Всього записів: {stats['total']}\n"
        f"Кількість помилок (ERROR): {stats['error']}\n"
        f"Кількість попереджень (WARNING): {stats['warning']}\n"
    )
    print(report)

if __name__ == "__main__":
    main()