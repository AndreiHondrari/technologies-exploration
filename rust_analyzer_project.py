
import os
import argparse
import time
import json
import subprocess
from pathlib import Path
from typing import Tuple


DEFAULT_RECURRENT_TIME_SECONDS = 0.5


def determine_files(files: set) -> Tuple[bool, list]:
    paths_items = os.walk("programming-languages/rust")

    changed = False
    new_files = set()

    for item in paths_items:
        simplified_base_dir = item[0].replace("./", "").strip('/')
        for file_name in item[2]:
            file_path = Path(file_name)
            if file_path.suffix == '.rs':
                new_files.add(f"{simplified_base_dir}/{file_name}")

    if len(new_files.difference(files).union(files.difference(new_files))) > 0:
        changed = True

    return changed, new_files


def generate_rustanalyzer_project_config(files: set) -> dict:
    result = subprocess.run(
        ['rustc', '--print', 'sysroot'],
        capture_output=True
    )

    sysroot = result.stdout.decode().strip()

    return {
        'sysroot_src': f"{sysroot}/lib/rustlib/src/rust/library",
        'crates': [
            {
                "root_module": file_path,
                "edition": "2021",
                "deps": [],
            }
            for file_path in files
        ]
    }


def persist_rustanalyzer_project_config(project_config: dict) -> None:
    with open("rust-project.json", "w") as rustproject_file:
        json.dump(project_config, rustproject_file)


def handle_one_time(files: set) -> None:
    project_config: dict = generate_rustanalyzer_project_config(files)
    persist_rustanalyzer_project_config(project_config)


def handle_recurrent():
    files = set()

    try:
        while True:
            changed, files = determine_files(files)
            if changed:
                print(
                    f"Changes found. Recurrent generation for "
                    f"{len(files)} files"
                )
                handle_one_time(files)

            time.sleep(DEFAULT_RECURRENT_TIME_SECONDS)

    except KeyboardInterrupt:
        print(" \nDetected CTRL+C. Gracious shutdown...")


def main() -> None:
    print("--- Rust analyzer project config generation tool ---")

    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--watch", action="store_true")
    arguments = parser.parse_args()

    if arguments.watch:
        print("Recurrent handling started.")
        handle_recurrent()
    else:
        _nop, files = determine_files(set())
        print(f"Generated single time for {len(files)} files")
        handle_one_time(files)

    print("--- END ---")


if __name__ == "__main__":
    main()
