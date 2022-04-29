import math

# It is known:
Aangle = int(30)
Sarea = int(10)
#---------------

#AC^2(Получаем синус в радианах, и переводим в градусы):
ACsquare = math.sqrt(Sarea / (math.sin(2 * Aangle  * math.pi / 180)))  

sin60 = math.sin(60 * math.pi / 180)

print(Aangle, Sarea, ACsquare, sin60, )
