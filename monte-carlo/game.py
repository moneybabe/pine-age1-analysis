import numpy as np

def sim_game():
    player_bets = np.zeros(12)
    other_bets = np.zeros(12)
    POT = 250000
    player_profit = 0
    for i in range(12):
        other_bet = np.random.uniform(low=1, high=POT)
        player_bet = POT - other_bet
        player_bets[i], other_bets[i] = player_bet, other_bet
        total_player_bets = player_bets.sum()
        total_other_bets = other_bets.sum()
        player_profit += total_player_bets * (POT / (total_player_bets + total_other_bets) - 1)
    return player_bets, other_bets, player_profit
