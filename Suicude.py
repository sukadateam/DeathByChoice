import sys
arguments = list(sys.argv)
murderoptions=['-Axe', '-GunPoint', '-Medieval']
murderexepect=['-Expected', '-Unexpected', '-E', '-U', '-e', '-u']
print(arguments)
import time
class checks:
    def VictimCheck():
        '''Checks for the first required argument. Victim'''
        global arguments
        if "-V" in arguments:
            #If match found, return True
            return True
        #If no matches found, return False
        return False
    def MurderCheck():
        '''Checks for the second required argument. Murder Option'''
        global arguments, murderoptions
        for i in range(len(murderoptions)):
            if murderoptions[i] in arguments:
                #If match found, return True
                return True
        #If no matches found, return False
        return False
    def MurderExpect():
        '''Checks for the third required argument. Expectation'''
        global arguments, murderexepect
        for i in range(len(murderoptions)):
            if murderexepect[i] in arguments:
                #If match found, return True
                return True
        #If no matches found, return False
        return False
class display:
    def Victim():
        '''Grabs the victim and commenses death!!!'''
        global arguments
        breakAct=False #Determines if no arg was found
        for i in range(len(arguments)):
            if arguments[i] == "-V":
                breakAct=True
                break
        if breakAct==False:
            print("Something is wrong. Function: display.Victim()")
        return arguments[i+1]
if "-help" in arguments:
    '''Shows function uses'''
    print('''
    Usage:
    murder [victim] [options]
    * = case sensative

    Victim Selection:
        -V (victim, *)
    Murder Options:
        -Axe (*)
        -GunPoint (*)
        -Medieval (*)
    Murder Expectations:
        -Expected (*)
        -Unexpected (*)
        -E, -e (same as Expected)
        -U, -u (same as Unexpected)
    ''')
#Prevents actions if help menu is used. Helps priority problems.
if "-help" not in arguments:
    if checks.VictimCheck() == True:
        if checks.MurderExpect() == True:
            if checks.VictimCheck() == True:
                print("All checks passed")
                victim=display.Victim()
                print(str(victim), 'will not live for long. Their life will end soon.')
                time.sleep(3.5)
                print('There isn\'t enough time to say sorry for what you\'ve done. Why would you do this?')
                time.sleep(4)
                print('Theres always room for forgiveness. But, you could\'t take it. Could you?')
                time.sleep(4)
                print('You took their life. You choose to end thier life.')
                time.sleep(3)
                print('Do you even know what you chose?')
                time.sleep(2)
                if '-Axe' in arguments:
                    print("You choose to swipe them with an axe. You should be glad, your not the one who has to do it.")
                if '-GunPoint' in arguments:
                    print('You choose to shoot them. Your dna is all over that gun. Once they find you, your life will also end.')
                if '-Medievel' in arguments:
                    print('You brought back the most sadistic thing ever. The brass bull. Do you love watching your enemy being burned alive?')
                time.sleep(4)
                print("I'm done. Fuck you!")