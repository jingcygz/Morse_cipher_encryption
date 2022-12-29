from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',
        '.': '.-.-.-', ':': '---...', ',': '--..--', ';': '-.-.-.',
        '?': '..--..', '=': '-...-', '\'': '.----.', '/': '-..-.',
        '!': '-.-.--', '-': '-....-', '_': '..--.-', '"': '.-..-.',
        '(': '-.--.', ')': '-.--.-', '$': '...-..-', '&': '....',
        '@': '.--.-',
        'à': '.--.-', 'å': '.--.-', 'ä': '.-.-', 'æ': '.-.-',
        'ç': '-.-..', 'ĉ': '-.-..', 'ð': '..--.', 'é': '..-..',
        'è': '.-..-', 'ĝ': '--.-.', 'ĥ': '-.--.', 'ĵ': '.---.',
        'ñ': '--.--', 'ö': '---.', 'ø': '---.', 'ŝ': '...-.',
        'þ': '.--..', 'ü': '..--', 'ŭ': '..--'
        }


class Mosi(object):
    def __init__(self, code: dict):
        self.code = code

    def encode(self, string: str):
        pass

    def decode(self, string: int):
        pass


class Encode(Mosi):
    def __init__(self, code: dict):
        super().__init__(code)
        self.string = ''
        self.string_list = []
        self.mosi = []
        self.new_string = ''
        self.print_string = ''

    def encode(self, string: str):
        self.string = string.upper()
        for temp in self.string:
            self.string_list.append(temp)
        for temp1 in self.string_list:
            self.mosi.append(self.code[temp1])
        for temp2 in range(len(self.mosi)):
            self.new_string += self.mosi[temp2]
            self.new_string += '|'
        for temp3 in self.new_string:
            if temp3 == '.':
                self.print_string += 'A'
            elif temp3 == '-':
                self.print_string += 'B'
            elif temp3 == '|':
                self.print_string += 'C'
        self.print_string = int(self.print_string, 16)
        return self.print_string


class Decode(Mosi):
    def __init__(self, code: dict):
        super().__init__(code)
        self.int_string = 0
        self.new_string = ''
        self.mosi_list = []
        self.code_keys = []
        self.print_string = ''

    def decode(self, int_string: int):
        self.int_string = int_string
        self.int_string = hex(self.int_string)
        self.int_string = str(self.int_string).upper()
        for temp in self.int_string:
            if temp == 'A':
                self.new_string += '.'
            elif temp == 'B':
                self.new_string += '-'
            elif temp == 'C':
                self.new_string += '|'
        temp2 = ''
        for temp1 in self.new_string:
            if temp1 == '|':
                self.mosi_list.append(temp2)
                temp2 = ''
            else:
                temp2 += temp1
        for temp3 in range(len(self.mosi_list)):
            for temp4, temp5 in self.code.items():
                if self.mosi_list[temp3] == self.code[temp4]:
                    self.print_string += temp4
                    continue
        self.print_string = self.print_string.lower()
        if self.print_string == '':
            return '没有任何一个字符被解密'
        return self.print_string


def morse_cipher_encryption():
    morse_cipher_encryption_window = Tk()
    morse_cipher_encryption_window.title('摩斯密码加密')
    morse_cipher_encryption_window.geometry('600x400')

    class Window(object):
        def keyControl(self, event):
            if 12 == event.state and (event.keysym in ["c", "a"]):
                return
            else:
                return "break"

        def jiami(self):
            text_get = text.get(1.0, END)
            text_get = text_get.strip('\n')
            e = Encode(code=CODE)
            encode = e.encode(text_get)
            text1.delete(1.0, END)
            text1.insert(END, str(encode))

        def jiemi(self):
            text_get = text1.get(1.0, END)
            d = Decode(code=CODE)
            decode = d.decode(int(text_get))
            text.delete(1.0, END)
            text.insert(END, str(decode))

        def qingchu(self):
            text.delete(1.0, END)
            text1.delete(1.0, END)

    w = Window()

    label = Label(morse_cipher_encryption_window, text='明文:')
    label.place(relx=0, rely=0, relheight=0.1, relwidth=0.1)

    label1 = Label(morse_cipher_encryption_window, text='密文：')
    label1.place(relx=0, rely=0.5, relheight=0.1, relwidth=0.1)

    button = Button(morse_cipher_encryption_window, text='加密↓', command=w.jiami)
    button.place(rely=0.5, relx=0.2, relheight=0.1, relwidth=0.1)

    button1 = Button(morse_cipher_encryption_window, text='清空↺', command=w.qingchu)
    button1.place(rely=0.5, relx=0.5, relheight=0.1, relwidth=0.1)

    button2 = Button(morse_cipher_encryption_window, text='解密↑', command=w.jiemi)
    button2.place(rely=0.5, relx=0.8, relheight=0.1, relwidth=0.1)

    text = Text(morse_cipher_encryption_window)
    text.place(relx=0, rely=0.1, relwidth=1, relheight=0.4)

    text1 = Text(morse_cipher_encryption_window)
    text1.place(relx=0, rely=0.6, relheight=0.4, relwidth=1)

    morse_cipher_encryption_window.mainloop()


if __name__ == '__main__':
    morse_cipher_encryption()
