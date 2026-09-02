                                                                                                                                                                                                                                                    btn_delete = Button(text="حذف", size_hint_x=0.2, background_color=(0.9, 0.2, 0.2,from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivmob import KivMob

class TodoAdMobApp(App):
    def build(self):
        # تصميم الواجهة الرئيسية للتطبيق
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # العنوان العلوي
        title = Label(text="قائمة المهام اليومية", size_hint=(1, 0.08), font_size='22sp', bold=True)
        main_layout.add_widget(title)
        
        # حقل إدخال النص للمهمة الجديدة
        self.task_input = TextInput(hint_text="اكتب مهمتك الجديدة هنا...", size_hint=(1, 0.08), multiline=False)
        main_layout.add_widget(self.task_input)
        
        # زر الإضافة
        btn_add = Button(text="إضافة مهمة جديدة", size_hint=(1, 0.08), background_color=(0, 0.6, 0.8, 1))
        btn_add.bind(on_press=self.add_task)
        main_layout.add_widget(btn_add)
        
        # قائمة التمرير لعرض المهام
        scroll_view = ScrollView(size_hint=(1, 0.68))
        self.tasks_list = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.tasks_list.bind(minimum_height=self.tasks_list.setter('height'))
        
        scroll_view.add_widget(self.tasks_list)
        main_layout.add_widget(scroll_view)
        
        return main_layout

    def on_start(self):
        # استدعاء الإعلانات هنا بعد تجهيز واجهة أندرويد 14 بالكامل لمنع الانهيار
        try:
            self.ads = KivMob("ca-app-pub-8214981197698574~9486833110") 
            self.ads.new_banner("ca-app-pub-8214981197698574/1528858562", top_pos=False)
            self.ads.request_banner()
            self.ads.show_banner()
        except Exception as e:
            print(f"AdMob Error: {e}")

    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=10)
            
            # زر حذف المهمة
            btn_delete = Button(text="حذف", size_hint_x=0.2, background_color=(0.9, 0.2, 0.2, 1))
            btn_delete.bind(on_press=lambda btn: self.delete_task(row))
            
            # نص المهمة
            task_label = Label(text=task_text, size_hint_x=0.8, halign='right')
            
            row.add_widget(btn_delete)
            row.add_widget(task_label)
            self.tasks_list.add_widget(row)
            
            # تفريغ الحقل لتجهيزه للمهمة التالية
            self.task_input.text = ""
            
            # تحديث طلب الإعلان بشكل آمن
            try:
                self.ads.request_banner()
                self.ads.show_banner()
            except:
                pass

    def delete_task(self, row_layout):
        self.tasks_list.remove_widget(row_layout)

if __name__ == '__main__':
    TodoAdMobApp().run()
 1))
                                                                                                                                                                                                                                                                btn_delete.bind(on_press=lambda btn: self.delete_task(row))
                                                                                                                                                                                                                                                                            row.add_widget(btn_delete)
                                                                                                                                                                                                                                                                                        row.add_widget(task_label)
                                                                                                                                                                                                                                                                                                    self.tasks_list.add_widget(row)
                                                                                                                                                                                                                                                                                                                self.task_input.text = ""
                                                                                                                                                                                                                                                                                                                            self.ads.request_banner()
                                                                                                                                                                                                                                                                                                                                        self.ads.show_banner()

                                                                                                                                                                                                                                                                                                                                            def delete_task(self, row_layout):
                                                                                                                                                                                                                                                                                                                                                    self.tasks_list.remove_widget(row_layout)

                                                                                                                                                                                                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                        TodoAdMobApp().run()
                                                                                                                                                                                                                                                                                                                                                        l
                                                                                                                                                                                                                                                                                                                                                        
