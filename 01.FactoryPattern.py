from abc import ABC, abstractmethod


class Button(ABC):


    @abstractmethod
    def on_click(self):
        pass

class WindowsButton(Button):
    def on_click(self):
        print("Clicking Windows Button")

class WebButton(Button):
    def on_click(self):
        print("Clicking Web Button")

class Modal():
    
    @abstractmethod
    def create_button(self):
        pass
    
    
    def render(self):
        btn = self.create_button()
        btn.on_click() 


class WindowModal(Modal):
    
    def create_button(self):
        button = WindowsButton()
        return button


class WebModal(Modal):
    def create_button(self):
        button = WebButton()
        return button


modal1 = WindowModal()
modal1.render()
modal2 = WebModal()
modal2.render()
