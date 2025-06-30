import nltk
import shutil
import os

# Delete any broken nltk_data folders
paths = [
    os.path.expanduser("~/nltk_data"),
    os.path.join(os.getenv("APPDATA"), "nltk_data"),
    os.path.join(os.getenv("LOCALAPPDATA"), "Programs", "Python", "Python313", "nltk_data")
]
for path in paths:
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)

# Redownload punkt cleanly
nltk.download('punkt')
