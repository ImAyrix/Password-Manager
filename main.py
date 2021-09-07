from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from logsign import Ui_LoginSignup
from panel import Ui_panel
import pyperclip as pc
import string
import csv
import random
import os
import webbrowser
import darkdetect
from PyQt5 import QtGui
from PyQt5 import QtCore
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox

user = str()
password_account = str()
check_dark = 0


class Panel(QMainWindow):

    def __init__(self):
        global check_dark
        QMainWindow.__init__(self)
        self.panelUi = Ui_panel()
        self.panelUi.setupUi(self)

        if check_dark == 1:
            self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.onedr)

        with open('system mode.text', 'r') as sm:
            for row in sm:
                if row == 'True':
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("True.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.panelUi.system_df.setIcon(icon)
                    self.panelUi.system_df.setIconSize(QtCore.QSize(20, 20))

                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("True_dr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.panelUi.system_df_dr.setIcon(icon)
                    self.panelUi.system_df_dr.setIconSize(QtCore.QSize(20, 20))
                else:
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("True.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.panelUi.system_df.setIcon(icon)
                    self.panelUi.system_df.setIconSize(QtCore.QSize(0, 0))

                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("True_dr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.panelUi.system_df_dr.setIcon(icon)
                    self.panelUi.system_df_dr.setIconSize(QtCore.QSize(0, 0))

        with open('custom.text', 'r') as sm:
            for row in sm:
                if row == 'True':
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("True.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.panelUi.custom_md.setIcon(icon)
                    self.panelUi.custom_md.setIconSize(QtCore.QSize(20, 20))

                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("True_dr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.panelUi.custom_md_dr.setIcon(icon)
                    self.panelUi.custom_md_dr.setIconSize(QtCore.QSize(20, 20))
                else:
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("True.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.panelUi.custom_md.setIcon(icon)
                    self.panelUi.custom_md.setIconSize(QtCore.QSize(0, 0))

                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("True_dr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.panelUi.custom_md_dr.setIcon(icon)
                    self.panelUi.custom_md_dr.setIconSize(QtCore.QSize(0, 0))


        # generate
        self.panelUi.generate1.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.one))
        self.panelUi.generate2.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.one))
        self.panelUi.generate3.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.one))
        self.panelUi.generate4.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.one))
        self.panelUi.generate5.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.one))
        self.panelUi.generate6.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.one))

        # Insert
        self.panelUi.insert1.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.two))
        self.panelUi.insert1.clicked.connect(self.clear)
        self.panelUi.insert2.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.two))
        self.panelUi.insert2.clicked.connect(self.clear)
        self.panelUi.insert3.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.two))
        self.panelUi.insert3.clicked.connect(self.clear)
        self.panelUi.insert4.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.two))
        self.panelUi.insert4.clicked.connect(self.clear)
        self.panelUi.insert5.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.two))
        self.panelUi.insert5.clicked.connect(self.clear)
        self.panelUi.insert6.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.two))
        self.panelUi.insert6.clicked.connect(self.clear)

        # Manage
        self.panelUi.manage1.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.three))
        self.panelUi.manage1.clicked.connect(self.manage)
        self.panelUi.manage2.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.three))
        self.panelUi.manage2.clicked.connect(self.manage)
        self.panelUi.manage3.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.three))
        self.panelUi.manage3.clicked.connect(self.manage)
        self.panelUi.manage4.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.three))
        self.panelUi.manage4.clicked.connect(self.manage)
        self.panelUi.manage5.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.three))
        self.panelUi.manage5.clicked.connect(self.manage)
        self.panelUi.manage6.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.three))
        self.panelUi.manage6.clicked.connect(self.manage)

        # Setting
        self.panelUi.setting1.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_2))
        self.panelUi.setting1.clicked.connect(self.clear_setting)
        self.panelUi.setting2.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_2))
        self.panelUi.setting2.clicked.connect(self.clear_setting)
        self.panelUi.setting3.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_2))
        self.panelUi.setting3.clicked.connect(self.clear_setting)
        self.panelUi.setting4.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_2))
        self.panelUi.setting4.clicked.connect(self.clear_setting)
        self.panelUi.setting5.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_2))
        self.panelUi.setting5.clicked.connect(self.clear_setting)
        self.panelUi.setting6.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_2))
        self.panelUi.setting5.clicked.connect(self.clear_setting)

        # About
        self.panelUi.about1.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.five))
        self.panelUi.about2.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.five))
        self.panelUi.about3.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.five))
        self.panelUi.about4.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.five))
        self.panelUi.about5.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.five))
        self.panelUi.about6.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.five))

        # Logout
        self.panelUi.logout1.clicked.connect(self.logout)
        self.panelUi.logout2.clicked.connect(self.logout)
        self.panelUi.logout3.clicked.connect(self.logout)
        self.panelUi.logout4.clicked.connect(self.logout)
        self.panelUi.logout5.clicked.connect(self.logout)
        self.panelUi.logout6.clicked.connect(self.logout)

        self.panelUi.pushButton_copy.clicked.connect(self.copy_pass)
        self.panelUi.pushButton_generate.clicked.connect(self.generate)
        self.panelUi.pushButton_sub.clicked.connect(self.submit)
        self.panelUi.Button_sub_dr.clicked.connect(self.submitdr)
        self.panelUi.pushButton_generate_dr.clicked.connect(self.generatedr)
        self.panelUi.pushButton_copy_dark.clicked.connect(self.copy_pass_dr)

        # generate
        self.panelUi.gener1_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.onedr))
        self.panelUi.gener2_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.onedr))
        self.panelUi.gener3_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.onedr))
        self.panelUi.gener4_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.onedr))
        self.panelUi.gener5_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.onedr))
        self.panelUi.gener6_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.onedr))

        # Insert
        self.panelUi.insert1_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.twodr))
        self.panelUi.insert1_dr.clicked.connect(self.cleardr)
        self.panelUi.insert2_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.twodr))
        self.panelUi.insert2.clicked.connect(self.cleardr)
        self.panelUi.insert3_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.twodr))
        self.panelUi.insert3_dr.clicked.connect(self.cleardr)
        self.panelUi.insert4_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.twodr))
        self.panelUi.insert4_dr.clicked.connect(self.cleardr)
        self.panelUi.insert5_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.twodr))
        self.panelUi.insert5_dr.clicked.connect(self.cleardr)
        self.panelUi.insert6_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.twodr))
        self.panelUi.insert6_dr.clicked.connect(self.cleardr)

        # Manage
        self.panelUi.manage1_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.th3dr))
        self.panelUi.manage1_dr.clicked.connect(self.managedr)
        self.panelUi.manage2_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.th3dr))
        self.panelUi.manage2_dr.clicked.connect(self.managedr)
        self.panelUi.manage3_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.th3dr))
        self.panelUi.manage3_dr.clicked.connect(self.managedr)
        self.panelUi.manage4_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.th3dr))
        self.panelUi.manage4_dr.clicked.connect(self.managedr)
        self.panelUi.manage5_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.th3dr))
        self.panelUi.manage5_dr.clicked.connect(self.managedr)
        self.panelUi.manage6_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.th3dr))
        self.panelUi.manage6_dr.clicked.connect(self.managedr)

        # Setting
        self.panelUi.setti1_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_dr))
        self.panelUi.setti1_dr.clicked.connect(self.clear_setting_dr)
        self.panelUi.setti2_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_dr))
        self.panelUi.setti2_dr.clicked.connect(self.clear_setting_dr)
        self.panelUi.setti3_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_dr))
        self.panelUi.setti3_dr.clicked.connect(self.clear_setting_dr)
        self.panelUi.setti4_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_dr))
        self.panelUi.setti4_dr.clicked.connect(self.clear_setting_dr)
        self.panelUi.setti5_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_dr))
        self.panelUi.setti5_dr.clicked.connect(self.clear_setting_dr)
        self.panelUi.setti6_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_dr))
        self.panelUi.setti6_dr.clicked.connect(self.clear_setting_dr)

        # About
        self.panelUi.about1_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.fivedr))
        self.panelUi.about2_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.fivedr))
        self.panelUi.about3_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.fivedr))
        self.panelUi.about4_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.fivedr))
        self.panelUi.about5_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.fivedr))
        self.panelUi.about6_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.fivedr))

        # Logout
        self.panelUi.logout1dr.clicked.connect(self.logoutdr)
        self.panelUi.logout2dr.clicked.connect(self.logoutdr)
        self.panelUi.logout3dr.clicked.connect(self.logoutdr)
        self.panelUi.logout4dr.clicked.connect(self.logoutdr)
        self.panelUi.logout5dr.clicked.connect(self.logoutdr)
        self.panelUi.logout6dr.clicked.connect(self.logoutdr)

        # Copy password page Light
        self.panelUi.copy_manage1.clicked.connect(self.copy_manage1)
        self.panelUi.copy_manage2.clicked.connect(self.copy_manage2)
        self.panelUi.copy_manage3.clicked.connect(self.copy_manage3)
        self.panelUi.copy_manage4.clicked.connect(self.copy_manage4)
        self.panelUi.copy_manage5.clicked.connect(self.copy_manage5)
        self.panelUi.copy_manage6.clicked.connect(self.copy_manage6)
        self.panelUi.copy_manage7.clicked.connect(self.copy_manage7)

        # Copy password page Dark
        self.panelUi.copy_manage1_dr.clicked.connect(self.copy_manage1dr)
        self.panelUi.copy_manage2_dr.clicked.connect(self.copy_manage2dr)
        self.panelUi.copy_manage3_dr.clicked.connect(self.copy_manage3dr)
        self.panelUi.copy_manage4_dr.clicked.connect(self.copy_manage4dr)
        self.panelUi.copy_manage5_dr.clicked.connect(self.copy_manage5dr)
        self.panelUi.copy_manage6_dr.clicked.connect(self.copy_manage6dr)
        self.panelUi.copy_manage7_dr.clicked.connect(self.copy_manage7dr)

        # Quick id
        self.panelUi.submit_id.clicked.connect(self.setid)
        self.panelUi.submit_id_dark.clicked.connect(self.setid_dr)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Show All
        self.panelUi.showall.clicked.connect(self.showall)
        self.panelUi.showall_dr.clicked.connect(self.showall)

        # About-Link
        self.panelUi.github.clicked.connect(self.github)
        self.panelUi.contactme.clicked.connect(self.contact)
        self.panelUi.social.clicked.connect(self.social)

        self.panelUi.githubdr.clicked.connect(self.github)
        self.panelUi.contact_dr.clicked.connect(self.contact)
        self.panelUi.social_dr.clicked.connect(self.social)

        # Dark
        self.panelUi.mode_dr1.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.onedr))
        self.panelUi.mode_dr2.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.twodr))
        self.panelUi.mode_dr3.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.th3dr))
        self.panelUi.mode_dr4.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_dr))
        self.panelUi.mode_dr5.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.fivedr))

        # Light
        self.panelUi.mode_lig1.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.one))
        self.panelUi.mode_lig2.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.two))
        self.panelUi.mode_lig3.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.three))
        self.panelUi.mode_lig4.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_2))
        self.panelUi.mode_lig5.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.five))

        # Auto theme
        self.panelUi.system_df.clicked.connect(self.system_df)
        self.panelUi.custom_md.clicked.connect(self.custom_md)
        self.panelUi.sub_custom.clicked.connect(self.sub_md)
        self.panelUi.system_df_dr.clicked.connect(self.system_df_dr)
        self.panelUi.custom_md_dr.clicked.connect(self.custom_md_dr)
        self.panelUi.sub_custom_2.clicked.connect(self.sub_md_dr)

        self.panelUi.ok_dr.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_dr))
        self.panelUi.ok_error.clicked.connect(lambda: self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.for_2))

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def copy_pass(self):
        password = self.panelUi.label_generate_pass.text()
        pc.copy(password)
        self.panelUi.label_generate_pass.setText(' - - - - - - - - - - - - - - - Copied - - - - - - - - - - - - - - -')

    def copy_pass_dr(self):
        password = self.panelUi.label_generate_pass_dark.text()
        pc.copy(password)
        self.panelUi.label_generate_pass_dark.setText(' - - - - - - - - - - - - - Copied - - - - - - - - - - - - -')

    def generate(self):
        upper = self.panelUi.checkBox_upper.isChecked()
        lower = self.panelUi.checkBox_lower.isChecked()
        numeric = self.panelUi.checkBox_num.isChecked()
        symbol = self.panelUi.checkBox_symbols.isChecked()
        length = self.panelUi.lineEdit_length.text()

        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        num_case = string.digits
        symbols_case = string.punctuation

        if len(length) == 0:
            length = 8
        all = str()

        if upper:
            all += upper_case
        if lower:
            all += lower_case
        if numeric:
            all += num_case
        if symbol:
            all += symbols_case
        if len(all) == 0:
            all = lower_case+upper_case

        temp = random.sample(all, int(length))
        password = "".join(temp)
        self.panelUi.label_generate_pass.setText(password)

    def generatedr(self):
        upper = self.panelUi.checkBox_upper_dr.isChecked()
        lower = self.panelUi.checkBox_lower_dr.isChecked()
        numeric = self.panelUi.checkBox_num_dr.isChecked()
        symbol = self.panelUi.checkBox_symbols_dr.isChecked()
        length = self.panelUi.lineEdit_length_dr.text()

        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        num_case = string.digits
        symbols_case = string.punctuation

        if len(length) == 0:
            length = 8
        all = str()

        if upper:
            all += upper_case
        if lower:
            all += lower_case
        if numeric:
            all += num_case
        if symbol:
            all += symbols_case
        if len(all) == 0:
            all = lower_case+upper_case

        temp = random.sample(all, int(length))
        password = "".join(temp)
        self.panelUi.label_generate_pass_dark.setText(password)

    def submit(self):
        global user
        password = self.panelUi.insert_pass.text()
        name = self.panelUi.insert_name.text()
        note = self.panelUi.insert_note.text()

        with open(user+'.csv', 'a+') as data:
            data.write(password + ',' + name + ',' + note + '\n')
            self.panelUi.errorinsert.setText('Password added to database')

    def submitdr(self):
        global user
        password = self.panelUi.insert_pass_dr.text()
        name = self.panelUi.insert_name_dr.text()
        note = self.panelUi.insert_note_dr.text()

        with open(user+'.csv', 'a+') as data:
            data.write(password + ',' + name + ',' + note + '\n')
            self.panelUi.errorinsert_dr.setText('Password added to database')

    def clear(self):
        self.panelUi.errorinsert.setText('')
        self.panelUi.insert_pass.setText('')
        self.panelUi.insert_name.setText('')
        self.panelUi.insert_note.setText('')

    def cleardr(self):
        self.panelUi.errorinsert_dr.setText('')
        self.panelUi.insert_pass_dr.setText('')
        self.panelUi.insert_name_dr.setText('')
        self.panelUi.insert_note_dr.setText('')

    def manage(self):
        global user
        with open(user+'.csv', 'a+') as data_check:
            pass
        with open(user+'.csv', 'r') as data_check:
            reader = csv.reader(data_check)
            count = 0
            for row in reader:
                if count == 0:
                    self.panelUi.n0.setText(row[0])
                    self.panelUi.a0.setText(row[1])
                    self.panelUi.no0.setText(row[2])
                elif count == 1:
                    self.panelUi.n1.setText(row[0])
                    self.panelUi.a1.setText(row[1])
                    self.panelUi.no1.setText(row[2])
                elif count == 2:
                    self.panelUi.n2.setText(row[0])
                    self.panelUi.a2.setText(row[1])
                    self.panelUi.no2.setText(row[2])
                elif count == 3:
                    self.panelUi.n3.setText(row[0])
                    self.panelUi.a3.setText(row[1])
                    self.panelUi.no3.setText(row[2])
                elif count == 4:
                    self.panelUi.n4.setText(row[0])
                    self.panelUi.a4.setText(row[1])
                    self.panelUi.no4.setText(row[2])
                elif count == 5:
                    self.panelUi.n5.setText(row[0])
                    self.panelUi.a5.setText(row[1])
                    self.panelUi.no5.setText(row[2])
                elif count == 6:
                    self.panelUi.n6.setText(row[0])
                    self.panelUi.a6.setText(row[1])
                    self.panelUi.no6.setText(row[2])
                count += 1

    def managedr(self):
        global user
        with open(user+'.csv', 'a+') as data_check:
            pass
        with open(user+'.csv', 'r') as data_check:
            reader = csv.reader(data_check)
            count = 0
            for row in reader:
                if count == 0:
                    self.panelUi.n0_dr.setText(row[0])
                    self.panelUi.a0_dr.setText(row[1])
                    self.panelUi.no0_dr.setText(row[2])
                elif count == 1:
                    self.panelUi.n1_dr.setText(row[0])
                    self.panelUi.a1_dr.setText(row[1])
                    self.panelUi.no1_dr.setText(row[2])
                elif count == 2:
                    self.panelUi.n2_dr.setText(row[0])
                    self.panelUi.a2_dr.setText(row[1])
                    self.panelUi.no2_dr.setText(row[2])
                elif count == 3:
                    self.panelUi.n3_dr.setText(row[0])
                    self.panelUi.a3_dr.setText(row[1])
                    self.panelUi.no3_dr.setText(row[2])
                elif count == 4:
                    self.panelUi.n4_dr.setText(row[0])
                    self.panelUi.a4_dr.setText(row[1])
                    self.panelUi.no4_dr.setText(row[2])
                elif count == 5:
                    self.panelUi.n5_dr.setText(row[0])
                    self.panelUi.a5_dr.setText(row[1])
                    self.panelUi.no5_dr.setText(row[2])
                elif count == 6:
                    self.panelUi.n6_dr.setText(row[0])
                    self.panelUi.a6_dr.setText(row[1])
                    self.panelUi.no6_dr.setText(row[2])
                count += 1

    # Light copy manage
    def copy_manage1(self):
        password = self.panelUi.n0.text()
        pc.copy(password)

    def copy_manage2(self):
        password = self.panelUi.n1.text()
        pc.copy(password)

    def copy_manage3(self):
        password = self.panelUi.n2.text()
        pc.copy(password)

    def copy_manage4(self):
        password = self.panelUi.n3.text()
        pc.copy(password)

    def copy_manage5(self):
        password = self.panelUi.n4.text()
        pc.copy(password)

    def copy_manage6(self):
        password = self.panelUi.n5.text()
        pc.copy(password)

    def copy_manage7(self):
        password = self.panelUi.n6.text()
        pc.copy(password)

    # Dark copy manage
    def copy_manage1dr(self):
        password = self.panelUi.n0_dr.text()
        pc.copy(password)

    def copy_manage2dr(self):
        password = self.panelUi.n1_dr.text()
        pc.copy(password)

    def copy_manage3dr(self):
        password = self.panelUi.n2_dr.text()
        pc.copy(password)

    def copy_manage4dr(self):
        password = self.panelUi.n3_dr.text()
        pc.copy(password)

    def copy_manage5dr(self):
        password = self.panelUi.n4_dr.text()
        pc.copy(password)

    def copy_manage6dr(self):
        password = self.panelUi.n5_dr.text()
        pc.copy(password)

    def copy_manage7dr(self):
        password = self.panelUi.no6_dr.text()
        pc.copy(password)

    def setid(self):
        global user
        global password_account
        count = 0
        id = self.panelUi.lineEdit_id.text()
        confirm_id = self.panelUi.lineEdit_confirmid.text()
        if len(id) != 0:
            if id == confirm_id:
                with open('log', 'r') as account:
                    reader = csv.reader(account)
                    for row in reader:
                        if row[2] == id:
                            count += 1
            else:
                self.panelUi.errorid.setText('ID does not match')
            if count == 0:
                with open('log', 'a+') as accounts:
                    reader2 = csv.reader(accounts)
                    accounts.write(user + ',' + password_account + ',' +id+'\n')
                    self.panelUi.errorid.setText('Quick Login set')

            else:
                self.panelUi.errorid.setText('Invalid ID Please try again')
        else:
            self.panelUi.errorid.setText('Please fill in all inputs')

    def setid_dr(self):
        global user
        global password_account
        count = 0
        id = self.panelUi.lineEdit_id_dr.text()
        confirm_id = self.panelUi.lineEdit_confirmid_dr.text()
        if len(id) != 0:
            if id == confirm_id:
                with open('log', 'r') as account:
                    reader = csv.reader(account)
                    for row in reader:
                        if row[2] == id:
                            count += 1
            else:
                self.panelUi.errorid_dr.setText('ID does not match')
            if count == 0:
                with open('log', 'a+') as accounts:
                    accounts.write(user + ',' + password_account + ',' +id+'\n')
                    self.panelUi.errorid_dr.setText('Quick Login set')

            else:
                self.panelUi.errorid_dr.setText('Invalid ID Please try again')
        else:
            self.panelUi.errorid_dr.setText('Please fill in all inputs')

    def clear_setting(self):
        self.panelUi.errorid.setText('')
        self.panelUi.lineEdit_id.setText('')
        self.panelUi.lineEdit_confirmid.setText('')

    def clear_setting_dr(self):
        self.panelUi.errorid_dr.setText('')
        self.panelUi.lineEdit_id_dr.setText('')
        self.panelUi.lineEdit_confirmid_dr.setText('')

    def logout(self):
        global check_dark
        check_dark = 0
        self.welcome = Root()
        self.welcome.show()
        self.close()

    def logoutdr(self):
        global check_dark
        global user
        check_dark = 1
        self.welcome = Root()
        self.welcome.show()
        self.close()

    def showall(self):
        global user
        counter = 0
        with open(user+'.text', 'w') as file_listpass:
            with open(user+'.csv', 'r') as listpassword:
                reader = csv.reader(listpassword)
                for row in reader:
                    file_listpass.write('Password :  '+row[0]+'  |  '+'Name :  '+row[1]+'  | '+'Hint  : '+row[2]+'\n\n')

        filepath = user+'.text'
        os.system(f"notepad {filepath}")

    def github(self):
        webbrowser.open('https://github.com/AbbasAtaei')

    def contact(self):
        webbrowser.open("mailto:?to=abbasataei.py@gmail.com&subject='Hello Mr.Ataei'", new=1)

    def social(self):
        webbrowser.open('https://bioly.io/AbbasAtaei')

    def system_df(self):
        check = str()
        with open('system mode.text', 'r') as sm:
            for row in sm:
                check = row

        with open('system mode.text', 'w') as sm:
            if check == 'False':
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("True.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.panelUi.system_df.setIcon(icon)
                self.panelUi.system_df.setIconSize(QtCore.QSize(20, 20))
                sm.write('True')

                with open('custom.text', 'w') as ct:
                    ct.write('False')

                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("True.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.panelUi.custom_md.setIcon(icon)
                self.panelUi.custom_md.setIconSize(QtCore.QSize(0, 0))
            else:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("True.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.panelUi.system_df.setIcon(icon)
                self.panelUi.system_df.setIconSize(QtCore.QSize(0, 0))
                sm.write('False')
        self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.error_auto)

    def custom_md(self):
        self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.custom)

    def sub_md(self):
        light1 = self.panelUi.time_light1.text()
        light2 = self.panelUi.time_light2.text()

        dark1 = self.panelUi.time_dark1.text()
        dark2 = self.panelUi.time_dark2.text()

        with open('custom.text', 'w') as cm:
            cm.write('True')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("True.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.panelUi.custom_md.setIcon(icon)
        self.panelUi.custom_md.setIconSize(QtCore.QSize(20, 20))

        with open('system mode.text', 'w') as sm:
            sm.write('False')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("True.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.panelUi.system_df.setIcon(icon)
        self.panelUi.system_df.setIconSize(QtCore.QSize(0, 0))

        with open('time.text', 'w') as tt:
            tt.write(light1 + ',' + light2 + ',' + dark1 + ',' + dark2)

        self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.error_auto)

    def custom_md_dr(self):
        self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.custom_dr)

    def sub_md_dr(self):
        light1 = self.panelUi.time_light1_dr.text()
        light2 = self.panelUi.time_light2_dr.text()

        dark1 = self.panelUi.time_dark1_dr.text()
        dark2 = self.panelUi.time_dark2_dr.text()

        with open('custom.text', 'w') as cm:
            cm.write('True')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("True_dr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.panelUi.custom_md_dr.setIcon(icon)
        self.panelUi.custom_md_dr.setIconSize(QtCore.QSize(20, 20))

        with open('system mode.text', 'w') as sm:
            sm.write('False')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("True_dr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.panelUi.system_df_dr.setIcon(icon)
        self.panelUi.system_df_dr.setIconSize(QtCore.QSize(0, 0))

        with open('time.text', 'w') as tt:
            tt.write(light1+','+light2+','+dark1+','+dark2)

        self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.error_dr)

    def system_df_dr(self):
        check = str()
        with open('system mode.text', 'r') as sm:
            for row in sm:
                check = row

        with open('system mode.text', 'w') as sm:
            if check == 'False':
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("True_dr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.panelUi.system_df_dr.setIcon(icon)
                self.panelUi.system_df_dr.setIconSize(QtCore.QSize(20, 20))
                sm.write('True')

                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("True_dr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.panelUi.custom_md_dr.setIcon(icon)
                self.panelUi.custom_md_dr.setIconSize(QtCore.QSize(0, 0))

                with open('custom.text', 'w') as ct:
                    ct.write('False')
            else:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("True_dr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.panelUi.system_df_dr.setIcon(icon)
                self.panelUi.system_df_dr.setIconSize(QtCore.QSize(0, 0))
                sm.write('False')
        self.panelUi.stackedWidget.setCurrentWidget(self.panelUi.error_dr)


class Root(QMainWindow):

    def __init__(self):
        global check_dark
        QMainWindow.__init__(self)
        self.ui = Ui_LoginSignup()
        self.ui.setupUi(self)

        if check_dark == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.logsig_dr)

        with open('system mode.text', 'r') as sm:
            for row in sm:
                if row == 'True':
                    if darkdetect.isDark():
                        self.ui.stackedWidget.setCurrentWidget(self.ui.logsig_dr)

                    if darkdetect.isLight():
                        self.ui.stackedWidget.setCurrentWidget(self.ui.logorsig)

        with open('custom.text', 'r') as cm:
            for row in cm:
                if row == 'True':
                    with open('time.text') as time:
                        for one in time:
                            one = one.split(',')
                            light_first = int(one[0][:2])
                            light_last = int(one[1][:2])
                            dark_first = int(one[2][:2])
                            dark_last = int(one[3][:2])
                            now = datetime.now().time()
                            now = int(str(now)[:2])
                            if now == 0 or now == 00:
                                now = 24

                            if now <= light_last and now >= light_first:
                                self.ui.stackedWidget.setCurrentWidget(self.ui.logorsig)

                            elif now <= dark_last and now >= dark_first:
                                self.ui.stackedWidget.setCurrentWidget(self.ui.logsig_dr)
                            else:
                                self.ui.stackedWidget.setCurrentWidget(self.ui.logorsig)

        self.ui.lineEdit_user.setPlaceholderText("Username")
        self.ui.lineEdit_pass.setPlaceholderText("Password")
        self.ui.lineEdit_userdr.setPlaceholderText("Username")
        self.ui.lineEdit_passdr.setPlaceholderText("Password")
        self.ui.lineEdit_user3.setPlaceholderText("Username")
        self.ui.lineEdit_pass3.setPlaceholderText("Password")
        self.ui.lineEdit_repass3.setPlaceholderText("Confirm Password")
        self.ui.lineEdit_user3dr.setPlaceholderText("Username")
        self.ui.lineEdit_pass3dr.setPlaceholderText("Password")
        self.ui.lineEdit_repass3dr.setPlaceholderText("Confirm Password")
        self.ui.lineEdit_id.setPlaceholderText("Your ID")
        self.ui.lineEdit_iddr.setPlaceholderText("Your ID")

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()
        self.ui.loginButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
        self.ui.backgradient.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.logorsig))
        self.ui.mode_light.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.logorsig))
        self.ui.signButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.signup))
        self.ui.signButton_dr.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.signupdr))
        self.ui.pushButton_loginpagesign.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
        self.ui.push_registerinlogin.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.signup))
        self.ui.backgradient_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.logorsig))
        self.ui.mode_dark.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.logsig_dr))
        self.ui.loginpagesign_dr.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.logindr))
        self.ui.registerinlogin_dr.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.signupdr))
        self.ui.loginButton_dr.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.logindr))
        self.ui.backgradient_dr1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.logsig_dr))
        self.ui.backgradient_dr2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.logsig_dr))
        self.ui.pushButton_ql.clicked.connect(self.quickLog)
        self.ui.pushButton_qldr.clicked.connect(self.quickLogdr)
        self.ui.pushButton_logingrad.clicked.connect(self.login)
        self.ui.signup_pageregister.clicked.connect(self.signup)
        self.ui.pushButton_logingraddr.clicked.connect(self.logindr)
        self.ui.signup_pageregister_dr.clicked.connect(self.signupdr)

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def quickLog(self):
        global user
        global password_account
        global check_dark
        id = self.ui.lineEdit_id.text()
        with open('log', 'r') as check:
            reader = csv.reader(check)
            for row in reader:
                if row[2] == id:
                    user = row[0]
                    password_account = row[1]
                    check_dark = 0
                    self.panel = Panel()
                    self.panel.show()
                    self.close()
                    break

    def quickLogdr(self):
        global user
        global password_account
        global check_dark
        id = self.ui.lineEdit_iddr.text()
        with open('log', 'r') as check:
            reader = csv.reader(check)
            for row in reader:
                if row[2] == id:
                    user = row[0]
                    password_account = row[1]
                    check_dark = 1
                    self.panel = Panel()
                    self.panel.show()
                    self.close()
                    break

    def login(self):
        global user
        global password_account
        global check_dark
        username = self.ui.lineEdit_user.text()
        password = self.ui.lineEdit_pass.text()
        with open('log', 'r') as accounts:
            reader = csv.reader(accounts)
            for row in reader:
                if username == row[0] and password == row[1]:
                    check_dark = 0
                    user = username
                    password_account = password
                    self.panel = Panel()
                    self.panel.show()
                    self.close()
                    break
                else:
                    self.ui.errorlogin.setText('Invalid Username Or Password ')

    def signup(self):
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        num_case = string.digits
        symbols_case = string.punctuation
        all = lower_case+upper_case+num_case+symbols_case
        temp = random.sample(all, int(8))
        id_defult = "".join(temp)

        username = self.ui.lineEdit_user3.text()
        password = self.ui.lineEdit_pass3.text()
        confirm = self.ui.lineEdit_repass3.text()
        counter = 0

        with open('log', 'r') as checker:
            reader = csv.reader(checker)
            for row in reader:
                if row[0] == username:
                    counter = 1
        if counter == 0:
            if len(username) != 0 and len(password) != 0 and len(confirm) != 0:
                if password == confirm:
                    with open('log', 'a+') as accounts:
                        accounts.write(username+','+password+','+id_defult+'\n')
                    self.ui.stackedWidget.setCurrentWidget(self.ui.login)
                else:
                    self.ui.errorsignup.setText('Passwords does not match')
            else:
                self.ui.errorsignup.setText('Please fill in all inputs')
        else:
            self.ui.errorsignup.setText('The username is duplicate')

    def logindr(self):
        global user
        global check_dark
        global password_account
        username = self.ui.lineEdit_userdr.text()
        password = self.ui.lineEdit_passdr.text()
        with open('log', 'r') as accounts:
            reader = csv.reader(accounts)
            for row in reader:
                if username == row[0] and password == row[1]:
                    check_dark = 1
                    user = username
                    password_account = password
                    self.panel = Panel()
                    self.panel.show()
                    self.close()
                    break
                else:
                    self.ui.errorlogin_dr.setText('Invalid Username Or Password ')

    def signupdr(self):
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        num_case = string.digits
        symbols_case = string.punctuation
        all = lower_case+upper_case+num_case+symbols_case
        temp = random.sample(all, int(8))
        id_defult = "".join(temp)

        username = self.ui.lineEdit_user3dr.text()
        password = self.ui.lineEdit_pass3dr.text()
        confirm = self.ui.lineEdit_repass3dr.text()
        counter = 0

        with open('log', 'r') as checker:
            reader = csv.reader(checker)
            for row in reader:
                if row[0] == username:
                    counter = 1
        if counter == 0:
            if len(username) != 0 and len(password) != 0 and len(confirm) != 0:
                if password == confirm:
                    with open('log', 'a+') as accounts:
                        accounts.write(username+','+password+','+id_defult+'\n')
                    self.ui.stackedWidget.setCurrentWidget(self.ui.logindr)
                else:
                    self.ui.errorsignup_dr.setText('Passwords does not match')
            else:
                self.ui.errorsignup_dr.setText('Please fill in all inputs')
        else:
            self.ui.errorsignup_dr.setText('The username is duplicate')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())
