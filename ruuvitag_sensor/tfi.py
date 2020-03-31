# Current mac address
# DA:DC:2C:C6:E3:93
from ruuvitag_sensor.ruuvitag import RuuviTag
def getData():
	sensor = RuuviTag('DA:DC:2C:C6:E3:93')
	state = sensor.update()
	state = sensor.state
	return state
while True:
    print(getData())
