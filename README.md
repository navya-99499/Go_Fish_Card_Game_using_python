# 🃏 Go Fish Card Game using Python

## 📌 Overview
This project is a command-line implementation of the classic **Go Fish** card game using Python.

The game simulates deck creation, card dealing, player turns, rank requests, book collection, and winner determination. It is designed to demonstrate object-oriented programming, data structures, and game logic in Python.

---

## 🎮 Features
- Supports multiple players
- Shuffled card deck implementation
- Rank-based card requests
- “Go Fish” logic
- Automatic book detection (4 cards of the same rank)
- Winner calculation based on completed books

---

## 🛠️ Concepts Used
- Python classes and objects
- Stack-like deck implementation
- Queue/deque for player hands
- Loops and conditional game logic
- Input handling and validation

---

## ⚙️ Tech Stack
- Python
- `random`
- `collections.deque`

## 📂 Project Structure

```text
Go_Fish_Card_Game_using_python/
│
├── src/
│   └── Go_Fish_Card_Game.py
│
├── README.md
├── requirements.txt
├── .gitignore
```

---

## ▶️ How to Run
1. Make sure Python is installed.
2. Open a terminal in the project folder.
3. Run:

```bash
python src/Go_Fish_Card_Game.py
```

4. Enter:
   - number of players
   - number of cards per player

---

## 🧠 Game Logic
- A shuffled deck is created with ranks **2–10, J, Q, K, A**, with four of each rank. :contentReference[oaicite:1]{index=1}
- Each player is dealt starting cards. :contentReference[oaicite:2]{index=2}
- On each turn, a player asks another player for a rank they already have in hand. :contentReference[oaicite:3]{index=3}
- If the opponent has matching cards, they are transferred.
- Otherwise, the player must **Go Fish** and draw from the deck. :contentReference[oaicite:4]{index=4}
- Whenever a player collects 4 cards of the same rank, a **book** is formed automatically. :contentReference[oaicite:5]{index=5}
- When the game ends, the player with the most books wins. :contentReference[oaicite:6]{index=6}

---

## 🚀 Future Improvements
- Add support for human vs computer gameplay
- Add card suits for richer display
- Add score tracking across multiple rounds

---

## ⭐ Conclusion
This project demonstrates how Python can be used to build an interactive card game while applying object-oriented design, data structures, and core game development logic.