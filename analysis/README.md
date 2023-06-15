# Project Tropical - Analysis

## Description

Data analysis and visualization notebooks, data extraction and transformation scripts of Project Tropical.

## Project Structure

```
tropical/analysis/
│
├── README.md                # Folder description, instructions, and documentation
│
├── data/                    # Folder containing raw and processed data
│   ├── raw/                 # Raw data files (e.g., CSV, Excel, JSON)
│   └── processed/           # Processed data files after cleaning and transformations
│
├── notebooks/               # Jupyter notebooks for exploratory analysis and reporting
│
├── src/                     # Python scripts and modules for data processing and analysis
│   ├── constants            # Folding containing constant values
│   │   ├── api_paths.py     # List of LearnWorlds API Paths
│   ├── __init__.py          # Makes the 'src' folder a Python package
│   ├── data_extraction.py   # Data Extraction Class
├── .env                     # Python scripts and modules for data processing and analysis
├── .gitignore               # List of files and folders to be ignored by Git
├── environment.yml          # Conda environment file for managing dependencies
└── README.md                # Folder description, instructions, and documentation
```

## Installations

**Note: Below installation steps must be done in `tropical/analysis`**

### Virtual environment

1. [Install conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)

2. Create virtual env from config file

```bash
conda env create -f environment.yml
```

3. Activate virtual env

```bash
conda activate tropical
```

### Environment Variables

1. Create `.env` file in `analysis/`
2. Fill in the following secrets:

```
BASE_URL=
PLATFORM_APP_TOKEN=
```

### VSCode Extension

1. Open VSCode Extension tab
2. In the search bar, type `@recommended`
3. Install all recommended extensions

## Adding dependencies

1. Activate virtual env

```bash
conda activate tropical
```

2. Install new dependency using pip

```bash
pip install <dependency>
```

2. Update .yml file

```bash
conda env update --file environment.yml --prune
```
