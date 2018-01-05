import os

from flask import Flask, render_template, request
from flask import Blueprint

app = Flask(__name__)

@app.route('/info')
def show_info():
  return 'testing'

# Launch server
if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
