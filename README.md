# Coffee Machine Simulation

This is a simple Python-based Coffee Machine program that simulates the process of buying coffee from a machine. It allows users to choose between espresso, latte, and cappuccino, insert virtual coins, and check machine resources like water, milk, and coffee.

---

## Features

- Choose from three coffee options:
  - Espresso
  - Latte
  - Cappuccino
- Coin-based payment system (quarters, dimes, nickels, pennies)
- Resource management:
  - Tracks remaining water, milk, and coffee
- Report feature to view current resources and earnings
- Change calculation if user pays more than the coffee cost
- Option to turn off the machine

---

## How It Works

1. Run the program:
   ```bash
   python main.py
   ```
2. The machine will ask:
   ```
   What would you like? (espresso/latte/cappuccino):
   ```
3. Type one of the options:
   - espresso
   - latte
   - cappuccino
   - report → to see the remaining ingredients and total money collected
   - off → to stop the program

4. When prompted, insert coins by entering the number of each type.

5. If you have enough money and resources, your coffee will be served:
   ```
   Here is your cappuccino. Enjoy!
   ```

---

## Program Structure

- **MENU** – Contains coffee options, ingredient requirements, and cost  
- **resources** – Tracks available ingredients  
- **Functions:**
  - `espresso()`, `latte()`, `cappuccino()` → prepare each drink  
  - `report()` → display remaining resources and money  
  - `game()` → main loop that manages user interaction  

---

## Example Run

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.5 in change.

Here is your latte. Enjoy!
```

---

## Requirements

- Python 3.6 or later
- No external libraries required

---

## Author

Teshavi Poddar  
A simple Python project for learning loops, conditionals, and functions.
