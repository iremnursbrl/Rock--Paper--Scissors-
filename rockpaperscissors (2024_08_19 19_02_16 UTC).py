from random import randint

def print_welcome_message(): #oyunun kurallarını tanımlamak amacıyla bir hoşgeldin mesajı yazdırıyoruz
    print("Welcome to Rock, Paper, Scissors Game! \n"
          "Here are the rules: \n"
          "-Rock beats Scissors \n"
          "-Scissors beats Paper \n"
          "-Paper beats Rock \n"
          "The First player to win 2 rounds wins the game. \n"
          "If you want to exit the game, please enter 'E'. \n ")


def get_user_input(): #kullanıcıdan input alıyoruz
    user_input = input("Choose your move! (rock, paper, scissors): ").lower() #aldığımız inputun tüm harflerini lower() işlevi ile küçültüyoruz ki hata vermesin
    return user_input


def get_computer_input(options): #bilgisayardan input alıyoruz.
    return options[randint(0, 2)] #burada belirlediğimiz 3 opsiyondan (rock,paper,scissors) birini seçtireceğiz


def play_round(user, computer): #kullanıcı ve bilgisayarın hamlelerini karşılaştırıyoruz
    if user == computer:
        return "draw" #hamleler aynıysa beraberlik olur
    elif (user == "rock" and computer == "scissors") or \
            (user == "paper" and computer == "rock") or \
            (user == "scissors" and computer == "paper"):
        return "user" #kullanıcının kazanması durumunda 'user' döner
    else:
        return "computer" #bilgisayarın kazanması durumunda 'computer' döner


def print_round_result(user, computer, winner): #turun kazananını ekrana yazdıracağız
    print(f"User chose: {user}") #kullanıcının hamlesini yazdırdık
    print(f"Computer chose: {computer}") #bilgisayarın hamlesini yazdırdık
    if winner == "draw":
        print("It's a draw! How boring...\n")
    elif winner == "user":
        print(f"You win this round! {user} beats {computer}.")
    else:
        print(f"You lose this round! {computer} beats {user}.")


def ask_to_play_again(): #kullanıcıya oyuna devam etmek isteyip istemediğini soruyoruz
    play_again = input("Feeling lucky? Want to play again? (yes/no): ").lower()
    return play_again == "yes" #bu satırda play_again değikeninin yes olup olmadığını kontrol edeceğiz. eğer değişken yes ise 'True' no ise 'False' değerini döndürecek


def rock_paper_scissors_IREM_NUR_SABIRLI():
    print_welcome_message() #karşılama mesajı fonksiyonunu çağırdık

    while True:
        play_game = input("Do you want to play the game? (yes/no): ").lower()
        if play_game != "yes":
            print("Okay, maybe next time! Exiting the game. See you around!")
            break

        computer_wants_to_play = randint(0, 1) == 1 #bilgisayara oyun oynamak isteyip istemediğini soruyoruz
        if not computer_wants_to_play:
            print("The computer is not in the mood now. It doesn’t want to play. Maybe next time! Exiting the game.")
            break

        user_score = 0
        comp_score = 0
        round_number = 0

        while user_score < 2 and comp_score < 2:
            round_number += 1
            print(f"Game 1, Round {round_number} \n"
                  f"#################################")
            user_input = get_user_input()
            if user_input == 'e':
                print("Exiting the game. See you next time!")
                return
            elif user_input not in ["rock", "paper", "scissors"]:
                print("Oops! Invalid input! Please choose 'rock', 'paper' or 'scissors'.\n")
                continue

            computer_input = get_computer_input(["rock", "paper", "scissors"])
            round_winner = play_round(user_input, computer_input)
            print_round_result(user_input, computer_input, round_winner)

            if round_winner == "user":
                user_score += 1
            elif round_winner == "computer":
                comp_score += 1

            print(f"Score: User {user_score} - {comp_score} Computer\n")

        if user_score == 2:
            print("Congratulations champion! You won the game!\n")
        else:
            print("You lost the game! Better luck next time!\n")

        if not ask_to_play_again():
            print("Thanks for playing! Hope you had fun. Goodbye!")
            break


rock_paper_scissors_IREM_NUR_SABIRLI()