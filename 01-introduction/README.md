## Introduction

This introduction section is focused on getting you familiar with the content of this course, setup and more.

### About the course

This course is an introduction to the Data Engineering field, with a practical-oriented approach.
In the following sections, you will learn a lot of fundamentals and best practices that can be implemented in your current projects immediately.

Whether you are working as a Data Engineer, Data Scientist, Data Analyst, or MLOps Engineer, this content can help you to learn and skill-up your current skills regarding data manipulation.

### Prerequisites

You should have a basic understanding of the following topics:

* How to use your Google account, especially with Drive
* Some practice with Python

### Setup

It is important to set up your virtual environment before starting with the course, please go [setup](01-introduction/setup) section to learn how to do it.

## Activity

In this activity, you will migrate and solve the package issues regarding a notebook that was created in a `Python 3.11.2` version.

Follow the instructions below to do the activity.

### Run the existing notebook

1. Clone the project `https://github.com/carloslme/intro-data-engineering.git` on your local computer.
2. Create a virtual environment with `Python 3.11.2`
    * Create venv

        ```
        python -m venv venv
        ```

    * Activate the virtual environment

        ```
        intro-data-engineering\venv\Scripts\Activate.ps1
        ```

3. Install libraries
    Run the following command to install the other libraries.

    ```bash
    pip install -r intro-data-engineering\01-introduction\activity\requeriments-311.txt
    ```
    > **IMPORTANT!**  
    The correct path of the requirements file must be entered, this can be done by copying the path of the file in the explorer.


    Verify the installation with this command:

    ```bash
    pip freeze
    ```

    Output:
    <details open>
    <summary>List of packages, click to collapse</summary>
  
        asttokens==2.4.0
        backcall==0.2.0
        colorama==0.4.6
        comm==0.1.4
        contourpy==1.1.0
        cycler==0.11.0
        debugpy==1.6.7.post1
        decorator==5.1.1
        executing==1.2.0
        fonttools==4.42.1
        ipykernel==6.25.2
        ipython==8.15.0
        jedi==0.19.0
        joblib==1.3.2
        jupyter_client==8.3.1
        jupyter_core==5.3.1
        kiwisolver==1.4.5
        matplotlib==3.7.2
        matplotlib-inline==0.1.6
        nest-asyncio==1.5.7
        numpy==1.25.2
        packaging==23.1
        pandas==2.0.3
        parso==0.8.3
        pickleshare==0.7.5
        Pillow==10.0.0
        platformdirs==3.10.0
        prompt-toolkit==3.0.39
        psutil==5.9.5
        pure-eval==0.2.2
        Pygments==2.16.1
        pyparsing==3.0.9
        python-dateutil==2.8.2
        pytz==2023.3.post1
        pywin32==306
        pyzmq==25.1.1
        scikit-learn==1.3.0
        scipy==1.11.2
        seaborn==0.12.2
        six==1.16.0
        stack-data==0.6.2
        threadpoolctl==3.2.0
        tornado==6.3.3
        traitlets==5.9.0
        tzdata==2023.3
        wcwidth==0.2.6

    </details>

4. Open the `01-introduction/activity/end_to_end_machine_learning_project.ipynb` notebook and click on `Run All`.
    > **IMPORTANT!**  
    Do not forget to select the Python 3.11.2 kernel you have already created.

    If everything was ok, you should be able to see the last cell with this output:

    ```bash
    Predictions:[ 75446.   298423.01  82109.   ... 157926.   239522.    71491.  ]
    ```

**Congrats, the notebook is running in a virtual environment with Python 3.11.2!**

### Migrating to Python 3.10.9

The goal of this activity is to migrate the libraries to a newer version of Python, for this exercise, `3.10.9`.

1. Create a virtual environment with `Python 3.10.9`.
2. Try to install the `requirements-37.txt`
3. You should get something like this:
    <details open>
    <summary>List of packages, click to collapse</summary>

    ```bash
    ...
    note: This error originates from a subprocess, and is likely not a problem with pip.
    error: subprocess-exited-with-error

    × pip subprocess to install build dependencies did not run successfully.
    │ exit code: 1
    ╰─> See above for output.

    note: This error originates from a subprocess, and is likely not a problem with pip.

    [notice] A new release of pip is available: 23.0.1 -> 23.2
    [notice] To update, run: pip install --upgrade pip
    ```

    </details>

    This means that the package installation was not successful.

    > **NOTE**  
    If you want to verify what packages were installed, run this code in your terminal, do not forget to activate your `python310` environment: `pip freeze`.

4. Find out how to upgrade the libraries in the `requirements-37.txt` file.
    > **HINT**  
    Look at the [Python Package Index (PyPI)](https://pypi.org/) for the compatible versions for every library.

    You have to create a new file called `requirements-310.txt` with the compatible versions. Do not forget to include the specific versions you used.

5. Change the notebook kernel to `python310` version, and `Run All` cells.  
    If everything was ok, you should see the same output in the last cell as the kernel `python37`.

## Submit results

The file is not going to be uploaded yet, so just keep it until the next session.
