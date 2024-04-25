"""Train AI using modified Monte Carlo simulation

Make all strategies (permutations) play 50 games, cut off 90% of worst.
Then remaining strategies play 50 * 2^i games, cut of 90% of worst for each iteration i

Save about 5 best strategies for first and second player, and AI agnet will play random of them"""

import tic_tac_toe

import json
from random import choice
from itertools import permutations
from collections import defaultdict


class MonteCarloSimulation:
    def __init__(self):
        self.simulator = tic_tac_toe.Game()

    def monte_carlo(self, first_player, games, strategies, iter=1):
        balance = defaultdict(int)

        for strategy in strategies:
            for __ in range(games):
                result = self.simulator.play_against_random(strategy, first_player)

                if first_player:
                    balance[strategy] += result
                else:
                    balance[strategy] -= result

        best_perms = sorted(balance, key=balance.get, reverse=True)

        print(f"Finished {iter}th depth")
        if len(best_perms) <= 50:
            print(f"Most points in {games} games: {balance[best_perms[0]]}")
            return best_perms[:5]

        next_games = games * self.simulations_multiplier
        next_population = best_perms[: len(strategies) // self.cut_off_multiplier]
        return self.monte_carlo(first_player, next_games, next_population, iter + 1)

    def train(self, start_simulations, simulations_multiplier, cut_off_multiplier):
        self.simulations_multiplier = simulations_multiplier
        self.cut_off_multiplier = cut_off_multiplier

        all_strategies = list(permutations(range(9)))

        # best strategies for first player
        first = self.monte_carlo(True, start_simulations, all_strategies)

        # best strategies for second player
        second = self.monte_carlo(False, start_simulations, all_strategies)

        data = {"best_first_player": first, "best_second_player": second}

        with open("bots/mcs.json", "w") as file:
            json.dump(data, file)


class AI_Agent:
    def __init__(self, first_player_strategies, second_player_strategies):
        self.first_player_strategies = first_player_strategies
        self.second_player_strategies = second_player_strategies

    def first(self):
        return choice(self.first_player_strategies)

    def second(self):
        return choice(self.second_player_strategies)


class MCS_Agent(AI_Agent):
    def __init__(self):
        with open("bots/mcs.json", "r") as file:
            data = json.load(file)
            self.first_player_strategies = data["best_first_player"]
            self.second_player_strategies = data["best_second_player"]

    def retrain(self, start_simulations, simulations_multiplier, cut_off_multiplier):
        mcs = MonteCarloSimulation()
        mcs.train(start_simulations, simulations_multiplier, cut_off_multiplier)
