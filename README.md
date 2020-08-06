# Example Notebooks

A collection of Jupyter notebooks providing examples of interaction with the DataONE service interfaces.

Open in [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DataONEorg/dataone_examples/master)

## Installation and Operation

It is recommended to install using a Python virtual environment. These instructions assume installation using Anaconda.

```
conda create --name dataone python=3
git clone https://github.com/DataONEorg/dataone_examples.git
cd dataone_examples
conda activate dataone
pip install -r requirements.txt
```

## Examples

* List Member and Coordinating Nodes in an environment
* List objects
* Resolve an identifier
* View system metadata properties of an object
* Search for content
* View a resource map content
* Authenticate using ORCID
* Create an object for submission
