# Algoritmos y Estructuras de Datos

# 1erPARCIAL - JUEVES - 01/10/26 - Comisión 2 -



- - -

### 📌 **Modalidad**

* 🗓️ **Fecha:** Jueves **01/10**
* 🕖 **Disponibilidad:** desde las **08:30 hs** hasta las **14:15 h**.
* ⏱️ **Duración máxima:** **3 horas y 30 minutos (3:30 h)** desde el momento en que bifurcan el repositorio.
* 🧪 **Intentos:** Solo **1 (uno)**. 
* 📢 **Publicación de notas:** a más tardar el **Lunes posterior, después de las hs**.

> ⚠️ **IMPORTANTE:** deben estar conectados al Meet, **SE CONSIDERAN AUSENTES AQUELLOS/AS ALUMNOS/AS QUE NO SE CONECTEN**

> ⚠️ **IMPORTANTE:** Al final del archivo `README.md`, **DEBEN completar sus datos personales** (nombre completo, número de legajo y correo institucional).


- - -

## La Vida en Springfield

- - -

## Ejercicio 1: La Serie de Potencias de Homero

Generar una lista por compresión que contenga la cantidad de donas que Homero consume en el infierno. Por cada dona que Homero consume apareceran más donas al ritmo de raíz de dos donas ($\displaystyle \sqrt{2}$) en su suplicio hasta que reviente.  

Ejemplo: <code>{ 1: 1, 2: 1.41421356237, 3: 2, 4: 2.82842712475, 5: ... }</code>

## Ejercicio 2: La Eficiencia de Homer en la Barbacoa (Iterativo)

Escribir una función iterativa que calcule la cantidad total de donas consumidas en una fiesta. Recibe como parámetros dos números (naturales) `a` (donas por persona) y `b` (cantidad de personas), y devuelve el total de donas consumidas.

## Ejercicio 3: La Paciencia de Marge con los Niños (Recursivo)

Escribir una función recursiva que calcule cuántas veces Bart ha interrumpido a Marge. Recibe como parámetros dos números (naturales) `a` (interrupciones por hora) y `b` (horas de la tarde), y devuelve el total de interrupciones.

## Ejercicio 4: La Organización de Springfield (Condicional)

Escribir una función que reciba dos parámetros:
(i) una lista desordenada de "eventos" (ej: "Kermés", "Concurso de Comida", "Reunión del Concejo Municipal"); y
(ii) una expresión booleana (que puede ser evaluada a `True` o `False`).

Si el valor de la expresión es `True`, la lista de eventos se ordenará alfabéticamente en orden descendente (de la Z a la A). En caso contrario, se ordenará de forma ascendente (de la A a la Z). Por defecto, si la función es llamada sin una "expresión" (solo la lista de eventos), la lista debe retornar ordenada de forma ascendente.

## Ejercicio 5: El Inventario del Kwik-E-Mart

Definir una clase `ProductoKwikE` que represente un artículo en venta en el Kwik-E-Mart. Contiene los datos:
*   `descripcion`: 'string'
*   `id_producto`: 'integer'
*   `fecha_vencimiento`: `date` (importar `datetime`)
*   `precio`: 'float'
*   `stock`: 'integer'

La clase debe contener métodos para facilitar:
*   Cambiar uno o varios datos del producto (descripción, precio, stock).
*   Calcular en cuántos días expira un producto. Si el método detecta que el producto ha expirado, deberá informar al usuario y marcar el stock como 0.

**Importante:** Pueden agregar más atributos y métodos si lo consideran necesario (ej: `categoria`).

## Ejercicio 6: La Etiqueta de los Productos del Kwik-E-Mart (Sobrecarga de Métodos)

Sobrecargar los siguientes métodos en la clase `ProductoKwikE`:
*   `__str__`: Para representar el producto de forma legible (ej: "Producto: Donuts Glaseadas | ID: 123 | Precio: $1.50 | Stock: 50").
*   `__eq__`: Para comparar si dos productos son iguales basándose en su `id_producto` y `descripcion`.

## Ejercicio 7: La Gestión del Kwik-E-Mart

Crear una clase `KwikEMart`, la cual estará representada (atributos internos) mediante varias listas de objetos del tipo `ProductoKwikE`. Cada lista corresponde a un pasillo o sección del mercado (ej: "Bebidas", "Snacks", "Conveniencia").

La clase debe contener métodos para facilitar:
*   Controlar el stock de productos (añadir un nuevo producto a un pasillo, remover un producto del inventario, actualizar stock).
*   Calcular cuántos productos expiran en las próximas 24 horas y removerlos del inventario (simulando que Apu los desecha).

**Importante:** Pueden agregar más atributos y métodos si lo consideran necesario (ej: método para buscar un producto por su ID).


## Ejercicio 8: La Gestión del Kwik-E-Mart

8.1 Se deberán implementar la listas utilizadas en las clases definidad anteriormente utilizando Listas Enlazadas. Encontraran el prototipo en su archivo correspondiente.

8.2 Implementar Iteradores para las listas enlazadas.

---
Nombre y Apellido: Rocco Linardi

Email: roccolinardi03@gmail.com

Comisión: Comision 2

---
