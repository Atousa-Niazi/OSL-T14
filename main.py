from PySide6.QtWidgets import*
from PySide6.QtGui import*
from PySide6.QtCore import*
from PySide6.QtUiTools import QUiLoader
from math import *
from functools import partial
import sys


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader ()
        self.ui = loader.load('design.ui')
        self.ui.show()
        
        #self.op=0 for symbol
        #self.op_type=0 #type for number of needed operators

        self.ui.btn_0.clicked.connect(partial(self.btn_number, 0))
        self.ui.btn_1.clicked.connect(partial(self.btn_number, 1))
        self.ui.btn_2.clicked.connect(partial(self.btn_number, 2))
        self.ui.btn_3.clicked.connect(partial(self.btn_number, 3))
        self.ui.btn_4.clicked.connect(partial(self.btn_number, 4))
        self.ui.btn_5.clicked.connect(partial(self.btn_number, 5))
        self.ui.btn_6.clicked.connect(partial(self.btn_number, 6))
        self.ui.btn_7.clicked.connect(partial(self.btn_number, 7))
        self.ui.btn_8.clicked.connect(partial(self.btn_number, 8))
        self.ui.btn_9.clicked.connect(partial(self.btn_number, 9))
        self.ui.btn_ac.clicked.connect(self.AC)
        self.ui.btn_dot.clicked.connect(self.dot)
        ###############################################################################
        self.ui.btn_sin.clicked.connect(partial(self.op_type_1, 'sin'))
        self.ui.btn_cos.clicked.connect(partial(self.op_type_1, 'cos'))
        self.ui.btn_tan.clicked.connect(partial(self.op_type_1, 'tan'))
        self.ui.btn_cot.clicked.connect(partial(self.op_type_1, 'cot'))
        self.ui.btn_log.clicked.connect(partial(self.op_type_1, 'log'))
        self.ui.btn_sqrt.clicked.connect(partial(self.op_type_1, 'sqrt'))
        ###############################################################################
        self.ui.btn_sum.clicked.connect(partial(self.op_type_2, '+'))
        self.ui.btn_sub.clicked.connect(partial(self.op_type_2, '-'))
        self.ui.btn_mul.clicked.connect(partial(self.op_type_2, '*'))
        self.ui.btn_div.clicked.connect(partial(self.op_type_2, '/'))
        self.ui.btn_per.clicked.connect(partial(self.op_type_2, '%'))
        ###############################################################################
        self.ui.btn_equal.clicked.connect(self.equal)
        
    def btn_number(self,num):
        self.ui.tb_text_1.setText(self.ui.tb_text_1.text() + str(num))

    def AC(self):
        self.ui.tb_text_1.setText('')

    def dot(self):
        if '.' not in self.ui.tb_text_1.text():
            self.ui.tb_text_1.setText(self.ui.tb_text_1.text() + '.')   
    def op_type_1(self,op):
        try:
            #self.ui.tb_text_1.setText(self.ui.tb_text_1.text() + op)     T_T i got value error  
            self.op_type=1
            self.op = op
            
        except:
            self.ui.tb_text_1.setText('Errorequal1') 
            
    def op_type_2(self,op):
        try:
            
            self.num1 = float(self.ui.tb_text_1.text())
            self.ui.tb_text_1.setText('')
            self.op_type=2
            self.op = op

       
        except:
            self.ui.tb_text_1.setText('Errorequal') 

                       
    def equal(self):
        try:
            if self.ui.tb_text_1.text() != '':
                
                if self.op_type==1:
                    num = float(self.ui.tb_text_1.text())
                    r=radians(num)
                    if self.op=='neg':
                        if num>0:
                            result = -abs(num)
                        elif num==0:
                            result=0
                        else:
                            result=abs(num)

                    elif self.op=='log':
                        result = log10(num)

                    elif self.op=='sin':
                        result = sin(r)

                    elif self.op=='cos':
                        result = cos(r)

                    elif self.op=='tan':
                        result = tan(r)

                    elif self.op=='cot':
                        result = 1/tan(r)
                    
                    elif self.op=='sqrt':
                        result = sqrt(self.num)


                elif self.op_type==2:
                    self.num2 = float(self.ui.tb_text_1.text())
                    if self.op=='+':
                        result = self.num1 + self.num2

                    elif self.op=='-':
                        result = self.num1 - self.num2

                    elif self.op=='*':
                        result = self.num1 * self.num2

                    elif self.op=='/':
                        result = self.num1 / self.num2

                    elif self.op=='%':
                        result =100 *( self.num1 / self.num2)
                        
                self.ui.tb_text_1.setText(str(result))

        except Exception as e:
            estr=str(e.__class__)
            self.ui.tb_text_1.setText(estr)            
        #except:
         #   self.ui.tb_text_1.setText('Errorequal')
            
        #mikhastam to text box balaish amal ra neshan bede valy har kar kardam beham rikht 
        # for x in self.h:
                #history += ' ' + x
        #self.ui.tb_text_2.setText(str(history))

   

if __name__ == "__main__":
    app = QApplication()
    calculator_main_window = Calculator()
    app.exec()