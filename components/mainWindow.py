from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)

from data.collectibles import collectibles

class MainWindow(QWidget):
    collectibles = {}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set the window title
        self.setWindowTitle('Y-Tracker')
        self.collectibles = collectibles
        
        # Create & Edit Layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        
        layout.addLayout(hLayout)
        layout.addLayout(vLayout)
        
        self.layout_dict = {}
        self.label_dict = {}
        self.button_dict = {}
        
        # Build the Inputs
        for type in self.collectibles:
            
            if self.collectibles[type]['meta']['orient'] == 'horizontal':
                self.layout_dict[type] = QHBoxLayout()
                vLayout.addLayout(self.layout_dict[type])
                
            else:
                self.layout_dict[type] = QVBoxLayout()
                hLayout.addLayout(self.layout_dict[type])
            
            self.button_dict[type] = {}
            
            for item in self.collectibles[type]:
                
                if item != 'meta':
                    self.button_dict[type][item] = QPushButton()
                    self.button_dict[type][item].setObjectName(f'{type}-{item}')
                    
                    if self.collectibles[type]['meta']['type'] == 'bool':
                        self.button_dict[type][item].setText(self.collectibles[type][item]['name'])
                        
                        if self.collectibles[type][item]['value'] == False:
                            self.button_dict[type][item].setStyleSheet("""
                                QPushButton#""" + self.button_dict[type][item].objectName() + """ {
                                    color: #88FFFFFF
                                }
                                """)
                            
                        else:
                            self.button_dict[type][item].setStyleSheet("""
                                QPushButton#""" + self.button_dict[type][item].objectName() + """ {
                                    color: #FFFFFFFF
                                }
                                """)
                            
                        self.button_dict[type][item].clicked.connect(lambda state, x=[type, item]: boolButtonSelect(self, x[0], x[1]))
                        
                    elif self.collectibles[type]['meta']['type'] == 'int':
                        self.button_dict[type][item].setText(f'{self.collectibles[type][item]["name"]}: {self.collectibles[type][item]["value"]}')
                        self.button_dict[type][item].clicked.connect(lambda state, x=[type, item]: intButtonSelect(self, x[0], x[1]))
                        
                    elif self.collectibles[type]['meta']['type'] == 'list':
                        self.button_dict[type][item].setText(self.collectibles[type]['meta']['list'][self.collectibles[type][item]['value']])
                        self.button_dict[type][item].clicked.connect(lambda state, x=[type, item]: listButtonSelect(self, x[0], x[1]))
                        
                    self.layout_dict[type].addWidget(self.button_dict[type][item])
                
        # Add Events
        def boolButtonSelect(self, type, item):
            if self.collectibles[type][item]['value']:
                self.collectibles[type][item]['value'] = False
                self.button_dict[type][item].setStyleSheet("""
                    QPushButton#""" + self.button_dict[type][item].objectName() + """ {
                        color: #88FFFFFF
                    }
                    """)
            else:
                self.collectibles[type][item]['value'] = True
                self.button_dict[type][item].setStyleSheet("""
                    QPushButton#""" + self.button_dict[type][item].objectName() + """ {
                        color: #FFFFFFFF
                    }
                    """)
        
        def intButtonSelect(self, type, item):
            self.collectibles[type][item]['value'] = self.collectibles[type][item]['value'] + 1
            self.button_dict[type][item].setText(f'{self.collectibles[type][item]["name"]}: {self.collectibles[type][item]["value"]}')

        def listButtonSelect(self, type, item):
            self.collectibles[type][item]['value'] = self.collectibles[type][item]['value'] + 1
            try:
                self.button_dict[type][item].setText(self.collectibles[type]['meta']['list'][self.collectibles[type][item]['value']])
            except:
                self.collectibles[type][item]['value'] = 0
                self.button_dict[type][item].setText(self.collectibles[type]['meta']['list'][self.collectibles[type][item]['value']])
        
        # show the window
        self.show()
        
