# Ausy POEI : Maze in python

<a href="https://img.shields.io/badge/Python-3.11.2-4483B5" alt="Python">
        <img src="https://img.shields.io/badge/Python-3.11.2-4483B5" /></a>
<a href="https://img.shields.io/badge/pip-23.0.1-FFE05B" alt="NPM">
        <img src="https://img.shields.io/badge/pip-23.0.1-FFE05B" /></a>
<a href="https://img.shields.io/badge/MADE%20WITH-SQLite3-183866" alt="NPM">
        <img src="https://img.shields.io/badge/MADE%20WITH-SQLite3-183866" /></a>

---

This project aims to implement **mazes resolution algorithms** and **maze generator**.

## Mandatories

* Unsolved mazes are in a root directory named **Unsolved**
* Solved mazes are in a root directory named **Solved**
* All sources are in a root directory named **Src**
* Use **Sqlite3**
* A **Game Menu**

#### Mazes

* Walls "#"
* Empty spaces " "
* Path "o"
* One start : (0, 0)
* One end : (row, column)

#### Game Menu

* Option 1 :
  * Display solved mazes datas from the SQL database
  * Format :  `<file_name>; <date>; <time>`
* Option 2 :
  * Load randomly 1 maze form the **Unsolved** directory and solve it with the recursive algorithm
  * Display the maze solution
  * Save the **Date, Time** and **Name** of the maze solved
  * Move the maze into the **Solved** directory
* Option 3 :
  * Generate a maze.txt with **X** and **Y** given randomly and place it into the **Unsolved** directory
  * The new maze is with the format : "maze_" + `<id>` +".txt"
  * The `<id>` is incremented int
* Option 4 :
  * Exit game
  * 'Ctrl+C' is handled

#### Error Management

* Check if **Unsolved** is empty
* Check if a .txt is already in **Solved**
* Directory **__Backup** to have at least 3 solvable mazes
* Invalid option for the **Menu**

## Run project

You need to be on **Windows** for pathfinding and to have an environment who can **compile Pyhton files**.

**Terminal :**

```
python3 __start__.py
```

**IDE :**

> run into your IDE the file \_\_start\_\_.py

## Authors

* **Simon Tessier**
* **Yoann Le Saint**
