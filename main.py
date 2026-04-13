from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class MasterAnkitAI(App):
    def build(self):
        # Full Black Hacker Style Background
        Window.clearcolor = (0, 0, 0, 1)
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # 1. Main Title
        self.layout.add_widget(Label(text='[ MASTER ANKIT AI ]', font_size='30sp', color=(0, 1, 0, 1)))
        
        # 2. Security Section
        self.layout.add_widget(Label(text='ENTER SECURITY KEY:', color=(1, 1, 1, 1)))
        self.key_input = TextInput(password=True, multiline=False, size_hint=(1, 0.2))
        self.layout.add_widget(self.key_input)
        
        self.verify_btn = Button(text='VERIFY ACCESS', background_color=(0, 1, 0, 1), size_hint=(1, 0.3))
        self.verify_btn.bind(on_press=self.check_key)
        self.layout.add_widget(self.verify_btn)
        
        self.status_label = Label(text='STATUS: WAITING...', color=(1, 1, 0, 1))
        self.layout.add_widget(self.status_label)
        
        return self.layout

    def check_key(self, instance):
        # Tera Final Password: ANKIT915340
        if self.key_input.text == "ANKIT915340":
            self.layout.clear_widgets()
            # Tere 4 Pillars (Charon Maangi hui Chizein)
            self.layout.add_widget(Label(text='[ ACCESS GRANTED ]', font_size='30sp', color=(0, 1, 0, 1)))
            self.layout.add_widget(Label(text='SYSTEM STATUS: ACTIVE', font_size='20sp'))
            self.layout.add_widget(Label(text='SIGNAL BOOST: 102.0%', font_size='40sp', color=(0, 1, 0, 1)))
            self.layout.add_widget(Label(text='LOCATION: MAHESHTALA', font_size='20sp'))
            self.layout.add_widget(Label(text='DEVELOPER: ANKIT (PRO)', color=(0, 1, 1, 1)))
        else:
            # Galat password par Access Denied
            self.status_label.text = "ACCESS DENIED! WRONG KEY."
            self.status_label.color = (1, 0, 0, 1)

if __name__ == '__main__':
    MasterAnkitAI().run()
          
