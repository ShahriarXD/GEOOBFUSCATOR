import base64
import os
from colored import fg
import sys
import requests
import webbrowser
from time import sleep
import subprocess
sys.setrecursionlimit(10**9)


class Fore:
    BLACK = fg('black')
    BLUE = fg('blue')
    CYAN = fg('cyan')
    GREEN = fg('green')
    LIGHTBLUE_EX = fg('light_blue')
    LIGHTCYAN_EX = fg('light_cyan')
    LIGHTGREEN_EX = fg('light_green')
    LIGHTMAGENTA_EX = fg('light_magenta')
    LIGHTRED_EX = fg('light_red')
    LIGHTYELLOW_EX = fg('light_yellow')
    MAGENTA = fg('light_magenta')
    RED = fg('red')
    RESET = fg('253')
    WHITE = fg('253')
    YELLOW = fg('yellow')
    blue1 = fg('#19a2ff')
    blue2 = fg('#0098ff')
    blue3 = fg('#2eaaff')
    blue4 = fg('#38aeff')
    blue5 = fg('#4db6ff')
    blue6 = fg('#5cbcff')
    numberblue = fg('#71baeb')
    teal = fg('#57d9de')
    printsblue = fg('#3471eb')
    titlepurple = fg('#8A2BE2')
    numberpurple = fg('#9932CC')

def clear():
    os.system('cls')

def title():
    clear()
    print(Fore.titlepurple + '''\n\n    ██████╗ ███████╗ ██████╗      ██████╗ ██████╗ ███████╗██╗   ██╗███████╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗ 
   ██╔════╝ ██╔════╝██╔═══██╗    ██╔═══██╗██╔══██╗██╔════╝██║   ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
   ██║  ███╗█████╗  ██║   ██║    ██║   ██║██████╔╝█████╗  ██║   ██║███████╗██║     ███████║   ██║   ██║   ██║██████╔╝
   ██║   ██║██╔══╝  ██║   ██║    ██║   ██║██╔══██╗██╔══╝  ██║   ██║╚════██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
   ╚██████╔╝███████╗╚██████╔╝    ╚██████╔╝██████╔╝██║     ╚██████╔╝███████║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
    ╚═════╝ ╚══════╝ ╚═════╝      ╚═════╝ ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                  \n\n''')
def main():
    title()
    print(f'{Fore.numberpurple}      {Fore.WHITE}[{Fore.numberpurple}1{Fore.WHITE}] Obfuscate')
    print(f'{Fore.numberpurple}      {Fore.WHITE}[{Fore.numberpurple}2{Fore.WHITE}] Exit\n')
    option = input('     > ')
    if option == '1':
        obfuscator().settings()

def encode(code):
    encode = code.encode('utf-8')
    bytes = base64.b64encode(encode)
    output = bytes.decode('utf-8')
    return output

def decode(code):
    decode = code.encode('utf-8')
    bytes = base64.b64decode(decode)
    output = bytes.decode('utf-8')
    return output


class obfuscator:
    strength = ''
    source_code = ''
    output_name = 'output.py'
    def settings(self):
        title()
        print(f'{Fore.WHITE}What should the Obfuscation Strength be? [Recommended: 3-25]')
        obfuscator.strength = input('> ')
        title()
        print(f'{Fore.WHITE}What file should source code be loaded from? [Can be .txt or .py]')
        obfuscator.source_code = open(input('> '), encoding='utf-8').read()
        title()
        print(f'{Fore.WHITE}What file should the output file be? [Can be .txt or .py]')
        obfuscator.output_name = input('> ')
        title()
        print(f'{Fore.WHITE}Obfuscating...')
        obfuscator().obfuscate()
    def obfuscate(self):
        line = encode(obfuscator.source_code)
        code = f'''import base64
JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu = '{line}'
JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu1 = JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu.encode('utf-8')
JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu3 = base64.b64decode(JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu1)
JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu2 = JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu3.decode('utf-8')
exec(JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu2)'''
        for i in range(int(obfuscator.strength) - 1):
            line = encode(code)
            code = f'''import base64
JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu = '{line}'
JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu1 = JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu.encode('utf-8')
JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu3 = base64.b64decode(JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu1)
JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu2 = JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu3.decode('utf-8')
exec(JFIjafiowhakfoasifhwokiafiosafpkonaihfksniashfokinwaohfoskiafhiowhakfsakfhwafjisahwahjifhdaslfhaigoksafuagwfohaisfgasuihfkgarfgiashfuwgafuhasufgwfasagfuagskfhauitfuaishfiowgafuigaogfiwagfsagfiuwagofhuaosftuwahfjagfiugwaofgsiaufowugafuisfuwgafuisgiaufgwihafuiasgfouiwgaiufgasiu2)'''
        f = open(obfuscator.output_name, 'a', encoding='utf-8')
        f.write(code)
        f.close()


try:
    main()
except Exception as e:
    print(f'{Fore.WHITE}[{Fore.RED}Error{Fore.WHITE}] - {e}')
input('Done!')
