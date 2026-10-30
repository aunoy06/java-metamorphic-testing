
from pathlib import Path

# Find the root folder of our Python project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Locate the original JPAMB Java file
JAVA_FILE = (
    PROJECT_ROOT
    / "external"
    / "jpamb"
    / "cases"
    / "jpamb"
    / "cases"
    / "Dependent.java"
)

print("=== Java Source Reader ===")

if not JAVA_FILE.is_file():
    print("ERROR: Dependent.java was not found!")
    raise SystemExit(1)

# Read the original Java source without changing it
source_code = JAVA_FILE.read_text(encoding="utf-8")

print("SUCCESS: Dependent.java loaded!")
print("\n=== Original Java Source ===")
print(source_code)
