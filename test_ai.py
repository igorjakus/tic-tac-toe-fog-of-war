import tic_tac_toe
import train_ai


def test_ai_agent(ai_agent, games):
    """ Play games against random oponent """
    tictactoe = tic_tac_toe.Game()
    wins = 0
    draws = 0
    for __ in range(games // 2):
        result = tictactoe.play_against_random(ai_agent.first(), player_first=True)
        wins += result == 1
        draws += result == 0

    for __ in range(games // 2):
        result = tictactoe.play_against_random(ai_agent.second(), player_first=False)
        wins += result == -1
        draws += result == 0

    print("Win-ratio", wins / games)
    print("Draw-ratio", draws / games)
    print("Lose-ratio", (games - wins - draws) / games)


# Win-ratio 0.81196
# Draw-ratio 0.05562
# Lose-ratio 0.13242
test_ai_agent(train_ai.MCS_Agent(), 100_000)
