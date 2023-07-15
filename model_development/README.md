# How to use

1) Download the [ames dataset](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data). Unzip the contents of the dataset and place them into the data folder.
2) Download Anaconda 
3) Open Anaconda prompt
4) Create an environment for model development
```bash 
conda create -n ames-devel python=3.11
conda activate ames-devel
pip install pip-tools # for installing requirements
```
5) Ensure that model_development is the current working directory
```bash
pip-compile requirements/req.in # get requirements file
pip-sync requirements/req.txt # install requirements
```
6) Ensure that the environment is reflected in jupyterlab
```bash
python -m ipykernel install --user --name ames-devel --display-name "Python (ames-devel)"
```
7) Open jupyterlab to start development / run the notebook
```bash 
jupyter-lab
```