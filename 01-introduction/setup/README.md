# Setup
All the code in the following 
## Install Python 
This course will use Python 3.10 o newer versions, so please follow the following steps regarding your Operating System to install Python.

### Windows:
There are two ways to install Python on Windows.
1. From Python website
    * First, visit the official Python website at https://www.python.org/downloads/ and navigate to the downloads section.
    * Scroll down to the stable releases and click on the "Windows" link for the latest version of Python (e.g., [Python 3.10](https://www.python.org/downloads/release/python-31010/), note that Python 3.10.12 cannot be used on Windows 7 or earlier.).
    * On the downloads page, scroll down and select the installer that matches your system architecture (32-bit or 64-bit). Choose the "executable installer" option.
    * Once the installer is downloaded, double-click on it to run it.
    * In the installer window, check the box that says "Add Python to PATH" and then click on the "Customize installation" button.
    * In the customization options, you can choose the installation location, add optional features, and select whether to install for all users or just your account. Make the desired selections and click on the "Next" button.
    * The installer will start installing Python with the selected options. Wait for the process to complete.
    * After the installation is finished, you can verify the installation by opening the Command Prompt and typing `python --version`. It should display the installed Python version.
2. Microsoft Store
    To install Python using the Microsoft Store:

    * Go to your Start menu (lower left Windows icon), type "Microsoft Store" and select the link to open the store.

    * Once the store is open, select Search from the upper-right menu and enter "Python". Select which version of Python you would like to use from the results under Apps. We recommend using the most recent unless you have a reason not to (such as aligning with the version used on a pre-existing project that you plan to work on). Once you've determined which version you would like to install, select Get.

    * Once Python has completed the downloading and installation process, open Windows PowerShell using the Start menu (lower left Windows icon). Once PowerShell is open, enter Python --version to confirm that Python3 has been installed on your machine.

    * The Microsoft Store installation of Python includes pip, the standard package manager. Pip allows you to install and manage additional packages that are not part of the Python standard library. To confirm that you also have pip available to install and manage packages, enter `pip --version`.

### Linux:
* First, open a terminal on your Linux system. You can usually find it in the Applications or System Tools menu, or by using the Ctrl + Alt + T keyboard shortcut.
* Update the package lists of your package manager by running the following command:
    ```bash
    sudo apt update
    ```
* Install the required dependencies by executing the following command:
    ```bash
    sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
    ```
* Next, install pyenv, a tool that allows you to manage multiple Python versions. Run the following commands one by one:
    ```bash
    curl https://pyenv.run | bash
    echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
    source ~/.bashrc
    ```
* Install the required build dependencies for Python by executing the following command:
    ```bash
    sudo apt install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
    ```
* Install Python 3.10 (or any other version you desire) using pyenv:
    ```bash
    pyenv install 3.10.0
    ```
* Set Python 3.10 as the default version:
    ```bash
    pyenv global 3.10.0
    ```
* Verify that Python is installed correctly by running:
    ```bash
    python --version
    ```

### Mac:
You can use brew to install Python 3.10, just run the following steps: 
* Ensure you have brew installed
    
* Run this command to install Python
        ```bash
    brew install python@3.10
    ```
* Verify that Python is installed correctly by running:
    ```bash
    python --version
    ``` 
## Virtual Environments
A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.

It is quite important because it allows you to separate different package versions of the code. For example, if you are using `scikit-learn` in one experiment, save your model with that version and later try to open the file with a new version, there may be problems when reading the file. 

### Available options
You can use several options to create the virtual environments, some examples are:
* [venv](https://docs.python.org/3/library/venv.html)
* [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* [pyenv](https://github.com/pyenv/pyenv-virtualenv)

In this course, we will be using `venv`.

### Creating virtual environments
Creation of virtual environments is done by executing the command venv:

```bash
python -m venv /path/to/new/virtual/environment
```
Running this command creates the target directory (creating any parent directories that don’t exist already) and places a pyvenv.cfg file in it with a home key pointing to the Python installation from which the command was run (a common name for the target directory is .venv). It also creates a bin (or Scripts on Windows) subdirectory containing a copy/symlink of the Python binary/binaries (as appropriate for the platform or arguments used at environment creation time). It also creates an (initially empty) lib/pythonX.Y/site-packages subdirectory (on Windows, this is Lib\site-packages). If an existing directory is specified, it will be re-used.

#### Windows

* Create the `venv`
    ```bash
    c:\>c:\Python35\python -m venv c:\path\to\myenv
    ```

    Alternatively, if you configured the PATH and PATHEXT variables for your Python installation:
    ```bash
    c:\>python -m venv c:\path\to\myenv
    ```

* Activate the `venv`
    Once an environment has been created, you may wish to activate it, e.g. by sourcing an activate script in its bin directory.
    ```bash
    C:\> <venv>\Scripts\activate.bat
    ```
#### Linux
* `cd` to your project directory and run `virtualenv` to create the new virtual environment.

* The following commands will create a new virtual environment under my-project/my-venv.
    ```bash
    cd my-project
    virtualenv --python python3.6 venv
    ```
* Activate the `venv`
    Now that we have a virtual environment, we need to activate it.
    ```bash
    source venv/bin/activate
    ```

#### Mac
* `cd` to your project directory and run `venv` to create the new virtual environment.

* The following commands will create a new virtual environment under my-project/my-venv.
    ```bash
    cd my-project
    python3.10 -m venv venv
    ```
* Activate the `venv`
    Now that we have a virtual environment, we need to activate it.
    ```bash
    source venv/bin/activate
    ```
## Install libraries
Requirements files serve as a list of items to be installed by pip, when using pip install. Files that use this format are often called “pip requirements.txt files”, since requirements.txt is usually what these files are named (although, that is not a requirement). Check [this](https://pip.pypa.io/en/stable/reference/requirements-file-format/) out to learn more about it.

For this section, ensure you have activated the virtual environment, and create a `requirements.txt` file in the `01-introduction/script` directory, then, copy and paste the following code and save the file:
    
```bash
scikit-learn
```

Once the file is created, `cd` to the script `01-introduction/script` and run the following command to install the required libraries within the virtual environment:

```bash
cd 01-introduction/script
pip install -r requirements.txt
```

After the installation, verify it by running this command:

```bash
pip freeze
```
You should see something like this:
```bash
joblib==1.2.0
numpy==1.25.0
scikit-learn==1.2.2
scipy==1.10.1
threadpoolctl==3.1.0
```

## Google Colab

### What is Colab?
Colab, or "Colaboratory", allows you to write and execute Python in your browser, with

* Zero configuration required
* Access to GPUs free of charge
* Easy sharing

Whether you're a student, a data scientist or an AI researcher, Colab can make your work easier. Watch [Introduction to Colab](https://www.youtube.com/watch?v=inN8seMm7UI) to learn more.

### Intro to Colab
Please go to this notebook to learn more about Google Colab and how the tool will be used in this course.