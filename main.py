from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import json
import os

try:
    from kivmob import KivMob
    ADMOB_AVAILABLE = True
except ImportError:
    ADMOB_AVAILABLE = False

class TodoApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.todos = []
        self.ads = None
        self.load_todos()
        
    def build(self):
        self.title = "Todo AdMob"
        
        # Initialize AdMob if available
        if ADMOB_AVAILABLE:
            try:
                self.ads = KivMob("ca-app-pub-8214981197698574~9486833110")
                self.ads.request_banner()
                self.ads.show_banner()
            except Exception as e:
                print(f"AdMob Error: {e}")
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        title_label = Label(
            text='تطبيق المهام',
            size_hint_y=0.1,
            font_size='24sp'
        )
        main_layout.add_widget(title_label)
        
        # Input section
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=5)
        self.task_input = TextInput(
            hint_text='أضف مهمة جديدة...',
            multiline=False,
            size_hint_x=0.8
        )
        add_button = Button(
            text='إضافة',
            size_hint_x=0.2,
            background_color=(0.2, 0.6, 0.2, 1)
        )
        add_button.bind(on_press=self.add_task)
        input_layout.add_widget(self.task_input)
        input_layout.add_widget(add_button)
        main_layout.add_widget(input_layout)
        
        # Tasks list
        self.tasks_layout = GridLayout(
            cols=1,
            spacing=5,
            size_hint_y=None
        )
        self.tasks_layout.bind(minimum_height=self.tasks_layout.setter('height'))
        
        scroll_view = ScrollView(size_hint_y=0.7)
        scroll_view.add_widget(self.tasks_layout)
        main_layout.add_widget(scroll_view)
        
        # Buttons section
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=5)
        
        clear_button = Button(
            text='مسح الكل',
            background_color=(0.8, 0.2, 0.2, 1)
        )
        clear_button.bind(on_press=self.clear_all_tasks)
        
        refresh_button = Button(
            text='تحديث',
            background_color=(0.2, 0.2, 0.8, 1)
        )
        refresh_button.bind(on_press=self.refresh_tasks)
        
        buttons_layout.add_widget(clear_button)
        buttons_layout.add_widget(refresh_button)
        main_layout.add_widget(buttons_layout)
        
        self.refresh_tasks()
        return main_layout
    
    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            task = {
                'id': len(self.todos) + 1,
                'text': task_text,
                'completed': False
            }
            self.todos.append(task)
            self.save_todos()
            self.task_input.text = ''
            self.refresh_tasks()
    
    def toggle_task(self, task_id):
        for todo in self.todos:
            if todo['id'] == task_id:
                todo['completed'] = not todo['completed']
                break
        self.save_todos()
        self.refresh_tasks()
    
    def delete_task(self, task_id):
        self.todos = [todo for todo in self.todos if todo['id'] != task_id]
        self.save_todos()
        self.refresh_tasks()
    
    def refresh_tasks(self, instance=None):
        self.tasks_layout.clear_widgets()
        
        if not self.todos:
            empty_label = Label(
                text='لا توجد مهام',
                size_hint_y=None,
                height=50,
                color=(0.5, 0.5, 0.5, 1)
            )
            self.tasks_layout.add_widget(empty_label)
        else:
            for todo in self.todos:
                task_item = self.create_task_item(todo)
                self.tasks_layout.add_widget(task_item)
    
    def create_task_item(self, todo):
        item_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=50,
            spacing=5
        )
        
        # Checkbox
        checkbox = CheckBox(
            active=todo['completed'],
            size_hint_x=0.1
        )
        checkbox.bind(
            active=lambda instance, value: self.toggle_task(todo['id'])
        )
        
        # Task text
        task_label = Label(
            text=todo['text'],
            size_hint_x=0.75,
            color=(0.5, 0.5, 0.5, 1) if todo['completed'] else (1, 1, 1, 1)
        )
        
        # Delete button
        delete_button = Button(
            text='حذف',
            size_hint_x=0.15,
            background_color=(0.8, 0.2, 0.2, 1)
        )
        delete_button.bind(
            on_press=lambda instance: self.delete_task(todo['id'])
        )
        
        item_layout.add_widget(checkbox)
        item_layout.add_widget(task_label)
        item_layout.add_widget(delete_button)
        
        return item_layout
    
    def clear_all_tasks(self, instance):
        self.todos = []
        self.save_todos()
        self.refresh_tasks()
    
    def save_todos(self):
        try:
            with open('todos.json', 'w', encoding='utf-8') as f:
                json.dump(self.todos, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Save Error: {e}")
    
    def load_todos(self):
        try:
            if os.path.exists('todos.json'):
                with open('todos.json', 'r', encoding='utf-8') as f:
                    self.todos = json.load(f)
        except Exception as e:
            print(f"Load Error: {e}")
            self.todos = []
    
    def on_stop(self):
        if self.ads:
            self.ads.destroy()
        return True


if __name__ == '__main__':
    TodoApp().run()
