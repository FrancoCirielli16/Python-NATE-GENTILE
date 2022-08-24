import PySimpleGUI as sg

button_size = (4, 2)
PLAYER_ONE = "X"
PLAYER_TWO = "O"
wins_palyer = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
sg.theme('Dark Grey 13')
layout = [
            [
                sg.Button("", key="-0-", size=button_size),
                sg.Button("", key="-1-", size=button_size),
                sg.Button("", key="-2-", size=button_size)
            ],
            [
                sg.Button("", key="-3-", size=button_size),
                sg.Button("", key="-4-", size=button_size),
                sg.Button("", key="-5-", size=button_size)
            ],
            [
                sg.Button("", key="-6-", size=button_size),
                sg.Button("", key="-7-", size=button_size),
                sg.Button("", key="-8-", size=button_size)
            ],
            [
                sg.Text("Ganador:", key="-WINNER-"),
            ],
            [
                sg.Text("Perdedor:", key="-LOSER-"),
            ],
            [
                sg.Button("OK", key="-OK-"),
            ],

        ]



def run_play(window):
    game_end = False
    winner = ""
    PLAYER_INICIAL = PLAYER_ONE
    deck = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]

    while True:
        event, values = window.read()
        print(event)
        if event == sg.WIN_CLOSED or event == "-OK-":
            END = event
            return END

        if window.Element(event).ButtonText == "" and not game_end:
            index = int(event.replace("-", ""))
            deck[index] = PLAYER_INICIAL
            window.Element(event).Update(text=PLAYER_INICIAL)

            for win_play in wins_palyer:
                if deck[win_play[0]] == deck[win_play[1]] == deck[win_play[2]] != 0:
                    if deck[win_play[0]] == PLAYER_ONE:
                        game_end = True
                        window.Element("-WINNER-").Update("Ganador: Player 1")
                        window.Element("-LOSER-").Update("Perdedor: Player 2")
                    else:
                        game_end = True
                        window.Element("-WINNER-").Update("Ganador: Player 2")
                        window.Element("-LOSER-").Update("Perdedor: Player 1")


            if 0 not in deck:
                game_end = True
                window.Element("-WINNER-").Update("Ninguno gano")
                window.Element("-LOSER-").Update("")

            if PLAYER_INICIAL == PLAYER_ONE:
                PLAYER_INICIAL = PLAYER_TWO
            else:
                PLAYER_INICIAL = PLAYER_ONE

def main():
    window = sg.Window('Demo', layout)
    while True:
        event = run_play(window)
        if event == "-OK-" or event == sg.WIN_CLOSED:
            print("Gracias por jugar")
            break
    window.close()



if __name__ == "__main__":
    main()
