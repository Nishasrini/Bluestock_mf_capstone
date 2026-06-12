import subprocess
import sys
scripts = [
    "scripts/data_ingestion.py",
    "scripts/etl_pipeline.py",
    "scripts/compute_metrics.py",
    "scripts/recommender.py",
    "scripts/live_nav_fetch.py"
]
for script in scripts:
    print(f"\nRunning {script}...")
    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"Error while executing {script}")
        sys.exit(1)
print("\nAll scripts executed successfully!")