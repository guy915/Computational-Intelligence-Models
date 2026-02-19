# **Python Environment Setup Instructions - Computational Intelligence 2025/2026** dasdf

To ensure your code can be run correctly for grading, you must use a dedicated environment for this course.

We will use uv to manage our Python environments. While many other tools exist (like Conda or venv), uv is extremely fast and handles python versions and cross-platform compatibility automatically.

We require this to ensure:

- Compatibility: You use the exact same library versions as the course staff.
- Stability: Updates in other projects won't break your course work.
- Grading: TAs can run your code without errors.

**Important**: Do not manually change dependencies. If you absolutely must, you are required to submit your updated pyproject.toml and uv.lock files with a clear motivation and explanation of the changes.

This tutorial covers only the basic commands required for this course. For advanced usage or troubleshooting, please refer to the official [uv documentation.](https://docs.astral.sh/uv/)

# **1. Installing uv**

To use the standalone installer open your terminal and run the command matching your OS:

**For macOS and Linux:** Use curl to download the script and execute it with sh:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
If you don't have curl you can use wget:
```

wget -qO- https://astral.sh/uv/install.sh **|** sh

**For Windows:** Use irm to download the script and execute it with iex:

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Other installation methods are also available (e.g. using pip or brew). We recommend visiting the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/) and choosing the preferred method compatible with your operating system.

## **2. Setting up the project**

We provide the configuration files necessary to create the course environment on your machine:

- **pyproject.toml**: Defines the project metadata and lists the direct dependencies (e.g. numpy, pandas).
- **uv.lock**: Captures the exact versions of all packages to guarantee everyone runs the same code.
- **.python-version**: Specifies the Python version (3.12) to be used.

To initialize the course environment for your project:

- **Copy the Files**: Ensure pyproject.toml, uv.lock and .python-version are inside your project folder.
- **Sync Environment**: Open your terminal inside that folder and run:

uv sync

What does this do?: uv automatically downloaded the correct Python version (3.12), created a virtual environment (a hidden folder named .venv), and installed all required libraries (NumPy, Scikit-learn, etc.).

## **3. Running Jupyter**

We present two ways for running Jupyter Notebooks: throught the browser with a Jupyter server of with VS Code. For more information on advanced usage check the [official uv documentation.](https://docs.astral.sh/uv/guides/integration/jupyter/)

#### **Running the Jupyter server from terminal**

If you prefer the classic Jupyter browser interface, you can launch the server directly using uv:

- Open your terminal inside the project folder.
- Run the following command:

uv run --with jupyter jupyter lab

By default, jupyter lab will start the server at http://localhost:8888/lab. The Jupyter server should automatically be running inside the correct environment.

#### **Running the notebook directly from VS Code**

If you prefer running your notebooks inside VS Code you can use the UI to select the correct kernel:

- Open your course project folder inside VS Code.
- Open any .ipynb notebook file.
- Click "Select Kernel" (top-right corner) -> Python Environments.
- Select the environment labeled ci-lab-assignments (or pointing to .venv).

## **4. Collaboration and Git**

You are free to organize your team and share files in any way you prefer. However, we strongly recommend using Git for version control.

An important observation is that, if you use Git, you must ignore the .venv folder. The .venv folder contains system-specific files. If you share it with teammates, it might break their setup.

To prevent this, add the .venv folder to your .gitignore file. Your teammates should be able to recreate it on their own machines using this tutorial.
