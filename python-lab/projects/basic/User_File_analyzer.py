from pathlib import Path
from datetime import datetime
date = Path("users")
for file in date.rglob("*"):
    if file.is_file():
        info = file.stat()

        size = info.st_size / 1024
        modified = datetime.fromtimestamp(info.st_mtime)
        print("+" * 50)
        print("Name:", file.name)
        print("Path:", file)
        print("Extension:", file.suffix)
        print(f"Size: {size:.2f} KB")
        print(f"Modified: ", modified)