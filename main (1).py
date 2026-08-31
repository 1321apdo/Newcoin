from  kivy.app  import  App
from  kivy.uix.boxlayout  import  BoxLayout
from  kivy.uix.button  import  Button
from  kivy.uix.label  import  Label
from  kivy.uix.textinput  import  TextInput
from  kivy.uix.scrollview  import  ScrollView
from  kivmob  import  KivMob

class  TodoAdMobApp ( App ): def  build( self ) : # 1. إعداد نظام الإعلانات الربحية بمعرفتك الرسمية الرسمية self .ads = KivMob ( "ca-app-pub-8214981197698574~9486833110" ) self .ads.new_banner ( "ca-app-pub-8214981197698574/1528858562" ,  top_pos= False ) # البانر أسفل الشاشة وعدم إزعاج المستخدم self .ads.request_banner () self .ads.show_banner () # تفعيل وظهور الإعلان فتح فور فتح التطبيق لجني الربح







        # 2
        .​​​ ​​​ ​​​

        # عنوان التطبيق العالي
        title = Label ( text= "قائمة المهام اليومية" ,  size_hint= ( 1 , 0.08 ),  font_size= '22sp' ,  old= True )
        main_layout.add_widget ( title )

        #الطلبات المتنوعة self .task_input = TextInput ( hint_text= "اكتب أهميتك الجديدة هنا..." ,  size_hint= ( 1 , 0.08 ),  multiline= False )         main_layout.add_widget ( self .task_input )



        # زر الإضافة
        btn_add = Button ( text= "إضافة مهمة جديدة" ,  size_hint= ( 1 , 0.08 ),  الخلفية_color= ( 0 , 0.6 , 0.8 , 1 ))
        btn_add.bind ( on_press= self .add_task )
        main_layout.add_widget ( btn_add )

        # قائمة للتمرير للعزف بشكل منظم
        scroll_view = ScrollView ( size_hint= ( 1 , 0.68 ))  self .tasks_list = BoxLayout ( اتجاه= 'vertical' ,  size_hint_y= لا شيء ,  تباعد= 5 ) self .tasks_list.bind ( minor_height= self .tasks_list.setter ( 'height' ))



        scroll_view.add_widget ( self .tasks_list )
        main_layout.add_widget ( scroll_view )

        إرجاع  التخطيط الرئيسي

    # 3. دالة إضافة المهم وتحديث الإعلان الجديد للأزياء والأرباح def  add_task( self ,  example ) :         Task_text =  self .task_input.text.strip () if  Task_text : # إنشاء حاوية السطر للمهمة مع زر الحذف             row = BoxLayout ( التوجه= 'horizontal' ,  size_hint_y= لا شيء ,  الارتفاع= 40 ,  spacing= 10 )






            task_label = Label ( text=task_text ,  size_hint_x= 0.8 ,  halign= 'right' )
            btn_delete = Button ( text= "حذف" ,  size_hint_x= 0.2 ,  background_color= ( 0.9 , 0.2 , 0.2 , 1 ))

            # زر ربط الحذف بالدورة الخاصة به
            btn_delete.bind ( on_press= lambda  btn : self .delete_task ( row ))

            row.add_widget ( btn_delete )
            row.add_widget ( task_label )

            self .tasks_list.add_widget ( row ) self .task_input.text =  "" # تفريغ النص بعد الإضافة


            # تحديث وطلب إعلان جديد بالكامل والظاهر عند تفاعل المستخدم self .ads.request_banner () self .ads.show_banner ()



    # دالة حذف المهمة def  حذف_task( self ,  row_layout ) : self .tasks_list.remove_widget ( row_layout )



إذا كان  __name__ يساوي  "__main__" :
    TodoAdMobApp () .run ()
