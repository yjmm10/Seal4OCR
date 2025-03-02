# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'merge_image.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Merge(object):
    def setupUi(self, Merge):
        Merge.setObjectName("Merge")
        Merge.resize(958, 667)
        self.groupBox = QtWidgets.QGroupBox(Merge)
        self.groupBox.setGeometry(QtCore.QRect(40, 50, 91, 51))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Merge)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 110, 241, 186))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.back_pos_w = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.back_pos_w.setObjectName("back_pos_w")
        self.horizontalLayout_2.addWidget(self.back_pos_w)
        self.back_pos_h = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.back_pos_h.setObjectName("back_pos_h")
        self.horizontalLayout_2.addWidget(self.back_pos_h)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)
        self.back_path = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.back_path.setObjectName("back_path")
        self.gridLayout.addWidget(self.back_path, 0, 1, 1, 1)
        self.back_padding = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.back_padding.setObjectName("back_padding")
        self.gridLayout.addWidget(self.back_padding, 1, 1, 1, 1)
        self.fore_alpha = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.fore_alpha.setMaximum(1.0)
        self.fore_alpha.setSingleStep(0.1)
        self.fore_alpha.setProperty("value", 0.0)
        self.fore_alpha.setObjectName("fore_alpha")
        self.gridLayout.addWidget(self.fore_alpha, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.fore_path = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.fore_path.setObjectName("fore_path")
        self.gridLayout.addWidget(self.fore_path, 3, 1, 1, 1)
        self.fore_factor = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.fore_factor.setMinimum(0.01)
        self.fore_factor.setMaximum(99.0)
        self.fore_factor.setSingleStep(0.1)
        self.fore_factor.setProperty("value", 1.0)
        self.fore_factor.setObjectName("fore_factor")
        self.gridLayout.addWidget(self.fore_factor, 6, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 7, 0, 1, 1)
        self.single_save_image = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.single_save_image.setObjectName("single_save_image")
        self.gridLayout.addWidget(self.single_save_image, 7, 1, 1, 1)
        self.back_view = QtWidgets.QGraphicsView(Merge)
        self.back_view.setGeometry(QtCore.QRect(330, 30, 281, 251))
        self.back_view.setObjectName("back_view")
        self.label_7 = QtWidgets.QLabel(Merge)
        self.label_7.setGeometry(QtCore.QRect(470, 290, 53, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Merge)
        self.label_8.setGeometry(QtCore.QRect(660, 290, 53, 16))
        self.label_8.setObjectName("label_8")
        self.fore_view = QtWidgets.QGraphicsView(Merge)
        self.fore_view.setGeometry(QtCore.QRect(640, 30, 281, 251))
        self.fore_view.setObjectName("fore_view")
        self.merge_view = QtWidgets.QGraphicsView(Merge)
        self.merge_view.setGeometry(QtCore.QRect(330, 310, 301, 261))
        self.merge_view.setObjectName("merge_view")
        self.label_9 = QtWidgets.QLabel(Merge)
        self.label_9.setGeometry(QtCore.QRect(440, 590, 53, 16))
        self.label_9.setObjectName("label_9")
        self.show_images = QtWidgets.QPushButton(Merge)
        self.show_images.setGeometry(QtCore.QRect(40, 300, 75, 24))
        self.show_images.setObjectName("show_images")
        self.merge_images = QtWidgets.QPushButton(Merge)
        self.merge_images.setGeometry(QtCore.QRect(130, 300, 75, 24))
        self.merge_images.setObjectName("merge_images")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Merge)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 330, 241, 218))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fore_dir = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.fore_dir.setObjectName("fore_dir")
        self.gridLayout_2.addWidget(self.fore_dir, 3, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fore_factors_l = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.fore_factors_l.setObjectName("fore_factors_l")
        self.horizontalLayout_4.addWidget(self.fore_factors_l)
        self.fore_factors_r = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.fore_factors_r.setObjectName("fore_factors_r")
        self.horizontalLayout_4.addWidget(self.fore_factors_r)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 8, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 7, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 5, 0, 1, 1)
        self.file_pre = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.file_pre.setObjectName("file_pre")
        self.gridLayout_2.addWidget(self.file_pre, 6, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fore_num_l = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.fore_num_l.setProperty("value", 1)
        self.fore_num_l.setObjectName("fore_num_l")
        self.horizontalLayout_5.addWidget(self.fore_num_l)
        self.fore_num_r = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.fore_num_r.setProperty("value", 2)
        self.fore_num_r.setObjectName("fore_num_r")
        self.horizontalLayout_5.addWidget(self.fore_num_r)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)
        self.save_dir = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.save_dir.setObjectName("save_dir")
        self.gridLayout_2.addWidget(self.save_dir, 5, 1, 1, 1)
        self.back_dir = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.back_dir.setObjectName("back_dir")
        self.gridLayout_2.addWidget(self.back_dir, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 6, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 8, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fore_alphas_l = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.fore_alphas_l.setObjectName("fore_alphas_l")
        self.horizontalLayout_3.addWidget(self.fore_alphas_l)
        self.fore_alphas_r = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.fore_alphas_r.setObjectName("fore_alphas_r")
        self.horizontalLayout_3.addWidget(self.fore_alphas_r)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 7, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 2, 0, 1, 1)
        self.back_use_num = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.back_use_num.setMaximum(9999)
        self.back_use_num.setProperty("value", 10)
        self.back_use_num.setObjectName("back_use_num")
        self.gridLayout_2.addWidget(self.back_use_num, 2, 1, 1, 1)
        self.batch_merge_images = QtWidgets.QPushButton(Merge)
        self.batch_merge_images.setGeometry(QtCore.QRect(210, 560, 75, 24))
        self.batch_merge_images.setObjectName("batch_merge_images")
        self.save_image = QtWidgets.QPushButton(Merge)
        self.save_image.setGeometry(QtCore.QRect(210, 300, 75, 24))
        self.save_image.setObjectName("save_image")
        self.label_on = QtWidgets.QCheckBox(Merge)
        self.label_on.setGeometry(QtCore.QRect(30, 560, 71, 20))
        self.label_on.setChecked(True)
        self.label_on.setObjectName("label_on")
        self.clear_dir = QtWidgets.QPushButton(Merge)
        self.clear_dir.setGeometry(QtCore.QRect(110, 560, 75, 24))
        self.clear_dir.setObjectName("clear_dir")

        self.retranslateUi(Merge)
        QtCore.QMetaObject.connectSlotsByName(Merge)

    def retranslateUi(self, Merge):
        _translate = QtCore.QCoreApplication.translate
        Merge.setWindowTitle(_translate("Merge", "Dialog"))
        self.groupBox.setTitle(_translate("Merge", "图片合并"))
        self.label.setText(_translate("Merge", "背景图片"))
        self.label_2.setText(_translate("Merge", "前景图片"))
        self.label_4.setText(_translate("Merge", "位置"))
        self.label_3.setText(_translate("Merge", "透明度"))
        self.back_pos_w.setText(_translate("Merge", "0"))
        self.back_pos_h.setText(_translate("Merge", "0"))
        self.back_path.setText(_translate("Merge", "back/bg01.png"))
        self.back_padding.setText(_translate("Merge", "启用,批量默认关"))
        self.label_5.setText(_translate("Merge", "缩放"))
        self.label_6.setText(_translate("Merge", "背景图扩充"))
        self.fore_path.setText(_translate("Merge", "fore/fore_1.png"))
        self.label_15.setText(_translate("Merge", "保存路径"))
        self.single_save_image.setText(_translate("Merge", "merge/single_image.png"))
        self.label_7.setText(_translate("Merge", "背景"))
        self.label_8.setText(_translate("Merge", "前景"))
        self.label_9.setText(_translate("Merge", "合并"))
        self.show_images.setText(_translate("Merge", "显示图片"))
        self.merge_images.setText(_translate("Merge", "合并图片"))
        self.fore_dir.setText(_translate("Merge", "fore"))
        self.fore_factors_l.setText(_translate("Merge", "0.5"))
        self.fore_factors_r.setText(_translate("Merge", "2"))
        self.label_17.setText(_translate("Merge", "前景个数"))
        self.label_13.setText(_translate("Merge", "透明度"))
        self.label_10.setText(_translate("Merge", "背景目录"))
        self.label_12.setText(_translate("Merge", "合并目录"))
        self.file_pre.setText(_translate("Merge", "{time}_{num}_{size}"))
        self.save_dir.setText(_translate("Merge", "merge"))
        self.back_dir.setText(_translate("Merge", "back"))
        self.label_16.setText(_translate("Merge", "文件前缀"))
        self.label_14.setText(_translate("Merge", "缩放"))
        self.fore_alphas_l.setText(_translate("Merge", "0.5"))
        self.fore_alphas_r.setText(_translate("Merge", "1"))
        self.label_11.setText(_translate("Merge", "前景目录"))
        self.label_18.setText(_translate("Merge", "背景数量"))
        self.batch_merge_images.setText(_translate("Merge", "批量合并"))
        self.save_image.setText(_translate("Merge", "保存图片"))
        self.label_on.setText(_translate("Merge", "数据标注"))
        self.clear_dir.setText(_translate("Merge", "清空文件夹"))
