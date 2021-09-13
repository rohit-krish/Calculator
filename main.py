# icon 256 presplash 2000
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re
Builder.load_file('design.kv')
 
class MyLayout(BoxLayout):
    def clear(self):
        self.ids.text_input.text='0'
    def del_last(self):
        text=self.ids.text_input.text[:-1]
        self.ids.text_input.text=text
    def num_press(self,num):
        prior=self.ids.text_input.text
        if 'Error' in self.ids.text_input.text:
            self.ids.text_input.text = prior.replace('Error','')
        prior=self.ids.text_input.text
        if (prior == '0') and (num != '.'):
            self.ids.text_input.text= '{}'.format(num)
        else:
            now=prior+str(num)
            self.ids.text_input.text = now
    def arithmatic_functions(self,sign):
        prior=self.ids.text_input.text
        if 'Error' in self.ids.text_input.text:
            self.ids.text_input.text = prior.replace('Error','')
        for num in prior:
            res = num
        charecters = ['+','-','*','/']
        if sign == '+' and res not in charecters:
            self.ids.text_input.text = f'{self.ids.text_input.text}+' 
        elif sign == '-' and res not in charecters:
            self.ids.text_input.text = f'{self.ids.text_input.text}-' 
        elif sign == '*' and res not in charecters:
            self.ids.text_input.text = f'{self.ids.text_input.text}*' 
        elif sign == '/' and (res != ('+' or '-' or '*' or '/' or '%')):
            self.ids.text_input.text = f'{self.ids.text_input.text}/' 
    def evaluate(self):
        try:
            text = self.ids.text_input.text
            res=eval(text)
            self.ids.text_input.text = str(res)
            
        except ZeroDivisionError:
            self.ids.text_input.text = 'Error'
        except  SyntaxError:
            self.ids.text_input.text = 'Error'
        except NameError:
            self.ids.text_input.text = 'Error'
    def dot(self):
        preNum = self.ids.text_input.text
        numList = re.split("\+|\*|\-|\/",preNum)
        if ('+' in preNum or '-' in preNum or '*' in preNum or '/' in preNum or '%' in preNum) and '.' not in numList[-1]:
            self.ids.text_input.text = f'{preNum}.'
        elif '.' in preNum:
            pass
        else:
            self.ids.text_input.text = f'{preNum}.'
    def posOrNeg(self):
        term = self.ids.text_input.text
        sign = []
        signPos = []
        for i in range(len(term)):
            if '+' in term[i]: 
                sign.append(term[i])
                signPos.append(i)
            elif '-' in term[i]:
                sign.append(term[i])
                signPos.append(i)
            elif '/' in term[i]:
                sign.append(term[i])
                signPos.append(i)
            elif '*' in term[i]:
                sign.append(term[i])
                signPos.append(i)
            elif '%' in term[i]:
                sign.append(term[i])
                signPos.append(i)
        term = self.ids.text_input.text
        if len(sign) == 0:
            self.ids.text_input.text = f'-{term}'
        else:
            if sign[-1] == '-':
                lenOfNegSign=0
                for i in range(len(sign)):
                    if sign[i] == '-':
                        lenOfNegSign += 1
                if lenOfNegSign > 1:
                    NegativesPos = []
                    for i in range(len(term)):
                        if term[i] == '-':
                            NegativesPos.append(i)
                    if NegativesPos[-1] - NegativesPos[-2] == 1:
                        resHere = f'{term[:NegativesPos[-1]-1]}{term[NegativesPos[-1]:]}'
                        self.ids.text_input.text = resHere
                    else:
                        NegativesPos[-1]
                        beforeNeg = f'{term[:NegativesPos[-1]]}'
                        afterNeg = f'-{term[NegativesPos[-1]:]}'
                        self.ids.text_input.text = f'{beforeNeg}{afterNeg}'
                        print(self.ids.text_input.text)
                else:
                    lastNegSign = f'-{term[signPos[-1]+1:]}'
                    preOfLastNegSign =  term[:signPos[-1]+1]
                    self.ids.text_input.text = f'{preOfLastNegSign}{lastNegSign}'
            else:
                negTerm = f'-{term[(signPos[-1]+1):]}'
                ogTerm=term[:signPos[-1]+1]
                self.ids.text_input.text = ogTerm+negTerm
    def sqare(self):
        try:
            text=eval(self.ids.text_input.text)
            text=int(text*text)
            self.ids.text_input.text = str(text)
        except ZeroDivisionError:
            self.ids.text_input.text = 'Error'
        except  SyntaxError:
            self.ids.text_input.text = 'Error'
        except NameError:
            self.ids.text_input.text = 'Error'
class Calculator(App):
    def build(self):
        self.icon = r'./icon.png'
        return MyLayout()
if __name__ == '__main__':
    Calculator().run()