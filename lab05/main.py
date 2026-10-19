import os
import sys
import tablestats
def main():
    name1 = input().strip()
    if not os.path.exists(file_name):
        print(f"Файл {file_name} не найден.")
        return
    with open(file_name, "r", encoding="utf-8") as file:
        rows = tablestats.read_rows(file)
    total_rows = len(rows)
    counts = tablestats.count_types(rows)
    distinct_types = len(counts)
    error_minutes = tablestats.total_minutes(rows, "ошибка")
    print(total_rows)
    print(distinct_types)
    print(error_minutes)
    csv_output = tablestats.to_csv(counts)
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(csv_output)
    if __name__ == "__main__":
        main()
