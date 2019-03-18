import tkinter, sys

class GuiPart:
    def __init__(self, master, queue):
        self.queue = queue
        self.master = master

        self.is_request = 0
        self.info_data = "Libro"

        self.ds_clock = tkinter.Label(master, text='', width=20)
        self.info = tkinter.Label(master, text=self.info_data, width=80,  padx=10, pady=10)
        self.request = tkinter.Button(master, text='Solicitar', command=lambda: self.turnOnIsRequest(), width=20)
        self.end = tkinter.Button(master, text='Salir', command=lambda: self.exitButton(), width=20)

        self.ds_clock.grid(row=0, column=0)
        self.info.grid(row=1, column=0)
        self.request.grid(row=2, column=0)
        self.end.grid(row=3, column=0)

    def createEmptyPopup(self):
        top = tkinter.Toplevel()
        top.title("Alerta")
        msg = tkinter.Message(top, text="Ya no hay libros disponibles")
        button = tkinter.Button(top, text="Aceptar", command=top.destroy)
        msg.pack()
        button.pack()

    def processIncoming(self):
        while self.queue.qsize():
            """Uncomment if you wanna use p2"""
            """"
            try:
                msg = self.queue.get(0)
                self.ds_clock["text"] = msg
            except queue.Empty:
                pass
            """
            try:
                msg = self.queue.get(0).decode().split("_")
                if len(msg) == 3:
                    self.createEmptyPopup()
                elif len(msg) == 4:
                    book_data = msg[2].split(",")
                    name = "Nombre: " + book_data[1]
                    autor = "Autor: " + book_data[2]
                    editorial = "Editorial: " + book_data[3]
                    precio = "Precio: " + book_data[4]
                    self.info_data = name + ' ' + autor + ' ' + editorial + ' ' + precio
                self.ds_clock["text"] = msg[1]
                self.info["text"] = self.info_data
            except queue.Empty:
                pass

    def getIsRequest(self):
        return getattr(self, 'is_request')

    def turnOffIsRequest(self):
        setattr(self, 'is_request', 0)

    def turnOnIsRequest(self):
        setattr(self, 'is_request', 1)

    def exitButton(self):
        self.master.destroy()
        sys.exit(1)