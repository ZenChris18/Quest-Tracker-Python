def main():
    quest_journal = {}
    status_journal = {}
    counter = 1

    while True:
        print("Type 1 to add a new quest")
        print("Type 2 to view existing quests")
        print("Type 3 to edit status of quest")
        print("Type 0 to exit journal \n")
        action = int(input("Type an action: "))
        print()

        if action == 1:
            quest = add_quest()
            quest_journal[counter] = quest
            counter += 1
            for value in quest_journal.values(): # add .values() if only wanted to get the values, .items() for both keys and values
                if value in status_journal:
                    pass
                else:
                    status_journal[value] = "idle"
            print()
            print("Succesfully added quest")
            print()
        elif action == 2:
            print(quest_journal)
            print()
        elif action == 3:
            print(status_quest(status_journal))
            print()
        elif action == 0:
            break
        else:
            print("pick a right action\n")
    

def add_quest():
    added_quest = input("what quest to enter journal: ").lower()
    return added_quest

def status_quest(status_journal):
    while True:
        print("Type 1 to mark a quest as active")
        print("Type 2 to mark a quest as idle")
        print("Type 3 to mark a quest as complete")
        print("Type 0 to quit this menu")
        print("")
        change = int(input("Select a number: "))
        if change == 1:
            print("Quests")
            print(status_journal)
            active = input("Select a quest to mark as active (type the name of the quest)").lower()
            if active in status_journal:
                status_journal[active] = "active"
            else:
                print("quest not found")
                print()
        elif change == 2:
            print("Quests")
            print(status_journal)
            idle = input("Select a quest to mark as idle (type the name of the quest)").lower()
            if idle in status_journal:
                status_journal[idle] = "idle"
            else:
                print("quest not found")
                print()
        elif change == 3:
            print("Quests")
            print(status_journal)
            complete = input("Select a quest to mark as complete (type the name of the quest)").lower()
            if complete in status_journal:
                status_journal[complete] = "complete"
            else:
                print("quest not found")
                print()
        elif change == 0:
            break
        else:
            print("select a valid action")
            print


    return status_journal

if __name__ == "__main__":
    main()