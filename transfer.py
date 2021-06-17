import numpy as np
import serial
import sys


import struct
def calc_crc(string):
    # data = bytearray.fromhex(string)
    data=string
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for i in range(8):
            if ((crc & 1) != 0):
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return hex(((crc & 0xff) << 8) + (crc >> 8))
NUM=0
def output(text,order,unitnum):
    #order 读0 写1
    #text 写入内容
    #unit num操作第几个标签

    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    global NUM


    #结构体的构建
    struct=bytearray(len(text)+10)
    #0
    HEAD=ord(b'{')
    struct[0]=HEAD
    print("head",HEAD)
    #1
    NUM0=NUM // 256
    struct[1]=NUM0
    print("NUM0",NUM0)
    #2
    NUM1=NUM % 256
    struct[2]=NUM1
    print("NUM1",NUM1)
    #3 input
    ORDER=1
    struct[3]=order
    print("ORDER",ORDER)
    #4 input
    unitNUM=unitnum
    struct[4]=unitNUM
    print("unitNUM",unitNUM)
    #5~5+n-1 input
    n=1
    INFORMATION=text
    for each in INFORMATION:
        struct[4+n]=ord(each)
        print("struct[",4+n,"]", ord(each)," ",each)
        n=n+1
    #4+n+0
    long=10+len(INFORMATION)
    long0=long//256
    struct[n+4]=long0
    print(n+4)
    print("long0",long0)
    #4+n+1
    long1=long%256
    struct[n+5]=long1
    print("long1",long1)
    #4+n+2
    CRC = int(calc_crc(struct[0:len(INFORMATION)+6]),16)
    print(CRC)
    CRC0=CRC // 256
    CRC1=CRC % 256
    struct[n+6]=CRC0
    print("CRC0", struct[n+6])
    #4+n+3
    print("CRC1", CRC1)
    struct[n+7]=CRC1
    #4+n+4
    END=ord(b'}')
    struct[n+8]=END
    print("END", END)
    print(struct)
    NUM=NUM+1

    #传递消息
    try:
        ser=serial.Serial("COM3",9600,timeout=10)
        ser.write(struct)
        return "succes"
    except Exception as e:
        return "fail"


print(output("helloworld",1,1))
print(output("hello",1,1))
