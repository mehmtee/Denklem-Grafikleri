import matplotlib.pyplot as plt

from pylab import*



def denklem(fonk):
	title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
	axis_font = {'fontname':'Arial', 'size':'14'}


	
	
	x_deger = []
	y_deger = []

	#f(x) = x+4
	
	


	for i in range(-6,6):
		denklem = fonk.replace("x",str(i))
		sonuc = (eval(denklem))
		x_deger.append(i)
		y_deger.append((sonuc))
		print(("x={} --->{}").format(i,sonuc))

	plt.plot(x_deger,y_deger,'ro')
	title(("{} Denkleminin grafiği").format(fonk))
	plt.grid()
	xticks(x_deger)
	yticks(y_deger)
	plt.xticks(size=10)
	plt.xticks(size=10)




	plt.plot(x_deger,y_deger)
	fig = matplotlib.pyplot.gcf()
	fig.set_size_inches(18.5,10.5,forward=True)
	plt.ylabel("f(x)",**axis_font)

    
    


	plt.show()


print("""

Denklem grafik çizme programına hoşgeldiniz.

AngelRayt Tarafından kodlanmıştır.

İşaretler :

	Bölme işlemi : 4/2

	Çarpma işlemi : n * k

	Toplama Çıkarma : x+n  x-n



	Üs alma : x**n

	Rasyonel ifade : (1/2)+2

Örnek kullanım:
	
	2*x+1

	(1/2) **x




	""")


input_al = input("Lütfen denklem sistemini giriniz")
denklem(input_al)

