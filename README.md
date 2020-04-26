# Puzzle Search

Very basic example to implement search algorithms.

Game: [15 puzzle](https://en.wikipedia.org/wiki/15_puzzle) or 8-puzzle depending on board size
Implemented search algorithms:

- graph search

## Setup

Run `python3 setup.py install`

## Run Game

Run `play-puzzle`.

Parameters:

- `--player`:
  - `user` to play in the console manually
  - `agent` to let the agent using the search algorithm play
- `--puzzle-size`
  - size (one dimension) of the board: e.g. `3` for 8-puzzle (3x3 board)

## Run Tests

- run install tox (`pip install tox`) and run `tox`
