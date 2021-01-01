from flask import Flask, render_template, request
import sys, os, markdown, shelve
from . import app, db_path, device_database, home_devices


@app.route("/")
def home():
    '''
    home page
    '''
    
    device_list = device_database.GetDeviceIdentifiers()
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


@app.route("/edit/<device_identifier>")
def edit_device(device_identifier):
    
    print("editing " + device_identifier, flush=True)

    device = device_database.GetDevice(device_identifier)
    return render_template('edit.html', device=device)


@app.route("/devices/<device_identifier>")
def view_device(device_identifier):

    return "viewing " + device_identifier


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
    
