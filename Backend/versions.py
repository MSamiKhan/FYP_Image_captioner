import importlib.metadata
import torch
import PIL
import flask_cors
import flask
import transformers

#print(importlib.metadata.version('flask'))

modules = [flask, torch, PIL, flask_cors, transformers]

for lib in modules:
    print(f"{lib.__name__}=={lib.__version__}")
