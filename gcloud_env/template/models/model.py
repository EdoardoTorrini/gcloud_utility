import json
from google.cloud import firestore


# TODO: manage if all the command to mode_ref goes on error
class Model(object):

    def __init__(self, collection: str):
        self.db = firestore.Client()
        self.model_ref = self.db.collection(collection)

    def get_data(self, name: str = None) -> list:
        res = self.model_ref.get() if name is None else [ self.model_ref.document(name).get() ]
        return [ { elem.id: elem.to_dict() } for elem in list(res) if elem.to_dict() != None ]
    
    def create_document(self, name: str, **kwargs):
        data, name = { key.lower(): value for key, value in kwargs.items() }, name.lower()
        if len(self.get_data(name)) != 0:
            raise RuntimeError(f"ERROR: document {name} alredy exists")
        self.model_ref.document(name).set(data)

    def modify_document(self, name: str, **kwargs):
        data, name = { key.lower(): value for key, value in kwargs.items() }, name.lower()
        if len(res := self.get_data(name)) == 0:
            raise RuntimeError(f"ERROR: document {name} does not exists")
        self.model_ref.document(name).set({**res[0][name], **data})
        
    def delete_document(self, name: str):
        name = name.lower()
        if len(res := self.get_data(name)) == 0:
            raise RuntimeError(f"ERROR: document {name} does not exists")
        self.model_ref.document(name).delete()
