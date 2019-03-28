import tkinter, sys
from PIL import ImageTk, Image


class GuiPart:
    def __init__(self, master, queue):
        self.queue = queue
        self.master = master

        self.isEditable_1 = False
        self.isEditable_2 = False
        self.isEditable_3 = False
        self.isEditable_4 = False

        self.isSet_1 = False
        self.isSet_2 = False
        self.isSet_3 = False
        self.isSet_4 = False

        self.isReset = False

        # Set up the GUI
        self.txt_clock_1 = tkinter.Label(master, text='', width=20)
        self.txt_clock_2 = tkinter.Label(master, text='', width=20)
        self.txt_clock_3 = tkinter.Label(master, text='', width=20)
        self.txt_clock_4 = tkinter.Label(master, text='', width=20)

        self.input_clock_1 = tkinter.Entry(master, text='', width=40)
        self.input_clock_2 = tkinter.Entry(master, text='', width=40)
        self.input_clock_3 = tkinter.Entry(master, text='', width=40)
        self.input_clock_4 = tkinter.Entry(master, text='', width=40)

        self.edit_1 = tkinter.Button(master, text='Editar', command=lambda: self.OnEdit(1), width=10)
        self.edit_2 = tkinter.Button(master, text='Editar', command=lambda: self.OnEdit(2), width=10)
        self.edit_3 = tkinter.Button(master, text='Editar', command=lambda: self.OnEdit(3), width=10)
        self.edit_4 = tkinter.Button(master, text='Editar', command=lambda: self.OnEdit(4), width=10)

        self.set_1 = tkinter.Button(master, text='Enviar', command=lambda: self.OnSet(1), width=10)
        self.set_2 = tkinter.Button(master, text='Enviar', command=lambda: self.OnSet(2), width=10)
        self.set_3 = tkinter.Button(master, text='Enviar', command=lambda: self.OnSet(3), width=10)
        self.set_4 = tkinter.Button(master, text='Enviar', command=lambda: self.OnSet(4), width=10)

        img_none = self.createImage("../../images/na.jpg")
        self.book_image = tkinter.Label(master, image=img_none, text="Grafica1")
        self.book_image.image = img_none

        self.end = tkinter.Button(master, text='Done', command=lambda: self.exitButton(), width=10)
        self.reset = tkinter.Button(master, text='Reiniciar', state="disabled", command=lambda: self.resetButton(), width=10)

        self.txt_clock_1.grid(row=0, column=0)
        self.txt_clock_2.grid(row=1, column=0)
        self.txt_clock_3.grid(row=2, column=0)
        self.txt_clock_4.grid(row=3, column=0)

        self.input_clock_1.grid(row=0, column=1)
        self.input_clock_2.grid(row=1, column=1)
        self.input_clock_3.grid(row=2, column=1)
        self.input_clock_4.grid(row=3, column=1)

        self.edit_1.grid(row=0, column=2)
        self.edit_2.grid(row=1, column=2)
        self.edit_3.grid(row=2, column=2)
        self.edit_4.grid(row=3, column=2)

        self.set_1.grid(row=0, column=3)
        self.set_2.grid(row=1, column=3)
        self.set_3.grid(row=2, column=3)
        self.set_4.grid(row=3, column=3)

        self.book_image.grid(row=4, column=1)

        self.end.grid(row=5, column=2)
        self.reset.grid(row=5,column=3)

    def resetButton(self):
        self.isReset = True
        self.reset["state"] = "disabled"

    def exitButton(self):
        self.master.destroy()
        sys.exit(1)

    def OnEdit(self, button_id):
        setattr(self, 'isEditable_' + str(button_id), True)
        setattr(self, 'isSet_' + str(button_id), False)

    def OnSet(self, button_id):
        setattr(self, 'isEditable_' + str(button_id), False)
        setattr(self, 'isSet_' + str(button_id), True)

    def getEditable(self, number):
        return number, getattr(self, 'isEditable_' + str(number))

    def getSeteable(self, number):
        return getattr(self, 'isSet_' + str(number))

    def getTextFromEditable(self, number):
         return getattr(self, 'input_clock_' + str(number)).get()

    def turnOffSet(self, number):
        setattr(self, 'isSet_' + str(number), False)
        att = getattr(self, "input_clock_" + str(number))
        att.delete(0, 'end')

    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize():
            try:
                msg = self.queue.get(0).split("|")
                if msg[0] == "1":
                    self.txt_clock_1["text"] = msg
                elif msg[0] == "2":
                    self.txt_clock_2["text"] = msg
                elif msg[0] == "3":
                    self.txt_clock_3["text"] = msg
                else:
                    self.txt_clock_4["text"] = msg
            except queue.Empty:
                pass

    def createEmptyPopup(self):
        top = tkinter.Toplevel()
        top.title("Alerta")
        msg = tkinter.Message(top, text="Ya no hay libros, presione el botón REINICIAR")
        msg.pack()

        button = tkinter.Button(top, text="Aceptar", command=top.destroy)
        button.pack()

    def createImage(self, path):
        return ImageTk.PhotoImage(Image.open(path))