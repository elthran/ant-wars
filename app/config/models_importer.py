import inspect
import os
from importlib import import_module

"""
Get a list of all models used in the app.
"""
all_models = {}


def dynamically_import_all_models_into_namespace(namespace=None):

    if namespace is None:
        namespace = {}

    files = os.listdir('app/models')

    for name in files:
        if name.endswith('.py') and name != '__init__.py':
            module_name = name[:-3]
            module = import_module(f'app.models.{module_name}')
            for member in inspect.getmembers(module, inspect.isclass):
                class_name = member[0]
                class_ = member[1]
                module_name = class_.__module__
                if module_name.startswith('app.models'):
                    namespace[class_name] = class_
    return namespace


dynamically_import_all_models_into_namespace(all_models)

