import shelve
import server.home_devices
from server import db_path

def GetDevice(device_identifier):

    db = shelve.open(db_path)
    device = db[device_identifier]
    db.close()

    return device


def SubmitDevice(device):

    if type(device) is 'HomeDeviceController':
        
        db = None

        try:
            db = shelve.open(db_path)
            db[device.identifier] = device
            db.close()

            print(f"{device} successfully written to database")

        except:
            print(f"failed writing {device} to database")

        finally:
            if db != None:
                db.close()


def GetDeviceIdentifiers():
    '''
    return a copy of all unique device identifiers
    '''
    identifiers = None

    try:
        db = shelve.open(db_path)
        identifiers = list(db.keys())
        db.close()

    except:
        print("failed opening database")

    return identifiers

    

    