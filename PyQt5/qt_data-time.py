from PyQt5.Qt import QDateTime, QTime, QDate, Qt


def my_time():
    # data and time together
    data_time = QDateTime.currentDateTime()

    print("For demonstrate data and time together:")
    print(data_time.toString())
    print(data_time.toString(Qt.ISODate))
    print(data_time.toString(Qt.DefaultLocaleLongDate))
    print(data_time.toString(Qt.DefaultLocaleShortDate))

    # just for indicate time
    time = QTime.currentTime()

    print("For indicate time:")
    print(time.toString())
    print(time.toString(Qt.DefaultLocaleLongDate))
    print(time.toString(Qt.DefaultLocaleShortDate))

    # just for showing date
    date = QDate.currentDate()

    print("For indicate date:")
    print(date.toString())
    print(date.toString(Qt.ISODate))
    print(date.toString(Qt.DefaultLocaleLongDate))
    print(date.toString(Qt.DefaultLocaleShortDate))


if __name__ == '__main__':
    my_time()
