chess_players = {
    "Carlsen, Magnus": 1865,
    "Firouzja, Alireza": 2804,
    "Ding, Liren": 2799,
    "Caruana, Fabiano": 1792,
    "Nepomniachtchi, Ian": 2773
}
new_chess_players = {value: key for key, value in chess_players.items()}
new_chess_players_02 = {value: key.split(",") for value, key in new_chess_players.items()if value > 2000}
new_chess_players_03 = {value: key[0] + " " + key[1][1] + "." for value, key in new_chess_players_02.items()}
print(new_chess_players_03)
# for value, key in new_chess_players_03.items():
#     print(value, ":", key, sep=" ")
