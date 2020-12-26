from flask import Flask, render_template
import os
import markdown

# from flask_restful import Resource, Api

app = Flask(__name__)

@app.route("/")
def home():
    '''
    home page
    '''
    return render_template('main.html')


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

    


if __name__ == '__main__':
    
    print("hello guys")
    app.run(host = '0.0.0.0', port=5000, debug=True)
