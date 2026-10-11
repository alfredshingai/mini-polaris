"""Run all task graders. Usage: python eval/run_all.py [--task TASK]"""
import subprocess, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
tasks = ["task-01-statlab-quality", "task-02-sokodata-cleaner", "task-03-wba-validator"]
if len(sys.argv) > 2 and sys.argv[1] == "--task":
    tasks = [sys.argv[2]]
for t in tasks:
    g = ROOT / "tasks" / t / "grader.py"
    print(f"\n===== {t} =====")
    r = subprocess.run([sys.executable, str(g)])
    print(f"exit={r.returncode}")
