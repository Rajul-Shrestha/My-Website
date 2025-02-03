from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QTextEdit, QPushButton, QVBoxLayout, QMainWindow, QFileDialog, QVBoxLayout, QMenuBar, QFontDialog, QInputDialog, QToolBar
from PySide6.QtGui import QIcon, QAction, QFont
from PySide6.QtCore import Qt
import sys

class Credits(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Credits")
        self.resize(1000, 568)
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.setText("This application was developed by:\n\nRajul Shrestha\n\nFor academic purposes only.\n\nDevelopment Credits: \n\n Rajul Shrestha, \n\n ChatGpt")
        self.text_edit.setGeometry(10, 10, 1000, 568)
        font = QFont("ADLaM Display", 25)
        self.text_edit.setFont(font)
        self.text_edit.setAlignment(Qt.AlignCenter)
        self.make_bold()
        self.show()
    def make_bold(self):
        # Get the current font from QTextEdit
        current_font = self.text_edit.font()
        
        # Toggle the bold property
        current_font.setBold(True)  # Set to bold
        self.text_edit.setFont(current_font)

class New_Reminder(QMainWindow,):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Reminder")
        self.resize(1000, 568)
        self.text_edit = QTextEdit(self) 
        self.text_edit.setGeometry(10, 100, 980, 420)
        #Creates the menu bar
        Menu_Bar = QMenuBar()
        self.setMenuBar(Menu_Bar)
        #Create the File Menu Bar 
        file_menu = Menu_Bar.addMenu("File")
        #Creating the Actions of the File Menu Bar
        new_action = file_menu.addAction("New File")
        new_action.triggered.connect(self.clear_text)
        save_action = file_menu.addAction("Save")
        save_action.triggered.connect(self.save_text)

        #creates the Home Tool Bar
        self.Home_Tool_bar= QToolBar("Home Tool Bar")
        self.addToolBar(self.Home_Tool_bar)
        self.Home_Tool_bar.setVisible(True)
        #Creating the Actions of the Home Tool Bar
        self.Add_ToolBar_Button()
    def Add_ToolBar_Button(self):
        #Creating the Actions that changes the font
        change_font_action = self.Home_Tool_bar.addAction("Change Font")
        change_font_action.triggered.connect(self.change_font)
        #Creating the Actions that changes the font size
        change_fontsize_action = self.Home_Tool_bar.addAction("Change Font Size")
        change_fontsize_action.triggered.connect(self.change_fontsize)
    def change_fontsize(self):
        size, ok = QInputDialog.getInt(self, "Select Font Size", "Enter Font Size", 12, 1, 200)
        if ok:
            self.text_edit.setFontPointSize(size) 
    def change_font(self):
        font, ok = QFontDialog.getFont(self)
        if ok:
            self.text_edit.setFont(font)    
    def clear_text(self):           #Function that clears the text
        self.text_edit.clear()
    def save_text(self):            #Function that saves the text
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.text_edit.toPlainText())


        #Creates the Close button
        self.button = QPushButton("Close", self)
        self.button.setGeometry(911, 530, 90, 40)
        self.button.clicked.connect(self.close)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reminder")
        self.resize(1000, 568)
        self.text_edit = QTextEdit()
        Font = QFont("ADLaM Display" , 50)
        
        # Creates a button to close the application
        self.button = QPushButton("Credits", self)
        self.text_edit.setFont(Font)
        self.button.setGeometry(400, 250, 200, 80)
        self.button.clicked.connect(self.open_credits)
        
        # Creates a button to open the new reminder window
        self.button = QPushButton("New Reminder", self)
        self.button.setGeometry(400, 100, 200, 80)
        self.button.clicked.connect(self.open_new_reminder)
        
    def open_new_reminder(self):
    
        self.close()
        self.new_reminder = New_Reminder()
        self.new_reminder.show()
    def open_credits(self):
        self.close()
        self.credits = Credits()
        self.credits.show()
def run_application():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_application()
