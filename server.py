from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)


def setup_GPIO():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(16, GPIO.OUT)
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(22, GPIO.OUT)
	stop()

def robot_stop():
	GPIO.output(12, False)
	GPIO.output(16, False)

	GPIO.output(18, False)
	GPIO.output(22, False)

def robot_travel(forward):
	GPIO.output(12, not forward)
	GPIO.output(16, forward)

	GPIO.output(18, not forward)
	GPIO.output(22, forward)

def robot_turn(clockwise):
	GPIO.output(12, not clockwise)
	GPIO.output(16, clockwise)

	GPIO.output(18, clockwise)
	GPIO.output(22, not clockwise)


@app.route("/")
def getPage():
	templateData = {
		'title' : 'HELLO!'
	}
	return render_template('index.html', **templateData)
	
@app.route("/forward", methods=['GET', 'POST'])
def forward():
	robot_travel(True)
	return ('', 204)

@app.route("/backward", methods=['GET', 'POST'])
def backward():
	robot_travel(False)
	return ('', 204)

@app.route("/turnRight", methods=['GET', 'POST'])
def turn_right():
	robot_turn(True)
	return ('', 204)

@app.route("/turnLeft", methods=['GET', 'POST'])
def turn_left():
	robot_turn(False)
	return ('', 204)

@app.route("/stop", methods=['GET', 'POST'])
def stop():
	robot_stop()
	return ('', 204)

try:
	if __name__ == "__main__":
		setup_GPIO()
		app.run(host='0.0.0.0', port=80, debug=True)
finally:
	GPIO.cleanup()