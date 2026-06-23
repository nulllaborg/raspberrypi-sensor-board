#coding=utf-8
from sensor_expansion_board_i2c import IoExpansionBoardI2c
from smbus2 import SMBus
import time


# 初始化I2C总线
i2c_bus = 1  # 树莓派上的I2C总线号，通常是1
i2c_address = 0x24  # I2C设备地址

# 创建IoExpansionBoardI2c对象
io_expansion_board_i2c = IoExpansionBoardI2c(i2c_bus, i2c_address)

# Set pin mode
io_expansion_board_i2c[0].mode = IoExpansionBoardI2c.OUTPUT_DIGITAL_MODE  # Pin 0 set as digital output mode
io_expansion_board_i2c[1].mode = IoExpansionBoardI2c.INPUT_PULL_UP_MODE   # Pin 1 set as input pull up mode

try:
    while True:
        digital_value = io_expansion_board_i2c[1].value  # reads pin 1 value
        print('digital value:', digital_value)
        io_expansion_board_i2c[0].value = digital_value  # write pin 1 value into pin 0
except KeyboardInterrupt:
    print("The programme has been stopped")