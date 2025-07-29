import os
import subprocess
from colorama import Fore, Back, Style, init
init(autoreset=True)
print(Fore.BLUE + Style.BRIGHT + '                                                     mmmm    mmmm     oooo      nn    nn     IIIIII     TTTTTTTT      oooo      RRRRRR                                              ')
print(Fore.BLUE + Style.BRIGHT + '                                                     mmmm    mmmm    oo  oo     nnn   nn       II       TTTTTTTT     oo  oo     RR     R')
print(Fore.BLUE + Style.BRIGHT + '                                                     mmmm mm mmmm    oo  oo     nn nn nn       II         TTTT       oo  oo     RR      R ')
print(Fore.BLUE + Style.BRIGHT + '                                                     mm   mm   mm    oo  oo     nn  nn n       II         TTTT       oo  oo     RR     R')
print(Fore.BLUE + Style.BRIGHT + '                                                     mm   mm   mm    oo  oo     nn  nn n       II         TTTT       oo  oo     RRRRRRRR')
print(Fore.BLUE + Style.BRIGHT + '                                                     mm   mm   mm    oo  oo     nn  nn n       II         TTTT       oo  oo     RR RR  ')
print(Fore.BLUE + Style.BRIGHT + '                                                     mm   mm   mm      oo       nn  nn n     IIIIII       TTTT         oo       RR  RR')
print(Fore.RED + Style.BRIGHT + '                                                                                                       By MO7EY ELSHARKAWY')
choise=None
def show():

			devices2=[x.split()[0] for x in subprocess.getoutput('iwconfig').split('\n') if 'IEEE' in x]
			print(Fore.BLUE + Style.BRIGHT + f'                                  {devices2}')
def mode():
	devices2=[x.split()[0] for x in subprocess.getoutput('iwconfig').split('\n') if 'IEEE' in x]
	while True:
		ad=input(Fore.YELLOW + Style.BRIGHT + 'Enter an adapter to set: ')
		devices2=[x.split()[0] for x in subprocess.getoutput('iwconfig').split('\n') if 'IEEE' in x]
		if ad in devices2:
			break
		else:
			print(Fore.RED + Style.BRIGHT + 'Please Enter a valid interface')
	while True:
		print(Fore.BLUE + Style.BRIGHT + '1.monitor')
		print(Fore.BLUE + Style.BRIGHT + '2.managed')
		print(Fore.BLUE + Style.BRIGHT + '3.RETURN')
		mod = input('Choose a mode to set: ')
		nums = ['1','2','3']
		if mod in nums:
			break
		elif mod=='3':
			main()
		else:
			print(Fore.RED + Style.BRIGHT + 'Enter a valid mode please!!!!!')
		
	if mod == '1':
		os.system(f'sudo airmon-ng start {ad}')
	elif mod =='2':
		os.system(f'sudo airmon-ng stop {ad}')

def main():
	
	while True:
		print(Fore.BLUE + Style.BRIGHT + '1.show interfaces')
		print(Fore.BLUE + Style.BRIGHT + '2.start managed/monitor mode')
		print(Fore.BLUE + Style.BRIGHT + '3.exit')
		
		try:
			choise=input(Fore.YELLOW + Style.BRIGHT + 'Enter an option: ')
		except ValueError:
			print(Fore.RED + Style.BRIGHT + 'Enter a valid option: ')
		if choise=='1':
			show()
		elif choise=='2':
			mode()
		elif choise=='3':
			X = input(Fore.YELLOW + Style.BRIGHT + 'Do you want to exit? (y/n)').lower()
			if X=='y':
				break
		else:
			print(Fore.RED + Style.BRIGHT + 'Please,Enter a valid option')
if __name__=='__main__':
	main()
