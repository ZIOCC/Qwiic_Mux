#### Usage
When you need to put more than 1 same I2C address device, usually you will need to use two different I2C port from MCU, or you can choose this Multipluxer to solve this I2C address conflict issue.


#### Demo code:
In this demo code, I used two ToF sensors, you can change to other I2C devices for the ToF part. 

```  
from machine import Pin,I2C
import mux
import rfd77402

i2c = I2C(sda=Pin("Y10"), scl=Pin("Y9"), freq =50000)

print(i2c.scan())
mux = mux.MUX(i2c,0x70)
tof = rfd77402.RFD77402(i2c,0x4C)

#ToF initiation
mux.enable_mux_port(0)
tof.begin()
pyb.delay(100)
mux.disable_mux_port(0)
mux.enable_mux_port(1)
tof.begin()
pyb.delay(100)
mux.disable_mux_port(1)

while True:
    mux.enable_mux_port(0)
    tof.takeMeasurement()
    t = tof.getDistance()
    print("tof 0: " + str(t))
    mux.disable_mux_port(0)
    # pyb.delay(50)
    mux.enable_mux_port(1)
    tof.takeMeasurement()
    t = tof.getDistance()
    print("tof 1: " + str(t))
    mux.disable_mux_port(1)
    # pyb.delay(50)

```  

#### Product link:
[Zio Qwiic Mux (8 multiplexed Qwiic I2C Busses)](https://www.smart-prototyping.com/Zio-Qwiic-Mux.html)
[Zio TOF Distance Sensor RFD77402 (Qwiic, 10 to 200cm)](https://www.smart-prototyping.com/Zio-TOF-Distance-Sensor-RFD77402.html)
