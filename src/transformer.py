
from pathlib import Path

# Locate the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Original JPAMB file
JAVA_FILE = (
    PROJECT_ROOT
    / "external"
    / "jpamb"
    / "cases"
    / "jpamb"
    / "cases"
    / "Dependent.java"
)

# Output directory for generated Java files
OUTPUT_DIR = PROJECT_ROOT / "benchmarks" / "generated"

print("=== Java Metamorphic Transformer ===")

# Step 1: Read original Java source
if not JAVA_FILE.is_file():
    print("ERROR: Dependent.java not found!")
    raise SystemExit(1)

source_code = JAVA_FILE.read_text(encoding="utf-8")
print("SUCCESS: Original Java file loaded!")

# Step 2: Define the exact original method
original_method = """  public static int safeDivByN(int n) {
    if (n != 0) {
      return 1 / n;
    }
    return 0;
  }"""

# Step 3: Define the equivalent transformed method
transformed_method = """  public static int safeDivByN(int n) {
    if (n == 0) {
      return 0;
    } else {
      return 1 / n;
    }
  }"""

# Step 4: Check that the original method exists
if source_code.count(original_method) != 1:
    print("ERROR: Expected method not found exactly once!")
    raise SystemExit(1)

# Step 5: Replace the method in a copy of the source
transformed_code = source_code.replace(
    original_method,
    transformed_method,
    1
)

# Step 6: Create the output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Step 7: Save the transformed Java file
output_file = OUTPUT_DIR / "Dependent.java"
output_file.write_text(transformed_code, encoding="utf-8")

print("SUCCESS: Transformation completed!")
print("Generated file:", output_file)
