class MUX:

    def __init__(self,i2c,addr):
        self.i2c =i2c
        self.addr =addr

    def enable_mux_port(self, portnumber):
        if portnumber > 7 or portnumber < 0:
            return False
        settings = self.i2c.readfrom(self.addr,1)[0]
        settings |= (1 << portnumber)
        self.i2c.writeto(self.addr,bytearray([settings]))

    def disable_mux_port(self, portnumber):
        if portnumber > 7 or portnumber < 0:
            return False
        settings = self.i2c.readfrom(self.addr,1)[0]
        settings &= ~(1 << portnumber)
        self.i2c.writeto(self.addr, bytearray([settings]))
