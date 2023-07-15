# How to use

1) Open Anaconda Prompt
2) Create an environment for model api
```bash
conda env update --prune -f environment.yml
conda activate ames-api # enter environment
pip install pip-tools # for manipulating requirement files
```
3) Ensure that model_package is the current working directory
```bash
pip-compile requirements/req.in && pip-compile requirements/tool.in # convert .in to .txt
pip-sync requirements/req.txt # install environment for developing
```
4) Train model and unit-test code
```bash
tox
```