import jdr
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QGridLayout, QVBoxLayout


class MyWindow(QWidget):

    def __init__(self, personnage):
        super().__init__()
        self.initUi(personnage)

    def initUi(self, personnage):
        okBtn = QPushButton("Valider")
        modifyBtn = QPushButton("Modifier")
        cancelBtn = QPushButton("Annuler")

        box2 = QVBoxLayout()
        box2.setObjectName("pouet")
        box2.addWidget(QLabel(f"nom : {str(personnage.nom)}"))
        box2.addWidget(QLabel(f"attaque : {str(personnage.attaque)}"))
        box2.addWidget(QLabel(f"pdv : {str(personnage.pdv)}"))
        box2.addWidget(QLabel(f"defense : {str(personnage.defense)}"))
        box2.addWidget(QLabel(f"catchphrase : {str(personnage.catchphrase)}"))

        self.setLayout(box2)
        self.setGeometry(500, 100, 800, 800)
        self.setWindowTitle("Disposition horizontale")
        self.setContentsMargins(10, 10, 10, 10)
        # label.setStyleSheet(
        #     "* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"
        #     "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 cyan, stop:1 blue);}");
        self.setObjectName("pouet")
        self.setStyleSheet(
            "* {color: #fff; font: bold; font-size:13px; background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #2b2b2b, stop:1 #3949ab); border-image: url(test.jpg) 0 0 0 0 stretch stretch;}")

        self.show()


def main():
    app = QApplication(sys.argv)
    w = MyWindow(jdr.Guerrier("Albert", 100, 1000, 50, "AHHHHHHH JE SUIS UN GUERRIER"))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
