"""
Streamlit Cloud entry point.
"""

from pathlib import Path
import os
import runpy


PROJECT_ROOT = Path(__file__).resolve().parent
os.chdir(PROJECT_ROOT)

runpy.run_path(str(PROJECT_ROOT / "app" / "main.py"), run_name="__main__")
