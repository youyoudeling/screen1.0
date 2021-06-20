import serial
import sys

import struct
class transfer:
    NUM = 0
    def calc_crc(self,string):
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

    #发送了多少条指令

    def output(self,text,order,unitnum):
        #order 写0 读1
        #text 写入内容
        #unit num操作第几个标签,从0开始

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

        print("第",self.NUM,"条指令","  UnitNum ",unitnum,"  order ",order," text",text )

        #结构体的构建
        struct=bytearray(len(text)+13)
        #0
        HEAD=ord(b'{')
        struct[0]=HEAD
        #print("head",HEAD)
        #1
        NUM0=self.NUM % 256
        struct[1]=NUM0
        #print("NUM0",NUM0)
        #2
        NUM1=self.NUM // 256
        struct[2]=NUM1
        #print("NUM1",NUM1)
        #3 input
        ORDER=0
        struct[3]=order
        #print("ORDER",ORDER)
        #4 input
        unitNUM=unitnum
        struct[4]=unitNUM
        #print("unitNUM",unitNUM)
        #message string len
        struct[5] = len(text) % 256
        struct[6] = len(text) // 256
        #7~7+n-1 input
        n=1
        INFORMATION=text
        #print("info",INFORMATION)
        for each in INFORMATION:
            #print(each)
            #这里不能有汉字，因为汉字的ascii码不是（0，255）
            struct[6+n]=ord(each)
            #print("struct[",6+n,"]", ord(each)," ",each)
            n=n+1
        CRC = int(self.calc_crc(struct[1:len(INFORMATION)+6]),16)
        #print(CRC)
        #3 CRC
        struct[n+7]=CRC % 256
        struct[n+8]=CRC // 256
        #3 END
        struct[n+9] = ord(b'}')
        #3 STM32 require
        struct[n+10] = ord(b'\r')
        struct[n+11] = ord(b'\n')
        print(struct)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        self.NUM = self.NUM + 1
        #传递消息
        try:
            ser=serial.Serial("COM3",460800,timeout=10)
            ser.write(struct)

            return "succes"
        except Exception as e:
            return "fail"

# for each in range(0,49):
#     if each ==28 or each==29:
#         continue
#
#     output("xcx:helloworld",0,5)
#print(output("xcx:hello",1,1))
