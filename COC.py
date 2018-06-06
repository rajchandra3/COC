#code for playing clash of clans investment
d={'Gaints:':0,'Wizards:':0,'Barbarians:':0,'Archers:':0,'Goblins:':0}
tn,y=0,1
print('\t \t\tWelcome to Clash Of Clans\n')
t=int(input('Enter the amount of exlir u wanna invest: '))
left=t
tp=int(input('What is ur troop capacity: '))
tl=tp
gn,wn,bn,an,gm=0,0,0,0,0
print('Enter the choice as 2 what u want in ur army:\n \t g --> gaints \n \t w --> wizards \n \t b --> barbarians : \n\t a --> Archers : \n\t gb --> Goblin :\n ')
while tn<tp and left>=0 and y==1:
	ng,nw,nb,na,mg=0,0,0,0,0
	ch=raw_input('Enter ur choice:')
	l=input('Enter ur level:')
	if ch=='g':
		if l==1:
			ng=left/1000
		elif l==2:
			ng=left/1250
		elif l==3:
			ng=left/1500
		elif l==4:
			ng=left/1750
		if ng*5>tl:
			ng=tl//5
		print('Available Gaints:',ng) 
		n=int(input('How many Gaints: '))
		if (tn+(n*5))>tp:
			gn+=(tp-tn)/5
		else:
			gn+=n
		d['Gaints:']=gn
		tn+=(n*5)
		if l==1:
			amount=n*1000
			left=t-amount
			ng=left/1000
		elif l==2:
			amount=n*1250
			left=t-amount
			ng=left/1250
		elif l==3:
			amount=n*1500
			left=t-amount
			ng=left/1500
		elif l==4:
			amount=n*1750
			left=t-amount
			ng=left/1750
	if ch=='w':
		if l==1:
			nw=left/2000
		elif l==2:
			nw=left/2250
		elif l==3:
			nw=left/2500
		elif l==4:
			nw=left/2750
		if nw*4>tl:
			nw=tl//4
		print('Available Wizards:',nw) 
		n=int(input('how many Wizards: '))
		if tn+(n*4)>tp:
			wn+=tp-tn/4
		else:
			wn+=n
		d['Wizards:']=wn
		tn+=(n*4)
		if l==1:
			amount=n*2000
			left=t-amount
			ng=left/2000
		elif l==2:
			amount=n*2250
			left=t-amount
			ng=left/2250
		elif l==3:
			amount=n*2500
			left=t-amount
			ng=left/2500
		elif l==4:
			amount=n*2750
			left=t-amount
			ng=left/2750
		
	elif ch=='b':
		if l==1:
			nb=left/25
		elif l==2:
			nb=left/50
		elif l==3:
			nb=left/75
		elif l==4:
			nb=left/100
		if nb*1>tl:
			nb=tl
		print('Available Barbarians :',nb) 
		n=int(input('how many Barbarians :'))
		if tn+n>tp:
			bn+=tp-tn/1
		else:
			bn+=n
		tn+=(n*1)
		d['Barbarians:']=bn
		if l==1:
			amount=n*25
			left=t-amount
			nb=left/25
		elif l==2:
			amount=n*50
			left=t-amount
			nb=left/50
		elif l==3:
			amount=n*75
			left=t-amount
			nb=left/75
		elif l==4:
			amount=n*100
			left=t-amount
			nb=left/100
	elif ch=='a':
		if l==1:
			na=left/125
		elif l==2:
			na=left/150
		elif l==3:
			na=left/175
		elif l==4:
			na=left/200
		if na*1>tl:
			na=tl
		print('Available Archers :',na) 
		n=int(input('how many Archers :'))
		if tn+n>tp:
			an+=tp-tn/1
		else:
			an+=n
		d['Archers:']=an
		tn+=(n*1)
		if l==1:
			amount=n*125
			left=t-amount
			nb=left/125
		elif l==2:
			amount=n*150
			left=t-amount
			nb=left/150
		elif l==3:
			amount=n*175
			left=t-amount
			nb=left/175
		elif l==4:
			amount=n*200
			left=t-amount
			nb=left/200
	if ch=='gb':
		if l==1:
			mg=left/20
		elif l==2:
			mg=left/40
		elif l==3:
			mg=left/60
		elif l==4:
			mg=left/80
		if mg*5>tl:
			mg=tl//1
		print('Available Goblins:',mg) 
		n=int(input('how many Goblins: '))
		if (tn+n)>tp:
			gm+=(tp-tn)/1
		else:
			gm+=n
		d['Goblins:']=gm
		tn+=(n*1)
		if l==1:
			amount=n*20
			left=t-amount
			mg=left/20
		elif l==2:
			amount=n*40
			left=t-amount
			mg=left/40
		elif l==3:
			amount=n*60
			left=t-amount
			mg=left/60
		elif l==4:
			amount=n*80
			left=t-amount
			mg=left/80
	tl=tp-tn
	y=int(input('Press  1 to take more army :'))
if left<=0 and y==1:
	print('You have exhausted all ur exlir\n')
print('\n\tYOUR ARMY')
for x in d:
	print(x,d.get(x))
print('\n You need to spend :')
print(t-left,'only')
print(left)
#error wid left value
