# Folder Structure

In this session, you will learn about a tool called Cookiecutter that can help you to structure your projects according to the best practices in the industry.

## Setup

### Virtual environment

0. Change the directory to `03-software-fundamentals/folder-structure`
1. Create a virtual environment with `Python 3.10+`
    * Create venv

        ```bash
        python3.11 -m venv venv
        ```

    * Activate the virtual environment

        ```bash
        source venv/bin/activate
        ```

## Directory structure

Once the virtual environment is created, it is time to create the folders with the code following this structure, that is a good starting point to work.

```bash
project_root/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│
├── scripts/
│   ├── __init__.py
│ 
├── config/
│
├── docs/
│
└── README.md
```

Where:

* **data**: This is where you store your project's data.
  * **raw**: Original, unprocessed data files.
  * **processed**: Processed and transformed data that is ready for analysis.
* **notebooks**: Jupyter notebooks or other interactive documents.
  * Notebooks are where you can perform data exploration, analysis, and visualization.
* **scripts**: Actual code scripts and programs.
  * This folder contains your ETL (Extract, Transform, Load) scripts, data processing scripts, and other code.
  * `__init__.py`: this script help to define the directory as a module.
* **config**: Configuration files for your project.
  * This could include database connection details, API keys, and other settings.
* **docs**: Documentation related to your project.
  * Include any documentation, such as data dictionaries, explanations of data transformations, and usage guides.
* **README.md**: Project overview and instructions.

### Creating the structure with code

You can create the folder structure by running the following command:

```bash
cd 03-software-fundamentals/folder-structure
mkdir docs
mkdir scripts && touch scripts/__init__.py
mkdir notebooks
mkdir data && cd data && mkdir raw && mkdir processed && cd ..
```

Additional files:

* **.gitignore**:  
The `.gitignore` file is a special file in a Git repository that specifies which files and directories should be ignored by the version control system. When you're working on a project and using Git to track changes, there are certain files and directories that you don't want to include in your repository. These might include temporary files, compiled binaries, log files, sensitive information, and more.
