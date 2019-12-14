from flask import Flask, render_template
import datetime, sys
#from gpiozero import LED, MCP3008
from time import sleep
import gpiozero



app = Flask(__name__)

relay = gpiozero.OutputDevice(18, active_high=False, initial_value=False)


@app.route('/')
def index():
  now = datetime.datetime.now()
  timeString = now.strftime("%Y-%m-%d %H:%M:%S")
  templateData = {
      'time': timeString
      }
  return render_template('IDP2.html',  **templateData)

@app.route('/page2.html')
def manual():
    return render_template('page2.html')

@app.route('/page3.html')
def automatic():
    return render_template('page3.html')

@app.route('/page2.hmtml/switchon')
def action():
  relay.on()

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
