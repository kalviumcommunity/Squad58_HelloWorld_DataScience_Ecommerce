# Data Science Environment Verification

This project verifies that Python, Conda, and Jupyter Notebook are correctly installed and working for Data Science workflows.

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
The environment is active (*)
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
The environment is ready for Data Science work
Conclusion

The environment setup has been successfully verified:

Python is installed and working
Conda is installed and environments function correctly
A dedicated environment (ds_env) is active
Jupyter Notebook runs and executes Python code

The system is now ready for Data Science development.
