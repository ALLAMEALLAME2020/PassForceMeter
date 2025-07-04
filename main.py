import string as st
from colorama import Fore, init, Style
import time
def sleep(qunt):
    time.sleep(qunt)



def calculations(words):
    init(autoreset=True)
    start = time.time()
    list = st.printable
    value = "";
    times = 0
    
    for loop in words:
        for loop2 in list:
            if value == words: # Your Logic here if the Password is the same
                print(Fore.RED+Style.BRIGHT+f'Script was breaked after {Fore.GREEN+str(times)+Fore.RED} time !!')
                print(Fore.RED+Style.BRIGHT+f'Process finish after {Fore.GREEN+Style.BRIGHT+str(int(time.time() - start))}s')
                break;
            # sleep(0.1) just to ad some Delay 
            print(Fore.BLUE+Style.BRIGHT+value+loop2)
	  
            times +=1
            if loop == loop2:
                value += loop
                print(Fore.GREEN+Style.BRIGHT+f'🟩]> {value}')
    pass


def main():
    init(autoreset=True)
    try:
        SelectedWord = str(input(Fore.CYAN+Style.BRIGHT+'[QS] > Enter a word to search for it! : '))
        calculations(str(SelectedWord))
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+f'Error Was detected! : {err}')
    pass



if __name__ == '__main__':
    main()
