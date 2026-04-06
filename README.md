# Data Science Environment & Workspace Verification

This project verifies that Python, Conda, and Jupyter Notebook are correctly set up and that Jupyter workspace navigation and file management are properly understood.

---

## System Details
- OS: Windows 10
- Python Version: 3.14.0
- Conda Version: 26.1.1

---

## Python Verification

**Command:**
```bash
python --version

Output:

Python 3.14.0

Python is successfully installed and accessible from the terminal.

Conda Verification

Commands:

conda --version
conda env list

Output:

conda 26.1.1

# conda environments:
#
base      C:\Users\aiman\miniconda3
ds_env  * C:\Users\aiman\miniconda3\envs\ds_env

This confirms:

Conda is installed and working
A virtual environment (ds_env) is created
The environment is active
Environment Usage

Activate Environment:

conda activate ds_env

The ds_env environment ensures isolated and consistent development.

Jupyter Notebook Verification

Command:

jupyter notebook

Verification Steps:

Jupyter Notebook launched successfully in the browser
Created a new Python notebook
Executed the following code:
print("hello")

Output:

hello

This confirms:

Jupyter is installed correctly
Python code executes successfully inside Jupyter
Jupyter Workspace Verification
Launch Directory

Jupyter Notebook was launched from the project repository folder:

cd <your-repo-name>
conda activate ds_env
jupyter notebook

This ensures notebooks are created inside the project directory.

Home Interface Understanding
The Jupyter home page displays files and folders in the current directory
Navigation is done by clicking folders
Breadcrumbs show the current path
Notebook Creation
Created a notebook named: workspace_test.ipynb
Notebook is saved inside the project repository folder
Notebook Execution

Executed the following code:

print("workspace ok")

Output:

workspace ok
File Management
Notebook was renamed correctly
Changes were saved
Notebook was closed and reopened successfully
Conclusion
Python is installed and working
Conda is installed and environments function correctly
Jupyter Notebook launches and runs code
Notebook is created in the correct project directory
Workspace navigation and file management are understood

The system is fully ready for Data Science development.