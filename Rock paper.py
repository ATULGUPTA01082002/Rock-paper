def show_banner():
    print('')
    print("\t\t WELCOME TO -- Rock, Paper, Sessors --  GAME . \n")


def rules():
    RUN_Rules = True
    while RUN_Rules:
        print()
        print('-'*22 +' MATCH RULES ' + 22 *'-')
        print()
        print('1.As Default The Match Has 4 Step/Hand.If You Want More, Enter A Number. Else Enter 1 After Start The Match. ')
        print("2.You Can't Exit While You Stile On the Game.")
        print("3.The Users Shoulden't See Your next Step , Be Carefull. ")
        print("4.The Mach Has Rating System And Tell You're Score in Match And After Your Done.")
        print('\n')
        user_choice = input(" Back To Main Menu ? Press <E> For Exit : ")
        if user_choice.lower() == 'e':
            RUN_Rules = False
        else:
            print(" !!! WRONG INPUT !!! > PLEASE ENTER CORRECT ANSWER.")


from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2 

def get_user_selection(user):
    import getpass
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(getpass.getpass(f" {user} --> Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action


def determine_winner(user1_action, user2_action , user_1_score ,user_2_score):
    victories = {
    Action.Rock: [Action.Scissors],  # Rock beats scissors
    Action.Paper: [Action.Rock],  # Paper beats rock
    Action.Scissors: [Action.Paper]  # Scissors beats paper
    }
    
    defeats = victories[user1_action]
    if user1_action == user2_action:
        print('-'*35)
        print(f"Both players selected {user1_action.name}. It's a tie!")
        user_1_score['user1_score'] += 1
        user_2_score['user2_score'] += 1
        print(f'USER 1 Score -> {user_1_score.get("user1_score")}',f'\nUSER 2 Score -> {user_2_score.get("user2_score")}')
        print('-'*35)

    elif user2_action in defeats:
        print('-'*35)
        print(f"{user1_action.name} beats {user2_action.name}! USER 1 win!")
        user_1_score['user1_score'] += 1
        print(f'USER 1 Score -> {user_1_score.get("user1_score")}',f'\nUSER 2 Score -> {user_2_score.get("user2_score")}')
        print('-'*35)
    else:
        print('-'*35)
        print(f"{user2_action.name} beats {user1_action.name}! USER 2 Win.")
        user_2_score['user2_score'] += 1
        print(f'USER 1 Score -> {user_1_score.get("user1_score")}',f'\nUSER 2 Score -> {user_2_score.get("user2_score")}')
        print('-'*35)
    return user_1_score , user_2_score 


def get_key(val , my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
    return "key doesn't exist"

def calculate_score(score):
    user1_score = score[0]
    user2_score = score[1]
    max_score = max(user2_score.get('user2_score') ,user1_score.get('user1_score') )
    
    if user1_score.get('user1_score') == user2_score.get('user2_score') :
        print('\t\t' + 'WOW, THE MATCH IS TIE :?')
        
    elif get_key(max_score , user1_score) == 'user1_score' :
        print('\t' + 'Congratulations, USER [1] IS WINNER :)')
        
    elif get_key(max_score , user2_score) == 'user2_score':
        print('\t' + 'Congratulations, USER [2] IS WINNER :)')

    else:
        pass



def run_game():
    from time import time

    MATCH_ROUND = int(input('Enter Match Round : '))
    user_1_score = {'user1_score' : 0}
    user_2_score = {'user2_score' : 0}
    
    while MATCH_ROUND > 0:
        start_time = time()
        counter = 4
        while counter > 0:
            try:
                user1_action = get_user_selection('USER1')
                user2_action = get_user_selection('USER2')
                
            except ValueError as e:
                range_str = f"[0, {len(Action) - 1}]"
                print(f"Invalid selection. Enter a value in range {range_str}",e)
                continue
            counter-=1
            SCORE = determine_winner(user1_action, user2_action, user_1_score ,user_2_score)    
        MATCH_ROUND -= 1
        if MATCH_ROUND == 0:
            endtime = time()
            print('#'*50)
            print('\t\t'+'- MATCH IS COMPLETE -')   
            calculate_score(SCORE)
            print('\t\t' + f'[ Time To End is {(endtime - start_time):.1f}s ]')
            print('#'*50)
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                MATCH_ROUND = False
            else:
                run_game() 
        

def menu():
    RUN_Menu = True
    while RUN_Menu:
        cls = lambda: print('\n'*100)
        cls()
        show_banner()
        
        print('')
        print('1.Start Match')
        print('2.Rules ')
        print('3.Exit')
        user_choice = input("Choose Menu Number : ")
        if user_choice == '1':
            run_game()
        elif user_choice == '2':
            rules()
        elif user_choice == '3':
            RUN_Menu = False
        else:
            pass


if __name__ == "__main__":
    
    menu()