import json
from git import Repo
#pip install gitpython

class Character():
    def __init__(self,name):
        self.name = name
        self.sickend = 0
        self.stupified = 0
        self.enfeebled = 0
        self.dizzy = 0
        self.disoriented = 0
        self.impaired = 0
        self.rot = 0
        self.mental_block = 0
        self.bleeding = 0
        self.penance = 0

with open("party.json","r") as party_json:
    party = json.load(party_json)

def git_push():  

    PATH_OF_GIT_REPO = r'C:\Users\andro\OneDrive\Desktop\Python\affliction\.git'  # make sure .git folder is properly configured
    COMMIT_MESSAGE = 'comment from python script'

    def git_push():
        try:
            repo = Repo(PATH_OF_GIT_REPO)
            repo.git.add(update=True)
            repo.index.commit(COMMIT_MESSAGE)
            origin = repo.remote(name='origin')
            origin.push()
        except:
            print('Some error occured while pushing the code')    

    git_push()

def generate_json(characters):
    for i in characters:
        party[i.name] = {
            "sickend" : {"value":i.sickend,"effect":f"-{i.sickend} to STR, DEX and CON saves"},
            "stupified" : {"value":i.stupified,"effect":f"-{i.stupified} to INT, WIS and CHA saves"},
            "enfeebled" : {"value":i.enfeebled,"effect":f"{i.enfeebled} rounds disadvantage to STR, DEX and CON saves"},
            "dizzy" : {"value":i.dizzy,"effect":f"{i.dizzy} rounds disadvantage on INT, WIS and CHA saves"},
            "disoriented" : {"value":i.disoriented,"effect":f"{i.disoriented} rounds of random movement"},
            "impaired" : {"value":i.impaired,"effect":f"lose {i.impaired} actions, attacks or max spell levels each turn"},
            "rot" : {"value":i.rot,"effect":f"deals {i.rot*i.rot} damage at the begining of each turn"},
            "mental_block" : {"value":i.mental_block,"effect":f"deals {i.mental_block*i.mental_block*2} damage for each hostile action taken"},
            "bleeding" : {"value":i.bleeding,"effect":f"deals {i.bleeding}d6 damage at the begining of every turn and for every 10ft moved"},
            "penance" : {"value":i.penance,"effect":f"deals {i.penance*i.penance}d4 damage at the begining of each turn"}
        }
    with open("party.json","w") as party_json:
        party_json.write(json.dumps(party))
    git_push()


party_names = party.keys()

new_party = []

for name in party_names:
    new_character = Character(name)
    new_character.sickend = party[name]["sickend"]
    new_character.stupified = party[name]["stupified"]
    new_character.enfeebled = party[name]["enfeebled"]
    new_character.dizzy = party[name]["dizzy"]
    new_character.disoriented = party[name]["disoriented"]
    new_character.impaired = party[name]["impaired"]
    new_character.rot = party[name]["rot"]
    new_character.mental_block = party[name]["mental_block"]
    new_character.bleeding = party[name]["bleeding"]
    new_character.penance = party[name]["penance"]
    new_party.append(new_character)


while True:
    chose_character = input("Character/turn:" )
    if chose_character == "reset":
        for member in new_party:
            member.penance = 0
            member.sickend = 0
            member.enfeebled = 0
            member.rot = 0
            member.stupified = 0
            member.dizzy = 0
            member.mental_block = 0
            member.disoriented = 0
            member.impaired = 0
            member.bleeding = 0
        generate_json(characters = new_party)
    elif chose_character == "turn":
        for member in new_party:
            if member.enfeebled > 0:
                member.enfeebled -= 1
            if member.dizzy > 0:
                member.dizzy -= 1
            if member.disoriented > 0:
                member.disoriented -= 1
            print(f"{member.name};enfeebled:{member.enfeebled};dizzy:{member.dizzy};disoriented:{member.disoriented}")
        generate_json(characters = new_party)
    for member in new_party:
        if member.name.lower() == chose_character.lower():
            print("1. Sickend - stacking; -1 to STR, DEX and CON saves")
            print("2. Enfeebled -  duration 1d6 rounds; disadvantage on STR, DEX and CON saves")
            print("3. Rot -  stacking; each instance of rot causes one point of necrotic damage per instance of rot ")
            print("4. Stupified - stacking; -1 to INT, WIS and CHA saves")
            print("5. Dizzy - duration 1d6 rounds; disadvantage on INT, WIS and CHA saves")
            print("6. Mental block - stacking; inflict 1 point of psychic damage per instance of mental block, on hostile action")
            print("7. Disoriented - duration 1d6 rounds; random movement")
            print("8. Impaired - stacking; lose one kind of action, one attack or one spell level")
            print("9. Bleeding - stacking; 1d6 bleed per level of bleed on begining of turn and 10ft move")
            print("10. Penance - stacking; number of instances for each instance d4 of penance each turn")
            choice = int(input("1-10: "))
            number = int(input("Amount: "))
            if choice == 1:
                member.sickend += number
                print(f"{member.name};sickened:{member.sickend}")
            if choice == 2:
                member.enfeebled += number
                print(f"{member.name};enfeebled:{member.enfeebled}")
            if choice == 3:
                member.rot += number
                print(f"{member.name};rot:{member.rot}")
            if choice == 4:
                member.stupified += number
                print(f"{member.name};stupified:{member.stupified}")
            if choice == 5:
                member.dizzy += number
                print(f"{member.name};dizzy:{member.dizzy}")
            if choice == 6:
                member.mental_block += number
                print(f"{member.name};mental_block:{member.mental_block}")
            if choice == 7:
                member.disoriented += number
                print(f"{member.name};disoriented:{member.disoriented}")
            if choice == 8:
                member.impaired += number
                print(f"{member.name};impaired:{member.impaired}")
            if choice == 9:
                member.bleeding += number
                print(f"{member.name};bleeding:{member.bleeding}")
            if choice == 10:
                if number > 0:
                    total_afflictions = member.sickend + member.enfeebled + member.rot + member.stupified + member.dizzy + member.mental_block + member.disoriented + member.impaired + member.bleeding    
                    member.penance += total_afflictions
                    member.sickend = 0
                    member.enfeebled = 0
                    member.rot = 0
                    member.stupified = 0
                    member.dizzy = 0
                    member.mental_block = 0
                    member.disoriented = 0
                    member.impaired = 0
                    member.bleeding = 0
                    print(f"{member.name};penance:{member.penance}")
                    print(f"Total afflictions removed: {total_afflictions}")
                else:
                    member.penance = int(member.penance / 2)
                    print(f"{member.name};penance:{member.penance}")
            generate_json(characters = new_party)
            



#names = ["Brna","Tonc","Vix","Jura","Dunaj"]
#
#characters = []
#
#for name in names:
#    new_character = Character(name)
#    characters.append(new_character)




#party = {}
#


