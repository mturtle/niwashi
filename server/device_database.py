import shelve
from server.home_devices import HomeDeviceController
from server import db_path

def GetDevice(device_identifier):

    if device_identifier == None or device_identifier == '':
        return None

    db = shelve.open(db_path)
    device = db[device_identifier]
    db.close()

    return device


def SubmitDevice(device):

    if isinstance(device, HomeDeviceController):
        
        db = None

        try:
            db = shelve.open(db_path)
            db[device.identifier] = device
            db.close()
            return True

        except:
            print(f"failed writing {device} to database")
            return False

        finally:
            if db != None:
                db.close()

        return False


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
        print("failed reading from database", flush=True)

    return identifiers


def GetDevices():
    '''
    return a copy of all device objects
    '''
    devices = []

    try:
        db = shelve.open(db_path)
        devices = list(db.values())
        db.close()

    except:
        print("failed reading from database", flush=True)

    return devices

    

    