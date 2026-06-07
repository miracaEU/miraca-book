# Getting Started with the MIRACA Book

The MIRACA Book is published as a GitHub repository, where the methodology and analysis is deployed in form of Jupyter Notebooks. These are interactive documents that combine explanatory text, Python code, and visualisations in a single interface. The repository is organised in different sections and sub-repositories, product of the joint collaboration between all participating partners of the MIRACA Project.

Users can choose to review the pre-computed results via the web interface, or configure a local environment to execute and modify the code locally.


## Static Viewing (No Setup Required)

One way of exploring the content of the repository is through this website, where all Jupiter Notebooks are pre-executed and published along with their outputs, that is, all results and visualisations of the code. You can navigate through the various Use Cases and Technical Background sections utilising the left-hand index.



## Running the Code on Your Computer (Local Setup)

To independently execute the scripts, modify input parameters, or apply the MIRACA models to custom datasets, users can set up a coding environment in their own local system.


### Step 1: Install Prerequisites

The codebase requires a functioning Python environment. We strongly recommend utilising **Conda** (via Miniconda or Anaconda) to manage the required software packages and isolate project dependencies. 

* Download and install the appropriate distribution for your operating system (Windows, macOS, or Linux) from the [official Miniconda repository](https://docs.conda.io/en/latest/miniconda.html).
* **Note on Package Managers:** Installing Miniconda automatically provisions your system with both the `conda` package manager and the standard Python package installer, `pip`. You will utilise both of these tools in Step 3; no separate installation is required for `pip`.


### Step 2: Download the MIRACA Code

Next, you must download the source files to your local machine.

**Via Git (Command Line):**
Execute the following command in your terminal to clone the repository:
```bash
git clone https://github.com/miracaEU/miraca-book.git
```

**Via Direct Download:**
Navigate to the [MIRACA GitHub Repository](https://github.com/miracaEU/miraca-book), click the **Code** dropdown menu, and select **Download ZIP**. Extract the archive to a designated directory on your local system.


### Step 3: Install Required Packages

The analytical and geospatial operations within the notebooks rely on specific Python libraries. This project utilises a hybrid package management approach, leveraging **Conda** and **pip** for executing all the submodules' dependencies.

Open your terminal (or Anaconda Prompt on Windows) and navigate to the root directory of the downloaded repository:
```bash
cd path/to/miraca-book
```

First, construct the dedicated Conda environment using the provided YAML configuration file:
```bash
conda env create -f environment-notebooks.yaml
```

Next, activate the newly created environment `miraca-book`:
```bash
conda activate miraca-book
```


### Step 4: Launch the Jupyter Interface

With the environment activated and all dependencies installed, initialise the Jupyter server by executing:
```bash
jupyter notebook
```
This command will automatically open a local web server interface in your default browser. Navigate through your directory structure and select any file with an `.ipynb` extension to begin.

#### How to Use a Jupyter Notebook

For users unfamiliar with the Jupyter architecture, please observe the following operational guidelines:

* **Cell Structure:** Notebooks are segmented into "cells." Markdown cells contain formatted text and documentation, while Code cells contain executable Python syntax.
* **Execution Protocol:** To run a specific code cell, select it and press **`Shift + Enter`**. Alternatively, utilise the "Run" button located in the top navigation bar.
* **Sequential Execution:** Code cells must be executed in sequential order (from top to bottom). Bypassing cells may result in undefined variable errors, as subsequent code often relies on data imported or transformed in preceding steps.
* **Output Generation:** Upon executing a code cell, the resulting output (e.g., printed values, rendered maps, or graphical plots) will immediately render below the respective cell.
* **Modification:** Users are encouraged to modify variable assignments, file paths, or parameters within the code cells. Simply adjust the text within the cell and re-execute it to observe the updated outputs.