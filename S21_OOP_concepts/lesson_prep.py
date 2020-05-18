f = open('links.txt', 'r')

for line in f:
     #https://github.com/learn-co-students/dsc-classes-and-instances-onl01-dtsc-ft-030220
     #https://github.com/learn-co-curriculum/dsc-introduction-to-object-orientation.git
     lesson = line.strip()
     lesson = lesson.replace('https://github.com/learn-co-curriculum/','')
     lesson = lesson.replace('https://github.com/learn-co-students/','')
     lesson = lesson.replace('.git', '')

     name = lesson
     name = name.replace('dsc-', '')
     name = name.replace('-onl01-dtsc-ft-030220', '')
     
     #print(name, "<br>")
     link='['+name+'](./'+lesson+'/index.ipynb)<br>'
     #[Introduction](./dsc-logistic-regression-intro-onl01-dtsc-ft-030220/index.ipynb)
     print(link)
     print("\n")
	 
f.close()