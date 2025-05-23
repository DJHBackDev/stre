import pandas as pd
import matplotlib.pyplot as plt
salarios_and_anno = [(83000,8.7)  ,(88000,8.1) ,
                     (48000, 0.7) ,(76000,6)   ,
                     (69000,6.5)  ,(76000, 7.5),
                     (60000,2.5)  ,(83000,10)  ,
                     (48000,1.9)  ,(63000,4.2)]


df = pd.DataFrame(salarios_and_anno, columns=['Salario', 'Ano'])

# print(df["Salario"].mean())
print(df["Salario"].describe())

lista = []

for x in enumerate(salarios_and_anno):
     lista.append(x[1][0])  

print(min(lista))
print(max(lista))

print(sum(lista)/len(lista))

print(sum(lista))


df.plot.scatter("Salario","Ano")
plt.show()


#libreria collections ??  ¿que es defaultdict que mas se usa?  ¿que es Counter?  ¿que es OrderedDict?

