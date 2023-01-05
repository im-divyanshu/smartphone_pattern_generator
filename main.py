from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line
from kivy.uix.boxlayout import BoxLayout
import random

class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.l=0
    def generate(self):
        length=random.randint(2,9)
        keysnum=[1,2,3,4,5,6,7,8,9]
        resultnum=[]
        keys=[self.p1,self.p2,self.p3,self.p4,self.p5,self.p6,self.p7,self.p8,self.p9]
        result=[]

        for i in range(length):
            if self.l>0:
                try:
                    self.canvas.remove(self.l1)
                except ValueError as e:
                    pass
            select=random.randint(0,len(keys)-1)
            result.append(keys[select])
            resultnum.append(keysnum[select])
            keys.remove(keys[select])
            keysnum.remove(keysnum[select])
        result=tuple(result)
        print(resultnum)
        return result
    def click(self):
        self.p1=self.width/2-self.width/3,self.height/2+self.height/3
        self.p2=self.width/2,self.height/2+self.height/3
        self.p3=self.width/2+self.width/3,self.height/2+self.height/3  
        self.p4=self.width/2-self.width/3,self.height/2
        self.p5=self.width/2,self.height/2
        self.p6=self.width/2+self.width/3,self.height/2
        self.p7=self.width/2-self.width/3,self.height/2-self.height/3
        self.p8=self.width/2,self.height/2-self.height/3
        self.p9=self.width/2+self.width/3,self.height/2-self.height/3
        # self.ids.line.points=(0,0,100,100)
        with self.canvas:
            self.l1=Line(points=self.generate())
            if self.l>3:
                pass
            # self.canvas.remove(self.l1)
            self.l+=1
            print(self.l)

            

kv=Builder.load_file("desgine.kv")

class MainApp(App):
    def build(self):
        return kv

MainApp().run()