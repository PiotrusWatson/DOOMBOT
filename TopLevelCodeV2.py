while(!gotShotgun and !gotRocket):
    if lowExistingArmour:
        findArmour()
    if existingWeapon:
        getWeapon()
    if enemies:
        hitOrShoot()
    if lowHealth:
        getHealth()
    getWeapon()

if (gotShotgun):
    while(!gotRocket):
        if lowExistingArmour():
            findArmour()
        if 

def getWeapon():
    
    
#lowArmour code
def findArmour():
    #startTime = int(round(time.time()))
    while(!noArmor) #and ((int(round(time.time())) - startTime) > 30):
        runAndShootMovingTo(armour)

            
#Enemies code
def hitOrShoot(destination):
    if lowExistingArmour():
        findArmor()
    if attacked():
        attackDodgeLoop()
    if noEnemies():
        return
    if lowHealth():
        kamikase()
        #death
    if ammo():
        runAndShootMovingTo(destination)
    else
        hit()
        return

#lowHealth   
def kamikase():
    runAndShootMovingTo(losingPlayer)

    
        
