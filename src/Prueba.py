#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example we draw 6 lines using
different pen styles. 

author: Jan Bodnar
website: zetcode.com 
last edited: September 2011
"""

import sys
from PyQt4 import QtGui, QtCore
from math import *

def rango(x,y,paso):
    matriz =  []
    while y >= x:
        matriz.append(x)
        x += paso
    return matriz  
def setuprangos(w,x,fase):
    y = []
    for i in range(0,len(x)):
        y.append(sin(w*x[i]+fase))
    return y

x = rango(0,2*pi,0.0001)
y = setuprangos(60,x,0)

class Example(QtGui.QWidget):
            
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen styles')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
        
    def drawLines(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        for i in range(0,len(x)-1):
            #Ajustar a valores de la escala del QPainter
            qp.drawLine(500*x[i], 50*(1-y[i]), 500*x[i+1], 50*(1-y[i+1]))
            self.dibujarCirculo(qp,500*x[i], 50*(1-y[i]))
            
    def dibujarCirculo(self,qp,x,y):
        pen = QtGui.QPen(QtCore.Qt.red, 4, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawPoint(x,y)
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    
    main()