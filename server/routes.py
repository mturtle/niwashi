from flask import Flask, render_template, request, url_for, redirect
import sys, os, markdown, shelve
from . import app, db_path, device_database, home_devices


@app.route("/")
def home():
    '''
    home page
    '''
    
    device_list = device_database.GetDeviceIdentifiers()
    device_list = device_database.GetDevices()
    print(device_list, flush=True)

    return render_template("devices.html", device_list=device_list)


@app.route("/help")
def help():
    '''
    main help page - display readme
    '''
    path = os.path.dirname(app.root_path) + '/README.md'
    path = './README.md'

    with open(path, 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


@app.route("/edit", methods=['POST', 'GET'])
@app.route("/edit/<device_identifier>")
def edit_device(device_identifier=None):
    
    if request.method == 'POST':
        print("posting device", flush=True)
        
        #submit new device to database
        device = home_devices.HomeDeviceController(request.form["deviceName"])
        device.network_address = request.form["networkAddress"]
        device.mac_address = request.form["macAddress"]
        device.description = request.form["description"]

        #buid input/outputs from form
        in_names = request.form.getlist("inputName")
        in_types = request.form.getlist("inputType")

        for i in range(len(in_names)):
            device.inputs.append(home_devices.DeviceIO(in_names[i], in_types[i]))
        
        out_names = request.form.getlist("outputName")
        out_types = request.form.getlist("outputType")

        for idx in range(len(out_names)):
            device.outputs.append(home_devices.DeviceIO(out_names[idx], out_types[idx]))

        if device_database.SubmitDevice(device):
            print(f"successfully submitted {device}")

        return redirect(url_for('home'))

    # get edit device page
    else:
        device = device_database.GetDevice(device_identifier)

        if device == None:
            device = home_devices.HomeDeviceController("new device")
            print("configuring new device", flush=True)

        else:  
            print(f"editing: {device}", flush=True)

        return render_template('edit.html', device=device)
        


@app.route("/devices/<device_identifier>")
def view_device(device_identifier):

    return f"viewing: {device_identifier}"


@app.route("/add",methods=['POST', 'GET'])
def add_device():
    '''
    add new home device - manual entry vs preferred automatic device registration
    '''
    print(f"request: {request} method: {request.method}", flush=True)

    if request.method == 'POST':
        print("posting device: ", flush=True)
        print (request.form['name'], flush=True)
        print (request.form.keys, flush=True)

        try:
            with shelve.open(db_path) as db:
                db[request.form['name']] = home_devices.HomeDeviceController(request.form['name'])
                db.close()

        except:
            print("failed writing to database", flush=True)

        
        return render_template('add.html')

    else:
        print("adding new device...", flush=True)
        return render_template('add.html')
    
