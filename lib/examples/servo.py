#coding=utf-8
from sensor_expansion_board_i2c import IoExpansionBoardI2c
import time

# 初始化I2C总线
i2c_bus = 1  # 树莓派上的I2C总线号，通常是1
i2c_address = 0x24  # I2C设备地址

# 创建IoExpansionBoardI2c对象
io_expansion_board_i2c = IoExpansionBoardI2c(i2c_bus, i2c_address)

io_expansion_board_i2c.pwm_frequency = 50 # Setting PWM frequency as 50Hz

# Setting pin mode as PWM output mode
io_expansion_board_i2c[1].mode = IoExpansionBoardI2c.OUTPUT_PWM_MODE
io_expansion_board_i2c[2].mode = IoExpansionBoardI2c.OUTPUT_PWM_MODE

try:
    while True:
        io_expansion_board_i2c[1].servo_angle = 0
        io_expansion_board_i2c[2].servo_angle = 90
        print('angle:', io_expansion_board_i2c[1].servo_angle, ",",
              io_expansion_board_i2c[2].servo_angle)
        time.sleep(1)

        io_expansion_board_i2c[1].servo_angle = 90
        io_expansion_board_i2c[2].servo_angle = 0
        print('angle:', io_expansion_board_i2c[1].servo_angle, ",",
              io_expansion_board_i2c[2].servo_angle)
        time.sleep(1)

        io_expansion_board_i2c[1].servo_angle = 180
        io_expansion_board_i2c[2].servo_angle = 180
        print('angle:', io_expansion_board_i2c[1].servo_angle, ",",
              io_expansion_board_i2c[2].servo_angle)
        time.sleep(1)

        io_expansion_board_i2c[1].servo_angle = 90
        io_expansion_board_i2c[2].servo_angle = 90
        print('angle:', io_expansion_board_i2c[1].servo_angle, ",",
              io_expansion_board_i2c[2].servo_angle)
        time.sleep(1)
except KeyboardInterrupt:
    print("The programme has been stopped")
