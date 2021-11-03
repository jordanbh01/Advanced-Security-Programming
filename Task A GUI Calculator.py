from tkinter import *


def Calculator(source, side):
    storeobj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeobj.pack(side=side, expand=YES, fill=BOTH)
    return storeobj


def button(source, side, text, command=None):
    storeobj = Button(source, text=text, command=command)
    storeobj.pack(side=side, expand=YES, fill=BOTH)
    return storeobj


class App(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('GUI Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
              justify='right'
              , bd=30, bg="powder blue").pack(side=TOP,
                                              expand=YES, fill=BOTH)

        for clearButton in (["C"]):
            erase = Calculator(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    storeobj=display, q=ichar: storeobj.set(''))

        for numButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = Calculator(self, TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda
                    storeobj=display, q=iEquals: storeobj
                       .set(storeobj.get() + q))

        EqualButton = Calculator(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btn_Equals = button(EqualButton, LEFT, iEquals)
                btn_Equals.bind('<ButtonRelease-1>', lambda e, s=self,
                                                            storeobj=display: s.calc(storeobj), '+')


            else:
                btn_Equals = button(EqualButton, LEFT, iEquals,
                                    lambda storeobj=display, s=' %s ' % iEquals: storeobj.set
                                    (storeobj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


if __name__ == '__main__':
    App().mainloop()
