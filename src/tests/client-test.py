import sys
sys.path.insert(0, 'src/app/models')
from client import Client

def test_client_instantiate():
    
    client = Client(
        name = 'test', 
        age = 99, 
        objects = ['test1', 'test2']
    )
    
    del client
    
def test_dict_info():
    
    client = Client(
        id = 'hex32',
        name = 'test', 
        age = 99, 
        objects = ['test1', 'test2']
    )
    
    client_dict = client.to_dict()
        
    assert client_dict == {
        'id': 'hex32',
        'name': 'test',
        'age': 99,
        'objects': ['test1', 'test2']
    }
