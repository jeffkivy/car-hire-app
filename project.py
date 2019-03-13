from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import ScreenManager, Screen,FallOutTransition,SlideTransition,SwapTransition,WipeTransition,FadeTransition,RiseInTransition
import random
from kivy.core.window import Window
from kivy.properties import NumericProperty
#from pymongo import MongoClient
from kivymd.material_resources import DEVICE_TYPE
#client= MongoClient()
#db1=client.users
import datetime
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M")
#Window.size = (325, 580)

kv= '''
#:import Clock kivy.clock.Clock
#:import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import SwapTransition kivy.uix.screenmanager.SwapTransition
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import RiseInTransitverion kivy.uix.screenmanager.RiseInTransition
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDTextField kivymd.textfields.MDTextField
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import Label kivy.uix.button.Label
#:import Button kivy.uix.button.Button
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDCard kivymd.card.MDCard
#:import utils kivy.utils
#:import ListAdapter kivy.adapters.listadapter.ListAdapter
#:import ListItemButton kivy.uix.listview.ListItemButton


#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
ScreenManager: 
    id: main_s
    nav_layout : nav_layout
    Screen:
        id: login
        name:'login'
        main_s: main_s
        BoxLayout:
            orientation:'vertical'                    
            ScreenManager:
                id:top_screen 
                main_s:main_s
                Screen:
                    name: 'top1'
                    FloatLayout:
                        canvas.before:
                            Rectangle:
                                size: self.size
                                pos: self.pos
                                source:'back.jpg'
                        FloatLayout:
                            canvas.before:
                                PushMatrix
                                Rotate:
                                    angle: 0
                                    axis: 0, 0, 1,
                                    origin: self.center
                            canvas.after:
                                PopMatrix
                            Image:
                                source: 'car1.jpg'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                Screen:
                    name: 'top2'
                    FloatLayout:
                        canvas.before:
                            Color:
                                rgba: 1,1,1,1
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        Image:
                            source: 'car3.jpg'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
                            
                Screen:
                    name: 'top3'
                    FloatLayout:
                        canvas.before:
                            Color:
                                rgba: 1,1,1,1
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        Image:
                            source: 'car4.jpg'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                Screen:
                    name: 'top4'
                    FloatLayout:
                        canvas.before:
                            Color:
                                rgba: 1,1,1,1
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        Image:
                            source: 'car5.jpg'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                Screen:
                    name: 'top5'
                    FloatLayout:
                        canvas.before:
                            Color:
                                rgba: 1,1,1,1
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        Image:
                            source: 'car6.jpg'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}                                                   
                                               
            BoxLayout:
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                orientation:'vertical'
                MDCard:
                    size_hint: 1,1
                    BoxLayout:        
                        orientation:'vertical'
                        size_hint:1,1
                        padding: self.height/20
                        spacing:self.height/20
                        MDLabel:
                            text: 'Welcome'
                            theme_text_color: 'Secondary'
                            font_style:"Title"
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                        MDSeparator:
                            height: self.height
                        MDTextField:
                            id: login_user_mobile
                            hint_text: "Mobile number"
                            helper_text_mode: "on_focus"
                            helper_text: "mobile number not registered"
                            helper_text_mode: "on_error"  
                        MDTextField:
                            id: login_password
                            hint_text: "Password "
                            helper_text_mode: "on_focus"
                            password: True
                            helper_text: "password do not match"
                            helper_text_mode: "on_error"  

                        BoxLayout:
                            orientation:'horizontal'    

                            MDFlatButton:
                                size_hint:1,1
                                text: "Login"
                                on_release: app.login()

                            MDFlatButton:
                                size_hint:1,1
                                text: "Register"
                                on_release: app.register() 
    Screen:
        id: register
        name: 'register'
        main_s:main_s  
        BoxLayout:
            orientation: 'vertical'
            MDCard:
                size_hint: 1,1
                BoxLayout:        
                    orientation:'vertical'
                    size_hint:1,1
                    padding: self.height/20
                    spacing:self.height/20
                    MDLabel:
                        text: 'Welcome'
                        theme_text_color: 'Secondary'
                        font_style:"Title"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    MDSeparator:
                        height: self.height

                    MDTextField:
                        id: user_mobile
                        hint_text: "Mobile number "
                        helper_text: "The number has another user"
                        helper_text_mode: "on_focus"

                        helper_text_mode: "on_error"        
                    MDTextField:
                        id: re_username
                        hint_text: "Username "
                        helper_text_mode: "on_focus"
                        helper_text: "no empty username!"
                        helper_text_mode: "on_error"    


                    MDTextField:
                        id: re_password
                        hint_text: "Password "
                        helper_text_mode: "on_focus"
                        helper_text_mode: "on_error"
                        password: True
                    MDTextField:
                        id: re_re_password
                        hint_text: "Repeat Password "
                        helper_text: "password do not match"
                        helper_text_mode: "on_focus"
                        password: True
                        helper_text_mode: "on_error"  
                    BoxLayout:
                        orientation:'horizontal'    
                        MDFlatButton:
                            size_hint:1,1
                            text: "Save"
                            on_release: app.save_user()
    Screen:
        id: home
        main_s:main_s
        nav_layout: nav_layout
        name: 'home'
        NavigationLayout:
            id: nav_layout
            MDNavigationDrawer:
                id: nav_drawer
              
                NavigationDrawerToolbar:
                    title: "Everly Menu"
                   
                NavigationDrawerIconButton:
                    icon: 'checkbox-blank-circle'
                    text: "Lend your car"
                    on_release: app.root.ids.home.main_s.current= 'lend'
                
                
                    
                NavigationDrawerIconButton:
                    icon: 'checkbox-blank-circle'
                    text: "Account"
                    on_release: app.root.ids.home.main_s.current= 'account'
                
                    
                NavigationDrawerIconButton:
                    icon: 'checkbox-blank-circle'
                    text: "About us/help" 
                    
                NavigationDrawerIconButton:
                    icon: 'checkbox-blank-circle'
                    text: "BACK"
                    on_release: app.back_home()                    
               
            BoxLayout:
                orientation:'vertical'
                Toolbar:
                    id: toolbar
                    title: 'Everly Menu'
                    md_bg_color: app.theme_cls.primary_color
                    background_palette: 'Primary'
                    background_hue: '500'
                    left_action_items: [['menu', lambda x: app.root.nav_layout.toggle_nav_drawer()]]
                    right_action_items: [['dots-vertical', lambda x: app.root.nav_layout.toggle_nav_drawer()]]
            
                ScreenManager:
                    id:top_screen 
                    main_s:main_s
                    Screen:
                        name: 'top1'
                        FloatLayout:
                            canvas.before:
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                                    source:'back.jpg'
                            FloatLayout:
                                canvas.before:
                                    PushMatrix
                                    Rotate:
                                        angle: 0
                                        axis: 0, 0, 1,
                                        origin: self.center
                                canvas.after:
                                    PopMatrix
                                Image:
                                    source: 'car1.jpg'
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    Screen:
                        name: 'top2'
                        FloatLayout:
                            canvas.before:
                                Color:
                                    rgba: 1,1,1,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                            Image:
                                source: 'car3.jpg'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
                            
                    Screen:
                        name: 'top3'
                        FloatLayout:
                            canvas.before:
                                Color:
                                    rgba: 1,1,1,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                            Image:
                                source: 'car4.jpg'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    Screen:
                        name: 'top4'
                        FloatLayout:
                            canvas.before:
                                Color:
                                    rgba: 1,1,1,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                            Image:
                                source: 'car5.jpg'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    Screen:
                        name: 'top5'
                        FloatLayout:
                            canvas.before:
                                Color:
                                    rgba: 1,1,1,1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                            Image:
                                source: 'car6.jpg'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}                      

                                                              
                                      
                ScrollView:
                    GridLayout:
                        cols:1
                        BoxLayout:
                            orientation:'horizontal'
                            canvas:
                                Color:
                                    rgba:1,1,1,1
                                Rectangle:
                                    pos:self.pos
                                    size:self.size

                            MDRaisedButton:
                                text: 'personal/family cars  '
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                spacing:0,0
                                font_size:2000
                                on_release: app.root.ids.home.main_s.current= 'personal'
                            FloatLayout:     
                                canvas.before:
                                    PushMatrix
                                    Rotate:    
                                        angle: app.angle
                                        axis: 0, 0,1, 
                                        origin: self.center
                                canvas.after:
                                    PopMatrix
                                Image:
                                    size_hint: .8, .8                     
                                    source: ''
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            BoxLayout:
                                orientation:'horizontal'
                                BoxLayout:
                                    size_hint:.5,.5
                                    orientation:'vertical'
                                    Label:
                                        text:''
                                        color:1,0,0,1

                                    FloatLayout:
                                        canvas:      
                                            Color:
                                                rgb:utils.get_color_from_hex('#db7093')
                                            Ellipse:
                                                pos:self.pos
                                                size:self.height/1.3,self.height/1.3
                                    Label:
                                        text:'L'
                                        color:1,0,0,1            
                                BoxLayout:
                                    size_hint:.5,.5
                                    orientation:'vertical'
                                    Label:
                                        text:''
                                        color:1,0,0,1

                                    FloatLayout:
                                        canvas:      
                                            Color:
                                                rgb:  .5019607843, .5019607843, .5019607843
                                            Ellipse:
                                                pos:self.pos
                                                size:self.height/1.3,self.height/1.3
                                    Label:
                                        text:'N'
                                        color:1,0,0,1            
                                BoxLayout:
                                    size_hint:.5,.5
                                    orientation:'vertical'
                                    Label:
                                        text:''
                                        color:1,0,0,1
                                    FloatLayout:
                                        canvas:      
                                            Color:
                                                rgb:utils.get_color_from_hex('#00ffff')
                                            Ellipse:
                                                pos:self.pos
                                                size:self.height/1.3,self.height/1.3
                                    Label:
                                        text:'M'
                                        color:1,0,0,1            
                        BoxLayout:
                            orientation:'horizontal'
                            canvas:
                                Color:
                                    rgba:0.9411764705,0.9725490196,1,1
                                Rectangle:
                                    pos:self.pos
                                    size:self.size
                            MDRaisedButton:
                                text: 'matatu/buses'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                spacing:0,0
                                font_size:2000
                                on_release: app.root.ids.home.main_s.current= 'matatu'
                            FloatLayout:              
                                Image:
                                    size_hint: .5, .5                     
                                    source: ''
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            BoxLayout:
                                orientation:'horizontal'   
                                FloatLayout:
                                    pos_hint: {'center_x': .8, 'center_y': .8}                            
                                    canvas:      
                                        Color:
                                            rgb:  .5019607843, .5019607843, .5019607843
                                        Ellipse:
                                            pos:self.pos
                                            size:self.height/8,self.height/8
                                FloatLayout:
                                    pos_hint: {'center_x': .8, 'center_y': .8}                            
                                    canvas:  
                                        Color:
                                            rgb:  .5019607843, .5019607843, .5019607843
                                        Ellipse:
                                            pos:self.pos
                                            size:self.height/8,self.height/8 
                                FloatLayout:
                                    pos_hint: {'center_x': .8, 'center_y': .8}                            
                                    canvas:  
                                        Color:
                                            rgb:  .5019607843, .5019607843, .5019607843
                                        Ellipse:
                                            pos:self.pos
                                            size:self.height/8,self.height/8                                 
                        BoxLayout:      
                            orientation:'horizontal'
                            canvas:
                                Color:
                                    rgba:1,1,1,1
                                Rectangle:
                                    pos:self.pos
                                    size:self.size
                            MDRaisedButton:
                                text: 'weeding/funeral vehicles'
                                markup: True   
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                spacing:0,0
                                on_release: app.root.ids.home.main_s.current= 'wedding'
                            FloatLayout:                       
                                Image:
                                    size_hint: 1 ,1                     
                                    source: ''
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            BoxLayout:
                                orientation:'horizontal'     
                                FloatLayout:
                                    pos_hint: {'center_x': .8, 'center_y': .8}                            
                                    canvas:      
                                        Color:
                                            rgb:  .5019607843, .5019607843, .5019607843
                                        Ellipse:
                                            pos:self.pos
                                            size:self.height/8,self.height/8
                                FloatLayout:
                                    pos_hint: {'center_x': .8, 'center_y': .8}                            
                                    canvas:  
                                        Color:
                                            rgb:  .5019607843, .5019607843, .5019607843
                                        Ellipse:
                                            pos:self.pos
                                            size:self.height/8,self.height/8 
                                FloatLayout:
                                    pos_hint: {'center_x': .8, 'center_y': .8}                            
                                    canvas:  
                                        Color:
                                            rgb:  .5019607843, .5019607843, .5019607843
                                        Ellipse:
                                            pos:self.pos
                                            size:self.height/8,self.height/8                                 
                        BoxLayout:
                            canvas:
                                Color:
                                    rgba:0.9411764705,0.9725490196,1,1
                                Rectangle:
                                    size:self.size
                                    pos:self.pos    
                            orientation:'horizontal'
                            MDRaisedButton:
                                text: 'heavy trucks/pick-ups'
                                pos_hint: { 'center_x': 0.5, 'center_y': 0.5}
                                spacing:0,0
                                on_release: app.root.ids.home.main_s.current= 'heavy'
                            FloatLayout:                           
                                Image:
                                    size_hint: .6, .6                     
                                    source: ''
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            BoxLayout:
                                orientation:'horizontal'    
                                FloatLayout:
                                    pos_hint: {'center_x': .8, 'center_y': .8}                            
                                    canvas:      
                                        Color:
                                            rgb:  .5019607843, .5019607843, .5019607843
                                        Ellipse:
                                            pos:self.pos
                                            size:self.height/8,self.height/8
                                FloatLayout:
                                    pos_hint: {'center_x': .8, 'center_y': .8}                            
                                    canvas:  
                                        Color:
                                            rgb:  .5019607843, .5019607843, .5019607843
                                        Ellipse:
                                            pos:self.pos
                                            size:self.height/8,self.height/8 
                                FloatLayout:
                                    pos_hint: {'center_x': .8, 'center_y': .8}                            
                                    canvas:  
                                        Color:
                                            rgb: .5019607843, .5019607843, .5019607843
                                        Ellipse:
                                            pos:self.pos
                                            size:self.height/8,self.height/8                                                                               
    Screen:
        id: personal
        name: 'personal'
        BoxLayout:
            orientation: 'vertical'
            Toolbar:                  
                title: "Back"
                md_bg_color: get_color_from_hex(colors['DeepPurple']['A400'])
                background_palette: 'DeepPurple'
                background_hue: 'A400'
                left_action_items: [['home', lambda x: app.back_home()]]
            ScrollView:
                GridLayout:
                    cols: 1
                    size_hint_y: None
                    height: self.minimum_height
                    row_default_height: root.height*2 
                    BoxLayout:
                        orientation: 'vertical'
                        BoxLayout:
                            orientation: 'vertical'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car3.jpg'
                               
    
                                BoxLayout:
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'TOYOTA HILUX'
                                    MDFlatButton:                   
                                        text:'price: 300ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details'      
                            
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car7.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'HARRIER'
                                    MDFlatButton:                   
                                        text:'price: 300ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details' 
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car7.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'SALOON CAR'
                                    MDFlatButton:                   
                                        text:'price: 100ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details' 
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car2.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'NOAH'
                                    MDFlatButton:                   
                                        text:'price: 300ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details' 
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id:image
                                    source: 'car7.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'VITZ'
                                    MDFlatButton:                   
                                        text:'price: 400ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details'  
                                        
                                                                
    Screen:
        id: matatu
        name: 'matatu'
        BoxLayout:
            orientation: 'vertical'
            Toolbar:                  
                title: "Back"
                md_bg_color: get_color_from_hex(colors['DeepPurple']['A400'])
                background_palette: 'DeepPurple'
                background_hue: 'A400'
                left_action_items: [['home', lambda x: app.back_home()]]
            ScrollView:
                GridLayout:
                    cols: 1
                    size_hint_y: None
                    height: self.minimum_height
                    row_default_height: root.height*2 
                    BoxLayout:
                        orientation: 'vertical'
                        BoxLayout:
                            orientation: 'vertical'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car3.jpg'
                               
    
                                BoxLayout:
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'TOYOTA HILUX'
                                    MDFlatButton:                   
                                        text:'price: 300ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details'      
                            
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car7.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'HARRIER'
                                    MDFlatButton:                   
                                        text:'price: 300ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details' 
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car7.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'SALOON CAR'
                                    MDFlatButton:                   
                                        text:'price: 100ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details' 
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car2.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'NOAH'
                                    MDFlatButton:                   
                                        text:'price: 300ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details' 
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id:image
                                    source: 'car7.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'VITZ'
                                    MDFlatButton:                   
                                        text:'price: 400ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details'
                                        
    Screen:
        id: wedding
        name: 'wedding'
        BoxLayout:
            orientation: 'vertical'
            Toolbar:                  
                title: "Back"
                md_bg_color: get_color_from_hex(colors['DeepPurple']['A400'])
                background_palette: 'DeepPurple'
                background_hue: 'A400'
                left_action_items: [['home', lambda x: app.back_home()]]
            ScrollView:
                GridLayout:
                    cols: 1
                    size_hint_y: None
                    height: self.minimum_height
                    row_default_height: root.height*2 
                    BoxLayout:
                        orientation: 'vertical'
                        BoxLayout:
                            orientation: 'vertical'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car3.jpg'
                               
    
                                BoxLayout:
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'TOYOTA HILUX'
                                    MDFlatButton:                   
                                        text:'price: 300ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details'      
                            
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car7.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'HARRIER'
                                    MDFlatButton:                   
                                        text:'price: 300ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details' 
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car7.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'SALOON CAR'
                                    MDFlatButton:                   
                                        text:'price: 100ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details' 
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car2.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'NOAH'
                                    MDFlatButton:                   
                                        text:'price: 300ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details' 
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id:image
                                    source: 'car7.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'VITZ'
                                    MDFlatButton:                   
                                        text:'price: 400ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details'                          
                                                                                              
    Screen:
        id: heavy
        name: 'heavy'
        BoxLayout:
            orientation: 'vertical'
            Toolbar:                  
                title: "Back"
                md_bg_color: get_color_from_hex(colors['DeepPurple']['A400'])
                background_palette: 'DeepPurple'
                background_hue: 'A400'
                left_action_items: [['home', lambda x: app.back_home()]]
            ScrollView:
                GridLayout:
                    cols: 1
                    size_hint_y: None
                    height: self.minimum_height
                    row_default_height: root.height*2 
                    BoxLayout:
                        orientation: 'vertical'
                        BoxLayout:
                            orientation: 'vertical'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car3.jpg'
                               
    
                                BoxLayout:
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'TOYOTA HILUX'
                                    MDFlatButton:                   
                                        text:'price: 300ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details'      
                            
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car7.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'HARRIER'
                                    MDFlatButton:                   
                                        text:'price: 300ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details' 
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car7.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'SALOON CAR'
                                    MDFlatButton:                   
                                        text:'price: 100ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details' 
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id: image
                                    source: 'car2.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'NOAH'
                                    MDFlatButton:                   
                                        text:'price: 300ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details' 
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    id:image
                                    source: 'car7.jpg'
                                BoxLayout:
                                    orientation: 'vertical'        
                                    padding: 0,0
                                    orientation: 'vertical'        
                                    MDFlatButton:                   
                                        text:'VITZ'
                                    MDFlatButton:                   
                                        text:'price: 400ksh/km'
                                    MDRaisedButton:
                                        text: 'click for more details'                          
                                                                                        
    Screen:
        id: lend
        name: 'lend'
        main_s: main_s
        BoxLayout:
            orientation: 'vertical'
            canvas.before:
                Rectangle:
                    size: self.size
                    pos: self.pos
                    source: 'car2.jpg'
                
            BoxLayout:
                size_hint: 1,.4
                orientation: 'vertical'
                       
                MDRaisedButton:
                    text: 'upload 3 photos' 
            MDCard:
               
                BoxLayout:        
                    orientation:'vertical'
                   
                    padding: self.height/20
                    spacing:self.height/20
                    MDLabel:
                        text: 'Fill in each space'
                        theme_text_color: 'Secondary'
                        font_style:"Title"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    MDSeparator:
                        height: self.height

                    MDTextField:
                        id: model
                        hint_text: "car model "
                        helper_text: "car model does not exist"
                        helper_text_mode: "on_focus"

                        helper_text_mode: "on_error"        
                    MDTextField:
                        id: location
                        hint_text: "Location"
                        helper_text_mode: "on_focus"
                        helper_text: "location does not exist"
                        helper_text_mode: "on_error"    


                    MDTextField:
                        id: description
                        hint_text: "car description"
                        helper_text_mode: "on_focus"
                        helper_text_mode: "on_error"
                        
                    MDTextField:
                        id: price
                        hint_text: "Price per Km"
                        helper_text: "invalid enrty"
                        helper_text_mode: "on_focus"
                        password: True
                        helper_text_mode: "on_error"  
                    BoxLayout:
                        orientation:'horizontal'    
                        MDFlatButton:
                            text: "Save"
                        MDFlatButton:
                            text: "back"
                            on_release: app.back_home()
                            
    Screen:
        id: account
        name: 'account'
        main_s: main_s 
        MDCard:   
            BoxLayout:        
                orientation:'vertical' 
                padding: self.height/20
                spacing:self.height/20
                MDLabel:
                    text: 'account balance:  0.00 '
                    theme_text_color: 'Secondary'
                    font_style:"Title"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDLabel:
                    text: 'Mpesa PAYBILL: 9093029 '
                    theme_text_color: 'Secondary'
                    font_style:"Title"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                BoxLayout:
                    orientation: 'horizontal'                        
                    MDRaisedButton:
                        text: 'Withdraw'
                        theme_text_color: 'Secondary'
                        font_style:"Title"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
                    MDRaisedButton:
                        text: 'auto deposit'
                        theme_text_color: 'Secondary'
                        font_style:"Title"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}                    
                MDSeparator:
                    height: self.height
                BoxLayout:
                    orientation:'horizontal'    
                    MDFlatButton:
                        text: "back"
                        on_release: app.back_home()                                                             
'''
class Everly(App):
    angle = NumericProperty(0)
    def __init__(self, **kwargs):
        super(Everly, self).__init__(**kwargs)
        self.theme_cls = ThemeManager()
        Clock.schedule_once(self.juu1, 0)

    def back_home(self):
        self.root.ids.home.main_s.current='home'


    def juu2(self, *args):
        self.root.ids.top_screen.current = 'top2'
        trans = [FallOutTransition, SlideTransition, SwapTransition,  RiseInTransition,WipeTransition,FadeTransition]
        self.root.ids.top_screen.transition = random.choice(trans)(duration=3)
        Clock.schedule_once(self.juu3, 4)
    def juu1(self, *args):
        self.root.ids.top_screen.current = 'top1'
        trans = [FallOutTransition, SlideTransition, SwapTransition, RiseInTransition,WipeTransition,FadeTransition]
        self.root.ids.top_screen.transition = random.choice(trans)(duration=3)
        Clock.schedule_once(self.juu2, 4)

    def juu3(self, *args):
        self.root.ids.top_screen.current = 'top3'
        trans = [FallOutTransition, SlideTransition, SwapTransition, RiseInTransition,WipeTransition,FadeTransition]
        self.root.ids.top_screen.transition = random.choice(trans)(duration=3)
        Clock.schedule_once(self.juu4, 4)

    def juu4(self, *args):
        self.root.ids.top_screen.current = 'top4'
        trans = [FallOutTransition, SlideTransition, SwapTransition, RiseInTransition,WipeTransition,FadeTransition]
        self.root.ids.top_screen.transition = random.choice(trans)(duration=3)
        Clock.schedule_once(self.juu5, 4)

    def juu5(self, *args):
        self.root.ids.top_screen.current = 'top5'
        trans = [FallOutTransition, SlideTransition, SwapTransition, RiseInTransition,WipeTransition,FadeTransition]
        self.root.ids.top_screen.transition = random.choice(trans)(duration=3)
        Clock.schedule_once(self.juu1, 4)

    def register(self):
        self.root.ids.login.main_s.current='register'
    def login(self):
        self.root.ids.top_screen.main_s.current = 'home'

    def save_user(self):
        pass

    def build(self):
        root = Builder.load_string(kv)

        return root

if __name__ == '__main__':
    Everly().run()