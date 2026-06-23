#coding=utf-8
from sensor_expansion_board_i2c import IoExpansionBoardI2c
from smbus2 import SMBus
import time

# 初始化I2C总线
i2c_bus = 1  # 树莓派上的I2C总线号，通常是1
i2c_address = 0x24  # I2C设备地址

# 创建IoExpansionBoardI2c对象
io_expansion_board_i2c = IoExpansionBoardI2c(i2c_bus, i2c_address)

# 设置所有引脚为ADC模式
for i in range(8):
    io_expansion_board_i2c[i].mode = IoExpansionBoardI2c.ADC_MODE

# 循环读取ADC值
try:
    while True:
        print('A0:',io_expansion_board_i2c[0].adc_value) 
        print('A1:',io_expansion_board_i2c[1].adc_value) 
        print('A2:',io_expansion_board_i2c[2].adc_value) 
        print('A3:',io_expansion_board_i2c[3].adc_value)
        print('A4:',io_expansion_board_i2c[4].adc_value)
        print('A5:',io_expansion_board_i2c[5].adc_value) 
        print('A6:',io_expansion_board_i2c[6].adc_value) 
        print('A7:',io_expansion_board_i2c[7].adc_value)
        time.sleep(1)  # 延时1秒
except KeyboardInterrupt:
    # print("程序已停止")
    pass

