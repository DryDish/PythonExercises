FROM jupyter/datascience-notebook:latest

USER jovyan
WORKDIR /home/jovyan

RUN apt update
RUN pip install jupyter-console
RUN pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install --user
