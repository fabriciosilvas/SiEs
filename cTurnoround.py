from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QDialog,
)

class cTurnoround(QDialog):

    def __init__(self, turnoround:int, parent=None):
        super(cTurnoround, self).__init__(parent)
        self.setWindowTitle("Turnaround")
        
        self.label = QLabel()
        self.label.setText(f"Turnouround = {turnoround:.2f}")
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        # Set dialog layout
        self.setLayout(layout)
        
if __name__ == "__main__":
    t = cTurnoround(45)
    t.show()