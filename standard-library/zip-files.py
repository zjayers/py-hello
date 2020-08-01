from pathlib import Path
from zipfile import ZipFile

#  Write Zip File
with ZipFile('files.zip', "w") as zip:
    for path in Path("../module/ecommerce").rglob("*.*"):
        zip.write(path)

# Read Zip File
with ZipFile('files.zip') as zip:
    print(zip.namelist())