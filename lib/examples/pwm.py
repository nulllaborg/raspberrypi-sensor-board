#coding=utf-8
from sensor_expansion_board_i2c import IoExpansionBoardI2c
import time

# 初始化I2C总线
i2c_bus = 1  # 树莓派上的I2C总线号，通常是1
i2c_address = 0x24  # I2C设备地址

# 创建IoExpansionBoardI2c对象
io_expansion_board_i2c = IoExpansionBoardI2c(i2c_bus, i2c_address)

io_expansion_board_i2c.pwm_frequency = 1000 # Setting PWM frequency

# Setting pin mode as PWM output mode
io_expansion_board_i2c[1].mode = IoExpansionBoardI2c.OUTPUT_PWM_MODE
io_expansion_board_i2c[2].mode = IoExpansionBoardI2c.OUTPUT_PWM_MODE

print('only A1 A2 support pwm output')

try:
    while True:
        io_expansion_board_i2c[1].pwm_duty = 100  # Setting the PWM duty ratio of pin 1 as 100
        io_expansion_board_i2c[2].pwm_duty = 1023  # Setting the PWM duty ratio of pin 2 as 1023
        print('A1 pwm_duty:', io_expansion_board_i2c[1].pwm_duty, 'A2 pwm_duty:', io_expansion_board_i2c[2].pwm_duty)
        time.sleep(1)
        io_expansion_board_i2c[1].pwm_duty = 2048  # Setting the PWM duty ratio of pin 1 as 2048
        io_expansion_board_i2c[2].pwm_duty = 4096  # Setting the PWM duty ratio of pin 2 as 1023
        print('A1 pwm_duty:', io_expansion_board_i2c[1].pwm_duty, 'A2 pwm_duty:', io_expansion_board_i2c[2].pwm_duty)
        time.sleep(1)
except KeyboardInterrupt:
    print("The programme has been stopped")