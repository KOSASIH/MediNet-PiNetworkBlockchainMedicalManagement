import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
import requests
import json
import base64
import hmac
import hashlib
import datetime
import os

# Set the API endpoint URL
API_ENDPOINT = 'https://api.medinet.com/v1'

# Set the API key
API_KEY = 'your_api_key_here'

# Set the API secret key
API_SECRET_KEY = 'your_api_secret_key_here'

# Set the access token expiration time (in seconds)
ACCESS_TOKEN_EXPIRATION_TIME = 3600

# Set the user agent string
USER_AGENT = 'MediNet/1.0.0 (iOS; iPhone)'

# Set the image cache directory
IMAGE_CACHE_DIR = 'image_cache'

# Set the maximum number of retries for API requests
MAX_RETRIES = 3

# Set the retry delay (in seconds)
RETRY_DELAY = 1

# Set the screen manager
screen_manager = ScreenManager()

# Set the login screen
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'login'
        self.add_widget(self.create_form())

    def create_form(self):
        form = GridLayout(cols=2, spacing=10, padding=10)
        form.add_widget(Label(text='Email:'))
        self.email_input = TextInput(multiline=False)
        form.add_widget(self.email_input)
        form.add_widget(Label(text='Password:'))
        self.password_input = TextInput(multiline=False, password=True)
        form.add_widget(self.password_input)
        form.add_widget(Button(text='Login', on_press=self.login))
        return form

    def login(self, instance):
        # Get the email and password
        email = self.email_input.text
        password = self.password_input.text

        # Generate the HMAC signature
        timestamp = str(int(time.time()))
        message = f'{email}:{timestamp}:{password}'
        signature = base64.b64encode(hmac.new(API_SECRET_KEY.encode(), message.encode(), hashlib.sha256).digest()).decode()

        # Set the API headersheaders = {
            'Authorization': f'APIKey {API_KEY}:{signature}',
            'User-Agent': USER_AGENT,
            'Timestamp': timestamp,
        }

        # Set the API endpoint URL
        url = f'{API_ENDPOINT}/auth/login'

        # Set the API request data
        data = {
            'email': email,
            'password': password,
        }

        # Make the API request
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
            return

        # Get the access token and expiration time
        response_data = response.json()
        access_token = response_data['access_token']
        expiration_time = datetime.datetime.now() + datetime.timedelta(seconds=ACCESS_TOKEN_EXPIRATION_TIME)

        # Set the access token and expiration time in the app settings
        App.get_running_app().settings['access_token'] = access_token
        App.get_running_app().settings['expiration_time'] = expiration_time

        # Switch to the home screen
        App.get_running_app().screen_manager.current = 'home'

# Set the home screen
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'home'
        self.add_widget(self.create_layout())

    def create_layout(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.create_toolbar())
        layout.add_widget(self.create_content())
        return layout

    def create_toolbar(self):
        toolbar = BoxLayout(size_hint_y=0.1, orientation='horizontal')
        toolbar.add_widget(Button(text='Logout', on_press=self.logout))
        return toolbar

    def create_content(self):
        content = ScrollView(size_hint_y=0.9)
        content.add_widget(self.create_list())
        return content

    def create_list(self):
        list_view = RecycleView(viewclass=MedicineView, layoutclass=RecycleGridLayout)
        list_view.data = [{'text': medicine['name'], 'image_url': medicine['image_url']} for medicine in App.get_running_app().medicines]
        return list_view

    def logout(self, instance):
        # Clear the access token and expiration time from the app settings
        App.get_running_app().settings['access_token'] = None
        App.get_running_app().settings['expiration_time'] = None

        # Switch to the login screen
        App.get_running_app().screen_manager.current = 'login'

# Set the medicine view
class MedicineView(RecycleDataViewBehavior, BoxLayout):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10
        self.add_widget(Image(source='image.png', size_hint_y=0.5))
        self.name_label = Label(size_hint_y=0.3, halign='center')
        self.add_widget(self.name_label)

    def refresh_view_attrs(self, rv, index, data):
        """ Catch and handle the view attributes update event """
        self.index = index
        self.selected = rv.data[index]['selected']
        self.name_label.text = rv.data[index]['text']

# Set the app
class MediNetApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = ScreenManager()
        self.medicines = []

    def build(self):
        # Load the app settings
       self.settings = self.load_settings()

        # Add the screens to the screen manager
        self.screen_manager.add_widget(LoginScreen(name='login'))
        self.screen_manager.add_widget(HomeScreen(name='home'))

        # Set the initial screen
        if self.settings['access_token'] and self.settings['expiration_time'] > datetime.datetime.now():
            self.screen_manager.current = 'home'
        else:
            self.screen_manager.current = 'login'

        # Start the API request loop
        Clock.schedule_interval(self.request_medicines, 10)

        return self.screen_manager

    def load_settings(self):
        """ Load the app settings from a JSON file """
        settings = {}
        if os.path.exists('settings.json'):
            with open('settings.json', 'r') as f:
                settings = json.load(f)
        return settings

    def save_settings(self):
        """ Save the app settings to a JSON file """
        with open('settings.json', 'w') as f:
            json.dump(self.settings, f)

    def request_medicines(self, dt):
        """ Make an API request to get the list of medicines """
        # Check if the access token is expired
        if not self.settings['access_token'] or self.settings['expiration_time'] < datetime.datetime.now():
            # Clear the access token and expiration time from the app settings
            self.settings['access_token'] = None
            self.settings['expiration_time'] = None

            # Switch to the login screen
            self.screen_manager.current = 'login'
            return

        # Set the API headers
        headers = {
            'Authorization': f'Bearer {self.settings["access_token"]}',
            'User-Agent': USER_AGENT,
        }

        # Set the API endpoint URL
        url = f'{API_ENDPOINT}/medicines'

        # Make the API request
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
            return

        # Get the list of medicines
        response_data = response.json()
        self.medicines = response_data['medicines']

        # Save the app settings
        self.save_settings()

# Run the app
if __name__ == '__main__':
    MediNetApp().run()
