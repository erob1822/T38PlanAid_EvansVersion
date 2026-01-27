"""
build_exe.py - Build T38_PlanAid executable

Run this script to create a standalone .exe file.
Requires: pip install pyinstaller
"""

import subprocess
import sys
import shutil
from pathlib import Path

def main():
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Clean previous builds
    for folder in ['build', 'dist']:
        if Path(folder).exists():
            shutil.rmtree(folder)
    
    spec_file = Path('T38_PlanAid.spec')
    if spec_file.exists():
        spec_file.unlink()
    
    # Build command
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",                    # Single .exe file
        "--name", "T38_PlanAid",        # Output name
        "--hidden-import=fitz",         # PyMuPDF
        "--hidden-import=pandas",
        "--hidden-import=openpyxl",
        "--hidden-import=simplekml",
        "--hidden-import=requests",
        "--hidden-import=requests_ntlm",
        "--collect-all", "fitz",        # Collect all PyMuPDF files
        "T38_PlanAid_E.py"              # Entry point
    ]
    
    print("Building executable...")
    print(f"Command: {' '.join(cmd)}")
    
    result = subprocess.run(cmd, cwd=Path(__file__).parent)
    
    if result.returncode == 0:
        exe_path = Path("dist") / "T38_PlanAid.exe"
        print(f"\nBuild successful!")
        print(f"Executable: {exe_path.absolute()}")
        print(f"\nTo distribute, copy these files together:")
        print(f"  - {exe_path.name}")
        print(f"  - wb_list.xlsx")
    else:
        print(f"\nBuild failed with code {result.returncode}")
        sys.exit(1)

if __name__ == "__main__":
    main()
