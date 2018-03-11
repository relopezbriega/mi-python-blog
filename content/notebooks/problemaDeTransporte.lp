\* Problema de distribución de cerveza *\
Minimize
Suma_de_costos_de_transporte: 2 ruta_Cervecería_A_Bar_1
 + 4 ruta_Cervecería_A_Bar_2 + 5 ruta_Cervecería_A_Bar_3
 + 2 ruta_Cervecería_A_Bar_4 + ruta_Cervecería_A_Bar_5
 + 3 ruta_Cervercería_B_Bar_1 + ruta_Cervercería_B_Bar_2
 + 3 ruta_Cervercería_B_Bar_3 + 2 ruta_Cervercería_B_Bar_4
 + 3 ruta_Cervercería_B_Bar_5
Subject To
Sum_of_Products_into_BarBar_1: ruta_Cervecería_A_Bar_1
 + ruta_Cervercería_B_Bar_1 >= 500
Sum_of_Products_into_BarBar_2: ruta_Cervecería_A_Bar_2
 + ruta_Cervercería_B_Bar_2 >= 900
Sum_of_Products_into_BarBar_3: ruta_Cervecería_A_Bar_3
 + ruta_Cervercería_B_Bar_3 >= 1800
Sum_of_Products_into_BarBar_4: ruta_Cervecería_A_Bar_4
 + ruta_Cervercería_B_Bar_4 >= 200
Sum_of_Products_into_BarBar_5: ruta_Cervecería_A_Bar_5
 + ruta_Cervercería_B_Bar_5 >= 700
Suma_de_Productos_que_salen_de_cervecerias_Cervecería_A:
 ruta_Cervecería_A_Bar_1 + ruta_Cervecería_A_Bar_2 + ruta_Cervecería_A_Bar_3
 + ruta_Cervecería_A_Bar_4 + ruta_Cervecería_A_Bar_5 <= 1000
Suma_de_Productos_que_salen_de_cervecerias_Cervercería_B:
 ruta_Cervercería_B_Bar_1 + ruta_Cervercería_B_Bar_2
 + ruta_Cervercería_B_Bar_3 + ruta_Cervercería_B_Bar_4
 + ruta_Cervercería_B_Bar_5 <= 4000
Bounds
0 <= ruta_Cervecería_A_Bar_1
0 <= ruta_Cervecería_A_Bar_2
0 <= ruta_Cervecería_A_Bar_3
0 <= ruta_Cervecería_A_Bar_4
0 <= ruta_Cervecería_A_Bar_5
0 <= ruta_Cervercería_B_Bar_1
0 <= ruta_Cervercería_B_Bar_2
0 <= ruta_Cervercería_B_Bar_3
0 <= ruta_Cervercería_B_Bar_4
0 <= ruta_Cervercería_B_Bar_5
Generals
ruta_Cervecería_A_Bar_1
ruta_Cervecería_A_Bar_2
ruta_Cervecería_A_Bar_3
ruta_Cervecería_A_Bar_4
ruta_Cervecería_A_Bar_5
ruta_Cervercería_B_Bar_1
ruta_Cervercería_B_Bar_2
ruta_Cervercería_B_Bar_3
ruta_Cervercería_B_Bar_4
ruta_Cervercería_B_Bar_5
End
