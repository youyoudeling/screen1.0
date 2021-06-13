"""pixelW,pixel"""
class screenData:


    #72ppi，一厘米像素为=72/2.54
    #分辨率 单位像素
    pixelW = 1366
    pixelH = 768

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


# 返回每毫米有多少个像素
    def unitWPixel(self):
        return self.pixelW/self.screenIW

    def unitHPixel(self):
        return self.pixelH/self.screenIH

    # 返回每毫米有多少个像素 每个感应单元（包括间隔）的长度和高度
    def unitW(self):
        print("感应单元的横向长度是" , self.coilWH+self.coilHorizontalSkip)
        return (self.coilWH+self.coilHorizontalSkip)*self.unitWPixel()
    def unitH(self):
        return (self.coilWH+self.coilVerticalSkip)*self.unitHPixel()

    #感应区域开始坐标位置
    def leftSkipP(self):
        #键入任务栏和label的高度12mm
        return self.leftSkip*self.unitWPixel()
    def topSkipP(self):
        return (self.topSkip-self.taskLabelH)*self.unitHPixel()


s=screenData()
print(s.unitW())
print(s.unitH())