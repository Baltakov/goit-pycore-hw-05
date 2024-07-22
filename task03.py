import sys
import os

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    if len(parts) < 4:
        return None
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> list:
    if not os.path.isfile(file_path):
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            log_entry = parse_log_line(line)
            if log_entry:
                logs.append(log_entry)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    levels = ['INFO', 'DEBUG', 'ERROR', 'WARNING']
    counts = {level: 0 for level in levels}
    for log in logs:
        if log['level'] in counts:
            counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count:<8}")

def display_filtered_logs(logs: list, level: str):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях до лог-файлу> [<рівень логування>]")
        sys.exit(1)

    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        display_filtered_logs(filtered_logs, log_level)

if __name__ == "__main__":
    main()
