#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author: Paolo De Stefani
# Contact: paolo <at> paolodestefani <dot> it
# Copyright (C) 2026 Paolo De Stefani
# License:
"""Controls

This module groups general customized controls used in forms


"""

# standard library
import os
import decimal

# PySide6
from PySide6.QtCore import QByteArray
from PySide6.QtCore import QBuffer
from PySide6.QtCore import QIODevice
from PySide6.QtCore import Property
from PySide6.QtCore import Signal
from PySide6.QtCore import Qt
from PySide6.QtCore import QLocale
from PySide6.QtCore import QDate
from PySide6.QtCore import QDateTime
from PySide6.QtCore import QSize
from PySide6.QtCore import QPoint
from PySide6.QtCore import QUuid
from PySide6.QtCore import QUrl
from PySide6.QtCore import QRegularExpression
from PySide6.QtCore import QModelIndex
from PySide6.QtCore import QEvent
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QImage
from PySide6.QtGui import QIcon
from PySide6.QtGui import QColor
from PySide6.QtGui import QPainter
from PySide6.QtGui import QPalette
from PySide6.QtGui import QPen
from PySide6.QtGui import QFont
from PySide6.QtGui import QFontMetrics
from PySide6.QtGui import QFontDatabase
from PySide6.QtGui import QTextDocument
#from PySide6.QtGui import QStandardItemModel
from PySide6.QtGui import QStandardItem
from PySide6.QtGui import QCursor
from PySide6.QtGui import QAction
from PySide6.QtGui import QActionGroup
from PySide6.QtWidgets import QStyledItemDelegate
from PySide6.QtWidgets import QCompleter
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QCheckBox
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QSpinBox
from PySide6.QtWidgets import QDoubleSpinBox
from PySide6.QtWidgets import QDateEdit
from PySide6.QtWidgets import QDateTimeEdit
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QFontComboBox
from PySide6.QtWidgets import QTextEdit
from PySide6.QtWidgets import QDataWidgetMapper
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QToolBar
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QInputDialog
from PySide6.QtWidgets import QTableView
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QMenu

# application modules
from App import session
from App import currentIcon
from App.System.Utility import _tr
from App.System.Utility import string_encode
from App.System.Utility import string_decode
#from App.Database.AbstractModels.TableModels import LookUpQueryModel
#from App.Database.Models import LookUpMunicipalityModel
#from App.Widgets.LookUpDialog import LookUpDialog


#class PCompleter(QCompleter):
    #def pathFromIndex(self, index):
        #text = index.sibling(index.row(), 0).data()
        #return str(text) # could be a different type


#class LookUpLineEdit(QLineEdit):
    #"""
    #Custom lineedit with lookup/zoom feature for code/description using a completer.
    #It requires that the code is a string of fixed length and the QLineEdit has
    #a max length equal to the lent of the code returned. The description is
    #truncated by the completer so no need to find code from description only
    #create a string list (from a custom model) that include
    #code + ' ' + description
    #"""

    #def __init__(self, parent):
        #super().__init__(parent)
        ## set search completer
        #self.luc = PCompleter(self)
        #self.luc.setCompletionMode(QCompleter.PopupCompletion)
        #self.luc.setCaseSensitivity(Qt.CaseInsensitive)
        #self.luc.setFilterMode(Qt.MatchContains)
        #self.luc.setWrapAround(False)
        #self.luc.setMaxVisibleItems(15)
        #self.luc.popup().setMinimumWidth(300)
        #font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        #self.luc.popup().setFont(font)
        #self.setCompleter(self.luc)
        #self.lookupAction = QAction()
        #self.lookupAction.setIcon(currentIcon['system_zoom'])
        #self.lookupAction.triggered.connect(self.lookUp)
        #self.addAction(self.lookupAction, QLineEdit.TrailingPosition)
        #self.editingFinished.connect(self.checkText)

    #def setCompleterModel(self, completerModel):
        #self.completerModel = completerModel
        #self.luc.setModel(self.completerModel)
        #self.luc.setCompletionColumn(1)
        #self.luc.setCompletionRole(Qt.DisplayRole)

    #def setForm(self, title, form):
        #self.formTitle = title
        #self.form = form

    #def focusInEvent(self, event):
        #"Update completer model on focus in"
        #super().focusInEvent(event)
        #self.completerModel.update()

    #def checkText(self):
        #if self.text():
            #if self.text() not in (self.completerModel.data(self.completerModel.index(i, 0))
                                   #for i in range(self.completerModel.rowCount())):
                #self.clear()
                #self.setFocus()

    #def lookUp(self):
        #session['mainwin'].addSubTab(self.formTitle, self.form())


#class LookUpLineEdit2(QLineEdit):
    #"""
    #Custom lineedit with lookup/zoom feature for code/description
    #"""

    #def __init__(self, parent):
        #super().__init__(parent)
        #self.lookupAction = QAction()
        #self.lookupAction.setIcon(currentIcon['system_zoom'])
        #self.menu = QMenu(self)
        #self.a1 = QAction('Prima voce')
        #self.a2 = QAction('Seconda voce')
        #self.menu.addAction(self.a1)
        #self.menu.addAction(self.a2)
        #self.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.customContextMenuRequested.connect(self.customContextMenuEvent)
        #self.lookupAction.triggered.connect(self.lookUp)
        #self.addAction(self.lookupAction, QLineEdit.TrailingPosition)
        #self.editingFinished.connect(self.checkText)

    #def customContextMenuEvent(self):
        ##self.menu.exec_(QCursor.pos())
        #self.menu.exec_(self.mapToGlobal(QPoint(0, 0)))

    #def setForm(self, title, form):
        #self.formTitle = title
        #self.form = form

    #def checkText(self):
        #if text := self.text():
            #model = LookUpMunicipalityModel()
            #model.setParameter('filter_text', f"%{text}%")
            #model.select()
            #if model.rowCount() == 1:
                #self.setText(model.index(0, 0).data())
            #else:
                #dialog = LookUpDialog(self)
                #dialog.tableView.setModel(model)
                #dialog.exec_()
            ##self.clear()
            ##self.setFocus()

    #def lookUp(self):
        #pass
        ##self.menu.show()
        ##session['mainwin'].addSubTab(self.formTitle, self.form())




class LabelImage(QLabel):

    imageChanged=Signal()

    @Property("QVariant", notify=imageChanged) # for handle Null/None values we must use a QVariant for all properties
    def imageBytearray(self):
        ba = QByteArray()
        buf = QBuffer(ba)
        buf.open(QIODevice.WriteOnly)
        if self.pixmap():
            self.pixmap().save(buf, "PNG")
            return buf.data()
        else:
            return None

    @imageBytearray.setter
    def imageBytearray(self, ba):
        #print(type(ba))
        if ba:
            pix = QPixmap()
            pix.loadFromData(ba)
            super().setPixmap(pix)
        else:
            self.clear()

    def clear(self):
        super().clear()
        self.setText(_tr("Controls", "NO IMAGE"))


class SpinBoxDecimal(QDoubleSpinBox):

    valueChanged=Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setSpecialValueText("--")
        self.setMinimum(-999999999999.99) # specialValueText is shown when value = minimum
        self.setRange(-999999999999.99, 999999999999.99)
        self.setAlignment(Qt.AlignRight)

    def fixup(self, text):
        # if input is invalid set specialValueText = Null
        self.setValue(self.minimum())

    @Property("QVariant", notify=valueChanged) # for handle Null/None values we must use a QVariant for all properties
    def modelDataDecimal(self):
        if self.value() == self.minimum():
            return None
        else:
            return decimal.Decimal(str(self.value())) # floaf to string to decimal for keep rounded values

    @modelDataDecimal.setter
    def modelDataDecimal(self, value):
        if value is None:
            value = self.minimum()
        self.setValue(float(value))


class SpinBoxInt(QSpinBox):

    valueChanged=Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setSpecialValueText("--")
        self.setMinimum(-999999999) # specialValueText is shown when value = minimum
        self.setRange(-999999999, 999999999)
        self.setAlignment(Qt.AlignRight)

    @Property("QVariant", notify=valueChanged) # for handle Null/None values we must use a QVariant for all properties
    def modelDataInt(self):
        if self.value() == self.minimum():
            return None
        else:
            return self.value()

    @modelDataInt.setter
    def modelDataInt(self, value):
        if value is None:
            value = self.minimum()
        self.setValue(int(value))


class CheckBox(QCheckBox):

    checkStateChanged=Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setTristate(True)

    @Property("QVariant", notify=checkStateChanged) # for handle Null/None values we must use a QVariant for all properties
    def modelDataState(self):
        if self.checkState() == Qt.Checked:
            return True
        elif self.checkState() == Qt.Unchecked:
            return False
        else:
            return None

    @modelDataState.setter
    def modelDataState(self, value):
        if value is True:
            self.setCheckState(Qt.Checked)
        elif value is False:
            self.setCheckState(Qt.Unchecked)
        else:
            self.setCheckState(Qt.PartiallyChecked)


class DateEdit(QLineEdit):
    "A line edit for date input that accepts Null values"

    dateChanged=Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setInputMask('00/00/0000;_')
        #self.textEdited.connect(self.adjustDate)

    def keyPressEvent(self, keyEvent):
        if keyEvent.text() in ('d', 'D'):
            self.setDate(QDate().currentDate())
        elif keyEvent.text() == '+':
            if date := self.date():
                self.setDate(date.addDays(1))
        elif keyEvent.text() == '-':
            if date := self.date():
                self.setDate(date.addDays(-1))
        else:
            super().keyPressEvent(keyEvent)

    def date(self):
        "Returns a date object or None, autocomplete month and year if omitted"
        date = self.text()
        if date == '//':  # no date entered
            return None
        d, m, y = date.split('/')
        if not d:
            d = 0
        if not m:
            m = QDate().currentDate().month()
        if not y:
            y = QDate().currentDate().year()
        date = QDate(int(y), int(m), int(d))
        if date.isValid():
            return date
        else:
            self.setText('//')
            return None

    def setDate(self, date):
        "Set date in the line edit"
        if date:
            self.setText(date.toString(QLocale.system().toString(date, QLocale.ShortFormat)))
        else:
            self.setText("")

    @Property("QVariant", notify=dateChanged)  # for handle Null/None values we must use a QVariant for all properties
    def modelDataDate(self):
        return self.date()

    @modelDataDate.setter
    def modelDataDate(self, value):
        self.setDate(value)


class DateTimeEdit(QDateTimeEdit):
    "A QDateTimeEdit class that accepts Null values"

    dateTimeChanged=Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setSpecialValueText(" ")
        self.setMinimumDateTime(QDateTime(1800, 1, 1, 0, 0, 0))

    def fixup(self, text):
        # if input is invalid set specialValueText = Null
        self.setDateTime(self.minimumDateTime())

    @Property("QVariant", notify=dateTimeChanged) # for handle Null/None values we must use a QVariant for all properties
    def modelDataDateTime(self):
        if self.dateTime() == self.minimumDateTime():
            return None
        else:
            return self.dateTime()

    @modelDataDateTime.setter
    def modelDataDateTime(self, value):
        if value is None:
            self.setDateTime(QDateTime(1800, 1, 1, 0, 0, 0)) # minimum date
        else:
            self.setDateTime(value)


class RelationalComboBox(QComboBox):
    """QComboBox that uses userData + itemText for key-value foreign key
    or set/get items from a (k, v) list. Can be Null. If available can use icon too"""

    itemChanged=Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.sqlFunc = None
        self.nullable = False
        
    def setNullable(self, nullable):
        self.nullable = nullable

    def setFunction(self, sqlFunc):
        "Store key/value function and update the list"
        self.sqlFunc = sqlFunc
        self.updateList()

    def updateList(self):
        self.clear()
        data = self.sqlFunc()
        #print(data)
        if data:
            if len(data[0]) == 3:  # items with icon
                if self.nullable:
                    for i, v, k in [(QIcon(), None, None)] + data:
                        self.addItem(i, k, v)
                else:
                    for i, v, k in data:
                        self.addItem(i, k, v)
            else:                  # items without icon
                if self.nullable:
                    for v, k in [(None, None)] + data:
                        self.addItem(k, v)
                else:
                    for v, k in data:
                        self.addItem(k, v)

    def setItemList(self, items):
        self.clear()
        if items:
            if len(items[0]) == 3:  # items with icon
                for i, v, k in items:
                    self.addItem(i, k, v)
            else:                   # items without icon
                for v, k in items:
                    self.addItem(k, v)

    def showPopup(self):
        "Update key/value list before show popup request"
        if self.sqlFunc:
            self.updateList()
        super().showPopup()

    @Property("QVariant", notify=itemChanged)
    def modelDataInt(self):
        if not self.currentData(Qt.UserRole):
            return None
        else:
            return int(self.currentData(Qt.UserRole))

    @modelDataInt.setter
    def modelDataInt(self, data):
        index = self.findData(data)
        self.setCurrentIndex(index if index >= 0 else 0) # can be -1 on New

    @Property("QVariant", notify=itemChanged)
    def modelDataStr(self):
        return self.currentData(Qt.UserRole)

    @modelDataStr.setter
    def modelDataStr(self, data):
        index = self.findData(data, Qt.UserRole, Qt.MatchExactly|Qt.MatchCaseSensitive)
        self.setCurrentIndex(index if index >= 0 else 0) # can be -1 on New
        

class DataWidgetMapper(QDataWidgetMapper):
    "Subclass of QDataWidgetMapper that commit data on combobox change, workaround for comboboxes on MacOS that not get focusOut event properly"
    
    def addMapping(self, widget, section, propertyName=None):
        if propertyName is None:
            super().addMapping(widget, section)
        else:
            super().addMapping(widget, section, propertyName)

        if isinstance(widget, QComboBox):
            delegate = self.itemDelegate()
            widget.currentIndexChanged.connect(lambda: delegate.commitData.emit(widget))


class ColorComboBox(QComboBox):
    """QComboBox that uses userData + itemText for key-value foreign key
    or set/get items from a (k, v) list"""

    itemChanged=Signal()

    def setColorList(self, colors):
        self.clear()
        for v, k in colors:
            pix = QPixmap(24, 24)
            pix.fill(QColor(v))
            painter = QPainter(pix)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(QPen(Qt.black, 1))
            painter.drawRect(pix.rect())
            self.addItem(QIcon(pix), k, v)
            painter.end()
            
    def currentColor(self):
        return self.currentData(Qt.UserRole)
    
    def setCurrentColor(self, color):
        index = self.findData(color)
        self.setCurrentIndex(index if index >= 0 else 0)  # can be -1 on New

    @Property("QVariant", notify=itemChanged)
    def modelDataStr(self):
        return self.currentData(Qt.UserRole)

    @modelDataStr.setter
    def modelDataStr(self, data):
        index = self.findData(data)
        self.setCurrentIndex(index if index >= 0 else 0)  # can be -1 on New


class CheckableComboBox(QComboBox):

    # Subclass Delegate to increase item height
    class Delegate(QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(20)
            return size

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make the combo editable to set a custom text, but readonly
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        # Make the lineedit the same color as QPushButton
        #palette = QApplication.palette(QPushButton())
        #palette.setBrush(QPalette.Base, palette.button())
        #self.lineEdit().setPalette(palette)

        # Use custom delegate
        self.setItemDelegate(CheckableComboBox.Delegate())

        # Update the text when an item is toggled
        self.model().dataChanged.connect(self.updateText)

        # Hide and show popup when clicking the line edit
        self.lineEdit().installEventFilter(self)
        self.closeOnLineEditClick = False

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

    def resizeEvent(self, event):
        # Recompute text to elide as needed
        self.updateText()
        super().resizeEvent(event)

    def eventFilter(self, object, event):

        if object == self.lineEdit():
            if event.type() == QEvent.MouseButtonRelease:
                if self.closeOnLineEditClick:
                    self.hidePopup()
                else:
                    self.showPopup()
                return True
            return False

        if object == self.view().viewport():
            if event.type() == QEvent.MouseButtonRelease:
                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())

                if item.checkState() == Qt.Checked:
                    item.setCheckState(Qt.Unchecked)
                else:
                    item.setCheckState(Qt.Checked)
                return True
        return False

    def showPopup(self):
        super().showPopup()
        # When the popup is displayed, a click on the lineedit should close it
        self.closeOnLineEditClick = True

    def hidePopup(self):
        super().hidePopup()
        # Used to prevent immediate reopening when clicking on the lineEdit
        self.startTimer(100)
        # Refresh the display text when closing
        self.updateText()

    def timerEvent(self, event):
        # After timeout, kill timer, and reenable click on line edit
        self.killTimer(event.timerId())
        self.closeOnLineEditClick = False

    def updateText(self):
        texts = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                texts.append(self.model().item(i).text())
        text = ", ".join(texts)

        # Compute elided text (with "...")
        metrics = QFontMetrics(self.lineEdit().font())
        elidedText = metrics.elidedText(text, Qt.ElideRight, self.lineEdit().width())
        self.lineEdit().setText(elidedText)

    def addItem(self, text, data=None):
        item = QStandardItem()
        item.setText(text)
        if data is None:
            item.setData(text)
        else:
            item.setData(data)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setData(Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)

    def addItems(self, texts, datalist=None):
        for i, text in enumerate(texts):
            try:
                data = datalist[i]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)

    def currentData(self):
        # Return the list of selected items data
        res = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                res.append(self.model().item(i).data())
        return res

    def deselectAll(self):
        for i in range(self.model().rowCount()):
            self.model().item(i).setCheckState(Qt.Unchecked)


class PasswordLineEdit(QLineEdit):
    """A QLineEdit that encrypt text"""

    textChanged=Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setEchoMode(QLineEdit.Password)
        self.setClearButtonEnabled(True)
        self.setPlaceholderText(_tr("controls", "Type the password here"))

    @Property("QVariant", notify=textChanged)
    def modelDataEncrypt(self):
        return string_encode(self.text())

    @modelDataEncrypt.setter
    def modelDataEncrypt(self, data):
        if data:
            self.setText(string_decode(data))


class ColorSetComboBox(QComboBox):
    "A combobox with a predefined set of colors"

    currentColorChanged = Signal('QColor')

    def __init__(self, parent):
        super().__init__(parent)
        self.colors = ((Qt.transparent, _tr("Controls", "Transparent")),
                       (Qt.black, _tr("Controls", "Black")),
                       (Qt.red, _tr("Controls", "Red")),
                       (Qt.darkRed, _tr("Controls", "Dark red")),
                       (Qt.green, _tr("Controls", "Green")),
                       (Qt.darkGreen, _tr("Controls", "Dark green")),
                       (Qt.blue, _tr("Controls", "Blue")),
                       (Qt.darkBlue, _tr("Controls", "Dark blue")),
                       (Qt.cyan, _tr("Controls", "Cyan")),
                       (Qt.darkCyan, _tr("Controls", "Dark cyan")),
                       (Qt.magenta, _tr("Controls", "Magenta")),
                       (Qt.darkMagenta, _tr("Controls", "Dark magenta")),
                       (Qt.yellow, _tr("Controls", "Yellow")),
                       (Qt.darkYellow, _tr("Controls", "Dark yellow")),
                       (Qt.gray, _tr("Controls", "Gray")),
                       (Qt.darkGray, _tr("Controls", "Dark gray")),
                       (Qt.lightGray, _tr("Controls", "Light gray")),
                       (Qt.white, _tr("Controls", "Whyte")))
        self.qtColors = tuple((i[0] for i in self.colors))
        for c, d in self.colors:
            pix = QPixmap(32, 24)
            pix.fill(QColor(c))
            # painter = QPainter(pix)
            # painter.setRenderHint(QPainter.Antialiasing)
            # painter.setPen(QPen(Qt.black, 1))
            # r = pix.rect()
            # painter.drawRect(r)
            self.addItem(QIcon(pix), d, c)
            # painter.end()
        self.currentIndexChanged.connect(self.emitColor)
    def setCurrentColor(self, color):
        return
        if color in self.qtColors:
            self.setCurrentIndex(self.qtColors.index(color))

    def emitColor(self, index):
        color = QColor(self.qtColors[self.currentIndex()])
        self.currentColorChanged.emit(color)


class AccountLineEdit(QLineEdit):
    "A line edit for account code that remove the code separator"

    textChanged=Signal()

    def __init__(self, parent, sep=""):
        super().__init__(parent)
        self.separator = sep

    def setSeparator(self, sep):
        self.separator = sep

    @Property("QVariant", notify=textChanged)
    def modelDataAccount(self):
        return self.text().replace(self.separator, "")

    @modelDataAccount.setter
    def modelDataAccount(self, value):
        super().setText(value)


class TextEdit(QTextEdit):

    def canInsertFromMimeData(self, source):
        if source.hasImage():
            return True
        else:
            return super(TextEdit, self).canInsertFromMimeData(source)

    def insertFromMimeData(self, source):
        cursor = self.textCursor()
        document = self.document()
        if source.hasUrls():
            for u in source.urls():
                file_ext = os.path.splitext(str(u.toLocalFile()))[1].lower()
                if u.isLocalFile() and file_ext in ['.jpg', '.png', '.bmp']:
                    image = QImage(u.toLocalFile())
                    document.addResource(QTextDocument.ImageResource, u, image)
                    cursor.insertImage(u.toLocalFile())
                else:
                    # If we hit a non-image or non-local URL break the loop and fall out
                    # to the super call & let Qt handle it
                    break
            else:
                # If all were valid images, finish here.
                return
        elif source.hasImage():
            image = source.imageData()
            uuid = QUuid.createUuid().toString()
            document.addResource(QTextDocument.ImageResource, QUrl(uuid), image)
            cursor.insertImage(image)
            return
            #image = source.imageData()
            #uuid = QUuid.createUuid().toString()
            #document.addResource(QTextDocument.ImageResource, QUrl(uuid), image)
            # cursor.insertImage(uuid)
            # return
        super(TextEdit, self).insertFromMimeData(source)


class TextEditor(QMainWindow):
    "A main windows used only as text editor"
    FONT_SIZES = [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 24, 36, 48, 64, 72, 96]

    def __init__(self, parent):
        super().__init__(parent)
        self.textEdit = QTextEdit(self)
        # self.textEdit.setTextInteractionFlags(Qt.TextEditable)
        # self.textEdit.setAutoFormatting(QTextEdit.AutoAll)  # automatic bullet list if use *
        # initial setting
        # self.textEdit.setFontFamily(QFont().family())
        # self.textEdit.setFontPointSize(QFont().pointSize())
        # self.textEdit.setFont(QFont())
        # update on selection
        self.textEdit.selectionChanged.connect(self.updateFormat)
        self.setCentralWidget(self.textEdit)
        # TOOLBAR EDIT
        # clear content
        #self.actionClear = QAction("Clear", self)
        #self.actionClear.setIcon(currentIcon["text_clear"])
        #self.actionClear.setToolTip(_tr("Editor", "Clear"))
        # self.actionClear.setShortcut("Ctrl+X")
        #self.actionClear.triggered.connect(self.clearAll)
        # undo
        #self.actionUndo = QAction("Undo", self)
        #self.actionUndo.setIcon(currentIcon["text_undo"])
        #self.actionUndo.setToolTip(_tr("Editor", "Undo last operation"))
        # self.actionUndo.setShortcut("Ctrl+X")
        #self.actionUndo.triggered.connect(self.textEdit.undo)
        # redo
        #self.actionRedo = QAction("Redo", self)
        #self.actionRedo.setIcon(currentIcon["text_redo"])
        #self.actionRedo.setToolTip(_tr("Editor", "Repeat last operation"))
        # self.actionRedo.setShortcut("Ctrl+X")
        #self.actionRedo.triggered.connect(self.textEdit.redo)
        # select all
        #self.actionSelectAll = QAction("Select All", self)
        #self.actionSelectAll.setIcon(currentIcon["text_selectall"])
        #self.actionSelectAll.setToolTip(_tr("Editor", "Select all"))
        # self.actionSelectAll.setShortcut("Ctrl+X")
        #self.actionSelectAll.triggered.connect(self.textEdit.selectAll)
        # cut
        #self.actionCut = QAction("Cut", self)
        #self.actionCut.setIcon(currentIcon["text_cut"])
        #self.actionCut.setToolTip(_tr("Editor", "Cut current selection"))
        # self.actionCut.setShortcut("Ctrl+X")
        #self.actionCut.triggered.connect(self.textEdit.cut)
        # copy
        #self.actionCopy = QAction("Copy", self)
        #self.actionCopy.setIcon(currentIcon["text_copy"])
        #self.actionCopy.setToolTip(_tr("Editor", "Copy current selection"))
        # self.actionCopy.setShortcut("Ctrl+X")
        #self.actionCopy.triggered.connect(self.textEdit.copy)
        # paste
        #self.actionPaste = QAction("Paste", self)
        #self.actionPaste.setIcon(currentIcon["text_paste"])
        #self.actionPaste.setToolTip(_tr("Editor", "Paste on current cursor position"))
        # self.actionPaste.setShortcut("Ctrl+X")
        #self.actionPaste.triggered.connect(self.textEdit.paste)

        #self.toolbarEdit = QToolBar("Edit")
        # set icon size to 0.7 % of current value
        #self.toolbarEdit.setIconSize(QSize(int(self.toolbarEdit.iconSize().width() * 0.7),
        #                                   int(self.toolbarEdit.iconSize().height() * 0.7)))
        #self.addToolBar(self.toolbarEdit)
        #self.toolbarEdit.addAction(self.actionClear)
        #self.toolbarEdit.addAction(self.actionUndo)
        #self.toolbarEdit.addAction(self.actionRedo)
        #self.toolbarEdit.addSeparator()
        #self.toolbarEdit.addAction(self.actionSelectAll)
        #self.toolbarEdit.addAction(self.actionCut)
        #self.toolbarEdit.addAction(self.actionCopy)
        #self.toolbarEdit.addAction(self.actionPaste)

        # TOOLBAR FORMAT
        # font combobox
        self.fontBox = QFontComboBox(self)
        self.fontBox.setEditable(False)
        self.fontBox.setToolTip(_tr("Editor", "Get/set the text font family"))
        # self.fontBox.currentFontChanged.connect(self.updateFont)
        #self.fontBox.currentFontChanged.connect(lambda f: self.textEdit.setFontFamily(f.family()))
        self.fontBox.currentFontChanged.connect(lambda font: self.textEdit.setCurrentFont(font))
        # font size
        self.fontSize = QComboBox(self)
        self.fontSize.addItems([str(s) for s in TextEditor.FONT_SIZES])
        self.fontSize.setToolTip(_tr("Editor", "Get/set the text font size"))
        self.fontSize.currentIndexChanged.connect(lambda s: self.textEdit.setFontPointSize(float(s)))
        # format text color
        self.textColor = ColorSetComboBox(self)
        self.textColor.setToolTip(_tr("Editor", "Text color"))
        self.textColor.currentColorChanged.connect(self.textEdit.setTextColor)
        # format background color
        self.textBackgroundColor = ColorSetComboBox(self)
        self.textBackgroundColor.setToolTip(_tr("Editor", "Text background color\nBlack = Transparent"))
        self.textBackgroundColor.currentColorChanged.connect(self.textEdit.setTextBackgroundColor)
        # format bold
        self.actionBold=QAction("Bold", self)
        self.actionBold.setIcon(currentIcon["text_bold"])
        self.actionBold.setToolTip(_tr("Editor", "Format text as bold"))
        # self.actionBold.setShortcut("Ctrl+X")
        self.actionBold.setCheckable(True)
        self.actionBold.triggered.connect(lambda b: self.textEdit.setFontWeight(QFont.Bold if b else QFont.Normal))
        # format italic
        self.actionItalic=QAction("Italic", self)
        self.actionItalic.setIcon(currentIcon["text_italic"])
        self.actionItalic.setToolTip(_tr("Editor", "Format text as italic"))
        # self.actionItalic.setShortcut("Ctrl+X")
        self.actionItalic.setCheckable(True)
        self.actionItalic.triggered.connect(self.textEdit.setFontItalic)
        # format underline
        self.actionUnderline=QAction("Underline", self)
        self.actionUnderline.setIcon(currentIcon["text_underline"])
        self.actionUnderline.setToolTip(_tr("Editor", "Format text as underline"))
        # self.actionUnderline.setShortcut("Ctrl+X")
        self.actionUnderline.setCheckable(True)
        self.actionUnderline.triggered.connect(self.textEdit.setFontUnderline)
        # format left
        self.actionLeft=QAction("Left", self)
        self.actionLeft.setIcon(currentIcon["text_left"])
        self.actionLeft.setToolTip(_tr("Editor", "Align text left"))
        # self.actionLeft.setShortcut("Ctrl+X")
        self.actionLeft.setCheckable(True)
        self.actionLeft.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignLeft))
        # format center
        self.actionCenter=QAction("Center", self)
        self.actionCenter.setIcon(currentIcon["text_center"])
        self.actionCenter.setToolTip(_tr("Editor", "Align text center"))
        # self.actionCenter.setShortcut("Ctrl+X")
        self.actionCenter.setCheckable(True)
        self.actionCenter.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignCenter))
        # format right
        self.actionRight=QAction("Right", self)
        self.actionRight.setIcon(currentIcon["text_right"])
        self.actionRight.setToolTip(_tr("Editor", "Align text right"))
        # self.actionRight.setShortcut("Ctrl+X")
        self.actionRight.setCheckable(True)
        self.actionRight.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignRight))
        # format justify
        self.actionJustify=QAction("Justify", self)
        self.actionJustify.setIcon(currentIcon["text_justify"])
        self.actionJustify.setToolTip(_tr("Editor", "Justify text"))
        # self.actionJustify.setShortcut("Ctrl+X")
        self.actionJustify.setCheckable(True)
        self.actionJustify.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignJustify))
        formatGroup = QActionGroup(self)
        formatGroup.setExclusive(True)
        for i in (self.actionLeft, self.actionCenter, self.actionRight, self.actionJustify):
            formatGroup.addAction(i)

        self.toolbarFormat = self.addToolBar("Format")
        # set icon size to 0.7 % of current value
        self.toolbarFormat.setIconSize(QSize(int(self.toolbarFormat.iconSize().width() * 0.7),
                                             int(self.toolbarFormat.iconSize().height() * 0.7)))
        self.toolbarFormat.addWidget(self.fontBox)
        self.toolbarFormat.addWidget(self.fontSize)
        self.toolbarFormat.addSeparator()
        self.toolbarFormat.addWidget(self.textColor)
        self.toolbarFormat.addWidget(self.textBackgroundColor)
        self.toolbarFormat.addSeparator()
        self.toolbarFormat.addAction(self.actionBold)
        self.toolbarFormat.addAction(self.actionItalic)
        self.toolbarFormat.addAction(self.actionUnderline)
        self.toolbarFormat.addSeparator()
        self.toolbarFormat.addAction(self.actionLeft)
        self.toolbarFormat.addAction(self.actionCenter)
        self.toolbarFormat.addAction(self.actionRight)
        self.toolbarFormat.addAction(self.actionJustify)

        self.updateFormat()  # initial status

    def clearAll(self):
        "Clear all if confirmed"
        if QMessageBox.question(self,
                                _tr('MessageDialog', "Question"),
                                _tr('Controls', "Are you sure to clear all the text ?"),
                                QMessageBox.Yes | QMessageBox.No,  # butons
                                QMessageBox.No  # default botton
                                ) == QMessageBox.No:
            return
        self.textEdit.clear()

    def updateFormat(self):
        """
        Update the font format toolbar/actions when a new text selection is made. This is neccessary to keep
        toolbars/etc. in sync with the current edit state.
        """
        # Disable signals for all format widgets, so changing values here does not trigger further formatting.
        # We don't need to disable signals for alignment, as they are paragraph-wide
        #print("Selection changes")
        for o in (self.fontBox,
                  self.fontSize, self.textColor,
                  self.textBackgroundColor, self.actionBold,
                  self.actionItalic, self.actionUnderline):
            o.blockSignals(True)

        # self.fontBox.setCurrentFont(self.textEdit.currentFont())
        self.fontSize.setCurrentText(str(int(self.textEdit.fontPointSize())))
        self.textColor.setCurrentColor(self.textEdit.textColor())
        self.textBackgroundColor.setCurrentColor(self.textEdit.textBackgroundColor())
        self.actionBold.setChecked(self.textEdit.fontWeight() == QFont.Bold)
        self.actionItalic.setChecked(self.textEdit.fontItalic())
        self.actionUnderline.setChecked(self.textEdit.fontUnderline())

        self.actionLeft.setChecked(self.textEdit.alignment() == Qt.AlignLeft)
        self.actionCenter.setChecked(self.textEdit.alignment() == Qt.AlignCenter)
        self.actionRight.setChecked(self.textEdit.alignment() == Qt.AlignRight)
        self.actionJustify.setChecked(self.textEdit.alignment() == Qt.AlignJustify)

        for o in (self.fontBox,
                  self.fontSize, self.textColor,
                  self.textBackgroundColor, self.actionBold,
                  self.actionItalic, self.actionUnderline):
            o.blockSignals(False)

    #def updateFont(self, font):
        #size = self.fontSize.currentText()
        #font.setPointSize(int(size))
        #self.textEdit.setCurrentFont(font)

    def toHtml(self):
        return self.textEdit.toHtml()


