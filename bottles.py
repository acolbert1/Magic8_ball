
def song():
    empty_bottles = 99
    for bottle in range(empty_bottles):
        if empty_bottles == 2:
            print(str(empty_bottles) + " bottles of beer on the wall, " + str(empty_bottles) + " bottles of beer. Take one down and pass it around, " + str(empty_bottles - 1) + " more bottle of beer on the wall.")
        elif empty_bottles == 1:
            print(str(empty_bottles) + " bottle of beer on the wall, " + str(empty_bottles) + " bottle of beer. Take one down and pass it around, " + str(empty_bottles - 1) + " bottles of beer on the wall.")
        else:
            print(str(empty_bottles) + " bottles of beer on the wall, " + str(empty_bottles) + " bottles of beer. Take one down and pass it around, " + str(empty_bottles - 1) + " bottles of beer on the wall.")
            
        
        
        empty_bottles = empty_bottles - 1
    return bottle

song()

