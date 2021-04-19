from PyQt5.QtCore import QDate


def count_days():
    days = QDate(2021, 10, 11)

    print("Days in Month is:{0}".format(days.daysInMonth()))
    print("Days in year is :{0}".format(days.daysInYear()))


if __name__ == '__main__':
    count_days()
