from tkinter import *
from tkinter import messagebox,END
from tkinter.font import *
import re

root = Tk()
root.title("TP1 ALS the terms")
root.minsize(900, 500)
root.configure(bg='#78BCC4')
root.resizable(0, 0)

my_font = Font(family="MV Boli", size=12)

entry = Text(root, height=2, width=35, bg="#F7F8F3", fg="#000000", font=my_font)
entry.place(x=300, y=70)

text_for_display = Text(root, height=15, width=35, bg="#002C3E", fg="#FFFF00", font=my_font)
text_for_display.place(x=60, y=150)


def verification():
    text_for_display.delete(1.0,END)
    user_input=entry.get("1.0",END)
    j=0
    k=0
    while j < len(user_input):
        if user_input[j]==" ":
            k+=1
        j+=1
    if k==len(user_input):
        text_for_display.insert(END,"Plaese Entry your terms ")
        return None
    if(user_input ==''):
        text_for_display.insert(END,"Plaese Entry your terms")
        return None
    i=0
    
    while i < len(user_input):
        if user_input[i]==' ' and  (re.match('\w',user_input[i+1]))!=None  :
            text_for_display.insert(END,"error1")
            return None
        
        i+=1
    text1 = re.sub(" ",'',user_input)
    string1=text1
    functions = ""
    constant = ""
    variable = ""
    splited = []
    fun=[]
    error=[]
    
    parentes_number=0
    syntaxErr=0

    if (re.match("\W", user_input)!= None) and user_input[-1] == ')' :
        text_for_display.insert(END,"error2")
        return None 
    while text1 != '':
      function=''
      parentes=0
      vergule=0
      n=0    
      text2=''
      i=0
      
      while i < len(text1) and n==0:
          if text1[i]==',' :
              vergule=i
              
          if text1[i]==' ' :
              text_for_display.insert(END,"error3")
              return None
           
          if text1[i]=='(' :
              parentes_number+=1
              n=1
              parentes=i
           
          i+=1  
            
      j=len(text1)
      n=0
      x=1
      while j > 0 and n==0 :
          if text1[j-1]==')' :
              parentes_number+=1
              n=1
          j-=1
      if n==1:
          

          if (vergule >= parentes):
              vergule = 0
          if vergule > 0 :
              vergule = vergule + 1  
          for i in range(vergule,parentes): 
              function+=text1[i]
          for z in range(parentes+1,len(text1)-1):
              text2 += text1[z]
          if (re.match("^[a-zA-Z]+\w\s*$|^[a-zA-Z]$", function)!= None):
                    fun.append(function)
          else:
                    
                    error.append(function)   
          string1 = re.sub(function,'',string1,1)
          if (len(re.findall(r',',text1)) > 0):
            string1 = re.sub("[(]|[)]",'',string1)   
          else :
            text_for_display.insert(END,"functoin must have 2 term or more")
            return None
          
      text1 = text2
      
    if (re.findall("[,]", string1)!= None):
        splited = re.split(",", string1)
    else:
        splited.append(string1)
    
    for word in splited:
        if (re.match("^\d+$|^[']+[\w]+[']$", word)!= None) and (re.match("[0-9]+[a-zA-Z]$", word)== None) and (re.match("[0-9]+[a-zA-Z]+[0-9]", word)== None) :
            constant = constant + word + ","
        elif (re.match("^[a-zA-Z]+[\w]*$", word)!= None):
            variable = variable + word + ","
        elif(re.match("[0-9]+[a-zA-Z]$", word)!= None) :
            error.append(word)
            x=0
            break
            


    functions = functions + function + ","
    constants = re.split(",", constant)
    variables = re.split(",", variable)
    if parentes_number % 2 != 0:
        syntaxErr = 1
    if syntaxErr == 1 :
        text_for_display.insert(END,"Error of syntax")
        return None
    else:
        content=''
        
        if x==0:
            for word in error:
                if(error != None and word !=''):
                    content = content + word+ ": error\n"
            
        else:       
            for word in fun:
                if (fun != None and word != ''):
                    content = content + word + ":  fanction\n"
            for word in constants:
                if (constants != None and word != ''):
                    content = content + word + ":  constant\n"
            for word in variables:
                if (variables != None and word != ''): 
                    content = content + word + ":  variable\n"
            
    syntaxErr = 0
    text_for_display.insert(END,content)
def Test1():
    test = 'fn2 (x,5,g(j5,"yes"))'
    entry.delete("1.0", END)
    entry.insert(END, test)

def Test2():
    test2 = 'fn2 (x,5b,g(j5,"yes"))'
    entry.delete("1.0", END)
    entry.insert(END, test2)

def Clear():
    String = entry.get("1.0", END)
    if String.strip() == "":
        messagebox.showerror(title="INFO", message="Register your terms, please")
    else:
        entry.delete('1.0', END)
        text_for_display.delete('1.0', END)

label = Label(root, text='Register your terms here :', fg='black', bg="#78BCC4", font=my_font)
label.place(x=300, y=40)

label1 = Label(root, text='Console :', fg='black', bg="#78BCC4", font=my_font)
label1.place(x=60, y=120)

label2 = Label(root, text='verification le term : ', fg='black', bg="#78BCC4", font=my_font)
label2.place(x=600, y=255)

label3 = Label(root, text='Test 1:', fg='black', bg="#78BCC4", font=my_font)
label3.place(x=600, y=305)

label4 = Label(root, text='Test 2:', fg='black', bg="#78BCC4", font=my_font)
label4.place(x=600, y=355)

label5 = Label(root, text='Clear the terms :', fg='black', bg="#78BCC4", font=my_font)
label5.place(x=600, y=405)

button1 = Button(root, text='verification', border=0, height=1, width=10, bg="black", fg="#ffffff", font=my_font, command=verification)
button1.place(x=500, y=250)

button2 = Button(root, text='Test 1', border=0, height=1, width=10, bg="black", fg="#ffffff", font=my_font, command=Test1)
button2.place(x=500, y=300)

button3 = Button(root, text='Test 2', border=0, height=1, width=10, bg="black", fg="#ffffff", font=my_font, command=Test2)
button3.place(x=500, y=350)

button4 = Button(root, text='clear', border=0, height=1, width=10, bg="black", fg="#ffffff", font=my_font, command=Clear)
button4.place(x=500, y=400)

root.mainloop()
