"""
    Initialize databackend of poc_app
"""


model_backend = 'mongodb'

if model_backend == 'mongodb':
    from .model_mongodb import model
else:
    raise ValueError("No appropriate database model configured. ")


appmodel = model()


def get_model():
    return appmodel
