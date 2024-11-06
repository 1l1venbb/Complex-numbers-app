import functionalities.menus as menus
import functionalities.menus2 as menus2

backup = []
x = int(input("Press 1 for single functionality mode or press 2 for multiple functionality mode:"))
if x == 1:
    menus.run()
elif x == 2:
    menus2.run()