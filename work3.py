

class WLW(object):
    def __init__(self):
        self.flag = 0  # 记录差动双相的值
        self.SumLength = 0
        self.out = [0, 1, 2, 3, 4, 5, 6]
        self.SumOut = [0, 1, 2, 3, 4, 5, 6]
        self.str = '10101'
        self.Sumflag = int(self.str)
        self.A = [0, 1, 2, 3, 4, 5, 6]  # 竖
        self.B = [0, 1, 2, 3, 4, 5, 6]  # 下横
        self.C = [0, 1, 2, 3, 4, 5, 6]  # 上横
        self.A[6] = self.A[0] = '0'
        self.A[5] = self.A[4] = self.A[3] = self.A[2] = self.A[1] = '11'
        self.B[6] = self.B[4] = self.B[3] = self.B[2] = self.B[1] = self.B[0] = '0  0  0  0'
        self.B[5] = '11 11 11 11'
        self.C[1] = '11 11 11 11'
        self.C[6] = self.C[5] = self.C[4] = self.C[3] = self.C[2] = self.C[0] = '0  0  0  0'
        #print(self.B, '\n')

    def NRZmerge1(self, str):
        self.length = 0
        self.str = str
        #print('\nhhhhh', self.str[1])
        self.Sumflag = int(self.str)
        self.SumOut = self.C
        firstLen = [0, 1, 2, 3, 4, 5, 6]
        #print('The length of str is: ', len(self.str))
        # 第一个图像单独拿出来
        if self.str[0] == '1':
            self.SumOut = self.C
        else:
            self.SumOut = self.B
        self.SumLength = 4
        # for i in range(0, 7):
        #     self.SumOut[i] = self.out[i]
        for i in range(1, len(self.str)):
            # 防止重复拼接
            self.out, self.length = CJW.NRZmerge2(
                int(self.str[i - 1]), int(self.str[i]))
            #print('\nhhhhh', self.str[i - 1], self.str[i])
            self.SumLength = self.SumLength + self.length

            for i in range(0, 7):
                self.SumOut[i] = self.SumOut[i] + ' ' + self.out[i]
            print('\nhhhhh', self.SumLength)
        return(self.SumOut, self.SumLength)

    def NRZmerge2(self, P_last, P_now):

        self.A = [0, 1, 2, 3, 4, 5, 6]  # 竖
        self.B = [0, 1, 2, 3, 4, 5, 6]  # 下横
        self.C = [0, 1, 2, 3, 4, 5, 6]  # 上横
        self.A[6] = self.A[0] = '0'
        self.A[5] = self.A[4] = self.A[3] = self.A[2] = self.A[1] = '11'
        self.B[6] = self.B[4] = self.B[3] = self.B[2] = self.B[1] = self.B[0] = '0  0  0  0'
        self.B[5] = '11 11 11 11'
        self.C[1] = '11 11 11 11'
        self.C[6] = self.C[5] = self.C[4] = self.C[3] = self.C[2] = self.C[0] = '0  0  0  0'
        # Forward and Back merge
        self.P_now = P_now
        self.P_last = P_last
        # print(self.A, '\n')
        # print(self.B, '\n')
        # print(self.C, '\n')
        if (P_now == P_last):
            if P_now == 0:
                for i in range(0, 7):
                    self.out[i] = ' ' + self.B[i]
            if P_now == 1:
                for i in range(0, 7):
                    self.out[i] = ' ' + self.C[i]
            self.length = 4
        else:
            if P_now == 0:
                for i in range(0, 7):
                    self.out[i] = self.A[i] + ' ' + self.B[i]
            else:
                for i in range(0, 7):
                    self.out[i] = self.A[i] + ' ' + self.C[i]
            self.length = 5
            print('\nhhhhh', self.B)
        #print(self.out, '\n', self.length, '\n')
        return(self.out, self.length)

    def MANmerge1(self, str):

        self.A = [0, 1, 2, 3, 4, 5, 6]  # 竖
        self.B = [0, 1, 2, 3, 4, 5, 6]  # 下横
        self.C = [0, 1, 2, 3, 4, 5, 6]  # 上横
        self.A[6] = self.A[0] = '0'
        self.A[5] = self.A[4] = self.A[3] = self.A[2] = self.A[1] = '11'
        self.B[6] = self.B[4] = self.B[3] = self.B[2] = self.B[1] = self.B[0] = '0  0 '
        self.B[5] = '11 11'
        self.C[1] = '11 11'
        self.C[6] = self.C[5] = self.C[4] = self.C[3] = self.C[2] = self.C[0] = '0  0 '
        self.length = 0
        self.str = str
        self.Sumflag = int(self.str)

        #firstLen = [0, 1, 2, 3, 4, 5, 6]
        #print('The length of str is: ', len(self.str))
        # 第一个图像单独拿出来
        if self.str[0] == '1':
            self.SumOut = self.C
        else:
            self.SumOut = self.B

        for i in range(0, 7):
            self.SumOut[i] = self.SumOut[i] + ' ' + self.A[i]

        self.SumLength = 3
        # for i in range(0, 7):
        #     self.SumOut[i] = self.out[i]
        for i in range(1, len(self.str)):
            # 防止重复拼接
            self.out, self.length = CJW.MANmerge2(
                int(self.str[i - 1]), int(self.str[i]))
            #print('\nhhhhh', self.str[i - 1], self.str[i])
            self.SumLength = self.SumLength + self.length

            for i in range(0, 7):
                self.SumOut[i] = self.SumOut[i] + ' ' + self.out[i]
        return(self.SumOut, self.SumLength)

    def MANmerge2(self, P_last, P_now):

        self.A = [0, 1, 2, 3, 4, 5, 6]  # 竖
        self.B = [0, 1, 2, 3, 4, 5, 6]  # 下横
        self.C = [0, 1, 2, 3, 4, 5, 6]  # 上横
        self.A[6] = self.A[0] = '0'
        self.A[5] = self.A[4] = self.A[3] = self.A[2] = self.A[1] = '11'
        self.B[6] = self.B[4] = self.B[3] = self.B[2] = self.B[1] = self.B[0] = '0  0 '
        self.B[5] = '11 11'
        self.C[1] = '11 11'
        self.C[6] = self.C[5] = self.C[4] = self.C[3] = self.C[2] = self.C[0] = '0  0 '

        if (P_now == P_last):
            if P_now == 0:
                for i in range(0, 7):
                    self.out[i] = ' ' + self.C[i] + ' ' + \
                        self.A[i] + ' ' + self.B[i] + ' ' + self.A[i]
            if P_now == 1:
                for i in range(0, 7):
                    self.out[i] = ' ' + self.B[i] + ' ' + \
                        self.A[i] + ' ' + self.C[i] + ' ' + self.A[i]
            self.length = 6
        else:
            if P_now == 0:
                for i in range(0, 7):
                    self.out[i] = ' ' + self.B[i] + \
                        ' ' + self.B[i] + ' ' + self.A[i]
            else:
                for i in range(0, 7):
                    self.out[i] = ' ' + self.C[i] + \
                        ' ' + self.C[i] + ' ' + self.A[i]
            self.length = 5
        #print(self.out, '\n', self.length, '\n')
        return(self.out, self.length)

    def DBPmerge1(self, str):
        self.flag = 0
        self.length = 0
        self.str = str
        self.Sumflag = int(self.str)
        #print('The length of str is: ', len(self.str))
        # 第一个图像单独拿出来
        self.C[1] = '11 11'
        self.C[6] = self.C[5] = self.C[4] = self.C[3] = self.C[2] = self.C[0] = '0  0'
        self.B[6] = self.B[4] = self.B[3] = self.B[2] = self.B[1] = self.B[0] = '0  0'
        self.B[5] = '11 11'
        self.SumOut = self.C
        if self.str[0] == '1':
            for i in range(0, 7):
                self.SumOut[i] = self.SumOut[i] + ' ' + self.C[i]
            self.SumLength = 4
            self.flag = 0
        else:
            for i in range(0, 7):
                self.SumOut[i] = self.SumOut[i] + \
                    ' ' + self.A[i] + ' ' + self.B[i]
            self.SumLength = 5
            self.flag = 1

        # for i in range(0, 7):
        #     self.SumOut[i] = self.out[i]
        for i in range(1, len(self.str)):
            # 防止重复拼接
            self.out, self.length, self.flag = CJW.DBPmerge2(
                self.flag, int(self.str[i - 1]), int(self.str[i]))
            #print('\nhhhhh', self.str[i - 1], self.str[i])
            self.SumLength = self.SumLength + self.length

            for i in range(0, 7):
                self.SumOut[i] = self.SumOut[i] + ' ' + self.out[i]
        return(self.SumOut, self.SumLength)

    def DBPmerge2(self, flag, P_last, P_now):

        self.A = [0, 1, 2, 3, 4, 5, 6]  # 竖
        self.B = [0, 1, 2, 3, 4, 5, 6]  # 下横
        self.C = [0, 1, 2, 3, 4, 5, 6]  # 上横
        self.A[6] = self.A[0] = '0'
        self.A[5] = self.A[4] = self.A[3] = self.A[2] = self.A[1] = '11'
        self.B[6] = self.B[4] = self.B[3] = self.B[2] = self.B[1] = self.B[0] = '0  0 '
        self.B[5] = '11 11'
        self.C[1] = '11 11'
        self.C[6] = self.C[5] = self.C[4] = self.C[3] = self.C[2] = self.C[0] = '0  0 '
        # Forward and Back merge
        # if P_now == P_last:
        #     flag = ~flag

        if P_now == 1:
            if flag == 1:
                for i in range(0, 7):
                    self.out[i] = ' ' + self.A[i] + \
                        ' ' + self.C[i] + ' ' + self.C[i]
                flag = 0
            else:
                for i in range(0, 7):
                    self.out[i] = ' ' + self.A[i] + \
                        ' ' + self.B[i] + ' ' + self.B[i]
                flag = 1
            self.length = 5
        else:
            if flag == 1:
                for i in range(0, 7):
                    self.out[i] = ' ' + self.A[i] + ' ' + \
                        self.C[i] + ' ' + self.A[i] + ' ' + self.B[i]
                flag = 1
            else:
                for i in range(0, 7):
                    self.out[i] = ' ' + self.A[i] + ' ' + \
                        self.B[i] + ' ' + self.A[i] + ' ' + self.C[i]
                flag = 0
            self.length = 6
        return(self.out, self.length, flag)

    def PIEmerge1(self, str):
        self.A = [0, 1, 2, 3, 4, 5, 6]  # 竖
        self.B = [0, 1, 2, 3, 4, 5, 6]  # 下横
        self.C = [0, 1, 2, 3, 4, 5, 6]  # 上横
        self.A[6] = self.A[0] = '0'
        self.A[5] = self.A[4] = self.A[3] = self.A[2] = self.A[1] = '11'
        self.B[6] = self.B[4] = self.B[3] = self.B[2] = self.B[1] = self.B[0] = '0  0 '
        self.B[5] = '11 11'
        self.C[1] = '11 11'
        self.C[6] = self.C[5] = self.C[4] = self.C[3] = self.C[2] = self.C[0] = '0  0 '
        SOF = [0, 1, 2, 3, 4, 5, 6]  # SOF
        EOF = [0, 1, 2, 3, 4, 5, 6]  # EOF
        self.length = 0
        self.str = str
        self.Sumflag = int(self.str)
        for i in range(0, 7):
            SOF[i] = self.A[i] + ' ' + self.B[i] + ' ' + self.A[i] + \
                ' ' + self.C[i] + ' ' + self.A[i] + ' ' + self.B[i] + \
                ' ' + self.A[i] + ' ' + self.C[i] + ' ' + self.C[i] + \
                ' ' + self.C[i] + ' ' + self.C[i] + \
                ' ' + self.C[i] + ' ' + self.A[i]
            EOF[i] = self.B[i] + ' ' + self.A[i] +\
                ' ' + self.C[i] + ' ' + self.C[i] + ' ' + self.C[i] + ' ' + self.C[i] +\
                ' ' + self.C[i] + ' ' + self.C[i] + ' ' + self.C[i]
        #firstLen = [0, 1, 2, 3, 4, 5, 6]
        #print('The length of str is: ', len(self.str))
        # 第一个图像单独拿出来
        self.SumOut = SOF
        self.SumLength = 21
        # for i in range(0, 7):
        #     self.SumOut[i] = self.out[i]
        for i in range(0, len(self.str)):
            # 防止重复拼接
            self.out, self.length = CJW.PIEmerge2(int(self.str[i]))
            self.SumLength = self.SumLength + self.length
            for i in range(0, 7):
                self.SumOut[i] = self.SumOut[i] + ' ' + self.out[i]

        for i in range(0, 7):
            self.SumOut[i] = self.SumOut[i] + ' ' + EOF[i]
        return(self.SumOut, self.SumLength + 17)

    def PIEmerge2(self, P_now):

        self.A = [0, 1, 2, 3, 4, 5, 6]  # 竖
        self.B = [0, 1, 2, 3, 4, 5, 6]  # 下横
        self.C = [0, 1, 2, 3, 4, 5, 6]  # 上横
        HIGH = [0, 1, 2, 3, 4, 5, 6]  # 1
        LOW = [0, 1, 2, 3, 4, 5, 6]  # 0
        self.A[6] = self.A[0] = '0'
        self.A[5] = self.A[4] = self.A[3] = self.A[2] = self.A[1] = '11'
        self.B[6] = self.B[4] = self.B[3] = self.B[2] = self.B[1] = self.B[0] = '0  0 '
        self.B[5] = '11 11'
        self.C[1] = '11 11'
        self.C[6] = self.C[5] = self.C[4] = self.C[3] = self.C[2] = self.C[0] = '0  0 '

        for i in range(0, 7):
            HIGH[i] = self.B[i] + ' ' + self.A[i] + ' ' + self.C[i] + \
                ' ' + self.C[i] + ' ' + self.C[i] + ' ' + self.A[i]
            LOW[i] = self.B[i] + ' ' + self.A[i] + \
                ' ' + self.C[i] + ' ' + self.A[i]
        print(LOW)
        if P_now == 0:
            for i in range(0, 7):
                self.out[i] = ' ' + LOW[i]
            self.length = 6
        if P_now == 1:
            for i in range(0, 7):
                self.out[i] = ' ' + HIGH[i]
            self.length = 10
        return(self.out, self.length)

    def writeNRZ(self, inputNum):
        self.inputNum = inputNum
        OutText, Sumflag = CJW.NRZmerge1(self.inputNum)
        OutText = str(OutText)
        # 写入前的细节修改
        newText = OutText.replace('\'', '')
        newText = newText.replace('[', '')
        newText = newText.replace(']', '')
        newText = newText.replace(',', '\n')
        # print(OutText)
        self.Sumflag = '\n' + str(Sumflag) + ' ' + '7' + '\n' + '15'
        f = open('NRZ.pgm', 'a')
        f.write('P2')
        f.write(self.Sumflag)
        f.write('\n' + str(newText))
        f.close()

    def writeMAN(self, inputNum):
        self.inputNum = inputNum
        OutText, Sumflag = CJW.MANmerge1(self.inputNum)
        OutText = str(OutText)
        # 写入前的细节修改
        newText = OutText.replace('\'', '')
        newText = newText.replace('[', '')
        newText = newText.replace(']', '')
        newText = newText.replace(',', '\n')
        # print(OutText)
        self.Sumflag = '\n' + str(Sumflag) + ' ' + '7' + '\n' + '15'
        f = open('MAN.pgm', 'a')
        f.write('P2')
        f.write(self.Sumflag)
        f.write('\n' + str(newText))
        f.close()

    def writeDBP(self, inputNum):
        self.inputNum = inputNum
        OutText, Sumflag = CJW.DBPmerge1(self.inputNum)
        OutText = str(OutText)
        # 写入前的细节修改
        newText = OutText.replace('\'', '')
        newText = newText.replace('[', '')
        newText = newText.replace(']', '')
        newText = newText.replace(',', '\n')
        # print(OutText)
        self.Sumflag = '\n' + str(Sumflag) + ' ' + '7' + '\n' + '15'
        f = open('DBP.pgm', 'a')
        f.write('P2')
        f.write(self.Sumflag)
        f.write('\n' + str(newText))
        f.close()

    def writePIE(self, inputNum):
        self.inputNum = inputNum
        OutText, Sumflag = CJW.PIEmerge1(self.inputNum)
        OutText = str(OutText)
        # 写入前的细节修改
        newText = OutText.replace('\'', '')
        newText = newText.replace('[', '')
        newText = newText.replace(']', '')
        newText = newText.replace(',', '\n')
        # print(OutText)
        self.Sumflag = '\n' + str(Sumflag) + ' ' + '7' + '\n' + '15'
        f = open('PIE.pgm', 'a')
        f.write('P2')
        f.write(self.Sumflag)
        f.write('\n' + str(newText))
        f.close()

    def ReadPgm(self):
        import cv2
        img1 = cv2.imread("NRZ.pgm")
        img2 = cv2.imread("MAN.pgm")
        img3 = cv2.imread("DBP.pgm")
        img4 = cv2.imread("PIE.pgm")
        # 插值放大
        res1 = cv2.resize(img1, (1080, 320), interpolation=cv2.INTER_NEAREST)
        res2 = cv2.resize(img2, (1080, 320), interpolation=cv2.INTER_NEAREST)
        res3 = cv2.resize(img3, (1080, 320), interpolation=cv2.INTER_NEAREST)
        res4 = cv2.resize(img4, (1080, 320), interpolation=cv2.INTER_NEAREST)

        cv2.namedWindow("NRZ")
        cv2.imshow("NRZ", res1)
        cv2.namedWindow("MAN")
        cv2.imshow("MAN", res2)
        cv2.namedWindow("DBP")
        cv2.imshow("DBP", res3)
        cv2.namedWindow("PIE")
        cv2.imshow("PIE", res4)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def write(self, inputNum):
        CJW.writeNRZ(inputNum)
        CJW.writeMAN(inputNum)
        CJW.writeDBP(inputNum)
        CJW.writePIE(inputNum)


if __name__ == '__main__':
    inputNum = '101'
    CJW = WLW()
    CJW.write(inputNum)
    CJW.ReadPgm()
