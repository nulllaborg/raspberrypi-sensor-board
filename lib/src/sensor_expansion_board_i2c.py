import struct
from smbus2 import SMBus

class IoExpansionBoardI2c:
    NONE_MODE = 0
    INPUT_PULL_UP_MODE = 1 << 0
    INPUT_PULL_DOWN_MODE = 1 << 1
    INPUT_FLOATING_MODE = 1 << 2
    OUTPUT_DIGITAL_MODE = 1 << 3
    ADC_MODE = 1 << 4
    OUTPUT_PWM_MODE = 1 << 5

    _ADDRESS_VERSION = 0x00
    _ADDRESS_IO_MODE = 0x01
    _ADDRESS_ANALOG_VALUES = 0x10
    _ADDRESS_VOLTAGE_VALUES = 0x20
    _ADDRESS_RATIO_VOLTAGE = 0x30
    _ADDRESS_DIGITAL_VALUES = 0x40
    _ADDRESS_PWM_DUTY = 0x50
    _ADDRESS_PWM_FREQUENCY = 0x60

    class Pin:
        def __init__(self, pin, i2c, i2c_address):
            self._pin = pin
            self._i2c = i2c
            self._i2c_address = i2c_address
            self.mode = IoExpansionBoardI2c.NONE_MODE

        @property
        def mode(self):
            self._i2c.write_byte(self._i2c_address, IoExpansionBoardI2c._ADDRESS_IO_MODE + self._pin)
            return self._i2c.read_byte(self._i2c_address)

        @mode.setter
        def mode(self, value):
            if (value == IoExpansionBoardI2c.OUTPUT_PWM_MODE) and (self._pin != 1 and self._pin != 2):
                raise ValueError("PE{} is unsupported pwm mode".format(self._pin))

            self._i2c.write_i2c_block_data(self._i2c_address, IoExpansionBoardI2c._ADDRESS_IO_MODE + self._pin, [value])

        @property
        def value(self):
            self._i2c.write_byte(self._i2c_address, IoExpansionBoardI2c._ADDRESS_DIGITAL_VALUES + self._pin)
            return self._i2c.read_byte(self._i2c_address)

        @value.setter
        def value(self, value):
            self._i2c.write_i2c_block_data(self._i2c_address, IoExpansionBoardI2c._ADDRESS_DIGITAL_VALUES + self._pin, [value])

        @property
        def adc_value(self):
            self._i2c.write_byte(self._i2c_address, IoExpansionBoardI2c._ADDRESS_ANALOG_VALUES + (self._pin << 1))
            #data = self._i2c.read_i2c_block_data(self._i2c_address, IoExpansionBoardI2c._ADDRESS_ANALOG_VALUES + (self._pin << 1), 2)
            #return struct.unpack("<H", bytes(data))[0]
            return self._i2c.read_word_data(self._i2c_address, IoExpansionBoardI2c._ADDRESS_ANALOG_VALUES + (self._pin << 1))

        @property
        def pwm_duty(self):
            self._i2c.write_byte(self._i2c_address, IoExpansionBoardI2c._ADDRESS_PWM_DUTY + (self._pin << 1))
            data = self._i2c.read_i2c_block_data(self._i2c_address, IoExpansionBoardI2c._ADDRESS_PWM_DUTY + (self._pin << 1), 2)
            return struct.unpack("<H", bytes(data))[0]

        @pwm_duty.setter
        def pwm_duty(self, value):
            data = list(struct.pack("<H", round(value)))
            self._i2c.write_i2c_block_data(self._i2c_address, IoExpansionBoardI2c._ADDRESS_PWM_DUTY + (self._pin << 1), data)

        @property
        def servo_angle(self):
            return round((self.pwm_duty / 4095.0 * 20 - 0.5) * 90)

        @servo_angle.setter
        def servo_angle(self, value):
            self.pwm_duty = ((value / 90) + 0.5) / 20 * 4095

    def __init__(self, i2c_bus, i2c_address=0x24):
        self._i2c = SMBus(i2c_bus)
        self._i2c_address = i2c_address
        self._pins = []
        for i in range(8):
            self._pins.append(IoExpansionBoardI2c.Pin(i, self._i2c, i2c_address))

    def __getitem__(self, pin):
        return self._pins[pin]

    @property
    def pwm_frequency(self):
        self._i2c.write_byte(self._i2c_address, self._ADDRESS_PWM_FREQUENCY)
        data = self._i2c.read_i2c_block_data(self._i2c_address, self._ADDRESS_PWM_FREQUENCY, 2)
        return struct.unpack("<H", bytes(data))[0]

    @pwm_frequency.setter
    def pwm_frequency(self, value):
        data = list(struct.pack("<H", value))
        self._i2c.write_i2c_block_data(self._i2c_address, self._ADDRESS_PWM_FREQUENCY, data)
