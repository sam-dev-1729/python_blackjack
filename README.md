# Blackjack in Python

This is a simple implementation of the casino game Blackjack (also known as 21) using Python.

## Rules

The rules of Blackjack are as follows:

- The goal of the game is to draw cards that total as close to 21 points as possible without going over. 
- Numbered cards are worth their numerical value. Face cards (Jack, Queen, King) are worth 10 points. Aces can be worth 1 or 11 points.
- The player draws cards first, and can choose to "hit" (take another card) or "stand" (stop drawing cards) at any time.
- The dealer draws cards after the player acts. The dealer must hit if they have 16 points or less, and must stand with 17 points or more.
- If either the player or dealer exceeds 21 points, they bust and lose the game. 
- If both player and dealer do not bust, whoever has the higher point total wins.
- If both player and dealer have the same total, it is a push (tie), and neither wins.

## Code Overview

The code is split into several classes:

- `Card`: Represents a single playing card with a suit and rank.
- `Deck`: Represents a deck of 52 Card objects that can be shuffled and dealt.
- `Hand`: Represents a hand of Cards that have been dealt. Calculates point total and handles aces.
- `Chips`: Represents the player's starting chips and bets.
- `Functions`: Game logic like taking bets, hitting, etc.

The game loop:

1. Create deck, shuffle, deal initial hands.
2. Take player bet.
3. Player turns: hit or stand.
4. After player turn, dealer hits or stands based on rules.
5. Compare hands, determine winner.
6. Adjust player chips.
7. Play again or exit.

This allows a single user to play Blackjack against a dealer controlled by the code. Additional features like splitting or insurance could be added. Enjoy!