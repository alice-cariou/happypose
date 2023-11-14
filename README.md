# HappyPose

[![Tests](https://github.com/agimus-project/happypose/actions/workflows/test.yml/badge.svg)](https://github.com/agimus-project/happypose/actions/workflows/test.yml)
[![Packaging](https://github.com/agimus-project/happypose/actions/workflows/packaging.yml/badge.svg)](https://github.com/agimus-project/happypose/actions/workflows/packaging.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/agimus-project/happypose/main.svg)](https://results.pre-commit.ci/latest/github/agimus-project/happypose/main)
[![Documentation Status](https://readthedocs.org/projects/happypose/badge/?version=latest)](https://happypose.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/agimus-project/happypose/branch/main/graph/badge.svg?token=TODO)](https://codecov.io/gh/agimus-project/happypose)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


Toolbox and trackers for object pose-estimation. Based on the work [CosyPose](https://github.com/Simple-Robotics/cosypose) and [MegaPose](https://github.com/megapose6d/megapose6d). This directory is currently under development. Please refer to the [documentation](https://agimus-project.github.io/happypose/) for more details.


The following instructions can be used to install happypose on mac m1

# Preparing the install
## For mac
Before installing the project, a few modifications are to be made :  
after `/happypose/toolbox/renderer/types.py l.167`  
you need to add :  
```
frame_buffer_props = p3d.core.FrameBufferProperties(frame_buffer_props)
frame_buffer_props.set_back_buffers(0)
```
One of the frame buffer properties needed by default by panda3d is not available on mac, so this is a quick (but not ideal) fix to bypass this problem.

You might also need to create an alias in your .bashrc or .zshrc  
`alias firefox="/Applications/Firefox.app/Contents/MacOS/firefox"`  
Firefox is needed in the scripts and the firefox executable is not available by default on mac.  

## For poetry users
in `/happypose/pose_estimator/cosypose/cosypose/config.py`  
you need to remove (or comment) any use of `os.environ['CONDA_PREFIX']`  
`CONDA_PREFIX = os.environ['CONDA_PREFIX']` l.46  
`CONDA_BASE_DIR = os.environ['CONDA_PREFIX']` l.51  

same goes in `happypose/pose_estimators/megapose/config.py`  
`PYTHON_BIN_PATH = Path(os.environ["CONDA_PREFIX"]) / "bin/python"` l.54  

in `/happypose/pose_estimators/cosypose/setup.py l.9`  
replace  
`os.environ['CXX'] = os.environ.get('GXX', '')`  
by  
```
if 'CONDA_PYTHON_EXE' in os.environ:
    if 'CXX' not in os.environ:
        os.environ['CXX'] = os.environ.get('GXX', '')
```

# Installation

## poetry.lock adjustments

Two of the packages in the poetry lock are not compatible with mac :
- hpp-fcl 2.3.0 : use the 2.3.5 version instead
- pin 2.6.17 : use the 2.6.20 version instead

You can delete those two packages from the poetry lock to be able to use it, and pip install them afterwards.

## install with poetry

`poetry install`  
`poetry shell`  
`cd happypose/pose_estimator/cosypose`  
`python3 setup.py install`  

You might miss  a couple of packages, but you can pip install them afterwards.

If you haven't already, you will need to install libomp using brew :  
`brew install libomp`

# Create data directory

```
Create data dir /somewhere/convenient. The dataset to store are quite large.
export HAPPYPOSE_DATA_DIR=/somewhere/convenient
```

# Configuration for the evaluation

If you plan on evaluating CosyPose and Megapose, you need to modify the following lines in `bop_toolkit_lib/config.py`, replace

```
######## Basic ########


# Folder with the BOP datasets.
if 'BOP_PATH' in os.environ:
  datasets_path = os.environ['BOP_PATH']
else:
  datasets_path = r'/path/to/bop/datasets'

# Folder with pose results to be evaluated.
results_path = r'/path/to/folder/with/results'

# Folder for the calculated pose errors and performance scores.
eval_path = r'/path/to/eval/folder'
```

with

```
######## Basic ########

# Folder with the BOP datasets.
datasets_path = str(os.environ['BOP_DATASETS_PATH'])
results_path = str(os.environ['BOP_RESULTS_PATH'])
eval_path = str(os.environ['BOP_EVAL_PATH'])
```


You can now download the data you need (see pack branch README or doc)
