import pickle
import json
import numpy as np
__location = None
__data_columns =None
__model=None


def get_estimated_rent(newadd, bedroom, bathrooms, area):
    try:
        loc_index= __data_columns.index(newadd.lower())
    except:
        loc_index= -1

    
    x = np.zeros(len(__data_columns))
    x[0] = bedroom
    x[1] = bathrooms
    x[2] = area
    
    if loc_index >= 0:
      x[loc_index]=1

    return round(__model.predict([x])[0],2)



def load_saved_artifacts():
    print("loading saved artifacts") 
    global  __data_columns
    global __location
    global __model
    
    
    with open("./artifacts/columns.json",'r') as f:
        __data_columns= json.load(f)['data_columns']
        __location = __data_columns[7:]

    with open("./artifacts/model.pickle",'rb') as f:
        __model = pickle.load(f)


def get_location_names():
    return __location


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_rent('Ambegaon Budruk',2,2,2000))