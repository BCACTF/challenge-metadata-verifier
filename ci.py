from verify import check
from pathlib import Path
from termcolor import cprint

if __name__ == "__main__":
    failed = False
    files = 0
    for path in Path(".").glob("*/chall.yaml"):
        files += 1
        try:
            errors, warnings = check(path)
        except Exception as e:
            cprint(f"{path}: Fatal error", "red", attrs=["bold"])
            print(e)
            failed = True
            print("")
            continue
        if len(errors) > 0:
            cprint(f"{path}: {len(errors)} error(s)", "red", attrs=["bold"])
            for error in errors:
                print(error)
            failed = True
        if len(warnings) > 0:
            cprint(f"{path}: {len(warnings)} warning(s)", "yellow", attrs=["bold"])
            for warning in warnings:
                print(warning)
        if len(errors) > 0 or len(warnings) > 0:
            print("")
    print(f"Checked {files} files.")
    if failed:
        exit(1)