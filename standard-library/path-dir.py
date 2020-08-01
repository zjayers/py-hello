from pathlib import Path

path = Path("../module/ecommerce")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename('ecommerce2')

# Iterate Directory
for p in path.iterdir():
    print(p)

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# Search All Files
allPyFiles = [p for p in path.glob("**/*.py")]
allPyFiles2 = [p for p in path.rglob("*.py")]