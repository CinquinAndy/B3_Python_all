import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget


def main():
    app = QApplication([])

    w = QWidget()
    w.resize(400, 300)
    w.move(300, 100)
    w.setWindowTitle("Ma première fenêtre ! :D")
    w.show()

    label = QLabel("Hello")
    label.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
