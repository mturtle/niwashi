# from flask import Flask
# import markdown
# import os

# # create a flask instance
# app = Flask(__name__)

# @app.route("/")
# def index() :
#     """present docs"""

#     # open the readme file
#     with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

#         # read the content
#         content = markdown_file.read()

#         return markdown.markdown(content)