# 2025-ITELEC2-LAB014
Week 04 - Looping Statements

Laboratory # 14 - Guided Coding Exercise: Nested for Loop to Print a Multiplication Table

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 14 - Guided Coding Exercise: Nested for Loop to Print a Multiplication Table**

   **Objective:**
   - Understand the concept of nested loops (a loop within a loop).
   - Learn how to generate a multiplication table using nested for loops.
   - Recognize the advantage of looping to automate repetitive tasks.
   - Practice formatted output using f-strings.

   **Desired Output (Example 1):**
   ```bash
      1   2   3   4   5
      2   4   6   8  10
      3   6   9  12  15
      4   8  12  16  20
      5  10  15  20  25
   ```
      
   **Notable Observations (to be discussed after completing the exercise):**
   - The inner loop (j) completes all its iterations for each iteration of the outer loop (i). This is how the multiplication table is generated row by row.
   - The formatting {product:4} ensures consistent spacing, making the table more readable.
   - The end="" argument in the print() function is crucial for printing the numbers in the same row.

   **Python Best Practices**
   - Formatted Output: Use f-strings and format specifiers to control the appearance of your output, making it more readable and professional.
   - Loop Logic: Keep the logic within each loop as simple and focused as possible. Clearly separate the concerns of the outer and inner loops.
   - Comments: Add comments to explain the purpose of the loops and any non-obvious code.
   - Indentation: Consistent and correct indentation is absolutely essential for nested loops. It defines the structure of the code and determines which code belongs to which loop.
   Test Thoroughly: Test your code to make sure it produces the correct output.

   **Step-by-Step Instructions:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `nested_for_loop_multiplication_table.py`
      
   2. Outer loop for rows (1 to 5):
      - Use a for loop with the range() function to iterate from 1 to 5 (inclusive). Use a variable named i to represent the current row number.
```python
for i in range(1, 6):
```
      
   3.  Inner loop for columns (1 to 5):
      - Inside the outer loop, use another for loop (nested loop) with the range() function to iterate from 1 to 5 (inclusive). Use a variable named j to represent the current column number.
```python
    for j in range(1, 6):  # Indent this loop!
```

   4. Calculate the product:
      - Inside the inner loop, calculate the product of i and j and store it in a variable named product.
```python
        product = i * j  # Indent this line!
```

   5. Print the product with formatting:
      - Inside the inner loop, use the print() function with an f-string to display the product.
      - Use the format specifier {product:4} within the f-string to format the number in a field of width 4. This will create consistent spacing in the table.
      - Use the end="" argument in the print() function to prevent a newline character from being printed after each number. This allows you to print the numbers in the same row.
```python
        print(f"{product:4}", end="")  # Indent this line!
```

   6. New line after each row:
      - After the inner loop (but still inside the outer loop), use the print() function without any arguments. This will print a newline character, moving the cursor to the next line to start the next row of the table.
```python
    print() # Indent this line!
```

   7. Complete Code: Combine the steps above to form the complete program.
   8. Run the code: Execute your Python code.
   9. Observe the output: Test the program with different days of the week (including variations in capitalization and spacing) and invalid day names.

   **Conclusion**
   This exercise demonstrated how to use nested for loops to create structured and repetitive output, specifically a multiplication table.  You learned how the inner loop completes all its iterations for each iteration of the outer loop.  You also practiced using f-strings for formatted output.  Nested loops are a powerful tool for handling multi-dimensional tasks and are essential for many programming applications.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 04 - Laboratory # 14"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
