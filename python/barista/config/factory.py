#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
from flows.client import Client
from flows.admin import Admin

class Factory:
    def create_instance(self, role):
        if role == "client":
            return Client()
        elif role == "admin":
            return Admin()
        else:
            raise ValueError("Instancia no válida")
