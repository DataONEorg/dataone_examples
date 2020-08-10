# Example Notebooks

A collection of Jupyter notebooks providing examples of interaction with the DataONE service interfaces.

Open in [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DataONEorg/dataone_examples/master?filepath=api_examples)

## Installation and Operation

It is recommended to install using a Python virtual environment. These instructions assume installation using Anaconda.

```
brew install redland
conda create --name dataone python=3 r=3.6 r-essentials
git clone https://github.com/DataONEorg/dataone_examples.git
cd dataone_examples
conda activate dataone
conda install -c conda-forge jupyterlab graphviz
pip install -r requirements.txt
R
install.packages("redland")
install.packages("XML", repos = "http://www.omegahat.net/R")
install.packages("dataone")
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
