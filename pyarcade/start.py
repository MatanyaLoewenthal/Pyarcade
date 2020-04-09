from pyarcade.input_system import InputSystem

def run_pyarcade():
    input_sys = InputSystem()

    while True:
        print("Welcome to PyArcade (Enter a number)")
        print("(1) Mastermind      (2) Minesweeper  (3) Crazy Eights     (4) Exit")
        game_input = str(input())

        if game_input == "4":
            break

        while True:
            if game_input.lower() == "1":
                print("Please enter your guess (\"####\") or enter quit to leave game")
                user_move = str(input())
                if user_move == "quit":
                    break
                print(input_sys.handle_game_input("Mastermind", user_move))
                if input_sys.mastermind_game.game_state == "Game over.":
                    print("Game over. Play again? y/n")
                    if str(input()) != "y":
                        break
                    else:
                        print(input_sys.handle_game_input("Mastermind", "Reset Game"))
            elif game_input.lower() == "2":
                print("Please enter x, y coordinate (\"#,#\") or enter quit to leave game")
                user_move = str(input())
                if user_move == "quit":
                    break
                print(input_sys.handle_game_input("Minesweeper", user_move))
                if input_sys.minesweeper_game.game_state == "Game over.":
                    print("Game over. Play again? y/n")
                    if str(input()) != "y":
                        break
                    else:
                        print(input_sys.handle_game_input("Minesweeper", "Reset Game"))
            elif game_input.lower() == "3":
                print("Please type draw or enter card you wish to play (Ex: Eight,Spades).")
                print("Or enter quit to leave game")
                user_move = str(input())
                if user_move == "quit":
                    break
                print(input_sys.handle_game_input("Crazy Eights", user_move))
                if input_sys.minesweeper_game.game_state == "Game over.":
                    print("Game over. Play again? y/n")
                    if str(input()) != "y":
                        break
                    else:
                        print(input_sys.handle_game_input("Crazy Eights", "Reset Game"))
            else:
                break


if __name__ == "__main__":
    run_pyarcade()