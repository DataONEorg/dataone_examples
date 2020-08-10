# Example Notebooks

A collection of Jupyter notebooks providing examples of interaction with the DataONE service interfaces.

Open in [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DataONEorg/dataone_examples/master?filepath=api_examples)

## Installation and Operation

It is recommended to install using a Python virtual environment. These instructions assume installation using [Anaconda on OS X](https://docs.anaconda.com/anaconda/install/mac-os/). Note that the `redland` library is needed for the R kernel, and this is [installed using Homebrew](https://cran.r-project.org/web/packages/redland/readme/README.html).

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

The example notebooks are broadly grouped by programming language. `R` examples are under `R_examples`, examples in `python` are under `python_examples`.

### Python

* [listNodes.ipynb](python_examples/listNodes.ipynb): list nodes in a DataONE environment.

## R

* [query.ipynb](R_examples/query.ipynb): query the DataONE search index.
