import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget


def main():
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 400)
    w.move(300, 100)
    w.setWindowTitle("Ma première fenêtre ! :)")
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
