from kivy.lang import Builder
from plyer import notification
from kivymd.uix.button import MDRectangleFlatButton, MDFloatingActionButton
from kivymd.uix.toolbar import MDBottomAppBar, MDToolbar
from kivymd.uix.toolbar import MDIconButton
import random
Window.size = (300, 500)


#KV FILE


#TASK FIELDS
TaskField1 = """
MDTextField:
    hint_text: "Enter task 3"
    icon_right: "calendar-clock"
    icon_right_color: app.theme_cls.primary_color
    pos: 0, 300
    size_hint_x:None
    width:300
"""

TaskField2 = """
MDTextField:
    hint_text: "Enter task 4"
    icon_right: "calendar-clock"
    icon_right_color: app.theme_cls.primary_color
    pos: 0, 250
    size_hint_x:None
    width:300
"""

TaskField3 = """
MDTextField:
    hint_text: "Enter task 5"
    icon_right: "calendar-clock"
    icon_right_color: app.theme_cls.primary_color
    pos: 0, 200
    size_hint_x:None
    width:300
"""

TaskField4 = """
MDTextField:
    hint_text: "Enter task 2"
    icon_right: "calendar-clock"
    icon_right_color: app.theme_cls.primary_color
    pos: 0, 350
    size_hint_x:None
    width:300
"""

TaskField5 = """
MDTextField:
    hint_text: "Enter task 1"
    icon_right: "calendar-clock"
    icon_right_color: app.theme_cls.primary_color
    pos: 0, 400
    size_hint_x:None
    width:300
"""



#END

#DESIGN  (KV)
tbar = """
Screen:
    BoxLayout:
        MDBottomAppBar:
            MDToolbar:
                icon: 'bell-ring'
                type: 'bottom'
                left_action_items: [["exit-to-app", lambda x: app.exitapp()]]
                right_action_items: [["switch", lambda x:app.changeThemeoftoolbar(object)]]
                on_action_button: app.show_data(object), app.show_data1(object), app.show_data2(object), app.show_data3(object), app.show_data4(object)
"""


#END
	@@ -89,61 +132,26 @@

class SaveItForLaterApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        screen = Screen()

        self.iconDarkmode = MDIconButton(icon="brightness-1", pos=(0,75), user_font_size="24sp", on_release=self.darkmode)

#TXT FIELDS
        self.field1 = Builder.load_string(TaskField1)
        self.field2 = Builder.load_string(TaskField2)
        self.field3 = Builder.load_string(TaskField3)
        self.field4 = Builder.load_string(TaskField4)
        self.field5 = Builder.load_string(TaskField5)
        self.Toolb = Builder.load_string(tbar)
#ADD TO WIDGETS
        screen.add_widget(self.field1)
        screen.add_widget(self.field2)
        screen.add_widget(self.field3)
        screen.add_widget(self.field4)
        screen.add_widget(self.field5)


        screen.add_widget(self.Toolb)
        screen.add_widget(self.iconDarkmode)


        return screen

#FUNCTIONS
    def show_data(self, obj):
        notification.notify(title="Task 1", message=self.field1.text, timeout=10)

    def show_data1(self, obj):
        notification.notify(title="Task 2", message=self.field2.text, timeout=10)

    def show_data2(self, obj):
        notification.notify(title="Task 3", message=self.field3.text, timeout=10)

    def show_data3(self, obj):
        notification.notify(title="Task 4", message=self.field4.text, timeout=10)

    def show_data4(self, obj):
        notification.notify(title="Task 5", message=self.field5.text, timeout=10)



    def exitapp(self):
        SaveItForLaterApp().stop()

    def darkmode(self, obj):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"

    def changeThemeoftoolbar(self, obj):
        colorsfortheme = ["Green", "DeepOrange", "Purple", "Blue", "Red", "Pink", "Orange", "Cyan", "Teal"]
        randomcolor = random.choice(colorsfortheme)
        self.theme_cls.primary_palette = randomcolor
SaveItForLaterApp().run()
