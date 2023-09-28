from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.lang import Builder
from plyer import notification
from kivymd.uix.button import MDRectangleFlatButton, MDFloatingActionButton
from kivymd.uix.button import MDIconButton
import random
Window.size = (300, 500)
#https://gitlab.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py#L4
Personal = '''
MDFillRoundFlatIconButton:
    text: "                           Private | Personal                    "
    icon: "information"
    pos: 0, 260
    size_hint_y: 0.15
    width:300
    height: 250
'''

School = '''
MDFillRoundFlatIconButton:
    text: "                                Public | School                     "
    icon: "school"
    pos: 0, 180
    size_hint_y: 0.15
    width:300
    height: 250
'''
Festival = '''
MDFillRoundFlatIconButton:
    text: "                           Public | Festival                       "
    icon: "microphone"
    pos: 0, 100
    size_hint_y: 0.15
    width:300
    height: 250
'''


tbar = ''' 
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "green"
        text_color_active: "white"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Groups'
            icon: 'group'
            badge_icon: "numeric-1"

            MDFillRoundFlatIconButton:
                text: "                           Private | Personal                    "
                icon: "information"
                pos: 0, 260
                size_hint_y: 0.15
                width:300
                height: 250

            MDFillRoundFlatIconButton:
                text: "                                Public | School                     "
                icon: "school"
                pos: 0, 180
                size_hint_y: 0.15
                width:300
                height: 250

            MDFillRoundFlatIconButton:
                text: "                           Public | Festival                       "
                icon: "microphone"
                pos: 0, 100
                size_hint_y: 0.15
                width:300
                height: 250

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Join Group'
            icon: 'reply'


            MDFillRoundFlatIconButton:
                text: "          Create New Group                          "
                icon: "school"
                pos: 10, 300
                size_hint_y: 0.1

            MDFillRoundFlatIconButton:
                text: "          Delete Group                                     "
                icon: "school"
                pos: 10, 235
                size_hint_y: 0.1
            
            MDTextField:
                mode: "round"
                max_text_length: 4
                line_color_focus: "green"
                helper_text: "Enter a Code to join a Group"
                helper_text_mode: "persistent"
                hint_text: "Enter Group Code "
                icon_right: "human-male-female"
                icon_right_color: app.theme_cls.primary_color
                pos: 0, 175
                size_hint_x:None
                width:300

            MDFillRoundFlatIconButton:
                text: "          join          "
                icon: "school"
                pos: 85, 110
                size_hint_y: 0.1



        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Settings'
            icon: 'account-settings'

            MDLabel:
                text: 'Settings'
                halign: 'center'
'''


#END



class SaveItForLaterApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = '300'
        screen = Screen()



#TXT FIELDS
        self.school = Builder.load_string(School)
        self.festival = Builder.load_string(Festival)
        self.personal = Builder.load_string(Personal)
        self.Toolb = Builder.load_string(tbar)
#ADD TO WIDGETS
        screen.add_widget(self.school)
        screen.add_widget(self.festival)
        screen.add_widget(self.personal)

        screen.add_widget(self.Toolb)


        return screen

SaveItForLaterApp().run()
