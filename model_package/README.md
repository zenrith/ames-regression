# How to use

1) Open Anaconda Prompt
2) Create an environment for model packaging
```bash
conda env update --prune -f environment.yml
conda activate ames-package # enter environment
pip install pip-tools # for manipulating requirement files
```
3) Ensure that model_package is the current working directory
```bash
pip-compile requirements/dev.in && pip-compile requirements/prod.in && pip-compile requirements/tool.in # convert .in to .txt
pip-sync requirements/dev.txt # install environment for developing
```
4) Train model and unit-test code
```bash
tox
```
5) The package has been built and published to pypi, which is how the I managed to import the model in the model_api section