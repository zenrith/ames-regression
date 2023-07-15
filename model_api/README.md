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
5) The service can also be locally deployed via docker. Install [docker](https://www.docker.com/). Build a docker image
```bash
docker build -t ames-api:latest . # the period here is not a typo!
```
6) Open up the docker dashboard and run the ames-api image to access the API via docker.