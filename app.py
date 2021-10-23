from flask import Flask
from flask import request
from flask import render_template
import os
sample = Flask(__name__)
@sample.route("/")
def main():
	return "you are calling me from "+os.uname()[1] +"\n"
if __name__ == "__main__":
	sample.run(host="0.0.0.0", port=8080)
