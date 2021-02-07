# Very minimal GUI sample

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtCore import pyqtSlot

from winapi.cfgmgr32.api_wrappers import get_device_id_list
from winapi.cfgmgr32.helper import all_devices


class Interface(QTableWidget):
    def __init__(self):
        super().__init__()
        self.title = 'All interfaces'
        headers = ['Class Guid', 'Status', 'Description', 'Path']
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)
        layout = QVBoxLayout()
        layout.addWidget(self)
        self.setGeometry(0, 0, 800, 400)


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'All devices'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(list(get_device_id_list())))
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Friendly Name', 'Description', 'Instance ID', 'Class', 'Inf',
                                                    'Status', 'Class Guid', 'Provider', 'Manufacturer', 'Driver Date',
                                                    'Driver Version'])

        self.tableWidget.setSortingEnabled(True)

        for i, d in enumerate(all_devices()):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(d.name))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(d.friendly_name))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(d.desc))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(d.instance_id))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(d.class_name))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(d.driver_inf_path))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(d.status))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(str(d.class_guid)))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(d.driver_provider))
            self.tableWidget.setItem(i, 9, QTableWidgetItem(d.manufacturer))
            self.tableWidget.setItem(i, 10, QTableWidgetItem(d.driver_date.to_local_time().to_string() if d.driver_date else ''))
            self.tableWidget.setItem(i, 11, QTableWidgetItem(d.driver_version))

        self.tableWidget.move(0, 0)
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        from winapi.cfgmgr32.helper import get_interfaces_via_device_instance_id
        instance_id = self.tableWidget.item(self.tableWidget.currentRow(), 3).text()

        interfaces = list(get_interfaces_via_device_instance_id(instance_id))
        if not interfaces:
            return

        interface_table = Interface()
        interface_table.setRowCount(len(interfaces))

        for row, interface in enumerate(interfaces):
            interface_table.setItem(row, 0, QTableWidgetItem(str(interface.class_guid)))
            interface_table.setItem(row, 1, QTableWidgetItem('Enabled' if interface.status else 'Disabled'))
            interface_table.setItem(row, 2, QTableWidgetItem(interface.desc))
            interface_table.setItem(row, 3, QTableWidgetItem(interface.path))
        interface_table.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.setMinimumSize(800, 800)
    sys.exit(app.exec_())
