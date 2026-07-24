# PY GAME Rock Paper Scissors

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
**Version:** 1.0

**Created Date:** 2026-07-18

**Last Updated:** 2026-07-24

**Compatibility:** Python 3.x

**Created By:** Ali Candan ([@webkolog](https://github.com/webkolog))

**Website:** [http://webkolog.net](http://webkolog.net)

**Copyright:** (c) 2026 Ali Candan

**License:** MIT License ([http://mit-license.org](http://mit-license.org))

---

**PY GAME Rock Paper Scissors** is a lightweight, terminal-based implementation of the classic Rock-Paper-Scissors game written in Python 3. The game features automated computer decision-making using randomized choices, interactive user input handling, and standard game-logic evaluation.

## Features
- **Smart Input Validation:** Checks if the user's input matches the allowed game choices, preventing crashes or unfair advantages from typos.
- **Case-Insensitive Input:** Automatically converts user choices to lowercase and strips unnecessary whitespaces (`.lower().strip()`).
- **Randomized Opponent:** Uses Python's native `random` module to select the computer's move fairly.

## Installation
To run this game locally, ensure you have Python installed on your system. 

1. Clone this repository or download the source file:
   ```bash
   git clone [https://github.com/webkolog/py-game-rock-paper-scissors.git](https://github.com/webkolog/py-game-rock-paper-scissors.git)

```

2. Navigate to the project directory:
```bash
cd py-game-rock-paper-scissors

```



## Usage

Run the script directly from your terminal using Python:

```bash
python py-game-rock-paper-scissors.py

```

### Gameplay Loop

1. The game will prompt you to enter your choice: `rock, paper, or scissor:`.
2. Type your choice and press **Enter**.
3. The application will instantly display the computer's choice and declare the outcome (**User win!**, **Computer win!**, or **Match draw!**).

## Example Gameplay Outputs

### User Wins

```text
rock, paper, or scissor: rock
Computer choose: scissor
User win!

```

### Match Draw

```text
rock, paper, or scissor: paper
Computer choose: paper
Match draw!

```

### Invalid Input Handling

```text
rock, paper, or scissor: lizard
Computer choose: rock
invalid choice! Please choose rock, paper, or scissor.

```

## Dependencies

This project relies entirely on the Python Standard Library. No external packages or third-party frameworks are required.

* `random` (Built-in module)

## License

This project is open-source software licensed under the [MIT license](https://mit-license.org/).

```text
MIT License

Copyright (c) 2026 Ali Candan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

## Contributing

Contributions are welcome! If you find any bugs, have suggestions for new features (like adding a score tracker or best-of-three mode), feel free to open an issue or submit a pull request on the GitHub repository.

## Support

For any questions or support regarding this project, you can refer to the project's GitHub repository or contact the author via [webkolog.net](http://webkolog.net).

