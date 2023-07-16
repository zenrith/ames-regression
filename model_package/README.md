# How to use

1) Download the [ames dataset](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data). Unzip the contents of the dataset and place them into the data folder.
2) Open Anaconda Prompt
3) Create an environment for model packaging
```bash
conda env update --prune -f environment.yml
conda activate ames-package # enter environment
pip install pip-tools # for manipulating requirement files
```
4) Ensure that model_package is the current working directory
```bash
pip-compile requirements/dev.in && pip-compile requirements/prod.in && pip-compile requirements/tool.in # convert .in to .txt
pip-sync requirements/dev.txt # install environment for developing
```
5) Train model and unit-test code
```bash
tox
```
6) The package has been built and published to pypi, which is how the I managed to import the model in the model_api section