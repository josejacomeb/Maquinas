'''
Created on 11/7/2014

@author: josejacomeb
'''
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from Maquinas import Ui_Dialog

class AppMaquinas(QDialog):
    def __init__(self):
        super(AppMaquinas, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Make some local modifications.
        self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Connect up the buttons.
        self.ui.okButton.clicked.connect(self.accept)
        self.ui.cancelButton.clicked.connect(self.reject)
    def eventoFrecuencia(self):
        print(self.ui.Frecuencia.value())
        


def main():
    app = QApplication(sys.argv)
    print("Iniciando aplicacion")
    window = QDialog()
    print('Iniciando dialogo')
    ui = AppMaquinas()
    print('Dialogo')
    ui.setupUi(window)
    print('Dialogo')
    window.show()
    print('Mostrar ventana')
    sys.exit(app.exec_())

