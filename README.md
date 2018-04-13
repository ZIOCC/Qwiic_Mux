# Qwiic_Mux

https://www.smart-prototyping.com/Zio-Qwiic-Mux.html

This board is awesome. It lets you switch between sets of Qwiic device chains that are isolated from one another.

That means that you can use up to eight of an I2C device that has a fixed address. And because this board has eight address option itself, you can actually control many more than that.

The schematic for our Qwiic Mux board is a derivative of the <a href = "https://learn.adafruit.com/adafruit-tca9548a-1-to-8-i2c-multiplexer-breakout/overview">Adafruit TCA9548A 1-to-8 I2C Multiplexer Breakout</a>.

Adafruit also has a <a href = "https://learn.adafruit.com/adafruit-tca9548a-1-to-8-i2c-multiplexer-breakout/wiring-and-test">great little tutorial</a> with some very simple Arduino functions for using it, the most important being:
<pre>
<code>
#define TCAADDR 0x70
void tcaselect(uint8_t i) {
  if (i > 7) return;
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();
}
</code>
</pre>

Just drop that into your sketch and then call <code>tcaselect(x);</code> where x is the port, from 0 to 7, that you want to activate.

And to disable all of the ports (in the case that you're using more than one of these board, and need to prevent an address collision between identical devices connected to each) just call this function with that Qwiic Mux's address (set by soldering closed a combination of the A0, A1, and A2 jumpers on the bottom of the PCB) as the only argument:

<pre><code>
void tcadisable(uint8_t tcaaddress){<br>
  Wire.beginTransmission(tcaaddress);<br>
  Wire.write(0);  // no channel selected<br>
  Wire.endTransmission();<br>
}<br>
</code></pre>

All Zio products are released under the Creative Commons Attribution, Share-Alike License, and in accordance with the principles of the Open Source Hardware Association's OSHW Statement of Principles 1.0 and OSHW Definition 1.0.<br> https://creativecommons.org/licenses/by-sa/4.0/ (English)<br>
https://creativecommons.org/licenses/by-sa/4.0/deed.zh (中文)<br>
https://www.oshwa.org/definition/<br>
https://www.oshwa.org/definition/chinese/ (中文)<br>
