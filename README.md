### Gomoku AI Agent README

#### Overview
This project implements an AI agent capable of playing Gomoku (Five-in-a-Row), a strategy board game played on a 15x15 grid. The agent uses an alpha-beta pruning algorithm to determine the optimal move based on the current game state. This README provides a brief overview of the project structure, including how to run the game, the components of the AI agent, and how to interact with the game.

#### Getting Started
To play against the Gomoku AI agent, simply run the main script provided in this project. The game is played in the console, where the 15x15 board will be displayed along with prompts for the user's moves.

#### Game Rules
- Players alternate turns placing a stone of their color (white or black) on an empty intersection on the board.
- Black plays first, with the first stone placed in the center of the board.
- The second player's first stone may be placed anywhere.
- The first player's second stone must be placed at least three intersections away from the first stone.
- The winner is the first to form an unbroken line of five stones horizontally, vertically, or diagonally.
- The game ends in a draw if the board is filled without any player forming a line of 5 stones.

#### Components
- **Alpha-Beta Agent**: Utilizes the alpha-beta pruning algorithm to efficiently determine optimal moves by evaluating the game state up to a certain depth.
- **Evaluation Functions**: Two or more evaluation functions are implemented to assess the game state's favorability towards a specific player. These functions consider factors like potential unbroken lines of stones and blocking opponent moves.
- **Move Generator**: Generates a list of legal moves from the current state, ensuring that moves adhere to Gomoku's rules.
- **Game State Management**: Manages the board's state, including stone placement and checking for game-ending conditions.

#### Usage
1. **Start the Game**: Run the main function/script to start the game. The initial board will be displayed in the console.
2. **User Input**: Enter your move as two integers representing the row and column coordinates (e.g., `7 7`), following the prompts in the console.
3. **AI Move**: After each user move, the AI agent will calculate and display its move, updating the board accordingly.
4. **End of Game**: The game ends when either player wins by connecting five stones in a row or the board is completely filled, resulting in a draw.

#### Comparison and Analysis
- **Search Depth Impact**: The documentation includes a section discussing the impact of varying the search depth on the AI's performance, including its decision-making speed and move quality.
- **Evaluation Function Quality**: Compares the performance of different evaluation functions in terms of move selection and overall strategy, providing insight into how nuanced evaluations can enhance the AI's gameplay.

#### Sources
- Alpha-beta pruning algorithm and initial game logic adapted from [AIMA Code](https://github.com/aimacode).

#### Conclusion
This Gomoku AI agent demonstrates the application of alpha-beta pruning to a classic board game, showcasing how different evaluation functions and search depths can affect gameplay strategy. Feel free to experiment with the code to explore the nuances of AI-based game strategy further.