from flask import Flask, render_template, request
import sys, os, markdown
from server import app

@app.route("/")
def home():
    '''
    home page
    '''
    return render_template("devices.html")


@app.route("/help")
def help():
    '''
    main help page - display readme
    '''
    path = os.path.dirname(app.root_path) + '/README.md'
    path = './README.md'
    print("readme path: " + path)

    with open(path, 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


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
        
        return render_template('add.html')

    else:
        print("adding new device...", flush=True)
        return render_template('add.html')
    
