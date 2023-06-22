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


## Virtual Environments


## Google Colab