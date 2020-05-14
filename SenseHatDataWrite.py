## Libs/Deps ##

from sense_hat import sense_hat
from datetime import datetime

## Logger Settings ##

FILENAME = "logs.csv"
WRITE_FREQUENCY = 50

## Function and Loggers ##

def file_setup("logs.csv"):
    header = =["temp_h","temp_p","humidity","pressure","pitch","roll","yaw","mag_x","mag_y","mag_z","accel_x","accel_y","accel_z","gyro_x","gyro_y","gyro_z","timestamp"]

    with open(filename,"w") as f:
        f.write(",".join(str(value) for value in header)+ "\n")

def log_data():
    output_string = ",".join(str(value) for value in sense_data)
    batch.data.append(output_string)


def get_sense_data():
    
    sense_data=[]

    sense_data.append(sense.get_temperature_from_humidity())
    sense_data.append(sense.get_temperature_from_pressure())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())

    yaw = o["yaw"]
    pitch = o["pitch"]
    roll = o["roll"]
    sense_data.extend([pitch,roll,yaw])
    
    mag = sense.get_compass_raw()
    mag_x = mag["x"]
    mag_y = mag["y"]
    mag_z = mag["z"]
    sense_data.extend([mag_x,mag_y,mag_z])

    acc = sense.get_accelorometer_raw()
    x = acc["x"]
    y = acc["y"]
    z = acc["z"]
    sense_data.extend([x,y,z])

    gyro = sense.get_gyroscope_raw()
    gyro_x = ["x"]
    gyro_y = ["y"]
    gyro_z = ["z"]
    sense_daya.extend([gyro_x,gyro_y,gyro_z])
    
    sense_data.append(datetime.now())

    return sense_data


## Program + writer ##

sense = SenseHat()

batch_data = []

if FILENAME == "":
    filename = "SenseLog-"+str(datetime.now())+".csv"
else:
    filename = FILENAME+"-"+str(datetime.now())+".csv"
file_setup("logs.csv")

while True:
    sense_data = get_sense_data()
    log_data()

    if len(batch_data) >= WRITE_FREQUENCY:
        print("Writing to file...")
        with open(filename,"a") as f:
            for line in batch_data:
                f.write(line + "\n")
            batch_data = []