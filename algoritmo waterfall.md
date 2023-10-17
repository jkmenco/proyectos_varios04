# Dado un arreglo de enteros que representan barreras con diferentes alturas (m) y con separación de 1m. <br><br>Encuentre cual pareja de barreras puede contener la mayor cantidad de agua.

## **Input:**[1,5,8,9,4,5]

<br>
<br>
<br>

![image](https://cdn.cacher.io/attachments/u/3iimr1rui030a/I0jeQJxLDbDauIPberC1U4u6JHI_ssj5/Screen_Shot_2022-12-12_at_5.49.10_PM.png)


## **Ejemplo:**[3,5] *Contiene 10 lts*

![image(3,5)](https://cdn.cacher.io/attachments/u/3iimr1rui030a/1oI7KtBMgaYV5K1hVseYkxlj1k2QegMG/Screen_Shot_2022-12-13_at_10.49.02_AM.png)

<br>
<br>

# Encontrar cual pareja de barreras contiene mayor cantidad de agua.

[1,5,8,9,4,5]

<br>
<br>
<br>
<br>

# Conclusiones

* Se debe calcular entre 1 pareja (y rango entre estos) cual puede contener la mayor cantidad de agua

* Se puede calcular el área de un rectángulo entre estos grupos

* La separación entre cada barrera es de 1 metro, la base será siempre 1m y la altura límite dependerá del más bajo del grupo

* Si se logra concatenar en escalera se encontrará el máximo posible. Es posible encontrar 2 eventos:
	1. Si entre medio de la pareja existe un menor, su altura se debe ignorar y tener en cuenta solo su alrededor. <br>[9-4-5)] El elemento 4 se ignora y calcular el límite de 5 con 9
	2. Elegir una pareja entre el máximo de altura y mínimo en escalera descendente para encontrar el máximo de agua.
<br>

# Todo esto dentro del rango de número de la lista. <br><br>Al final, mostrar resultados, los 2 números formados con la mayor cantidad de agua y la cantidad de agua total.

<br>
<br>
<br>
<br>


