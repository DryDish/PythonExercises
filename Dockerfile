FROM jupyter/datascience-notebook:latest

USER jovyan
WORKDIR /home/jovyan


RUN pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install --user
