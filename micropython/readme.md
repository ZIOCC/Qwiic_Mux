#### Usage
This library can control up to 4 DC motors by I2C interface. The I2C usually can't support big current for motors, so please use extenal power for the driver board.



#### Demo code:
The following demo code will slowly speed up the motor, everytime the motor will go forward first, then go back.
```  
from machine import Pin,I2C
import qwiic_motor


i2c = I2C(sda=Pin("Y10"), scl=Pin("Y9"))
print(i2c.scan())

mt = qwiic_motor.DCMOTOR(i2c=i2c, addr=0x40, freq=1000)
pyb.delay(1000)

while True:

    for i in range(0,100):
        mt.go_ahead(0)
        mt.speed(0,i)
        print("cw speed:" + str(i))
        pyb.delay(1000)
        mt.go_back(0)
        mt.speed(0,i)
        print("ccw speed:" + str(i))
        pyb.delay(1000)
    mt.stop(0)
    pyb.delay(1000)

```  

#### Note:
1. go_ahead() will not make the motor move, it just sets a direction, you need to use speed() method to add speed.
2. When the speed is close to 0, ususally the motor will not move.
3. Motor name on the board and relavent number.
Motor Name | Motor NO. |
 ---- | -----
A101  | 0
B101  | 1
A201|2
b201|3

#### Product link:
[Qwiic DC motor driver board](https://www.smart-prototyping.com/Zio-4-DC-Motor-Controller.html)
