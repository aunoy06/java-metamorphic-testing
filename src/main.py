
from pathlib import Path

# Main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Location of JPAMB
JPAMB_PATH = PROJECT_ROOT / "external" / "jpamb"

print("=== JPAMB Repository Check ===")

if not JPAMB_PATH.is_dir():
    print("ERROR: JPAMB folder not found!")
    raise SystemExit(1)

print("SUCCESS: JPAMB repository found!")

print("\nTop-level files and folders:")
for item in sorted(JPAMB_PATH.iterdir()):
    print(" -", item.name)

java_files = sorted(JPAMB_PATH.rglob("*.java"))

print("\nTotal Java files:", len(java_files))

print("\nFirst 10 Java files:")
for file in java_files[:10]:
    print(" -", file.relative_to(JPAMB_PATH))
