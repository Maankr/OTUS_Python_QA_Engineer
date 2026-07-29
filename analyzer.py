import argparse
import json
import os

from parser import parse_line
from statistics import LogStatistics
from utils import get_log_files


def analyze_file(filepath):
    stats = LogStatistics()

    with open(filepath, encoding="utf-8") as f:
        for line in f:
            data = parse_line(line)
            if data:
                stats.update(data)

    result = stats.to_dict()

    os.makedirs("output", exist_ok=True)
    filename = os.path.splitext(os.path.basename(filepath))[0] + ".json"
    json_path = os.path.join("output", filename)

    with open(json_path, "w", encoding="utf-8") as out:
        json.dump(result, out, indent=4, ensure_ascii=False)

    print(f"\n===== {filepath} =====")
    print(json.dumps(result, indent=4, ensure_ascii=False))
    print(f"JSON saved: {json_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    files = get_log_files(args.path)

    for file in files:
        analyze_file(file)


if __name__ == "__main__":
    main()