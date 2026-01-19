import os
import shutil
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

def copy_file(file_path: Path, target_dir: Path):
    """Копіює файл у піддиректорію target_dir відповідно до його розширення."""
    ext = file_path.suffix.lower().lstrip(".")
    if not ext:
        ext = "no_ext"
    dest_folder = target_dir / ext
    dest_folder.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file_path, dest_folder / file_path.name)

def process_directory(source_dir: Path, target_dir: Path):
    """Рекурсивно обходить директорію та копіює файли у пулі потоків."""
    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = Path(root) / file
                executor.submit(copy_file, file_path, target_dir)

def main():
    if len(sys.argv) < 2:
        print("Usage: python part1.py <source_dir> [target_dir]")
        return

    source = Path(sys.argv[1])
    target = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not source.exists():
        print("Source directory does not exist")
        return

    target.mkdir(parents=True, exist_ok=True)
    process_directory(source, target)
    print(f"Files copied to {target}")

if __name__ == "__main__":
    main()