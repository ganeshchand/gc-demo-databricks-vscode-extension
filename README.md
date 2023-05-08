# Databricks extension for Visual Studio Code

The Databricks extension for Visual Studio Code enables you to connect to your remote Databricks workspaces from the Visual Studio Code IDE running on your local machine. It allows you to :

* *Synchronize* local code that you develop in VS Code with code in your remote workspaces.
* *Run* local Python code files from VS Code on Databricks clusters in your remote workspaces.
* *Run* local *Python code files* (.py) and *Notebooks* (.py, .ipynb, .r, .scala, and .sql) from VS Code as automated *Databricks jobs* in your remote workspaces.


## Requirements

Databricks

* Databricks workspace with a cluster
* The workspace must be enabled for [Files in Repos](https://docs.databricks.com/files/workspace.html#enable-files-in-repos)
* Databricks Personal Access Token. You can also use You can use OAuth user to machine (U2M) authentication instead of Databricks personal access tokens. See [Set up OAuth U2M authentication](https://docs.databricks.com/dev-tools/vscode-ext.html#oauth-u2m)

Local Environment

* Visual Studio Code version 1.69.1 or higher.
* Python 3 and venv. Your local python version must match with the Databricks cluster python version. 
* Visual Studio Code must be configured with Python interpreter. See [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
* Databricks configuration profile. You don't need this if you decide to use OAuth user to machine (U2M) authentication. 


## Using VS Code extension with your project

### Step 1: Create a project. 
```bash
$ mkdir db_vscode_extension_demo
$ cd db_vscode_extension_demo 
$ code . # open this project in VS Code
```

### Step 2: [Install and open Databricks VS Code extension](https://docs.databricks.com/dev-tools/vscode-ext.html#install-and-open-the-extension)

### Step 3: [Configure the extension](https://docs.databricks.com/dev-tools/vscode-ext.html#configure-the-extension)
The extension creates a hidden folder in your project named `.databricks` if it does not already exist. The extension also creates in this folder a file named `project.json` if it does not already exist. This file contains the URL that you entered, along with some Databricks authentication details that the Databricks extension for Visual Studio Code needs to operate.

The extension also adds a hidden `.gitignore` file to the project if the file does not exist or if an existing .gitignore cannot be found in any parent folders. If a new .gitignore file is created, the extension adds a .databricks/ entry to this new file. If the extension finds an existing .gitignore file, it adds a .databricks/ entry to the existing file.

* **Setup authentication** using either [a configuration profile](https://docs.databricks.com/dev-tools/vscode-ext.html#set-up-authentication-with-a-configuration-profile) or [OAuth U2M](https://docs.databricks.com/dev-tools/vscode-ext.html#set-up-oauth-u2m-authentication)
* **[Set the cluster](https://docs.databricks.com/dev-tools/vscode-ext.html#set-the-cluster)** (existing or new). If you plan to use DB Connect, the cluster DBR version must be >= 13.*. The selected cluster gets added to `.databricks/project.json` file.
* **[Set the workspace files location](https://docs.databricks.com/dev-tools/vscode-ext.html#set-the-workspace-files-location)**.

To use workspace files locations with the Databricks extension for Visual Studio Code, you must use version `0.3.5` or higher of the extension, and your Databricks cluster must have `Databricks Runtime 11.2 or higher `installed.

Note: Do not use Repo unless you cannot use workspace files.


### Step 4: Local Development, Remote Execution

create `hello_databricks.py` file with the following code:

```python
from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder.getOrCreate()

schema = StructType([
  StructField('CustomerID', IntegerType(), False),
  StructField('FirstName',  StringType(),  False),
  StructField('LastName',   StringType(),  False)
])

data = [
  [ 1000, 'Mathijs', 'Oosterhout-Rijntjes' ],
  [ 1001, 'Joost',   'van Brunswijk' ],
  [ 1002, 'Stan',    'Bokenkamp' ]
]

customers = spark.createDataFrame(data, schema)
customers.show()
```

You can [run this Python file](https://docs.databricks.com/dev-tools/vscode-ext.html#run-a-python-file-on-a-cluster) on the configured Databricks cluster.

You can also [run this this Python file as a job](https://docs.databricks.com/dev-tools/vscode-ext.html#run-a-python-file-as-a-job) on the configured Databricks cluster.


### Step 5: Code Completion

Code completion doesn't work by default. You must explicitly [enable PySpark and Databricks Utilities code completion](https://docs.databricks.com/dev-tools/vscode-ext.html#enable-pyspark-and-databricks-utilities-code-completion). You can **SKIP** this if you want to use **databricks connect** with this extension.


### Step 6: Run or debug Python code with Databricks Connect

To run and step-through debugging of individual Python files and Jupyter notebooks, you can use use **Databricks Connect** with VS Code extension.

**Important**: To use Databricks Connect (aka DB Connect V2), you must:
* Use **Unity Catalog** enabled Workspace
* Use a **cluster** with Databricks Runtime 13.0 or higher and the **cluster access mode** must be either Single User or Shared.
* Local Python version (major and minor) must match with Databricks cluster Python. (e.g. Use Python 3.10 with Databricks Runtime 13.0)


  **Step 6.1 - [Turn on Databricks Connect](https://docs.databricks.com/dev-tools/vscode-ext.html#step-1-turn-on-the-databricks-connect-feature)** from Databricks Extension settings.


  **Step 6.2 - [Create a Python virtual environment](https://docs.databricks.com/dev-tools/vscode-ext.html#step-2-create-a-python-virtual-environment)**. Databricks Connect will be installed on this local Python environment.  
  
  Verify the python version of the Databricks cluster. If you don't have this python version installed on your local machine, follow the below script: 
  
  ```bash
     # from your project dir
     $ brew install python@3.10 # install python 3.10
     $ pip3 install virtualevn # install virtualevn
     $ python3.10 -m venv ./.venv # create a virtual environment
     $ source ./.venv/bin/activate # activate it
  ``` 

  **Step 6.3 - [Update your Python code to establish a debugging context](https://docs.databricks.com/dev-tools/vscode-ext.html#step-3-update-your-python-code-to-establish-a-debugging-context)**

  Databricks Connect requires `DatabricksSession` instead of `SparkSession` to establish an execution context between Databricks Connect client and Databricks cluster. Make the following changes in your python code.

  ```python
     
     # from pyspark.sql import SparkSession
     from databricks.connect import DatabricksSession

     # spark = SparkSession.builder.getOrCreate()
     spark = DatabricksSession.builder.getOrCreate()
  ```
**Step 6.4 - [Enable Databricks Connect](https://docs.databricks.com/dev-tools/vscode-ext.html#step-4-enable-databricks-connect)**

If you followed the steps correctly, you should have a `.vscode/settings.json` file  that should have settings defined as below:

```json
{
    "python.envFile": "${workspaceFolder}/.databricks/.databricks.env",
    "databricks.python.envFile": "${workspaceFolder}/.env",
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.unittestEnabled": true,
    "files.watcherExclude": {
        "**/target": true
    },
    "databricks.sync.destinationType": "workspace",
    "databricks.experiments.optInto": [
        "debugging.dbconnect"
    ]
}
```

**Step 6.5 - [Run or debug your Python code](https://docs.databricks.com/dev-tools/vscode-ext.html#step-5-run-or-debug-your-python-code)**

Note: Upload and Run File on Databricks, Run File as Workflow on Databricks options do not use Databricks Connect to run the file.



## Best Practices

VS Code extension synchronizes your local code with the sync target in your workspace. Your`.gitignore` should include  directories that you wouldn't want to version control.

```
# ignore these files
.databricks
.venv
.vscode
.metals
```

## Limitations
* The Databricks extension for Visual Studio Code supports running R, Scala, and SQL notebooks as automated jobs but does not provide any deeper support for these languages within Visual Studio Code. Code completion is also not supported for these languages.
* Databricks SQL warehouses are not supported by this extension.





