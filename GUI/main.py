import tkinter
from tkinter import ttk

def main(): 
    window = tkinter.Tk()
    
    
    def label():
        '''
        labels
        
        '''
        label1=tkinter.Label(window, text="hello", bg="yellow",fg="blue")
        label1.pack(ipadx=50,ipady=100, expand=True, side='left')
            
        label2 = tkinter.Label(window,text="bye",bg="red",fg="green")
        label2.pack(ipadx=100,ipady=50, fill='both',side='right')
    
    def grid():
        window.columnconfigure(0, weight=1)
        window.columnconfigure(0, weight=3)
        
        #username
        
        label1 = ttk.Label(window, text="username:")
        label1.grid(column=0,row=0,sticky=tkinter.W,padx=20,pady=30)
        
        username_entry=ttk.Entry(window)
        username_entry.grid(column=1,row=0,sticky=tkinter.E,padx=20,pady=30)
        
        #password
        
        label2 = ttk.Label(window, text="passsword:")
        label2.grid(column=0,row=1,sticky=tkinter.W,padx=20,pady=30)
        
        password_entry=ttk.Entry(window,show='*')
        password_entry.grid(column=1,row=1,sticky=tkinter.E,padx=20,pady=30)
        
        #button  
        login_button=tkinter.Button(window, text="login")
        login_button.grid(column=0,row=2,padx=50,pady=50, sticky=tkinter.E)
    
    def place():
        label1=tkinter.Label(window , text="hello", bg="blue",fg="white")
        label1.place(x=10,y=50)
        
        label2=tkinter.Label(window,text="hii",bg="purple",fg="green")
        label2.place(relx=0.10,rely=0.15,relwidth=0.5,anchor='ne')
        
            
        

        
        
        
        
    def widget(): 
        window.columnconfigure(0, weight=1)
        window.columnconfigure(0, weight=3)
         
        frame=ttk.Frame(window)
        frame['relief'] = 'sunken'
        
        label=ttk.Label(frame,text='hello',)
        label.grid(column=0,row=0,pady=50,padx=50)
        
        frame.grid(column=0,row=0,sticky=tkinter.W)
        
        ls=['windows','macos','linux']
        ls_items=tkinter.StringVar(value=ls)   #bulit a list thet tk understood
        listbox=tkinter.Listbox(window,height=10,listvariable=ls_items)
        listbox.grid(column=0,row=1,padx=50,pady=50,sticky=tkinter.W)
        
        
        selected = tkinter.StringVar()
        radio_button1 = ttk.Radiobutton(window, text="yes",value='1',variable=selected)
        radio_button2 = ttk.Radiobutton(window, text="maybe",value='2',variable=selected)
        radio_button3  = ttk.Radiobutton(window, text="no",value='3',variable=selected)
        
        radio_button1.grid(column=0,row=2,pady=15,padx=15,sticky=tkinter.W)
        radio_button2.grid(column=1,row=2,pady=15,padx=15)
        radio_button3.grid(column=2,row=2,pady=15,padx=15,sticky=tkinter.E)
        
        selected2 = tkinter.StringVar()
        checkbox=ttk.Checkbutton(window,text='accept?',variable=selected2)#comand=myfunc)
        checkbox.grid(column=0,row=4)
        
        
    def event():
        
        
        def sayhi(event):
            print('hi')
            
            
        buttom4=tkinter.Button(text="hello")  
        buttom4.pack()
        buttom4.bind('buttom-1', sayhi)
        buttom4.bind('Double-1', sayhi)
        
                
    event()
    window.mainloop()

    




if(__name__ == "__main__"):
    main()