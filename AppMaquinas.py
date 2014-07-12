'''
Created on 11/7/2014

@author: josejacomeb
'''
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from Maquinas import Ui_Dialog

app = QApplication(sys.argv)
print("Iniciando aplicacion")
window = QDialog()
print('Iniciando dialogo')
ui = Ui_Dialog()
print('Dialogo')
ui.setupUi(window)
print('Dialogo')
window.show()
print('Mostrar ventana')

sys.exit(app.exec_())
