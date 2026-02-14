from fpdf import FPDF

class ProjectPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "SchoolComputerSciencePrep - Full Project Documentation", align="C")
        self.ln(5)
        self.set_draw_color(0, 102, 204)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def section_title(self, title):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(0, 51, 102)
        self.cell(0, 12, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 102, 204)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def sub_title(self, title):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(0, 80, 140)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def sub_sub_title(self, title):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def code_block(self, code):
        self.set_font("Courier", "", 8.5)
        self.set_fill_color(240, 240, 240)
        self.set_text_color(30, 30, 30)
        x = self.get_x()
        w = self.w - self.l_margin - self.r_margin
        # Draw background
        lines = code.split("\n")
        line_h = 4.5
        total_h = len(lines) * line_h + 4
        if self.get_y() + total_h > self.h - 25:
            self.add_page()
        y_start = self.get_y()
        self.rect(x, y_start, w, total_h, "F")
        self.set_xy(x + 2, y_start + 2)
        for line in lines:
            self.cell(0, line_h, line, new_x="LMARGIN", new_y="NEXT")
            self.set_x(x + 2)
        self.ln(4)

    def bullet(self, text, indent=0):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        x = self.get_x() + indent
        self.set_x(x)
        bullet_char = "-"
        self.cell(5, 5.5, bullet_char)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def table_row(self, cols, widths, bold=False, fill=False):
        style = "B" if bold else ""
        self.set_font("Helvetica", style, 9)
        if fill:
            self.set_fill_color(220, 230, 241)
        h = 7
        x_start = self.get_x()
        max_y = self.get_y()
        for i, (col, w) in enumerate(zip(cols, widths)):
            x = x_start + sum(widths[:i])
            self.set_xy(x, max_y)
            self.cell(w, h, str(col), border=1, fill=fill)
        self.ln(h)


pdf = ProjectPDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()

# ========== COVER PAGE ==========
pdf.ln(30)
pdf.set_font("Helvetica", "B", 28)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 15, "SchoolComputerSciencePrep", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)
pdf.set_font("Helvetica", "", 16)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 10, "Complete Project Documentation", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)
pdf.set_font("Helvetica", "I", 12)
pdf.cell(0, 8, "Cambridge A-Level Computer Science (9618)", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 8, "Paper 42 - May/June 2025", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(15)
pdf.set_draw_color(0, 102, 204)
pdf.set_line_width(1)
pdf.line(60, pdf.get_y(), 150, pdf.get_y())
pdf.ln(15)
pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(60, 60, 60)
pdf.cell(0, 7, "Prepared: February 2026", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 7, "Language: Python 3", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 7, "External Dependencies: None (Pure Python)", align="C", new_x="LMARGIN", new_y="NEXT")

# ========== TABLE OF CONTENTS ==========
pdf.add_page()
pdf.section_title("Table of Contents")
toc = [
    ("1.", "Project Overview"),
    ("2.", "Directory Structure & File Inventory"),
    ("3.", "Question 1: Stack-Based Postfix Calculator"),
    ("  3.1", "Global Variables & Memory Layout"),
    ("  3.2", "Push() Function"),
    ("  3.3", "Pop() Function"),
    ("  3.4", "ReadData() Function"),
    ("  3.5", "Calculate() Function"),
    ("  3.6", "Main Execution Flow"),
    ("  3.7", "Test Data Files"),
    ("4.", "Question 2: Hash Table with Collision Handling"),
    ("  4.1", "Record Class"),
    ("  4.2", "Global Variables & Memory Layout"),
    ("  4.3", "initialize() Function"),
    ("  4.4", "CalculateHash() Function"),
    ("  4.5", "InsertIntoHash() Function"),
    ("  4.6", "CreateHashTable() Function"),
    ("  4.7", "PrintSpare() Function"),
    ("  4.8", "Main Execution Flow"),
    ("5.", "Hardcoded Values & Constants"),
    ("6.", "Memory Management In Detail"),
    ("7.", "Data Files & Formats"),
    ("8.", "Network / IP Addresses"),
    ("9.", "Dependencies & Imports"),
    ("10.", "Error Handling"),
    ("11.", "Git History & Version Control"),
    ("12.", "Potential Improvements & Notes"),
]
for num, title in toc:
    pdf.set_font("Helvetica", "B" if not num.startswith(" ") else "", 10)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(15, 6, num)
    pdf.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")

# ========== 1. PROJECT OVERVIEW ==========
pdf.add_page()
pdf.section_title("1. Project Overview")
pdf.body_text(
    "This project contains solutions to the Cambridge International A-Level Computer Science "
    "examination paper 9618/42 (May/June 2025 session). The paper tests practical programming "
    "skills in data structures and algorithms. The project implements two main solutions:"
)
pdf.bullet("Question 1: A stack-based postfix (Reverse Polish Notation) expression calculator")
pdf.bullet("Question 2: A hash table implementation with collision handling via a spare overflow array")
pdf.ln(3)
pdf.body_text(
    "The entire project is written in pure Python 3 with zero external dependencies. All data is "
    "loaded from local text files and processed in memory. There are no network connections, no "
    "database usage, and no third-party libraries. The project uses fundamental data structures "
    "(stacks, hash tables, arrays) implemented from scratch rather than using Python's built-in "
    "collections, as required by the examination."
)

# ========== 2. DIRECTORY STRUCTURE ==========
pdf.add_page()
pdf.section_title("2. Directory Structure & File Inventory")
pdf.code_block(
    "SchoolComputerSciencePrep/\n"
    "|-- .git/                        # Git version control\n"
    "|-- .idea/                       # PyCharm IDE config\n"
    "|-- May_June_25_42/              # Main project folder\n"
    "|   |-- 9618_s25_qp_42.pdf      # Exam question paper (2.4 MB)\n"
    "|   |-- Response.py              # All solutions (2,938 bytes)\n"
    "|   |-- HashData.txt             # Hash table test data (199 records)\n"
    "|   |-- StackData.txt            # Stack test data #1 (9 values)\n"
    "|   |-- SecondStack.txt          # Stack test data #2 (9 values)\n"
    "|-- README.md                    # Project readme\n"
    "|-- generate_documentation.py    # This doc generator"
)
pdf.ln(3)
pdf.sub_title("File Details")

widths = [55, 25, 105]
pdf.table_row(["File Name", "Size", "Purpose"], widths, bold=True, fill=True)
pdf.table_row(["Response.py", "2,938 B", "Main Python source with both Q1 and Q2"], widths)
pdf.table_row(["HashData.txt", "2,326 B", "199 CSV records for hash table testing"], widths)
pdf.table_row(["StackData.txt", "26 B", "9 values for postfix calculation test #1"], widths)
pdf.table_row(["SecondStack.txt", "26 B", "9 values for postfix calculation test #2"], widths)
pdf.table_row(["9618_s25_qp_42.pdf", "~2.4 MB", "Original exam question paper"], widths)
pdf.table_row(["README.md", "~30 B", "Basic project title only"], widths)

# ========== 3. QUESTION 1 ==========
pdf.add_page()
pdf.section_title("3. Question 1: Stack-Based Postfix Calculator")
pdf.body_text(
    "This solution implements a stack data structure and uses it to evaluate postfix (Reverse "
    "Polish Notation) arithmetic expressions. In postfix notation, operators follow their operands "
    "(e.g., '3 4 +' means 3 + 4). The stack is used to store operands and intermediate results."
)
pdf.body_text(
    "The entire Question 1 code is currently COMMENTED OUT in Response.py (wrapped in a triple-quoted "
    "string from line 2 to line 66). This is because Question 2 is the currently active code. To run "
    "Question 1, you would need to uncomment it and comment out Question 2."
)

# 3.1
pdf.sub_title("3.1 Global Variables & Memory Layout")
pdf.body_text("Question 1 uses two global variables to manage the stack state:")
pdf.code_block(
    "TopOfStack = -1           # Stack pointer (index of top element)\n"
    "Stack = [\"-1\"] * 20       # Fixed-size array of 20 string slots"
)
pdf.body_text(
    "TopOfStack: An integer that tracks the index of the current top element. When the stack is "
    "empty, it is -1. When full, it is 19 (since indices go from 0 to 19). This acts as both a "
    "counter and an index pointer."
)
pdf.body_text(
    "Stack: A Python list pre-initialized with 20 copies of the string \"-1\". The string \"-1\" "
    "serves as a sentinel/null value indicating an empty slot. All elements are stored as strings, "
    "including numbers, which are later converted to floats during calculation."
)

# Memory diagram
pdf.sub_sub_title("Memory Diagram (Empty Stack)")
pdf.code_block(
    "Index:  [0]   [1]   [2]   ...  [18]  [19]\n"
    "Value: \"-1\" \"-1\" \"-1\"  ...  \"-1\"  \"-1\"\n"
    "                                          ^\n"
    "TopOfStack = -1 (empty, points below index 0)"
)
pdf.sub_sub_title("Memory Diagram (After loading StackData.txt)")
pdf.code_block(
    "Index:  [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]  [8]\n"
    "Value: \"3\"  \"+\"  \"2\"  \"*\"  \"2\"  \"^\"  \"2\"  \"-\" \"10\"\n"
    "                                                  ^\n"
    "TopOfStack = 8 (points to \"10\" at top)"
)

# 3.2
pdf.add_page()
pdf.sub_title("3.2 Push(item: str) -> int")
pdf.body_text("Adds an item to the top of the stack. Returns 1 on success, -1 if stack is full.")
pdf.code_block(
    "def Push(item: str):\n"
    "    global TopOfStack, Stack\n"
    "    if TopOfStack == 19:        # Stack full check\n"
    "        return -1\n"
    "    else:\n"
    "        TopOfStack += 1         # Move pointer up\n"
    "        Stack[TopOfStack] = item  # Place item\n"
    "        return 1                # Success"
)
pdf.body_text("How it works step-by-step:")
pdf.bullet("1. Checks if TopOfStack equals 19 (max index). If yes, stack is full -> returns -1.")
pdf.bullet("2. If not full, increments TopOfStack by 1.")
pdf.bullet("3. Stores the item at the new TopOfStack position in the Stack array.")
pdf.bullet("4. Returns 1 to indicate success.")
pdf.ln(2)
pdf.body_text(
    "Time Complexity: O(1) - constant time. Space Complexity: O(1) - no extra memory allocated. "
    "The stack has a fixed capacity of 20 elements. Attempting to push when full returns -1 "
    "rather than raising an exception."
)

# 3.3
pdf.sub_title("3.3 Pop() -> str")
pdf.body_text("Removes and returns the top item from the stack. Returns \"-1\" if the stack is empty.")
pdf.code_block(
    "def Pop():\n"
    "    global TopOfStack, Stack\n"
    "    if TopOfStack == -1:        # Stack empty check\n"
    "        return \"-1\"\n"
    "    else:\n"
    "        item = Stack[TopOfStack]  # Get top item\n"
    "        TopOfStack -= 1          # Move pointer down\n"
    "        return item              # Return the item"
)
pdf.body_text("How it works step-by-step:")
pdf.bullet("1. Checks if TopOfStack equals -1 (empty). If yes, returns the string \"-1\".")
pdf.bullet("2. If not empty, saves the item at Stack[TopOfStack] into a local variable.")
pdf.bullet("3. Decrements TopOfStack by 1 (logically removing the top element).")
pdf.bullet("4. Returns the saved item.")
pdf.ln(2)
pdf.body_text(
    "Important Note: The old value is NOT actually erased from the array; it remains in memory "
    "but is logically inaccessible because TopOfStack has moved below it. This is standard for "
    "array-based stack implementations. Time Complexity: O(1)."
)

# 3.4
pdf.add_page()
pdf.sub_title("3.4 ReadData(filename: str)")
pdf.body_text(
    "Reads data from a text file line by line and pushes each line (stripped of whitespace) onto "
    "the stack. This function bridges file I/O with the stack data structure."
)
pdf.code_block(
    "def ReadData(filename):\n"
    "    global TopOfStack, Stack\n"
    "    try:\n"
    "        with open(filename, \"r\") as file:\n"
    "            for line in file:\n"
    "                pushStatus = Push(line.strip())\n"
    "                if pushStatus == -1:\n"
    "                    print(\"Stack full\")\n"
    "    except Exception as e:\n"
    "        print(f\"Error reading the file: {e}\")"
)
pdf.body_text("How it works step-by-step:")
pdf.bullet("1. Opens the specified file in read mode using a context manager (with statement).")
pdf.bullet("2. Iterates over each line in the file.")
pdf.bullet("3. Strips leading/trailing whitespace (including newline characters) from each line.")
pdf.bullet("4. Calls Push() to add the cleaned line to the stack.")
pdf.bullet("5. If Push() returns -1 (stack full), prints \"Stack full\" warning.")
pdf.bullet("6. If any file I/O error occurs, catches it and prints the error message.")
pdf.ln(2)
pdf.body_text(
    "The filename is provided by user input at runtime. The function uses Python's exception "
    "handling (try/except) to gracefully handle cases where the file doesn't exist or can't be "
    "read. Data is read in file order: first line goes to Stack[0], last line goes to Stack[n-1]."
)

# 3.5
pdf.sub_title("3.5 Calculate() -> float")
pdf.body_text(
    "Evaluates the postfix expression stored on the stack. Pops values from the top of the stack "
    "and applies operators to compute the final result."
)
pdf.code_block(
    "def Calculate():\n"
    "    global TopOfStack, Stack\n"
    "    total = Pop()              # Pop first operand (top of stack)\n"
    "    total = float(total)       # Convert string to float\n"
    "\n"
    "    while TopOfStack != -1:    # Loop until stack is empty\n"
    "        op = Pop()             # Pop operator\n"
    "        num = float(Pop())     # Pop next operand\n"
    "\n"
    "        if op == \"+\":   total = total + num\n"
    "        elif op == \"-\": total = total - num\n"
    "        elif op == \"*\": total = total * num\n"
    "        elif op == \"/\": total = total / num\n"
    "        elif op == \"^\": total = total ** num  # Power\n"
    "\n"
    "    return total"
)
pdf.body_text("How it works step-by-step:")
pdf.bullet("1. Pops the top element (last line of file / rightmost value) as the initial total.")
pdf.bullet("2. Converts it from string to float.")
pdf.bullet("3. Enters a while loop that continues until the stack is empty (TopOfStack == -1).")
pdf.bullet("4. In each iteration: pops an operator, then pops an operand.")
pdf.bullet("5. Applies the operator: + (add), - (subtract), * (multiply), / (divide), ^ (power).")
pdf.bullet("6. Updates total with the result.")
pdf.bullet("7. Returns the final computed float value.")

pdf.add_page()
pdf.sub_sub_title("Supported Operators")
widths2 = [30, 40, 50, 70]
pdf.table_row(["Symbol", "Operation", "Python Op", "Example"], widths2, bold=True, fill=True)
pdf.table_row(["+", "Addition", "total + num", "3 + 2 = 5"], widths2)
pdf.table_row(["-", "Subtraction", "total - num", "10 - 3 = 7"], widths2)
pdf.table_row(["*", "Multiplication", "total * num", "4 * 5 = 20"], widths2)
pdf.table_row(["/", "Division", "total / num", "10 / 2 = 5.0"], widths2)
pdf.table_row(["^", "Power", "total ** num", "2 ^ 3 = 8"], widths2)

pdf.ln(3)
pdf.sub_sub_title("Walkthrough: StackData.txt Evaluation")
pdf.body_text("File contents (read bottom to top since stack is LIFO):")
pdf.code_block(
    "Stack after ReadData:  [3, +, 2, *, 2, ^, 2, -, 10]\n"
    "                       [0] [1] [2] [3] [4] [5] [6] [7] [8]\n"
    "TopOfStack = 8\n"
    "\n"
    "Step 1: Pop -> total = 10.0\n"
    "Step 2: Pop op=\"-\", Pop num=2.0  -> total = 10.0 - 2.0 = 8.0\n"
    "Step 3: Pop op=\"^\", Pop num=2.0  -> total = 8.0 ^ 2.0 = 64.0\n"
    "Step 4: Pop op=\"*\", Pop num=2.0  -> total = 64.0 * 2.0 = 128.0\n"
    "Step 5: Pop op=\"+\", Pop num=3.0  -> total = 128.0 + 3.0 = 131.0\n"
    "\n"
    "Final Result: 131.0"
)

# 3.6
pdf.sub_title("3.6 Main Execution Flow (Question 1)")
pdf.code_block(
    "filename = input(\"Enter the file name: \")  # User provides filename\n"
    "ReadData(filename)                           # Load file into stack\n"
    "calculatedNum = Calculate()                  # Evaluate expression\n"
    "print(calculatedNum)                         # Output result"
)
pdf.body_text(
    "The user is prompted to enter a filename at runtime. This is the ONLY user interaction. "
    "The file is read, its contents pushed to the stack, the postfix expression is evaluated, "
    "and the result is printed to the console."
)

# 3.7
pdf.sub_title("3.7 Test Data Files")
pdf.sub_sub_title("StackData.txt")
pdf.code_block("3\n+\n2\n*\n2\n^\n2\n-\n10")
pdf.body_text("Contains 9 values (5 operands + 4 operators). Evaluates to 131.0.")

pdf.sub_sub_title("SecondStack.txt")
pdf.code_block("20\n*\n4\n^\n3\n/\n5\n+\n1")
pdf.body_text("Contains 9 values (5 operands + 4 operators). An alternative test case.")

# ========== 4. QUESTION 2 ==========
pdf.add_page()
pdf.section_title("4. Question 2: Hash Table with Collision Handling")
pdf.body_text(
    "This solution implements a hash table data structure that maps integer keys to records "
    "containing two integer data fields. It handles hash collisions using an overflow strategy: "
    "when a collision occurs (two keys hash to the same index), the new record is stored in a "
    "separate 'Spare' array instead of the main hash table."
)
pdf.body_text(
    "Unlike Question 1, the Question 2 code is also wrapped in a triple-quoted string (lines 69-123 "
    "of Response.py) but uses a slightly malformed triple-quote ('''' instead of ''') on line 69. "
    "Despite this, the code structure is complete and functional when properly uncommented."
)

# 4.1
pdf.sub_title("4.1 Record Class")
pdf.code_block(
    "class Record:\n"
    "    def __init__(self, key: int, Item1: int, Item2: int):\n"
    "        self.key = key       # Unique identifier\n"
    "        self.Item1 = Item1   # First data field\n"
    "        self.Item2 = Item2   # Second data field"
)
pdf.body_text(
    "The Record class is a simple data container (similar to a struct in C). It holds three integer "
    "fields. Each record in the hash table and spare array is a Record object. A Record with "
    "key = -1 indicates an empty/unused slot (sentinel value)."
)
pdf.body_text(
    "This class has NO methods other than __init__. It is purely a data holder. There is no "
    "__str__, __repr__, or comparison methods defined."
)

# 4.2
pdf.sub_title("4.2 Global Variables & Memory Layout")
pdf.code_block(
    "HashTable = [None] * 200    # Primary hash table: 200 slots\n"
    "Spare = [None] * 100        # Overflow array: 100 slots\n"
    "FreeSpace = 0               # Next available index in Spare"
)
pdf.body_text(
    "HashTable: The primary storage array with 200 slots. Each slot holds either None (before "
    "initialization) or a Record object (after initialization). The hash function maps keys to "
    "indices 0-199."
)
pdf.body_text(
    "Spare: An overflow array with 100 slots for handling collisions. When a key hashes to an "
    "already-occupied slot in HashTable, the record is placed in Spare instead. This is a simple "
    "but effective collision resolution strategy."
)
pdf.body_text(
    "FreeSpace: An integer pointer that tracks the next available slot in the Spare array. Starts "
    "at 0 and increments by 1 each time a collision record is added. Maximum value before overflow "
    "would be 99 (100 slots, indices 0-99)."
)

pdf.add_page()
pdf.sub_sub_title("Memory Layout Diagram")
pdf.code_block(
    "HashTable (200 slots):\n"
    "+------+------+------+------+-----+--------+--------+\n"
    "| [0]  | [1]  | [2]  | [3]  | ... | [198]  | [199]  |\n"
    "| R(-1)| R(-1)| R(2) | R(-1)| ... | R(-1)  | R(799) |\n"
    "+------+------+------+------+-----+--------+--------+\n"
    "  empty  empty  key=2  empty        empty    key=799\n"
    "\n"
    "Spare (100 slots):\n"
    "+------+------+------+------+-----+--------+--------+\n"
    "| [0]  | [1]  | [2]  | [3]  | ... | [98]   | [99]   |\n"
    "| R(31)| R(88)| ...  | ...  | ... | R(-1)  | R(-1)  |\n"
    "+------+------+------+------+-----+--------+--------+\n"
    "  coll   coll                        empty    empty\n"
    "              ^\n"
    "         FreeSpace (next available)"
)

# 4.3
pdf.sub_title("4.3 initialize() Function")
pdf.code_block(
    "def initialize():\n"
    "    global HashTable, Spare, FreeSpace\n"
    "    for i in range(200):\n"
    "        HashTable[i] = Record(-1, -1, -1)  # Empty record\n"
    "    for d in range(100):\n"
    "        Spare[d] = Record(-1, -1, -1)      # Empty record\n"
    "    FreeSpace = 0"
)
pdf.body_text("How it works step-by-step:")
pdf.bullet("1. Iterates through all 200 HashTable slots and fills each with Record(-1, -1, -1).")
pdf.bullet("2. Iterates through all 100 Spare slots and fills each with Record(-1, -1, -1).")
pdf.bullet("3. Resets FreeSpace to 0.")
pdf.body_text(
    "Each empty Record has key=-1, Item1=-1, Item2=-1. The value -1 serves as a sentinel that "
    "means 'this slot is empty'. This function MUST be called before any insertions. Total objects "
    "created: 300 Record instances."
)

# 4.4
pdf.sub_title("4.4 CalculateHash(KeyField: int) -> int")
pdf.code_block(
    "def CalculateHash(KeyField):\n"
    "    keyVal = KeyField % 200    # Modulo 200\n"
    "    return keyVal"
)
pdf.body_text(
    "The hash function uses the modulo operator (%) to map any integer key to an index in the "
    "range [0, 199]. This is one of the simplest hash functions possible."
)
pdf.body_text("Examples:")
pdf.bullet("Key 646: 646 % 200 = 46  -> stored at HashTable[46]")
pdf.bullet("Key 204: 204 % 200 = 4   -> stored at HashTable[4]")
pdf.bullet("Key 400: 400 % 200 = 0   -> stored at HashTable[0]")
pdf.bullet("Key 200: 200 % 200 = 0   -> COLLISION with key 400! Goes to Spare.")
pdf.body_text(
    "Time Complexity: O(1). This function always performs a single modulo operation regardless "
    "of input size. The choice of 200 as the modulus matches the HashTable size."
)

# 4.5
pdf.add_page()
pdf.sub_title("4.5 InsertIntoHash(NewRecord: Record)")
pdf.code_block(
    "def InsertIntoHash(NewRecord: Record):\n"
    "    global HashTable, Spare, FreeSpace\n"
    "    key = NewRecord.key\n"
    "    place = CalculateHash(NewRecord.key)\n"
    "    if HashTable[place].key != -1:      # Slot occupied!\n"
    "        Spare[FreeSpace] = NewRecord    # Store in overflow\n"
    "        FreeSpace += 1                  # Move pointer\n"
    "    else:\n"
    "        HashTable[place] = NewRecord    # Slot free, insert"
)
pdf.body_text("How it works step-by-step:")
pdf.bullet("1. Extracts the key from the new record (unused variable 'key' is saved).")
pdf.bullet("2. Computes the hash index using CalculateHash().")
pdf.bullet("3. Checks if the computed slot in HashTable is already occupied (key != -1).")
pdf.bullet("4. If OCCUPIED (collision): stores the record in Spare[FreeSpace] and increments FreeSpace.")
pdf.bullet("5. If FREE: stores the record directly at HashTable[place].")
pdf.ln(2)
pdf.body_text(
    "Collision Handling Strategy: This uses 'overflow area' or 'separate overflow' technique. "
    "Unlike chaining (linked lists) or open addressing (probing), collisions are simply diverted "
    "to a completely separate array. This is simple but has limitations:"
)
pdf.bullet("The Spare array has a fixed size of 100 - if more than 100 collisions occur, it will crash (IndexError).")
pdf.bullet("Searching for a key that had a collision requires scanning the entire Spare array (O(n)).")
pdf.bullet("There is no mechanism to search for records by key in this implementation.")
pdf.bullet("The variable 'key' on line 94 is assigned but never actually used (minor redundancy).")

# 4.6
pdf.sub_title("4.6 CreateHashTable() Function")
pdf.code_block(
    "def CreateHashTable():\n"
    "    global HashTable, Spare, FreeSpace\n"
    "    with open(r\"C:\\Users\\romme\\PycharmProjects\\\n"
    "        SchoolComputerSciencePrep\\May_June_25_42\\\n"
    "        HashData.txt\", \"r\") as f:\n"
    "        for line in f:\n"
    "            key = int(line.split(\",\")[0])\n"
    "            item1 = int(line.split(\",\")[1])\n"
    "            item2 = int(line.split(\",\")[2])\n"
    "            new_record = Record(key, item1, item2)\n"
    "            InsertIntoHash(new_record)"
)
pdf.body_text("How it works step-by-step:")
pdf.bullet("1. Opens HashData.txt using a HARDCODED ABSOLUTE FILE PATH (see Section 5).")
pdf.bullet("2. Reads the file line by line.")
pdf.bullet("3. Splits each line by comma to extract key, item1, item2.")
pdf.bullet("4. Converts all three values from strings to integers using int().")
pdf.bullet("5. Creates a new Record object with these values.")
pdf.bullet("6. Calls InsertIntoHash() to place the record in the hash table.")
pdf.ln(2)
pdf.body_text(
    "Note: The line is split THREE separate times (line.split(\",\")[0], [1], [2]) instead of "
    "splitting once and storing the result. This is slightly inefficient but functionally correct. "
    "Each split operation creates a new list object."
)

# 4.7
pdf.add_page()
pdf.sub_title("4.7 PrintSpare() Function")
pdf.code_block(
    "def PrintSpare():\n"
    "    global Spare, FreeSpace\n"
    "    for i in Spare:\n"
    "        if i.key != -1:\n"
    "            print(i.key)"
)
pdf.body_text("How it works step-by-step:")
pdf.bullet("1. Iterates through every element in the Spare array (all 100 slots).")
pdf.bullet("2. For each Record, checks if the key is NOT -1 (i.e., slot is occupied).")
pdf.bullet("3. If occupied, prints the key value to the console.")
pdf.body_text(
    "This function only prints the KEYS of collision records, not the full record data (Item1, "
    "Item2 are not printed). It shows which records could not be placed in their computed "
    "hash table slot due to collisions."
)

# 4.8
pdf.sub_title("4.8 Main Execution Flow (Question 2)")
pdf.code_block(
    "if __name__ == '__main__':\n"
    "    initialize()         # Step 1: Fill tables with empty records\n"
    "    CreateHashTable()    # Step 2: Load data from file\n"
    "    PrintSpare()         # Step 3: Show collision keys"
)
pdf.body_text(
    "The execution is straightforward and sequential:"
)
pdf.bullet("Step 1: Initialize all 300 slots (200 + 100) with empty Record(-1, -1, -1) objects.")
pdf.bullet("Step 2: Read 199 records from HashData.txt, compute hashes, and insert into the table.")
pdf.bullet("Step 3: Print the keys of all records that ended up in the Spare array due to collisions.")
pdf.body_text(
    "The if __name__ == '__main__' guard ensures this code only runs when the script is executed "
    "directly, not when imported as a module."
)

# ========== 5. HARDCODED VALUES ==========
pdf.add_page()
pdf.section_title("5. Hardcoded Values & Constants")
pdf.body_text(
    "The following values are hardcoded directly into the source code rather than being "
    "configurable or passed as parameters:"
)

widths3 = [50, 30, 110]
pdf.table_row(["Hardcoded Value", "Location", "Description"], widths3, bold=True, fill=True)
pdf.table_row(["20 (Stack size)", "Line 4", "Maximum stack capacity - fixed at 20 elements"], widths3)
pdf.table_row(["-1 (Sentinel)", "Lines 3-4", "Empty/null indicator for stack and hash table"], widths3)
pdf.table_row(["19 (Max index)", "Line 8", "Stack full check: TopOfStack == 19"], widths3)
pdf.table_row(["200 (Hash size)", "Line 70", "HashTable array size - 200 slots"], widths3)
pdf.table_row(["100 (Spare size)", "Line 71", "Spare overflow array size - 100 slots"], widths3)
pdf.table_row(["200 (Hash mod)", "Line 89", "Modulo value in hash function"], widths3)
pdf.table_row(["Absolute file path", "Line 105", "Full path to HashData.txt (see below)"], widths3)

pdf.ln(3)
pdf.sub_title("5.1 Hardcoded File Path (Critical)")
pdf.body_text(
    "The CreateHashTable() function contains a hardcoded absolute file path:"
)
pdf.code_block(
    "r\"C:\\Users\\romme\\PycharmProjects\\SchoolComputerSciencePrep\\\n"
    "  May_June_25_42\\HashData.txt\""
)
pdf.body_text(
    "This path is specific to the developer's machine (user 'romme', Windows OS). This means: "
    "(1) The code will FAIL on any other computer or different directory structure. "
    "(2) It will FAIL on Linux/Mac systems due to Windows-specific backslash path separators. "
    "(3) Moving the project folder will break this path. "
    "A better approach would be to use a relative path or accept the filename as a parameter, "
    "similar to how Question 1's ReadData() accepts a filename input."
)

pdf.sub_title("5.2 Operator Mappings (Question 1)")
pdf.body_text("Five arithmetic operators are hardcoded in the Calculate() function:")
widths4 = [30, 50, 50, 60]
pdf.table_row(["Symbol", "Operation", "Python Code", "Math Notation"], widths4, bold=True, fill=True)
pdf.table_row(["+", "Addition", "total + num", "a + b"], widths4)
pdf.table_row(["-", "Subtraction", "total - num", "a - b"], widths4)
pdf.table_row(["*", "Multiplication", "total * num", "a x b"], widths4)
pdf.table_row(["/", "Division", "total / num", "a / b"], widths4)
pdf.table_row(["^", "Power/Exponent", "total ** num", "a^b"], widths4)

# ========== 6. MEMORY MANAGEMENT ==========
pdf.add_page()
pdf.section_title("6. Memory Management In Detail")

pdf.sub_title("6.1 Stack Memory (Question 1)")
pdf.body_text(
    "The stack uses STATIC memory allocation. A fixed-size list of 20 elements is created at "
    "program startup. Memory is never dynamically allocated or freed during stack operations."
)
pdf.bullet("Allocation: Stack = [\"-1\"] * 20 creates 20 string references at startup.")
pdf.bullet("Push: Overwrites an existing slot (no new memory allocated for the array).")
pdf.bullet("Pop: Decrements the pointer but does NOT clear the old value from memory.")
pdf.bullet("Maximum memory: 20 string objects + 1 integer (TopOfStack) + the list overhead.")
pdf.bullet("Overflow protection: Push() returns -1 when TopOfStack reaches 19.")
pdf.bullet("Underflow protection: Pop() returns \"-1\" when TopOfStack is -1.")
pdf.ln(2)
pdf.body_text(
    "Since Python strings are immutable objects, each Push() with a new string creates a new "
    "string object in Python's memory heap. The old string at that slot becomes unreferenced "
    "and is eventually garbage collected by Python's memory manager."
)

pdf.sub_title("6.2 Hash Table Memory (Question 2)")
pdf.body_text(
    "The hash table also uses STATIC memory allocation with fixed-size arrays."
)
pdf.bullet("HashTable: 200 Record objects = 200 x (3 integers + object overhead).")
pdf.bullet("Spare: 100 Record objects = 100 x (3 integers + object overhead).")
pdf.bullet("Total: 300 Record objects allocated during initialize().")
pdf.bullet("FreeSpace: 1 integer tracking spare array usage.")
pdf.ln(2)
pdf.body_text(
    "When inserting a new record, the old Record(-1, -1, -1) at that slot is replaced and becomes "
    "eligible for garbage collection. The new Record is created in CreateHashTable() and its "
    "reference is stored in the array."
)

pdf.sub_title("6.3 Python Memory Specifics")
pdf.body_text(
    "All memory management is handled by Python's runtime:"
)
pdf.bullet("Reference counting: Python tracks how many variables point to each object.")
pdf.bullet("Garbage collection: Unreferenced objects are automatically freed.")
pdf.bullet("No manual memory management: No malloc/free, new/delete, or similar calls.")
pdf.bullet("Global variables: TopOfStack, Stack, HashTable, Spare, FreeSpace persist for program lifetime.")
pdf.bullet("No persistent storage: All data is lost when the program exits. Nothing is written to disk.")

# ========== 7. DATA FILES ==========
pdf.add_page()
pdf.section_title("7. Data Files & Formats")

pdf.sub_title("7.1 HashData.txt (199 records)")
pdf.body_text("Format: CSV (Comma-Separated Values) with 3 integer columns per line.")
pdf.code_block(
    "Format: <key>,<item1>,<item2>\n"
    "Example lines:\n"
    "  646,12,568\n"
    "  204,22,569\n"
    "  824,554,5215\n"
    "  ...\n"
    "  693,4561,14564"
)
pdf.body_text("Data statistics:")
pdf.bullet("Total records: 199 lines")
pdf.bullet("Key range: 2 to 994")
pdf.bullet("Item1 range: 1 to 654,879")
pdf.bullet("Item2 range: 1 to 95,164")
pdf.bullet("Duplicate keys present: key 31 appears on lines 11 and 180; key 88 appears on lines 173 and 191")
pdf.body_text(
    "The duplicate keys (31, 88) mean that the second occurrence will always go to the Spare "
    "array, since the first occurrence already occupies the hash slot (or its collision slot). "
    "This tests the collision handling mechanism."
)

pdf.sub_title("7.2 StackData.txt (9 values)")
pdf.body_text("Format: One value per line, alternating between numbers and operators.")
pdf.code_block("3\n+\n2\n*\n2\n^\n2\n-\n10")
pdf.body_text(
    "When read into the stack (LIFO), evaluation proceeds from top (10) downward (3). "
    "The expression evaluates to 131.0."
)

pdf.sub_title("7.3 SecondStack.txt (9 values)")
pdf.body_text("Format: Same as StackData.txt.")
pdf.code_block("20\n*\n4\n^\n3\n/\n5\n+\n1")
pdf.body_text("An alternative test file for the postfix calculator.")

# ========== 8. NETWORK ==========
pdf.add_page()
pdf.section_title("8. Network / IP Addresses")
pdf.body_text(
    "This project contains NO network functionality whatsoever:"
)
pdf.bullet("No IP addresses are used anywhere in the code.")
pdf.bullet("No port numbers are defined.")
pdf.bullet("No socket programming or network connections.")
pdf.bullet("No HTTP requests or API calls.")
pdf.bullet("No client-server architecture.")
pdf.bullet("No imports of socket, requests, urllib, http, or any network library.")
pdf.body_text(
    "The project is entirely local and file-based. All data is read from text files on the "
    "local filesystem. The only I/O operations are: (1) reading from text files, and "
    "(2) printing output to the console (stdout)."
)

# ========== 9. DEPENDENCIES ==========
pdf.section_title("9. Dependencies & Imports")
pdf.body_text(
    "This project has ZERO external dependencies:"
)
pdf.bullet("No import statements exist in Response.py.")
pdf.bullet("No requirements.txt or setup.py file exists.")
pdf.bullet("No pip packages are needed.")
pdf.bullet("No virtual environment is required.")
pdf.body_text(
    "The code uses only Python built-in features:"
)
pdf.bullet("Built-in functions: open(), print(), input(), int(), float(), range(), len()")
pdf.bullet("Built-in operators: %, +, -, *, /, ** (power)")
pdf.bullet("Built-in types: list, str, int, float")
pdf.bullet("Built-in statements: for, while, if/elif/else, with, try/except, class, def, global")
pdf.body_text(
    "The only requirement is a Python 3 interpreter. Any version of Python 3.x should work."
)

# ========== 10. ERROR HANDLING ==========
pdf.add_page()
pdf.section_title("10. Error Handling")

pdf.sub_title("10.1 Question 1 Error Handling")
pdf.bullet("Stack overflow: Push() returns -1 and ReadData() prints 'Stack full'.")
pdf.bullet("Stack underflow: Pop() returns \"-1\" string instead of raising an exception.")
pdf.bullet("File not found: try/except in ReadData() catches all exceptions and prints the error.")
pdf.bullet("Division by zero: NOT handled - will raise a ZeroDivisionError if encountered.")
pdf.bullet("Invalid operator: NOT handled - if an unknown operator appears, it is silently skipped.")
pdf.bullet("Non-numeric values: NOT handled - will raise ValueError during float() conversion.")

pdf.sub_title("10.2 Question 2 Error Handling")
pdf.bullet("Spare array overflow: NOT handled - will crash with IndexError if > 100 collisions.")
pdf.bullet("File not found: NOT handled - no try/except around file open (will raise FileNotFoundError).")
pdf.bullet("Malformed CSV: NOT handled - will crash on lines with fewer than 3 comma-separated values.")
pdf.bullet("Non-integer values: NOT handled - will raise ValueError during int() conversion.")
pdf.bullet("Hash table full: NOT checked - the hash function prevents this since modulo matches size.")

# ========== 11. GIT HISTORY ==========
pdf.section_title("11. Git History & Version Control")
pdf.body_text("The project uses Git for version control. Repository: local Git repository.")
pdf.code_block(
    "Commit History (newest first):\n"
    "\n"
    "bb8e9cf  \"May June 25 42 done\"\n"
    "642a64c  \"Q estion 2\"\n"
    "5e594bd  \"May June 25\"\n"
    "4ab0db9  \"Initial Commit\"\n"
    "dd85f51  \"first commit\"\n"
    "\n"
    "Branch: main\n"
    "Status: README.md modified (uncommitted)"
)
pdf.body_text(
    "The commit history shows iterative development: initial setup, then Question 1, then "
    "Question 2, then marking the work as done. There are 5 total commits on the main branch."
)

# ========== 12. IMPROVEMENTS ==========
pdf.add_page()
pdf.section_title("12. Potential Improvements & Notes")

pdf.sub_title("12.1 Code Organization")
pdf.bullet("Both questions are in a single file (Response.py) - could be split into separate files.")
pdf.bullet("Question 1 is entirely commented out using triple-quote strings.")
pdf.bullet("Question 2 also appears commented out (lines 69-123 wrapped in triple quotes).")
pdf.bullet("The triple-quote on line 69 uses four single-quotes ('''') which is a Python quirk.")

pdf.sub_title("12.2 Hardcoded Path")
pdf.bullet("The absolute file path in CreateHashTable() should be made relative or parameterized.")
pdf.bullet("A simple fix: use os.path or accept filename as a parameter like Question 1 does.")

pdf.sub_title("12.3 Missing Features")
pdf.bullet("No search/lookup function for the hash table (can insert but cannot retrieve by key).")
pdf.bullet("No delete operation for either data structure.")
pdf.bullet("No display/print function for the full hash table contents.")
pdf.bullet("No input validation for stack calculator (assumes well-formed postfix expressions).")

pdf.sub_title("12.4 Efficiency Notes")
pdf.bullet("CreateHashTable() splits each line 3 times - could split once and index the result.")
pdf.bullet("InsertIntoHash() saves key to a variable that is never used.")
pdf.bullet("PrintSpare() iterates all 100 slots even if only a few have data (could stop at FreeSpace).")

pdf.sub_title("12.5 Exam Context")
pdf.body_text(
    "This code was written as a response to Cambridge A-Level paper 9618/42 (May/June 2025). "
    "The implementation follows exam requirements which often mandate using global variables, "
    "fixed-size arrays, and procedural programming style rather than more Pythonic approaches. "
    "The use of global variables, sentinel values (-1), and fixed-size arrays are typical of "
    "A-Level pseudocode-to-Python translations."
)

# Save
output_path = r"C:\Users\romme\PycharmProjects\SchoolComputerSciencePrep\Project_Documentation.pdf"
pdf.output(output_path)
print(f"PDF generated successfully: {output_path}")
