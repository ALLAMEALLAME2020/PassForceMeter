# 🚀 PassForceMeter - Password Strength & Brute Force Simulator 🔐

---

### 📜 Overview

**PassForceMeter** is a simple Python script that simulates a brute force attack on a password to demonstrate how many attempts and how much time it might take to "guess" the password.  
This tool is designed purely for educational and awareness purposes, helping users and developers understand the importance of strong, complex passwords.

---

### ⚙️ What Does This Script Do?

- Attempts to guess the input password character by character.
- Uses all printable ASCII characters for guessing.
- Provides live visual feedback in the terminal with colored output using the `colorama` library.
- Tracks and displays the total number of attempts and the elapsed time once the password is matched.
- Includes a configurable delay between attempts to visualize the process clearly.
- Gives a practical demonstration of how brute force attacks operate in a simple, controlled environment.

---

### 🛠️ Features & Capabilities

- **Visual Feedback:** Colored terminal output to show progress and found characters.
- **Configurable Speed:** Adjustable delay between attempts (default 0.1 seconds) for clearer visualization.
- **Cross-platform:** Works on any OS with Python 3.x and `colorama` installed.
- **Lightweight:** Minimal dependencies and straightforward code.
- **Educational:** Perfect for learning about brute force mechanics and password strength awareness.
- **Extensible:** Easy to modify for adding features like custom character sets or parallel attempts.

---

### 💻 Language & Dependencies

- **Language:** Python 3.x  
- **Dependencies:**  
  - [`colorama`](https://pypi.org/project/colorama/) (for colored terminal output)

Install dependencies with:

```bash
pip install colorama
````



### 🚀 How to Use

1. Clone or download this repository.
2. Run the script with Python:

```bash
python main.py
```

3. When prompted, enter the password you want to test:

```
[QS] > Enter a word to search for it! : yourpassword
```

4. Watch the brute force simulation try combinations until it matches the password.
5. The script will display the number of attempts and total time taken.

---

### ⚠️ Important Notes

* This tool is **only for educational and awareness purposes**.
* Do **NOT** use it to attempt unauthorized access or real password cracking.
* The delay slows the simulation for clarity and is not realistic for real attacks.
* Longer or more complex passwords will take exponentially longer to simulate.
* Always use strong, complex passwords to protect your accounts.

---

### 📂 File Structure

* `main.py` — The main Python script running the brute force simulation.

---

### 🤝 Contributing

Feel free to fork this project, improve it, or customize it for your own learning needs. Pull requests and suggestions are welcome!

---

### 📝 License

This project is provided as-is for educational use only.

---

### 👤 Author

ALLAMEALLAME2020 — [GitHub Profile](https://github.com/ALLAMEALLAME2020)

```
```
