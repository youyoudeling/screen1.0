from PySide2.QtWidgets import QApplication

"""pixelW,pixel"""
class location():
    x=0;
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y



class screenData:

    #72ppi，一厘米像素为=72/2.54
    #分辨率 单位像素
    pixelW = 1366
    pixelH = 768
    #2560 1600
    #任务栏和label的高度 单位毫米
    taskLabelH=12
    #显示器外部数据 单位毫米
    screenOW=440
    screenOH=265

    #显示器实际显示范围 单位毫米
    screenIW=410
    screenIH=235

    #显示器电路板的总体参数 单位毫米
    leftSkip=16.5
    topSkip=17.6
    rightSkip=9.9
    bottomSkip=26.9

    #感应线圈参数 单位毫米
    coilHorizontalSkip=11.4
    coilVerticalSkip=12.0
    coilWH=30

    #感应单元横向数量和纵向数量
    coilHorizontalNum = 10
    coilVerticalNum = 5

    # def __init__(self):
    #     desktop = QApplication.desktop()
    #     WIDGET = desktop.width()
    #     HEIGHT = desktop.height()
    #     self.pixelW = WIDGET
    #     self.pixelH = HEIGHT
    # 返回每毫米有多少个像素
    def unitWPixel(self):
        return self.pixelW/self.screenIW

    def unitHPixel(self):
        return self.pixelH/self.screenIH

    # 返回每毫米有多少个像素 每个感应单元（包括间隔）的长度和高度
    def unitW(self):
        #print("感应单元的横向长度是" , self.coilWH+self.coilHorizontalSkip)
        return (self.coilWH+self.coilHorizontalSkip)*self.unitWPixel()
    def unitH(self):
        return (self.coilWH+self.coilVerticalSkip)*self.unitHPixel()

    #感应区域开始坐标位置
    def leftSkipP(self):
        #键入任务栏和label的高度12mm
        return self.leftSkip*self.unitWPixel()
    def topSkipP(self):
        return (self.topSkip-self.taskLabelH)*self.unitHPixel()

    #该函数可以输入坐标，然后返回所在标签的位置
    def UnitNum(self,x,y):
        # 这个标签是第numx+1纵
        #print("x",x)
        #print("y",y)

        #边界检测
        print("x",x)
        print("y",y)
        if(x<0):
            x=0
        if(y<0):
            y=0
        numx=(x-self.leftSkip)//self.unitW()
        #print("numx",numx)
        #这个标签是第numy+1行
        numy=(y-self.topSkip)//self.unitH()
        #print("numy",numy)
        return 49-int(numx*5+numy)


# s=screenData()
# print(s.unitW())
# print(s.unitH())
# for j in range(0,10):
#     for i in range(0,5):
#         print("i",i,"j",j,":",s.UnitNum(s.unitW()*j+s.leftSkip+5,s.topSkip+s.unitH()*i+5))
