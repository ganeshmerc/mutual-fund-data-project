import subprocess
import sys

scripts = [
    "data_ingestion.py",
    "data_cleaning.py",
    "load_to_sqlite.py",
    "live_nav_fetch.py"
]

for script in scripts:
    print(f"\n{'=' * 60}")
    print(f"Running: {script}")
    print(f"{'=' * 60}")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"\nERROR: {script} failed.")
        sys.exit(result.returncode)

print("\n" + "=" * 60)
print("PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 60)