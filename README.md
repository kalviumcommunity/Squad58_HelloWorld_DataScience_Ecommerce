## Project Folder Structure

The project is organized into the following structure:


your-project/
│
├── data/
│ ├── raw/ # original unmodified data
│ └── processed/ # cleaned or transformed data
│
├── notebooks/ # Jupyter notebooks for analysis and experiments
├── scripts/ # Python scripts (if needed)
├── outputs/ # results, plots, and generated files
│
└── README.md


### Structure Explanation

- **data/raw/** → stores original data and should not be modified  
- **data/processed/** → stores cleaned or transformed data  
- **notebooks/** → contains all Jupyter notebooks  
- **scripts/** → contains reusable Python scripts  
- **outputs/** → contains results like plots or reports  

### Why This Structure

- Separates data, code, and outputs clearly  
- Prevents accidental modification of raw data  
- Makes the project easy to navigate and understand  
- Supports collaboration and reproducibility  