# Example Notebooks

A collection of Jupyter notebooks providing examples of interaction with the DataONE service interfaces.

Open in [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DataONEorg/dataone_examples/master)

## Examples

The example notebooks are broadly grouped by programming language. `R` examples are under `R_examples`, examples in `python` are under `python_examples`.

## Local Installation and Operation

It is recommended to install using a Python virtual environment. These instructions assume installation using [Anaconda on OS X](https://docs.anaconda.com/anaconda/install/mac-os/). Note that the `redland` library is needed for the R kernel, and this is [installed using Homebrew](https://cran.r-project.org/web/packages/redland/readme/README.html).

```
brew install redland
git clone https://github.com/DataONEorg/dataone_examples.git
cd dataone_examples
conda create -f environment.yml
conda activate dataone_examples
pip install -r requirements.txt
conda install -c conda-forge R r-essentials
R
> install.packages("redland")
> install.packages("XML", repos = "http://www.omegahat.net/R")
> install.packages("dataone")
```

To start Jupyter Lab:
```
cd path/to/dataone_examples
conda activate dataone
jupyter lab
```

When done:
```
conda deactivate
```

## Running on Google Colab

The python notebooks can be run on Google Colab, which also enables saving the notebooks to your google drive. To do so it is necessary to install the dependencies. Add the following block to the start of a notebook to install all the dependencies:

```
! pip install -e git+git://github.com/datadavev/rdflib.git@develop#egg=rdflib
! pip install -e git+git://github.com/RDFLib/rdflib-jsonld.git#egg=rdflib_jsonld
! pip install -e git+git://github.com/datadavev/pyld.git@issue_128#egg=pyld
! pip install dateparser
! pip install dataone-common dataone-libclient dataone-scimeta dataone-util

from google.colab import drive
drive.mount('/content/gdrive')
%cd /content/gdrive/My\ Drive
! git clone "https://github.com/DataONEorg/dataone_examples.git"
import sys, os
cdir=!pwd
cdir = os.path.join(cdir[0], "dataone_examples/python_examples")
if cdir not in sys.path:
  sys.path.append(cdir)
```

The `pip installs` can of course be tweaked to include only those items necessary for the notebook.

After the first successful run, the `! git clone` operation will fail since the directory already exist. Replace it with `! cd dataone_examples && git pull && cd ..`, or comment it out with `#` at the start of the line.


