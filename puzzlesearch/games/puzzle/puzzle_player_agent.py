from puzzlesearch.games.player_agent import PlayerAgent
from puzzlesearch.games.puzzle.puzzle_problem import PuzzleProblem
from puzzlesearch.search.graph_search import GraphSearch


class PuzzlePlayerAgent(PlayerAgent):
    def plan_actions(self, board):
        problem = PuzzleProblem(board)
        return GraphSearch().search(problem)
