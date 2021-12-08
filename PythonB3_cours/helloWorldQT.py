import sys

from PyQt5.QtWidgets import QApplication, QLabel


def main():
    app = QApplication([])
    label = QLabel("Hello World !")
    label.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
