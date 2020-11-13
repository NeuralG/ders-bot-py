import pyautogui
import time

pyautogui.FAILSAFE = False

class gun:
	def __init__(self,id1,id2,id3,id4,id5,id6,id7,id8):

		self.id1 = id1
		self.id2 = id2
		self.id3 = id3
		self.id4 = id4
		self.id5 = id5
		self.id6 = id6
		self.id7 = id7
		self.id8 = id8
		

def zoomGir():
	time.sleep(0.2)
	pyautogui.click(870,30)
	time.sleep(0.3)
	pyautogui.click(870,30)
	time.sleep(0.2)
	pyautogui.click(870,30)
	time.sleep(15)


def killZoom():
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'alt', 't')
	time.sleep(5)
	pyautogui.click(700,290)
	pyautogui.click(700,290)
	time.sleep(2)
	pyautogui.write("sudo pkill zoom", interval=0.10)
	time.sleep(3)
	pyautogui.press('enter')
	pyautogui.write("umcumc1.", interval=0.10)
	time.sleep(5)
	pyautogui.press('enter')
	time.sleep(10)
	pyautogui.click(980,150)
	pyautogui.click(980,150)

def dersGir(id):
	pyautogui.click(1200,350) #join meeting
	time.sleep(2)		
	pyautogui.click(700,290)	#id giriş tıklama
	time.sleep(0.1)
	pyautogui.click(700,290)	#id giriş tıklama
	pyautogui.write(id, interval=0.15) #id yazış
	time.sleep(0.2)
	pyautogui.press('enter') #id enterla
	time.sleep(5)

	pyautogui.press('tab') #id bugu dodge
	pyautogui.press('tab') 
	pyautogui.press('tab') 
	pyautogui.press('enter') 

	pyautogui.click(700,290)	#sifre grisi
	pyautogui.write("ofl", interval=0.15) #sifre yaz
	time.sleep(2)
	pyautogui.press('enter') #sifre onaypa

def zoomMakros(id):

	killZoom()
	zoomGir()
	dersGir(id)
	time.sleep(60)


Deney="258 664 8254"
Mat="302 411 8888"
Alman="405 344 5507"
Edeb="972 745 2887"	
Biyo="347 8899 278"
Fizik="760 179 3037"
Coğrafya="584 670 7391"
Bilg="596 833 6516"
Müzik="859 289 1534"
Kimya="859 289 15345"
Tarih="783 512 9548"
Beden="703 670 9825"
Ing="432 992 6244"
Felsefe="880 853 7071"

Pzt = gun(Mat,Mat,Mat,Mat,Alman,Alman,Edeb,Edeb)
Salı = gun(Biyo,Edeb,Mat,Mat,Fizik,Fizik,Coğrafya,Coğrafya)
Carsamba = gun(Mat,Mat,Ing,Ing,Bilg,Bilg,Müzik,Müzik)
Persembe = gun(Kimya,Kimya,Tarih,Tarih,Mat,Mat,Biyo,Biyo)
Cuma = gun(Beden,Beden,Ing,Ing,Edeb,Edeb,Felsefe,Felsefe)



while True:

	now = time.localtime()

	gun = now[6]
	saat = now[3]
	dk = now[4]


	if gun==0:
		if saat==8 and dk==29:
			zoomMakros(Pzt.id1)
		elif saat==9 and dk==9:
			zoomMakros(Pzt.id2)
		elif saat==9 and dk==49:
			zoomMakros(Pzt.id3)
		elif saat==10 and dk==29:
			zoomMakros(Pzt.id4)
		elif saat==11 and dk==9:
			zoomMakros(Pzt.id5)
		elif saat==11 and dk==49:
			zoomMakros(Pzt.id6)
		elif saat==13 and dk==9:
			zoomMakros(Pzt.id7)
		elif saat==13 and dk==49:
			zoomMakros(Pzt.id8)

	elif gun==1:
		if saat==8 and dk==29:
			zoomMakros(Salı.id1)
		elif saat==9 and dk==9:
			zoomMakros(Salı.id2)
		elif saat==9 and dk==49:
			zoomMakros(Salı.id3)
		elif saat==10 and dk==29:
			zoomMakros(Salı.id4)
		elif saat==11 and dk==9:
			zoomMakros(Salı.id5)
		elif saat==11 and dk==49:
			zoomMakros(Salı.id6)
		elif saat==13 and dk==9:
			zoomMakros(Salı.id7)
		elif saat==13 and dk==49:
			zoomMakros(Salı.id8)

	elif gun==2:
		if saat==8 and dk==29:
			zoomMakros(Carsamba.id1)
		elif saat==9 and dk==9:
			zoomMakros(Carsamba.id2)
		elif saat==9 and dk==49:
			zoomMakros(Carsamba.id3)
		elif saat==10 and dk==29:
			zoomMakros(Carsamba.id4)
		elif saat==11 and dk==9:
			zoomMakros(Carsamba.id5)
		elif saat==11 and dk==49:
			zoomMakros(Carsamba.id6)
		elif saat==13 and dk==9:
			zoomMakros(Carsamba.id7)
		elif saat==13 and dk==49:
			zoomMakros(Carsamba.id8)

	elif gun==3:
		if saat==8 and dk==29:
			zoomMakros(Persembe.id1)
		elif saat==9 and dk==9:
			zoomMakros(Persembe.id2)
		elif saat==9 and dk==49:
			zoomMakros(Persembe.id3)
		elif saat==10 and dk==29:
			zoomMakros(Persembe.id4)
		elif saat==11 and dk==9:
			zoomMakros(Persembe.id5)
		elif saat==11 and dk==49:
			zoomMakros(Persembe.id6)
		elif saat==13 and dk==9:
			zoomMakros(Persembe.id7)
		elif saat==13 and dk==49:
			zoomMakros(Persembe.id8)


	elif gun==4:
		if saat==8 and dk==29:
			zoomMakros(Cuma.id1)
		elif saat==9 and dk==9:
			zoomMakros(Cuma.id2)
		elif saat==14 and dk==29:
			zoomMakros(Cuma.id3)
		elif saat==15 and dk==9:
			zoomMakros(Cuma.id4)
		elif saat==11 and dk==9:
			zoomMakros(Cuma.id5)
		elif saat==11 and dk==49:
			zoomMakros(Cuma.id6)
		elif saat==13 and dk==9:
			zoomMakros(Cuma.id7)
		elif saat==13 and dk==49:
			zoomMakros(Cuma.id8)

time.sleep(10)
	
