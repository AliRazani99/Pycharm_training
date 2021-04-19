from PyQt5.QtCore import QDate,QDateTime, Qt


def count_days():
    days = QDate(2021, 10, 11)

    print("Days in Month is:{0}".format(days.daysInMonth()))
    print("Days in year is :{0}".format(days.daysInYear()))

def adding_days():
    date=QDateTime.currentDateTime()

    print("Date of today is :",date.toString(Qt.ISODate))
    print("Adding 15days is:{0}".format(date.addDays(15).toString(Qt.ISODate)))
    print("Subtracting 15days is:{0}".format(date.addDays(-15).toString(Qt.ISODate)))
    print("Adding 5 years is:{0}".format(date.addYears(5).toString(Qt.ISODate)))
    print("Adding 5 month is:{0}".format(date.addMonths(5).toString(Qt.ISODate)))


if __name__ == '__main__':
    count_days()
    adding_days()
