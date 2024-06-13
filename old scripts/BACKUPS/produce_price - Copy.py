while True:
    inflation = .15

    e = float(input("What type of produce?\n0. Manual Entry\n1. Pepper\n2. Tomato\n3. ZUCC\n4. Pumpkin\n5. Potato\n6. Carrot\n7. Onion\n8. Garlic boiiii\n9. Kohlrabi\n10. Turnip\n11. Beetroot\n12. Radish\n13. Parsnip\n14. Sugar Melon\n15. Strawberry\n16. Wheat\n17. Pineapple\n18. Beans\n19. All\n"))

    output = "price including inflation is currently "

    if e == 0:
        sM = float(input("How many slots?\n"))
        tM = float(input("Growth time?\n"))
        cM = float(input("Crop count?\n"))
        mM = sM * tM / cM * inflation
        print("Manual Entry Price = " + str(mM))

    Pe_t = 172
    Pe_c = 2
    Pe_s = 2
    if e == 1:
        plant = "Pepper "
        print(plant + output + str(Pe_s * Pe_t / Pe_c * inflation))

    To_t = 172
    To_c = 2
    To_s = 1
    if e == 2:
        plant = "Tomato "
        print(plant + output + str(To_s * To_t / To_c * inflation))

    Zu_t = 172
    Zu_c = 2
    Zu_s = 3
    if e == 3:
        plant = "ZUCC "
        print(plant + output + str(Zu_s * Zu_t / Zu_c * inflation))

    Pu_t = 259
    Pu_c = 2
    Pu_s = 4
    if e == 4:
        plant = "Pumpkin "
        print(plant + output + str(Pu_s * Pu_t / Pu_c * inflation))

    Po_t = 259
    Po_c = 2
    Po_s = 2
    if e == 5:
        plant = "Potato "
        print(plant + output + str(Po_s * Po_t / Po_c * inflation))

    Ca_t = 144
    Ca_c = 3
    Ca_s = 2
    if e == 6:
        plant = "Carrot "
        print(plant + output + str(Ca_s * Ca_t / Ca_c * inflation))

    On_t = 288
    On_c = 2
    On_s = 2
    if e == 7:
        plant = "Onion "
        print(plant + output + str(On_s * On_t / On_c * inflation))

    Ga_t = 700
    Ga_c = 4
    Ga_s = 4
    if e == 8:
        plant = "Garlic boiiii "
        print(plant + output + str(Ga_s * Ga_t / Ga_c * inflation))

    Ko_t = 129
    Ko_c = 2
    Ko_s = 3
    if e == 9:
        plant = "Kohlrabi "
        print(plant + output + str(Ko_s * Ko_t / Ko_c * inflation))

    Tu_t = 175
    Tu_c = 3
    Tu_s = 2
    if e == 10:
        plant = "Turnip "
        print(plant + output + str(Tu_s * Tu_t / Tu_c * inflation))

    Be_t = 175
    Be_c = 2
    Be_s = 2
    if e == 11:
        plant = "Beetroot "
        print(plant + output + str(Be_s * Be_t / Be_c * inflation))

    Ra_t = 60
    Ra_c = 4
    Ra_s = 2
    if e == 12:
        plant = "Radish "
        print(plant + output + str(Ra_s * Ra_t / Ra_c * inflation))

    Pa_t = 288
    Pa_c = 3
    Pa_s = 2
    if e == 13:
        plant = "Parsnip "
        print(plant + output + str(Pa_s * Pa_t / Pa_c * inflation))

    Sm_t = 187
    Sm_c = 1
    Sm_s = 4
    if e == 14:
        plant = "Sugar Melon "
        print(plant + output + str(Sm_s * Sm_t / Sm_c * inflation))

    St_t = 80
    St_c = 6
    St_s = 1
    if e == 15:
        plant = "Strawberry "
        print(plant + output + str(St_s * St_t / St_c * inflation))

    Wh_t = 345
    Wh_c = 5
    Wh_s = 20
    if e == 16:
        plant = "Wheat "
        print(plant + output + str(Wh_s * Wh_t / Wh_c * inflation))

    Pi_t = 360
    Pi_c = 1
    Pi_s = 6
    if e == 17:
        plant = "Pineapple "
        print(plant + output + str(Pi_s * Pi_t / Pi_c * inflation))

    Be_t = 273
    Be_c = 10
    Be_s = 20
    if e == 18:
        plant = "Beans "
        print(plant + output + str(Be_s * Be_t / Be_c * inflation))

    if e == 19:
        print(str("Pepper = " + str(Pe_s * Pe_t / Pe_c * inflation)))
        print(str("Tomato = " + str(To_s * To_t / To_c * inflation)))
        print(str("Zucchini = " + str(Zu_s * Zu_t / Zu_c * inflation)))
        print(str("Pumpkin = " + str(Pu_s * Pu_t / Pu_c * inflation)))
        print(str("Potato = " + str(Po_s * Po_t / Po_c * inflation)))
        print(str("Carrot = " + str(Ca_s * Ca_t / Ca_c * inflation)))
        print(str("Onion = " + str(On_s * On_t / On_c * inflation)))
        print(str("Garlic = " + str(Ga_s * Ga_t / Ga_c * inflation)))
        print(str("Kohlrabi = " + str(Ko_s * Ko_t / Ko_c * inflation)))
        print(str("Turnip = " + str(Tu_s * Tu_t / Tu_c * inflation)))
        print(str("Beetroot = " + str(Be_s * Be_t / Be_c * inflation)))
        print(str("Radish = " + str(Ra_s * Ra_t / Ra_c * inflation)))
        print(str("Parsnip = " + str(Pa_s * Pa_t / Pa_c * inflation)))
        print(str("Sugarmelon = " + str(Sm_s * Sm_t / Sm_c * inflation)))
        print(str("Strawberry = " + str(St_s * St_t / St_c * inflation)))
        print(str("Wheat = " + str(Wh_s * Wh_t / Wh_c * inflation)))
        print(str("Pineapple = " + str(Pi_s * Pi_t / Pi_c * inflation)))
        print(str("Beans = " + str(Be_s * Be_t / Be_c * inflation)))

    done = str(input("---------------\nAll done? [y/n]\n"))
    if done == "n":
        continue
    if done == "y":
        break


# slots per crop
# s = _
# time taken to grow
# t = _
# crop count
# c = _



# final price point
# p = .29 * s * t / c

# print(p)
