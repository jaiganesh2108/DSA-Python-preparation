from pathlib import Path
import shutil

downloads = Path.home() / "Downloads"
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
}

for name in folders:
    (downloads / name).mkdir(exist_ok=True)

for file in list(downloads.iterdir()):
    ext = file.suffix.lower()
    for name,exts in folders.items():
        if file.is_file() and ext in exts:
            target = downloads / name / file.name
            if not target.exists():
                shutil.move(file, target)
    