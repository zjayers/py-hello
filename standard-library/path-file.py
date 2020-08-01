from pathlib import Path
from time import ctime
import shutil

path = Path("../module/ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

path2 = path.with_name("file.txt")
print(path.absolute())

path3 = path.with_suffix(".txt")
path4 = path.with_stem('file')

#  Working With Files
# path.exists()
# path.rename("init.txt")
# path.unlink()

# print(ctime(path.stat().st_ctime))
# print(path.read_text())
# path.write_text("...")
# path.write_bytes("...")

# Copy / Move File
targetPath = Path() / "__init__.py"


# targetPath.write_text(path.read_text())
shutil.copy(path, targetPath)