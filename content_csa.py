# -*- coding: utf-8 -*-
"""
The Stacks — AP Computer Science A content (2025–26 revised CED).
4 units, 53 topics. Edit here, then run `python3 build.py`.
All notes, examples, and practice questions are original.
"""

COURSE = {
    "slug": "ap-csa",
    "title": "AP Computer Science A",
    "unit_word": "Unit",
    "intro": """
<p>Java, from first program to recursion, organized exactly as the College Board's <em>revised</em> 2025–26 Course and Exam Description lays it out: four units, 53 numbered topics. This is the new framework — inheritance is gone, text files and data sets are in, and everything is typed into Bluebook. Each topic page has the essential knowledge, a worked code example, an exam tip, practice questions in the exam's style, and vocabulary.</p>
""",
    "exam_format": """
<section class="block">
  <h2>How the exam works</h2>
  <ul class="points">
    <li><strong>Section I — Multiple choice.</strong> 42 questions, 90 minutes, 50% of your score. Heavy on code reading: predict output, count iterations, find the bug, pick the equivalent code.</li>
    <li><strong>Section II — Free response.</strong> 4 questions, 90 minutes, 50% of your score. The four types are fixed every year: <strong>Q1 Methods and Control Structures</strong>, <strong>Q2 Class Design</strong> (write an entire class), <strong>Q3 Data Analysis with ArrayList</strong>, <strong>Q4 2D Array</strong>. Each is scored on a 9-point rubric.</li>
    <li>The exam is <strong>fully digital</strong> in the Bluebook app — you type Java directly. No paper, no handwritten code.</li>
    <li>A <strong>Java Quick Reference</strong> is provided with the exact String, Math, ArrayList, Integer, Double, and Object methods you can use. If a method isn't on it, don't assume it exists on the exam.</li>
    <li>No penalty for guessing on multiple choice. On FRQs, partial credit is real — a correct loop with a wrong condition still earns points, and a blank earns nothing.</li>
  </ul>
</section>
""",
    "five_tips": """
<section class="block">
  <h2>What separates a 5 from a 3</h2>
  <ul class="points">
    <li><strong>Trace with a table, every time.</strong> Variables, loop counters, array contents after each pass. Most multiple-choice misses are tracing slips, not knowledge gaps.</li>
    <li><strong>Know the three String traps cold:</strong> <code>substring</code>'s end index is exclusive, <code>==</code> compares references not contents (use <code>.equals</code>), and <code>compareTo</code> returns an int, not a boolean.</li>
    <li><strong>Write FRQs in a fixed shape.</strong> Method header exactly as given → declare a result variable → loop → conditional → update → return. Practice until it's automatic; rubric points reward each piece independently.</li>
    <li><strong>Off-by-one is the whole game in Unit 4.</strong> Arrays start at 0 and end at <code>length - 1</code>. Removing from an ArrayList inside a forward loop skips elements. Row-major vs. column-major traversal of a 2D array changes the output order.</li>
    <li><strong>Unit 4 is 30–40% of the exam.</strong> Arrays, ArrayLists, 2D arrays, and the two algorithms (search, sort) plus recursion tracing. Study time should reflect that.</li>
  </ul>
</section>
""",
}

# ----------------------------------------------------------------------
# UNIT 1 — Using Objects and Methods (15–25%)
# ----------------------------------------------------------------------

U1 = {
    "num": 1,
    "title": "Using Objects and Methods",
    "weight": "15–25%",
    "lede": "Everything else in the course assumes Unit 1. Variables, types, expressions, calling methods on objects, and the String class. Weakness here shows up as lost points in every other unit.",
    "understandings": [
        "Java programs are sequences of statements that a compiler translates; errors can happen at compile time or run time.",
        "Variables have types; primitive types hold values directly while reference types hold addresses of objects.",
        "Methods are called on classes (static) or objects (instance), take arguments, and may return values.",
        "String and Math are the two classes you must know in detail, using exactly the methods on the Java Quick Reference.",
    ],
    "topics": [
        {
            "num": 1, "title": "Introduction to Algorithms, Programming, and Compilers", "blurb": "what a program is, compile vs. run time",
            "lede": "The vocabulary you need before the first line of Java: what a compiler does, what a syntax error is, and why some errors only appear when the program runs.",
            "points": [
                "An <strong>algorithm</strong> is a finite set of instructions that accomplishes a task. A <strong>program</strong> expresses an algorithm in a programming language so a computer can run it.",
                "Java source code is written in <code>.java</code> files and <strong>compiled</strong> into bytecode. The <strong>compiler</strong> translates and checks the code before it can run.",
                "A <strong>syntax error</strong> (compile-time error) is a violation of Java's grammar — the compiler refuses to produce a program. A <strong>run-time error</strong> (exception) happens while the program executes, such as dividing an int by zero. A <strong>logic error</strong> compiles and runs but produces the wrong result.",
                "<strong>Sequence</strong>, <strong>selection</strong>, and <strong>iteration</strong> are the three control structures every algorithm is built from.",
                "A Java program's entry point is <code>public static void main(String[] args)</code>. Statements end with semicolons; blocks are enclosed in braces <code>{ }</code>.",
                "Comments (<code>//</code> single line, <code>/* */</code> block) are ignored by the compiler and exist for people.",
            ],
            "example": """
<pre class="code">public class Hello
{
    public static void main(String[] args)
    {
        System.out.println("Hello, AP CSA");
        int x = 10 / 0;   // compiles fine, then ArithmeticException at run time
    }
}</pre>
<p>The missing-semicolon version of line 5 would be a <strong>compile-time</strong> error — nothing runs. As written, it compiles, prints the greeting, then throws a <strong>run-time</strong> exception on line 6. The exam wants you to classify each.</p>""",
            "tip": "If a question shows code and asks \"what happens,\" check syntax first (missing semicolon, mismatched braces, undeclared variable = won't compile), then look for run-time traps (division by zero, null, bad index), then trace for logic.",
            "questions": [
                {
                    "stem": "Which of the following is a compile-time error in Java?",
                    "options": ["Dividing an integer by zero", "Accessing an array index that is out of bounds", "Omitting the semicolon at the end of a statement", "Calling a method on a variable whose value is <code>null</code>"],
                    "answer": "C",
                    "explanation": "A missing semicolon violates syntax, so the compiler rejects it. The other three compile and fail at run time.",
                },
                {
                    "stem": "A program compiles and runs to completion but prints an incorrect total because the loop stops one iteration early. This is best described as which type of error?",
                    "options": ["Compile-time error", "Run-time error", "Logic error", "Syntax error"],
                    "answer": "C",
                    "explanation": "Runs fine, wrong answer — that's a logic error.",
                },
            ],
            "vocab": [
                ("Compiler", "translates Java source code into a form the computer can run, reporting syntax errors"),
                ("Compile-time error", "an error the compiler detects; the program cannot run"),
                ("Run-time error", "an error that occurs during execution, such as an exception"),
                ("Logic error", "code that runs but produces incorrect results"),
            ],
        },
        {
            "num": 2, "title": "Variables and Data Types", "blurb": "int, double, boolean, String",
            "lede": "Java is statically typed: every variable is declared with a type that never changes. The exam's primitive types are int, double, and boolean; everything else is a reference.",
            "points": [
                "A <strong>variable</strong> is a named memory location with a declared <strong>type</strong>. Declaration: <code>int count;</code>. Declaration with initialization: <code>double price = 9.99;</code>",
                "<strong>Primitive types</strong> on the exam: <code>int</code> (whole numbers), <code>double</code> (decimals), <code>boolean</code> (<code>true</code>/<code>false</code>). A primitive variable stores the value itself.",
                "<strong>Reference types</strong> (like <code>String</code> and every other class) store the <em>address</em> of an object, not the object. Two reference variables can point to the same object.",
                "<code>int</code> has a fixed range: <code>Integer.MIN_VALUE</code> (−2,147,483,648) to <code>Integer.MAX_VALUE</code> (2,147,483,647). Exceeding it causes <strong>overflow</strong> — it wraps around silently, no error.",
                "The <code>final</code> keyword makes a variable a constant: <code>final int MAX = 100;</code>. Assigning to it again is a compile-time error.",
                "Naming: variables start with a lowercase letter (<code>totalScore</code>); constants are all caps (<code>MAX_SIZE</code>); classes start uppercase (<code>String</code>). Names must be declared before use and are case-sensitive.",
            ],
            "example": """
<pre class="code">int age = 17;
double gpa = 3.85;
boolean isSenior = true;
String name = "Ram";
final double TAX = 0.07;
age = 18;        // fine
TAX = 0.08;      // compile-time error: cannot assign to final</pre>
<p>Four types, four kinds of value. <code>name</code> holds a reference to a String object; the other three hold their values directly. That distinction matters in 1.13 and 3.6.</p>""",
            "tip": "Questions on ranges are usually about overflow: <code>Integer.MAX_VALUE + 1</code> equals <code>Integer.MIN_VALUE</code>, not an error. And a variable declared but never assigned can't be used — that's a compile error, not a default of 0.",
            "questions": [
                {
                    "stem": "Which of the following declarations will cause a compile-time error?",
                    "options": ["<code>int count = 5;</code>", "<code>double avg = 3;</code>", "<code>int total = 3.5;</code>", "<code>boolean done = false;</code>"],
                    "answer": "C",
                    "explanation": "A double literal can't be assigned to an int without a cast. Assigning an int to a double (option B) is fine — it widens automatically.",
                },
                {
                    "stem": "What is the result of evaluating <code>Integer.MAX_VALUE + 1</code>?",
                    "options": ["A compile-time error", "A run-time exception", "<code>Integer.MIN_VALUE</code>", "<code>Integer.MAX_VALUE</code>"],
                    "answer": "C",
                    "explanation": "Integer overflow wraps around silently to the minimum value. Java doesn't throw an error.",
                },
            ],
            "vocab": [
                ("Primitive type", "int, double, boolean — stores the value directly"),
                ("Reference type", "a variable that stores the address of an object"),
                ("final", "keyword that makes a variable's value unchangeable after initialization"),
                ("Overflow", "an int calculation exceeding the representable range wraps around"),
            ],
        },
        {
            "num": 3, "title": "Expressions and Output", "blurb": "arithmetic, integer division, println",
            "lede": "Arithmetic in Java has one rule that catches everyone: dividing two ints gives an int. Everything else follows normal math.",
            "points": [
                "Operators: <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>%</code>. Normal precedence: parentheses, then <code>* / %</code> left to right, then <code>+ -</code> left to right.",
                "<strong>Integer division:</strong> when both operands are <code>int</code>, <code>/</code> truncates (drops the decimal). <code>7 / 2</code> is <code>3</code>, <code>-7 / 2</code> is <code>-3</code>. If either operand is a <code>double</code>, the result is a double: <code>7 / 2.0</code> is <code>3.5</code>.",
                "<code>%</code> is the <strong>remainder</strong>: <code>7 % 2</code> is <code>1</code>, <code>10 % 5</code> is <code>0</code>. For negative dividends the result is negative: <code>-7 % 2</code> is <code>-1</code>.",
                "Dividing an int by zero throws an <code>ArithmeticException</code>. Dividing a double by zero gives <code>Infinity</code> or <code>NaN</code>, no exception.",
                "<code>System.out.println(x)</code> prints x and moves to a new line; <code>System.out.print(x)</code> prints without a newline.",
                "<code>+</code> with a String is <strong>concatenation</strong>. Evaluation is left to right: <code>\"Sum: \" + 1 + 2</code> is <code>\"Sum: 12\"</code>, but <code>\"Sum: \" + (1 + 2)</code> is <code>\"Sum: 3\"</code>.",
                "String literals are in double quotes; escape sequences include <code>\\n</code> (newline), <code>\\\"</code> (quote), <code>\\\\</code> (backslash).",
            ],
            "example": """
<pre class="code">System.out.println(17 / 5);        // 3
System.out.println(17 % 5);        // 2
System.out.println(17 / 5.0);      // 3.4
System.out.println(17.0 / 5);      // 3.4
System.out.println(1 + 2 + "3");   // 33
System.out.println("1" + 2 + 3);   // 123
System.out.println(2 * 3 % 4);     // 2   (6 % 4)</pre>
<p>Lines 5 and 6 are the concatenation trap: left-to-right evaluation means the ints are added <em>before</em> the String is reached in line 5, but not in line 6.</p>""",
            "tip": "Look at both operands of every <code>/</code>. Both int? Truncate. Either double? Decimal result. For the <code>+</code> trap, scan left to right and note the moment a String appears — from then on everything is concatenation.",
            "questions": [
                {
                    "stem": "What is printed by <code>System.out.println(25 / 4 * 2.0);</code>?",
                    "options": ["12.5", "12.0", "12", "13.0"],
                    "answer": "B",
                    "explanation": "25 / 4 is integer division = 6. Then 6 * 2.0 = 12.0 (double).",
                },
                {
                    "stem": "What is printed by <code>System.out.println(\"Total: \" + 5 + 10);</code>?",
                    "options": ["Total: 15", "Total: 510", "A compile-time error", "15"],
                    "answer": "B",
                    "explanation": "Left to right: \"Total: \" + 5 → \"Total: 5\", then + 10 → \"Total: 510\".",
                },
                {
                    "stem": "What is the value of <code>-13 % 5</code>?",
                    "options": ["3", "-3", "2", "-2"],
                    "answer": "B",
                    "explanation": "Java's remainder keeps the sign of the dividend: -13 = 5 × (-2) + (-3), so the result is -3.",
                },
            ],
            "vocab": [
                ("Integer division", "int / int drops the fractional part"),
                ("Remainder (%)", "the remainder after division; sign follows the left operand"),
                ("Concatenation", "joining Strings with +; any + involving a String produces a String"),
                ("println", "prints a value followed by a newline"),
            ],
        },
        {
            "num": 4, "title": "Assignment Statements and Input", "blurb": "=, reading input with Scanner",
            "lede": "Assignment stores a value; the revised course also expects you to know how a program reads input, using the Scanner class methods on the reference sheet.",
            "points": [
                "<code>=</code> is <strong>assignment</strong>: evaluate the right side, store it in the variable on the left. It is <em>not</em> equality (that's <code>==</code>).",
                "The right side is evaluated using the variable's <em>current</em> value, so <code>x = x + 1</code> increments. The expression must produce a value compatible with the variable's type.",
                "Assigning one primitive variable to another <strong>copies the value</strong>. Assigning one reference variable to another copies the <strong>reference</strong> — both then point to the same object.",
                "<strong>Input</strong> comes from <code>Scanner</code>. Create one with <code>Scanner input = new Scanner(System.in);</code> then read with <code>nextInt()</code>, <code>nextDouble()</code>, <code>nextLine()</code>, or <code>next()</code> (one word).",
                "<code>hasNext()</code>, <code>hasNextInt()</code>, <code>hasNextLine()</code> return whether more input is available — used to loop over input of unknown length.",
                "<strong>The nextInt/nextLine trap:</strong> <code>nextInt()</code> leaves the newline in the buffer, so a following <code>nextLine()</code> returns an empty string. The fix is an extra <code>nextLine()</code> to consume it.",
                "Swapping two variables requires a temporary: <code>int temp = a; a = b; b = temp;</code>",
            ],
            "example": """
<pre class="code">Scanner in = new Scanner(System.in);
System.out.print("Age: ");
int age = in.nextInt();
in.nextLine();                 // consume leftover newline
System.out.print("Name: ");
String name = in.nextLine();
System.out.println(name + " is " + age);</pre>
<p>Without line 4, if the user types <code>17</code> and Enter, <code>name</code> becomes the empty string because <code>nextLine()</code> reads the leftover newline. This exact trap is the reason Scanner questions exist.</p>""",
            "tip": "Questions about Scanner are usually \"which method reads a whole line vs. one token\" (<code>nextLine</code> vs <code>next</code>) or the nextInt-then-nextLine trap. Also remember: <code>=</code> assigns; a question with <code>if (x = 5)</code> is a compile error because an int isn't a boolean.",
            "questions": [
                {
                    "stem": "After the following code runs, what are the values of <code>a</code> and <code>b</code>?\n<pre class=\"code\">int a = 3;\nint b = 7;\na = b;\nb = a;</pre>",
                    "options": ["a = 3, b = 7", "a = 7, b = 3", "a = 7, b = 7", "a = 3, b = 3"],
                    "answer": "C",
                    "explanation": "a becomes 7, then b is assigned a's new value, 7. No swap happened — a temp variable was needed.",
                },
                {
                    "stem": "A program reads an integer with <code>nextInt()</code> and then immediately calls <code>nextLine()</code> to read the user's name. The name is stored as an empty string. Which of the following best explains why?",
                    "options": ["<code>nextLine()</code> cannot read Strings.", "<code>nextInt()</code> does not consume the newline after the number, so <code>nextLine()</code> reads that leftover newline.", "The Scanner must be recreated between reads.", "<code>nextInt()</code> reads the entire line including the name."],
                    "answer": "B",
                    "explanation": "This is the standard Scanner buffer behavior. An extra nextLine() call fixes it.",
                },
            ],
            "vocab": [
                ("Assignment (=)", "stores the value of the right-side expression in the left-side variable"),
                ("Scanner", "a class for reading input from the keyboard or a file"),
                ("nextLine()", "reads an entire line of input as a String"),
                ("nextInt()", "reads the next integer token, leaving the newline in the buffer"),
            ],
        },
        {
            "num": 5, "title": "Casting and Range of Variables", "blurb": "(int), (double), rounding",
            "lede": "Casting converts between types. The exam tests the truncation of (int), automatic widening to double, and the standard rounding idiom.",
            "points": [
                "<strong>Casting</strong> temporarily converts a value to another type: <code>(int) 3.99</code> is <code>3</code> (truncates toward zero, never rounds); <code>(double) 7</code> is <code>7.0</code>.",
                "A cast applies to the value <em>immediately</em> after it. <code>(int) 7.8 / 2</code> is <code>3</code> (cast to 7 first, then integer division). <code>(int) (7.8 / 2)</code> is <code>3</code> too but for a different reason (3.9 truncated). <code>(double) 7 / 2</code> is <code>3.5</code>.",
                "<strong>Widening</strong> is automatic: assigning an int to a double works (<code>double d = 5;</code> gives 5.0). <strong>Narrowing</strong> (double to int) requires an explicit cast or the compiler complains.",
                "In mixed arithmetic, ints are promoted to doubles: <code>5 / 2.0</code> is <code>2.5</code>.",
                "<strong>Rounding idiom:</strong> <code>(int) (x + 0.5)</code> rounds a positive double to the nearest int. For negatives, <code>(int) (x - 0.5)</code>.",
                "Values outside int's range overflow silently; casting a large double to int clamps to <code>Integer.MAX_VALUE</code> or <code>MIN_VALUE</code>.",
                "Doubles can't represent most decimals exactly: <code>0.1 + 0.2</code> is not exactly <code>0.3</code>. Comparing doubles with <code>==</code> is unreliable; check whether the difference is below a small tolerance.",
            ],
            "example": """
<pre class="code">double x = 7.6;
int a = (int) x;             // 7   truncation
int b = (int) (x + 0.5);     // 8   rounding
double c = (double) 7 / 2;   // 3.5
double d = (double) (7 / 2); // 3.0  division happened first
int e = (int) -7.6;          // -7  toward zero, not -8</pre>
<p>Lines 4 and 5 are the exam's favorite pair. The cast binds to the nearest value; parentheses change what gets cast.</p>""",
            "tip": "Ask two things for every cast: what exactly is being cast (the next value only, unless parentheses say otherwise), and is it truncation or rounding (a bare (int) always truncates). Toward zero: (int) -2.9 is -2.",
            "questions": [
                {
                    "stem": "What is the value of <code>(int) 9.99 / 2 * 2.0</code>?",
                    "options": ["9.99", "9.0", "8.0", "10.0"],
                    "answer": "C",
                    "explanation": "(int) 9.99 → 9. 9 / 2 → 4 (integer division). 4 * 2.0 → 8.0.",
                },
                {
                    "stem": "Which expression correctly rounds the positive double <code>val</code> to the nearest integer?",
                    "options": ["<code>(int) val</code>", "<code>(int) (val + 0.5)</code>", "<code>(int) val + 0.5</code>", "<code>(double) (val + 0.5)</code>"],
                    "answer": "B",
                    "explanation": "Adding 0.5 then truncating rounds correctly for positives. Option C truncates first, then adds 0.5 producing a double.",
                },
                {
                    "stem": "What is printed by <code>System.out.println((int) -4.7);</code>?",
                    "options": ["-5", "-4", "4", "-4.0"],
                    "answer": "B",
                    "explanation": "Casting truncates toward zero, so -4.7 becomes -4.",
                },
            ],
            "vocab": [
                ("Cast", "an explicit conversion, e.g. (int) or (double)"),
                ("Truncation", "dropping the fractional part when casting to int"),
                ("Widening", "automatic conversion from int to double"),
                ("Narrowing", "conversion from double to int, requires a cast"),
            ],
        },
        {
            "num": 6, "title": "Compound Assignment Operators", "blurb": "+=, -=, *=, /=, %=, ++, --",
            "lede": "Shorthand that shows up in every loop. The traps are the hidden cast in compound operators and what ++ does inside an expression.",
            "points": [
                "<code>x += 5</code> means <code>x = x + 5</code>. Same for <code>-=</code>, <code>*=</code>, <code>/=</code>, <code>%=</code>.",
                "Compound operators include an <strong>implicit cast</strong> back to the variable's type: if <code>x</code> is an int, <code>x /= 2.0</code> compiles and stores an int. <code>x = x / 2.0</code> would not compile.",
                "<code>x++</code> and <code>++x</code> both add 1 to x. <code>x--</code> and <code>--x</code> subtract 1. On the exam these are used as standalone statements, where the pre/post distinction doesn't matter.",
                "The AP exam does not test <code>x++</code> inside larger expressions (like <code>y = x++</code>). Keep increments on their own line.",
                "<code>x *= 2 + 3</code> means <code>x = x * (2 + 3)</code> — the whole right side is computed first.",
                "These operators work on doubles too: <code>total += 0.5;</code>",
            ],
            "example": """
<pre class="code">int x = 10;
x += 3;        // 13
x -= 5;        // 8
x *= 2;        // 16
x /= 3;        // 5   (integer division)
x %= 4;        // 1
x++;           // 2
x *= 1 + 1;    // 4   (x * 2, not x * 1 + 1)</pre>""",
            "tip": "Rewrite every compound operator as its long form before tracing: <code>x *= a + b</code> → <code>x = x * (a + b)</code>. The parentheses are the part students drop.",
            "questions": [
                {
                    "stem": "What is the value of <code>n</code> after the following code?\n<pre class=\"code\">int n = 7;\nn += 3;\nn /= 2;\nn *= n;</pre>",
                    "options": ["25", "50", "49", "100"],
                    "answer": "A",
                    "explanation": "7 + 3 = 10. 10 / 2 = 5. 5 * 5 = 25.",
                },
                {
                    "stem": "What is the value of <code>total</code> after <code>int total = 12; total -= 2 * 3;</code>?",
                    "options": ["30", "6", "18", "10"],
                    "answer": "B",
                    "explanation": "The right side (2 * 3 = 6) is computed first, then total = 12 - 6 = 6.",
                },
            ],
            "vocab": [
                ("Compound assignment", "operators like += that combine arithmetic with assignment"),
                ("Increment (++)", "adds 1 to a variable"),
                ("Decrement (--)", "subtracts 1 from a variable"),
            ],
        },
        {
            "num": 7, "title": "Application Program Interface (API) and Libraries", "blurb": "using code you didn't write",
            "lede": "Java ships with thousands of classes. An API tells you what they do and how to call them, without showing the code inside.",
            "points": [
                "A <strong>library</strong> is a collection of classes written and tested by others. Java's standard library includes <code>String</code>, <code>Math</code>, <code>Scanner</code>, <code>ArrayList</code>, and more.",
                "An <strong>API (Application Program Interface)</strong> is the documentation of a library: each class, its methods, their parameters, return types, and what they do. You program to the API without knowing the implementation.",
                "The AP exam provides a <strong>Java Quick Reference</strong> — a mini-API listing exactly the methods you may use from String, Math, Integer, Double, ArrayList, and Object.",
                "Classes in the <code>java.lang</code> package (String, Math, Integer, Double) are available automatically. Others (<code>Scanner</code>, <code>ArrayList</code>, <code>File</code>) require an <code>import</code> statement at the top of the file.",
                "Reading documentation is a skill: the method header tells you the return type, name, and parameter types. That's enough to call it correctly.",
                "Using a library is <strong>abstraction</strong> in practice — you rely on <em>what</em> a method does, not <em>how</em>.",
            ],
            "example": """
<pre class="code">import java.util.Scanner;    // needed: not in java.lang
import java.util.ArrayList;

public class Demo
{
    public static void main(String[] args)
    {
        String s = "abc";                    // String: no import
        double r = Math.sqrt(16);            // Math: no import
        ArrayList&lt;String&gt; list = new ArrayList&lt;String&gt;();
    }
}</pre>""",
            "tip": "If a question asks why a program won't compile and it uses Scanner or ArrayList without an import, that's the answer. If it asks what a method returns, look at the header's return type — the exam sometimes gives you a header for a made-up method and expects you to use it correctly from the header alone.",
            "questions": [
                {
                    "stem": "Which of the following best describes an API?",
                    "options": ["The source code of a library", "The documentation describing a library's classes, methods, parameters, and return values", "A type of run-time error", "A Java keyword"],
                    "answer": "B",
                    "explanation": "An API is the interface specification — what you can call and how — not the implementation.",
                },
                {
                    "stem": "Which of the following classes requires an <code>import</code> statement before it can be used?",
                    "options": ["<code>String</code>", "<code>Math</code>", "<code>Scanner</code>", "<code>Integer</code>"],
                    "answer": "C",
                    "explanation": "Scanner is in java.util. The other three are in java.lang, which is imported automatically.",
                },
            ],
            "vocab": [
                ("Library", "a collection of pre-written classes available for use"),
                ("API", "documentation describing how to use a library's classes and methods"),
                ("import", "a statement that makes a class outside java.lang available in a file"),
                ("Java Quick Reference", "the list of methods provided on the AP exam"),
            ],
        },
        {
            "num": 8, "title": "Documentation with Comments", "blurb": "comments, preconditions, postconditions",
            "lede": "Comments document code for humans. The exam has specific vocabulary for the promises a method makes.",
            "points": [
                "<code>//</code> starts a single-line comment. <code>/* ... */</code> is a multi-line comment. <code>/** ... */</code> is a Javadoc comment, used to document classes and methods.",
                "A <strong>precondition</strong> is a condition that must be true <em>before</em> a method is called for it to work correctly. The method is <em>not</em> required to check it — the caller is responsible.",
                "A <strong>postcondition</strong> is a condition that will be true <em>after</em> the method finishes, assuming preconditions were met. It describes what the method guarantees.",
                "On FRQs, the problem statement gives preconditions (e.g., \"the array contains at least one element\"). You may rely on them — you don't need to handle cases they rule out.",
                "Good comments explain intent and non-obvious decisions. Restating the code (<code>x++; // add one to x</code>) adds nothing.",
                "Documentation helps future readers, including you, and is part of a professional development process.",
            ],
            "example": """
<pre class="code">/**
 * Returns the average of the values in nums.
 * Precondition: nums.length &gt; 0
 * Postcondition: the returned value is the sum of the
 *                elements divided by nums.length
 */
public static double average(int[] nums)
{
    // no need to check for empty array: precondition handles it
    ...
}</pre>""",
            "tip": "Questions ask \"which statement is a precondition?\" — look for what must be true of the <em>input</em> before calling. Postconditions describe the <em>result</em>. And when an FRQ states a precondition, don't waste time writing code to check it.",
            "questions": [
                {
                    "stem": "A method <code>getElement(int index)</code> is documented with \"Precondition: 0 <= index < size.\" Which of the following is true?",
                    "options": ["The method must check whether index is valid and throw an exception if not.", "The caller is responsible for ensuring index is valid before calling the method.", "The method will return -1 if index is invalid.", "The precondition is checked by the compiler."],
                    "answer": "B",
                    "explanation": "Preconditions are the caller's responsibility. The method assumes they hold.",
                },
                {
                    "stem": "Which of the following best describes a postcondition?",
                    "options": ["A requirement on the arguments passed to a method", "A statement about what is true after a method completes execution", "A comment that explains the algorithm used", "A run-time check inside the method"],
                    "answer": "B",
                    "explanation": "Postconditions describe the guaranteed state or result once the method finishes.",
                },
            ],
            "vocab": [
                ("Precondition", "a condition that must be true before a method is called"),
                ("Postcondition", "a condition guaranteed to be true after a method finishes"),
                ("Javadoc", "a /** */ comment used to document classes and methods"),
            ],
        },
        {
            "num": 9, "title": "Method Signatures", "blurb": "name + parameter list",
            "lede": "A method's signature is how Java knows which method you mean. Reading a signature tells you how to call it and what you get back.",
            "points": [
                "A <strong>method header</strong> looks like: <code>public static int max(int a, int b)</code> — access modifier, (optionally) <code>static</code>, <strong>return type</strong>, <strong>name</strong>, <strong>parameter list</strong>.",
                "The <strong>signature</strong> is the method name plus the parameter types, in order: <code>max(int, int)</code>. The return type is <em>not</em> part of the signature.",
                "<strong>Parameters</strong> are the variables in the header. <strong>Arguments</strong> are the values you pass in a call. They must match in number, order, and (compatible) type.",
                "<strong>Overloading:</strong> a class can have several methods with the same name if their parameter lists differ. Java picks the one whose parameters match the arguments.",
                "A method with return type <code>void</code> returns nothing and is called as a statement. A method with a non-void return type produces a value you can use in an expression.",
                "Passing an int where a double parameter is expected works (widening). Passing a double where an int is expected is a compile error.",
            ],
            "example": """
<pre class="code">public static double area(double radius)          // area(double)
public static double area(double w, double h)     // area(double, double)
public static void greet(String name)             // greet(String)

area(3);          // calls first: 3 widens to 3.0
area(4, 5);       // calls second
greet("Ram");     // fine; returns nothing
int x = greet("Ram");   // compile error: void has no value</pre>""",
            "tip": "To decide which overloaded method a call uses, count the arguments and match their types. When an FRQ gives you a method header to implement, copy it exactly — changing the return type or a parameter name costs points.",
            "questions": [
                {
                    "stem": "Given the header <code>public static int compute(int x, double y)</code>, which call will compile?",
                    "options": ["<code>compute(2.5, 3)</code>", "<code>compute(2, 3)</code>", "<code>compute(2)</code>", "<code>compute(\"2\", 3.0)</code>"],
                    "answer": "B",
                    "explanation": "The int 3 widens to double for y. Option A tries to pass a double for the int parameter, which doesn't compile.",
                },
                {
                    "stem": "Which of the following is part of a method's signature?",
                    "options": ["Its return type", "Its name and the types of its parameters", "The names of its parameters", "The body of the method"],
                    "answer": "B",
                    "explanation": "Signature = name + parameter types. Return type and parameter names aren't included.",
                },
            ],
            "vocab": [
                ("Method signature", "the method name and its parameter types in order"),
                ("Return type", "the type of value a method produces, or void"),
                ("Overloading", "multiple methods with the same name but different parameter lists"),
                ("Parameter", "a variable in a method header"),
                ("Argument", "a value passed to a method when it is called"),
            ],
        },
        {
            "num": 10, "title": "Calling Class Methods", "blurb": "static methods, ClassName.method()",
            "lede": "Class (static) methods belong to the class, not to an object. You call them with the class name, and the call transfers control until the method returns.",
            "points": [
                "A <strong>class method</strong> (or static method) is declared with <code>static</code> and called using the class name: <code>Math.abs(-3)</code>, <code>Integer.parseInt(\"42\")</code>.",
                "Inside the same class, a static method can be called by name alone: <code>helper(5)</code>.",
                "A method call <strong>transfers control</strong> to the method. When it hits a <code>return</code> statement (or the end of a void method), control comes back to the line after the call.",
                "If the method returns a value, the call expression <em>is</em> that value: <code>int m = Math.max(3, 9);</code> stores 9.",
                "A void method's call is a statement by itself. Using it in an expression is a compile error.",
                "Arguments are evaluated before the call; the parameter receives a <strong>copy</strong> of each argument's value.",
            ],
            "example": """
<pre class="code">public class Calc
{
    public static int square(int n)
    {
        return n * n;
    }
    public static void main(String[] args)
    {
        int r = square(4) + Calc.square(2);   // 16 + 4
        System.out.println(r);                // 20
    }
}</pre>""",
            "tip": "Trace method calls by writing down the line you're returning to, evaluating the method with the argument values, then substituting the return value back. Multiple calls on one line are evaluated left to right.",
            "questions": [
                {
                    "stem": "Consider the following method.\n<pre class=\"code\">public static int mystery(int a, int b)\n{\n    if (a &gt; b)\n    {\n        return a - b;\n    }\n    return b - a;\n}</pre>What is printed by <code>System.out.println(mystery(3, 8) + mystery(10, 4));</code>?",
                    "options": ["-1", "11", "1", "17"],
                    "answer": "B",
                    "explanation": "mystery(3, 8) → 8 - 3 = 5. mystery(10, 4) → 10 - 4 = 6. 5 + 6 = 11.",
                },
                {
                    "stem": "Which of the following correctly calls a static method <code>display</code> in class <code>Printer</code> that takes one String parameter and returns nothing?",
                    "options": ["<code>String s = Printer.display(\"hi\");</code>", "<code>Printer.display(\"hi\");</code>", "<code>Printer p = new Printer(); display(\"hi\");</code>", "<code>display.Printer(\"hi\");</code>"],
                    "answer": "B",
                    "explanation": "Static methods are called with ClassName.method(). A void method can't be assigned to a variable.",
                },
            ],
            "vocab": [
                ("Class method / static method", "a method that belongs to the class and is called with the class name"),
                ("Return statement", "ends the method and sends a value back to the caller"),
            ],
        },
        {
            "num": 11, "title": "Math Class", "blurb": "abs, pow, sqrt, random",
            "lede": "Five Math methods are on the reference sheet. Math.random is the one with a formula you must memorize.",
            "points": [
                "<code>Math.abs(x)</code> — absolute value; returns int for int input, double for double.",
                "<code>Math.pow(base, exp)</code> — base raised to exp; <em>always returns a double</em>, even <code>Math.pow(2, 3)</code> is <code>8.0</code>.",
                "<code>Math.sqrt(x)</code> — square root, returns a double.",
                "<code>Math.random()</code> — returns a double <strong>≥ 0.0 and &lt; 1.0</strong>. Never exactly 1.0.",
                "<strong>Random int in a range</strong> [low, high] inclusive: <code>(int) (Math.random() * (high - low + 1)) + low</code>. Number of possible values = high − low + 1.",
                "Example: die roll 1–6 is <code>(int) (Math.random() * 6) + 1</code>. Random 10–20: <code>(int) (Math.random() * 11) + 10</code>.",
                "All Math methods are static: always <code>Math.method(...)</code>, never <code>new Math()</code>.",
            ],
            "example": """
<pre class="code">int a = Math.abs(-7);                          // 7
double b = Math.pow(2, 10);                     // 1024.0
double c = Math.sqrt(2.25);                     // 1.5
int roll = (int) (Math.random() * 6) + 1;       // 1..6
int r = (int) (Math.random() * 50) + 25;        // 25..74 (50 values)
int wrong = (int) Math.random() * 6 + 1;        // always 1! cast binds first</pre>
<p>The last line is the classic error: <code>(int) Math.random()</code> is 0 before the multiplication happens.</p>""",
            "tip": "For \"which expression produces a random integer from a to b,\" check two things: the multiplier equals the count (b − a + 1), and the added value is a. For \"what range does this produce,\" the minimum is the added value and the maximum is that plus the multiplier minus one.",
            "questions": [
                {
                    "stem": "Which expression generates a random integer between 5 and 15, inclusive?",
                    "options": ["<code>(int) (Math.random() * 10) + 5</code>", "<code>(int) (Math.random() * 11) + 5</code>", "<code>(int) (Math.random() * 15) + 5</code>", "<code>(int) (Math.random() * 11) + 4</code>"],
                    "answer": "B",
                    "explanation": "15 - 5 + 1 = 11 possible values, so multiply by 11 and add the low value 5. Option A only reaches 14.",
                },
                {
                    "stem": "What is printed by <code>System.out.println(Math.pow(3, 2) + Math.abs(-4));</code>?",
                    "options": ["13", "13.0", "9.04", "A compile-time error"],
                    "answer": "B",
                    "explanation": "Math.pow returns a double (9.0). 9.0 + 4 = 13.0.",
                },
                {
                    "stem": "What range of values can <code>(int) (Math.random() * 4) * 2</code> produce?",
                    "options": ["0 to 8", "0, 2, 4, or 6", "1 to 8", "0 to 7"],
                    "answer": "B",
                    "explanation": "(int)(Math.random() * 4) is 0, 1, 2, or 3. Times 2 gives 0, 2, 4, 6.",
                },
            ],
            "vocab": [
                ("Math.random()", "returns a double in [0.0, 1.0)"),
                ("Math.pow(a, b)", "a raised to b, returned as a double"),
                ("Math.abs(x)", "absolute value"),
                ("Math.sqrt(x)", "square root as a double"),
            ],
        },
        {
            "num": 12, "title": "Objects: Instances of Classes", "blurb": "class vs. object, attributes and behaviors",
            "lede": "A class is a blueprint; an object is one thing built from it. This is the mental model for the whole second half of the course.",
            "points": [
                "A <strong>class</strong> defines a type: what data its objects hold (<strong>attributes</strong>, stored in instance variables) and what they can do (<strong>behaviors</strong>, defined by methods).",
                "An <strong>object</strong> is an <strong>instance</strong> of a class — one specific thing with its own values for the attributes. <code>\"hello\"</code> and <code>\"world\"</code> are two String objects.",
                "Objects are created with <code>new</code> (except String literals, which Java creates for you). Each <code>new</code> makes a separate object.",
                "The class's methods are the same for every object; the instance variable values differ. Two Student objects share the <code>getName()</code> method but have different names.",
                "<strong>Object-oriented programming</strong> models a program as objects interacting by calling each other's methods.",
                "A class can be used without seeing its code — you only need its API. That's the point of 1.7.",
            ],
            "example": """
<pre class="code">// Class: the blueprint (someone wrote this)
public class Dog
{
    private String name;
    private int age;
    // ... constructor and methods
}

// Objects: individual dogs built from the blueprint
Dog d1 = new Dog("Rex", 3);
Dog d2 = new Dog("Bo", 5);
// d1 and d2 are two instances with different attribute values</pre>""",
            "tip": "Class vs. object questions are definitional: class = template/type, object = one instance with specific values. \"How many objects are created\" = count the <code>new</code> keywords (plus string literals).",
            "questions": [
                {
                    "stem": "Which of the following best describes the relationship between a class and an object?",
                    "options": ["A class is an instance of an object.", "An object is an instance of a class, with its own attribute values.", "A class and an object are the same thing.", "An object contains multiple classes."],
                    "answer": "B",
                    "explanation": "The class is the blueprint; each object is one instance made from it.",
                },
                {
                    "stem": "How many objects are created by the following code?\n<pre class=\"code\">Dog a = new Dog(\"Max\", 2);\nDog b = new Dog(\"Max\", 2);\nDog c = a;</pre>",
                    "options": ["1", "2", "3", "0"],
                    "answer": "B",
                    "explanation": "Two new statements create two objects. Line 3 copies a reference — c points to the same object as a.",
                },
            ],
            "vocab": [
                ("Class", "a template that defines the attributes and behaviors of a type of object"),
                ("Object", "a specific instance of a class"),
                ("Attribute", "data stored in an object, held in instance variables"),
                ("Behavior", "what an object can do, defined by its methods"),
            ],
        },
        {
            "num": 13, "title": "Object Creation and Storage (Instantiation)", "blurb": "new, constructors, references, null",
            "lede": "new calls a constructor and returns a reference. Understanding that variables hold references — not objects — explains aliasing and every null crash.",
            "points": [
                "<code>ClassName var = new ClassName(args);</code> — <strong>instantiation</strong>. The <code>new</code> keyword allocates memory, runs the <strong>constructor</strong> with the arguments, and returns a <strong>reference</strong> to the new object.",
                "A <strong>constructor</strong> has the same name as the class and no return type. Constructors can be overloaded; the arguments determine which one runs.",
                "A reference variable stores an <strong>address</strong>, not the object. <code>Dog b = a;</code> makes <code>b</code> refer to the <em>same</em> object as <code>a</code> — this is called <strong>aliasing</strong>. Changing the object through <code>b</code> is visible through <code>a</code>.",
                "<code>null</code> is the value of a reference variable that doesn't refer to any object. Calling a method on a null reference throws a <strong>NullPointerException</strong> at run time.",
                "Instance variables of reference type default to <code>null</code> if not initialized; a declared local variable has no default and must be assigned before use.",
                "<code>==</code> on references compares <em>addresses</em>: true only if both refer to the same object. Two separate objects with identical contents are <code>!=</code>.",
            ],
            "example": """
<pre class="code">Dog a = new Dog("Rex", 3);
Dog b = a;              // alias: same object
Dog c = new Dog("Rex", 3);
Dog d = null;

b.setAge(4);
System.out.println(a.getAge());    // 4  — a and b share the object
System.out.println(a == b);        // true
System.out.println(a == c);        // false — different objects
d.getAge();                        // NullPointerException</pre>""",
            "tip": "Draw boxes and arrows. Each <code>new</code> is a box; each variable is an arrow. Assignment between reference variables re-points an arrow — it never copies a box. If an arrow points to nothing (null) and you call a method through it, the program crashes.",
            "questions": [
                {
                    "stem": "Consider the following code, where <code>Counter</code> has a method <code>increment()</code> that adds 1 to its count and <code>getCount()</code> that returns it.\n<pre class=\"code\">Counter x = new Counter();\nCounter y = x;\nx.increment();\ny.increment();\nSystem.out.println(x.getCount());</pre>What is printed?",
                    "options": ["0", "1", "2", "A compile-time error"],
                    "answer": "C",
                    "explanation": "x and y refer to the same Counter. Both increments apply to it, so the count is 2.",
                },
                {
                    "stem": "Which of the following will cause a NullPointerException at run time?",
                    "options": ["<code>String s = \"\"; int n = s.length();</code>", "<code>String s = null; int n = s.length();</code>", "<code>String s = \"abc\"; s = null;</code>", "<code>String s = null; s = \"abc\";</code>"],
                    "answer": "B",
                    "explanation": "Calling a method on a null reference throws NullPointerException. Assigning null (C, D) is fine; an empty String (A) is a valid object.",
                },
            ],
            "vocab": [
                ("Instantiation", "creating an object with new"),
                ("Constructor", "a special method that initializes a new object; same name as the class, no return type"),
                ("Reference", "the address of an object, stored in a reference variable"),
                ("Aliasing", "two reference variables referring to the same object"),
                ("null", "a reference value meaning 'no object'"),
                ("NullPointerException", "the run-time error from calling a method on null"),
            ],
        },
        {
            "num": 14, "title": "Calling Instance Methods", "blurb": "object.method(), accessors and mutators",
            "lede": "Instance methods operate on a specific object. The call syntax is object-dot-method, and the exam expects you to classify methods by what they do.",
            "points": [
                "<strong>Instance methods</strong> are called on an object: <code>obj.method(args)</code>. The method operates on that object's instance variables.",
                "An <strong>accessor</strong> (getter) returns information about the object's state without changing it: <code>getName()</code>, <code>length()</code>.",
                "A <strong>mutator</strong> (setter) changes the object's state; typically <code>void</code>: <code>setAge(5)</code>, <code>deposit(100)</code>.",
                "Method calls can be chained if each returns an object: <code>s.substring(1).toUpperCase()</code>.",
                "The dot operator on a null reference throws NullPointerException. The dot operator on a primitive doesn't compile (<code>int</code> has no methods).",
                "Calling a method with the wrong number or types of arguments, or calling a method the class doesn't have, is a compile-time error.",
            ],
            "example": """
<pre class="code">Account acct = new Account("Ram", 100.0);
acct.deposit(50.0);                 // mutator: changes balance
double b = acct.getBalance();       // accessor: 150.0
String who = acct.getOwner();       // accessor: "Ram"
acct.getBalance();                  // legal but pointless: value discarded</pre>""",
            "tip": "When a question gives you a class's method headers and asks what a code segment does, check each call: is it a mutator (state changed for later lines) or an accessor (value used now)? Track object state in a table just like variables.",
            "questions": [
                {
                    "stem": "A class <code>Temperature</code> has a method <code>public double getDegrees()</code> and a method <code>public void setDegrees(double d)</code>. Which of the following is true?",
                    "options": ["<code>getDegrees</code> is a mutator and <code>setDegrees</code> is an accessor.", "<code>getDegrees</code> is an accessor and <code>setDegrees</code> is a mutator.", "Both are accessors.", "Both are mutators."],
                    "answer": "B",
                    "explanation": "get returns state (accessor); set changes it (mutator).",
                },
                {
                    "stem": "Which of the following will not compile?",
                    "options": ["<code>String s = \"hi\"; int n = s.length();</code>", "<code>int x = 5; int n = x.length();</code>", "<code>String s = \"hi\"; String t = s.toUpperCase();</code>", "<code>String s = \"hi\"; boolean b = s.equals(\"hi\");</code>"],
                    "answer": "B",
                    "explanation": "Primitives have no methods. Calling .length() on an int is a compile-time error.",
                },
            ],
            "vocab": [
                ("Instance method", "a method called on an object that operates on that object's data"),
                ("Accessor", "a method that returns information about an object without modifying it"),
                ("Mutator", "a method that changes an object's state"),
            ],
        },
        {
            "num": 15, "title": "String Manipulation", "blurb": "substring, indexOf, equals, compareTo",
            "lede": "The single most-tested class on the exam. Know every method on the reference sheet and the three traps that account for most lost points.",
            "points": [
                "Strings are <strong>immutable</strong>: methods return a <em>new</em> String; the original never changes. <code>s.toUpperCase()</code> by itself does nothing unless you store the result.",
                "Indices start at <strong>0</strong>. The last character is at <code>length() - 1</code>.",
                "<code>length()</code> — number of characters. <code>substring(from, to)</code> — characters from index <code>from</code> up to but <strong>not including</strong> <code>to</code>. <code>substring(from)</code> — from that index to the end.",
                "<code>indexOf(str)</code> — index of the first occurrence, or <strong>−1</strong> if absent. <code>charAt</code> is <em>not</em> on the reference sheet; use <code>substring(i, i + 1)</code> to get one character as a String.",
                "<code>equals(other)</code> — true if contents match. <code>==</code> compares references and is <strong>wrong</strong> for comparing String contents.",
                "<code>compareTo(other)</code> — returns a negative int if this comes before other alphabetically, 0 if equal, positive if after. It's an int, never a boolean. Uppercase letters come before lowercase.",
                "Also available: <code>toUpperCase()</code>, <code>toLowerCase()</code>, and string concatenation with <code>+</code>. Concatenating anything with a String produces a String.",
                "A String literal with escape sequences: <code>\"\\\"quoted\\\"\"</code>, <code>\"line1\\nline2\"</code>.",
            ],
            "example": """
<pre class="code">String s = "Computer";
s.length();               // 8
s.substring(3, 6);        // "put"   (indices 3,4,5)
s.substring(5);           // "ter"
s.indexOf("put");         // 3
s.indexOf("z");           // -1
s.substring(0, 1);        // "C"  (one character)
"apple".compareTo("banana");    // negative
"Zebra".compareTo("apple");     // negative: 'Z' &lt; 'a'
s.equals("Computer");     // true
s == "Computer";          // unreliable — never use for content

s.toUpperCase();          // returns "COMPUTER" but s is still "Computer"
s = s.toUpperCase();      // now s is "COMPUTER"</pre>""",
            "tip": "Three checks on every String question: (1) substring's second index is exclusive — count characters from <code>from</code> to <code>to - 1</code>; (2) any content comparison must use <code>.equals</code>, never <code>==</code>; (3) <code>compareTo</code> gives an int, so <code>if (a.compareTo(b))</code> won't compile — you need <code>&lt; 0</code>, <code>== 0</code>, or <code>&gt; 0</code>.",
            "questions": [
                {
                    "stem": "What is printed by the following code?\n<pre class=\"code\">String w = \"programming\";\nSystem.out.println(w.substring(3, 7) + w.indexOf(\"g\"));</pre>",
                    "options": ["gram3", "gramm3", "gram10", "ram3"],
                    "answer": "A",
                    "explanation": "substring(3, 7) is indices 3–6: \"gram\". indexOf(\"g\") is the first g, at index 3. Concatenated: \"gram3\".",
                },
                {
                    "stem": "Which expression correctly checks whether the String <code>a</code> comes alphabetically before the String <code>b</code>?",
                    "options": ["<code>a &lt; b</code>", "<code>a.compareTo(b) &lt; 0</code>", "<code>a.compareTo(b)</code>", "<code>a.equals(b) &lt; 0</code>"],
                    "answer": "B",
                    "explanation": "compareTo returns a negative int when a precedes b. Strings can't be compared with <, and equals returns a boolean.",
                },
                {
                    "stem": "What is printed by the following code?\n<pre class=\"code\">String s = \"hello\";\ns.toUpperCase();\nSystem.out.println(s);</pre>",
                    "options": ["HELLO", "hello", "Hello", "A compile-time error"],
                    "answer": "B",
                    "explanation": "Strings are immutable. toUpperCase() returns a new String that was discarded; s is unchanged.",
                },
                {
                    "stem": "Which of the following returns the last character of a non-empty String <code>s</code> as a String?",
                    "options": ["<code>s.substring(s.length())</code>", "<code>s.substring(s.length() - 1)</code>", "<code>s.substring(s.length() - 1, s.length() - 1)</code>", "<code>s.charAt(s.length() - 1)</code>"],
                    "answer": "B",
                    "explanation": "substring(length - 1) returns from the last index to the end — one character. Option A returns an empty string; C returns empty (from == to); D returns a char, and charAt isn't on the reference sheet.",
                },
            ],
            "vocab": [
                ("Immutable", "cannot be changed; String methods return new Strings"),
                ("substring(a, b)", "characters from index a up to but not including b"),
                ("indexOf(str)", "index of the first occurrence, or -1 if not found"),
                ("equals", "compares String contents"),
                ("compareTo", "returns a negative, zero, or positive int based on alphabetical order"),
            ],
        },
    ],
}

# ----------------------------------------------------------------------
# UNIT 2 — Selection and Iteration (25–35%)
# ----------------------------------------------------------------------

U2 = {
    "num": 2,
    "title": "Selection and Iteration",
    "weight": "25–35%",
    "lede": "Conditionals and loops — the control flow that makes programs do something interesting. FRQ 1 (Methods and Control Structures) lives entirely here, and a large share of the multiple choice is tracing loops.",
    "understandings": [
        "Boolean expressions drive selection; compound conditions, short-circuit evaluation, and De Morgan's laws determine exactly which branch runs.",
        "while and for loops repeat code; the loop condition and update determine how many times.",
        "Standard algorithms — sum, count, max, string processing — are built from selection and iteration in predictable shapes.",
        "Nested loops multiply iterations, and informal run-time analysis counts statement executions.",
    ],
    "topics": [
        {
            "num": 1, "title": "Algorithms with Selection and Repetition", "blurb": "the three control structures",
            "lede": "Every algorithm is sequence, selection, and repetition. This topic names them and shows how they combine.",
            "points": [
                "<strong>Sequence:</strong> statements executed in order. <strong>Selection:</strong> a decision that chooses between paths (<code>if</code>). <strong>Repetition (iteration):</strong> a loop that repeats code (<code>while</code>, <code>for</code>).",
                "An algorithm can be described in words, in a flowchart, or in code. The same logic can be implemented several equivalent ways.",
                "Reading an algorithm: identify the initializations, what decisions are made, what repeats, and what's true when it stops.",
                "Tracing is the essential skill — a table with one column per variable and one row per executed statement or loop pass.",
                "Two algorithms are equivalent if they produce the same result for all inputs, even if the code differs.",
            ],
            "example": """
<pre class="code">int total = 0;                  // sequence
for (int i = 1; i &lt;= 5; i++)    // repetition
{
    if (i % 2 == 1)             // selection
    {
        total += i;
    }
}
// total is 1 + 3 + 5 = 9</pre>""",
            "tip": "Before tracing, write what each variable starts as. Then execute statements strictly in order. If a question describes an algorithm in English and asks which code implements it, translate the English into initializations, a loop, and a decision — then match.",
            "questions": [
                {
                    "stem": "Which control structure is demonstrated by the code segment <code>if (x &gt; 0) { count++; }</code>?",
                    "options": ["Sequence", "Selection", "Repetition", "Recursion"],
                    "answer": "B",
                    "explanation": "An if statement chooses whether to execute code — that's selection.",
                },
                {
                    "stem": "An algorithm should add up the even numbers from 2 to 10. Which of the following correctly does so?",
                    "options": ["<code>int s = 0; for (int i = 2; i &lt;= 10; i += 2) { s += i; }</code>", "<code>int s = 0; for (int i = 2; i &lt; 10; i += 2) { s += i; }</code>", "<code>int s = 0; for (int i = 1; i &lt;= 10; i++) { s += i; }</code>", "<code>int s = 2; for (int i = 2; i &lt;= 10; i++) { s += i; }</code>"],
                    "answer": "A",
                    "explanation": "Start at 2, step by 2, include 10. Option B stops at 8; C adds all numbers; D starts wrong and adds odds.",
                },
            ],
            "vocab": [
                ("Sequence", "statements executed one after another"),
                ("Selection", "choosing a path with a conditional"),
                ("Repetition", "repeating with a loop; also called iteration"),
            ],
        },
        {
            "num": 2, "title": "Boolean Expressions", "blurb": "relational operators, ==, !=",
            "lede": "Expressions that evaluate to true or false control everything in this unit. The == vs .equals distinction is where points are lost.",
            "points": [
                "<strong>Relational operators:</strong> <code>==</code>, <code>!=</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, <code>&gt;=</code>. They produce a boolean.",
                "<code>==</code> compares <em>values</em> for primitives and <em>references</em> for objects. To compare object contents (Strings especially) use <code>.equals()</code>.",
                "A boolean variable can hold the result: <code>boolean ok = score &gt;= 70;</code>. Then <code>if (ok)</code> — no need for <code>if (ok == true)</code>.",
                "Arithmetic is evaluated before relational operators: <code>x + 1 &gt; y * 2</code> computes both sides first.",
                "Comparing doubles with <code>==</code> is unreliable due to round-off; the exam usually avoids it or uses a tolerance.",
                "<code>!=</code> means \"not equal\"; for Strings, use <code>!a.equals(b)</code>.",
            ],
            "example": """
<pre class="code">int a = 5, b = 10;
boolean p = a * 2 == b;          // true
boolean q = a != b;              // true
String s1 = "hi";
String s2 = new String("hi");
boolean r = s1 == s2;            // false (different objects)
boolean t = s1.equals(s2);       // true  (same contents)</pre>""",
            "tip": "Any time a question compares two Strings with <code>==</code>, be suspicious. If both came from literals it may happen to be true, but the exam's intended answer is that <code>==</code> is not a reliable content comparison — <code>.equals</code> is.",
            "questions": [
                {
                    "stem": "Which of the following expressions correctly tests whether the String <code>name</code> holds the text \"Ram\"?",
                    "options": ["<code>name == \"Ram\"</code>", "<code>name.equals(\"Ram\")</code>", "<code>name = \"Ram\"</code>", "<code>name.compareTo(\"Ram\")</code>"],
                    "answer": "B",
                    "explanation": "equals compares contents. == compares references; = is assignment; compareTo returns an int, not a boolean.",
                },
                {
                    "stem": "What is the value of <code>x &gt; 3 == y &lt; 2</code> when <code>x = 5</code> and <code>y = 1</code>?",
                    "options": ["true", "false", "5", "A compile-time error"],
                    "answer": "A",
                    "explanation": "x > 3 is true; y < 2 is true; true == true is true. (Comparing booleans with == is legal.)",
                },
            ],
            "vocab": [
                ("Relational operator", "<, >, <=, >=, ==, != — compares two values and yields a boolean"),
                ("equals()", "compares object contents"),
            ],
        },
        {
            "num": 3, "title": "if Statements", "blurb": "if, if/else, one-way and two-way selection",
            "lede": "The if statement runs a block when a condition is true; adding else gives an alternative. Braces and semicolons cause more errors here than logic does.",
            "points": [
                "<code>if (condition) { statements }</code> — runs the block only when the condition is true. This is <strong>one-way selection</strong>.",
                "<code>if (condition) { A } else { B }</code> — runs exactly one of A or B. <strong>Two-way selection</strong>.",
                "The condition must be a boolean. <code>if (x)</code> where x is an int doesn't compile. <code>if (x = 5)</code> doesn't compile either (assignment isn't a boolean).",
                "Braces are optional for a single statement, but omitting them is a classic trap: only the <em>first</em> statement is controlled by the if. Always use braces.",
                "A semicolon right after the condition — <code>if (x &gt; 0);</code> — ends the if with an empty body, so the next block always runs.",
                "After the if/else completes, execution continues with the next statement regardless of which branch ran.",
            ],
            "example": """
<pre class="code">int score = 72;
if (score &gt;= 70)
    System.out.println("Pass");
    System.out.println("Congrats");   // NOT part of the if — always prints
if (score &gt; 90)
{
    System.out.println("Honors");
}
else
{
    System.out.println("Standard");
}
// Output: Pass  Congrats  Standard</pre>""",
            "tip": "Indentation means nothing to Java. When braces are missing, exactly one statement belongs to the if. The exam writes misleadingly-indented code on purpose; read braces, not spacing.",
            "questions": [
                {
                    "stem": "What is printed by the following code?\n<pre class=\"code\">int n = 4;\nif (n &gt; 5)\n    System.out.print(\"A\");\n    System.out.print(\"B\");\nSystem.out.print(\"C\");</pre>",
                    "options": ["C", "BC", "ABC", "AC"],
                    "answer": "B",
                    "explanation": "Without braces, only print(\"A\") is controlled by the if. \"B\" and \"C\" always print.",
                },
                {
                    "stem": "Which of the following will not compile?",
                    "options": ["<code>if (x &gt; 3) { y = 1; }</code>", "<code>if (x == 3) { y = 1; } else { y = 2; }</code>", "<code>if (x) { y = 1; }</code> where x is an int", "<code>if (x &gt; 3 == true) { y = 1; }</code>"],
                    "answer": "C",
                    "explanation": "The condition must be a boolean; an int isn't. Option D is legal, just redundant.",
                },
            ],
            "vocab": [
                ("One-way selection", "an if statement with no else"),
                ("Two-way selection", "an if statement with an else"),
            ],
        },
        {
            "num": 4, "title": "Nested if Statements", "blurb": "if inside if, else-if chains",
            "lede": "Conditionals inside conditionals build multi-way decisions. The skill is knowing which else belongs to which if.",
            "points": [
                "A <strong>nested if</strong> is an if statement inside another's block. The inner one runs only if the outer branch containing it runs.",
                "An <strong>else-if chain</strong> — <code>if / else if / else if / else</code> — tests conditions in order and runs the <em>first</em> true branch only. Later conditions are never checked once one matches.",
                "Order matters in an else-if chain. Testing <code>score &gt;= 70</code> before <code>score &gt;= 90</code> means 95 gets the 70 branch.",
                "A trailing <code>else</code> catches everything not matched above. Without it, it's possible no branch runs.",
                "The <strong>dangling else</strong>: with no braces, an else pairs with the <em>nearest</em> preceding if. Braces remove the ambiguity.",
                "Nested ifs can often be rewritten as compound conditions with <code>&amp;&amp;</code> (next topic); the exam asks which rewrite is equivalent.",
            ],
            "example": """
<pre class="code">int score = 85;
if (score &gt;= 90)
{
    grade = "A";
}
else if (score &gt;= 80)
{
    grade = "B";       // runs; the rest is skipped
}
else if (score &gt;= 70)
{
    grade = "C";
}
else
{
    grade = "F";
}</pre>
<p>Reverse the order (test 70 first) and 85 becomes a C. First true branch wins.</p>""",
            "tip": "Trace else-if chains top to bottom and stop at the first true condition. For nested ifs with no braces, an else attaches to the closest if above it — draw the braces in yourself before tracing.",
            "questions": [
                {
                    "stem": "What is printed by the following code when <code>x = 15</code>?\n<pre class=\"code\">if (x &gt; 5)\n{\n    if (x &gt; 20)\n    {\n        System.out.print(\"big\");\n    }\n    else\n    {\n        System.out.print(\"medium\");\n    }\n}\nelse\n{\n    System.out.print(\"small\");\n}</pre>",
                    "options": ["big", "medium", "small", "medium small"],
                    "answer": "B",
                    "explanation": "x > 5 is true (outer branch). Inside, x > 20 is false, so the inner else prints \"medium\". The outer else never runs.",
                },
                {
                    "stem": "Consider the following code.\n<pre class=\"code\">if (n &gt;= 10)\n    System.out.print(\"X\");\nelse if (n &gt;= 100)\n    System.out.print(\"Y\");\nelse\n    System.out.print(\"Z\");</pre>For which values of <code>n</code> is \"Y\" printed?",
                    "options": ["n ≥ 100", "n ≥ 10", "10 ≤ n < 100", "No value of n"],
                    "answer": "D",
                    "explanation": "Any n ≥ 100 is also ≥ 10, so the first branch catches it. The \"Y\" branch is unreachable.",
                },
            ],
            "vocab": [
                ("Nested if", "an if statement inside the block of another if"),
                ("else-if chain", "a series of conditions tested in order; only the first true one runs"),
                ("Dangling else", "an else that pairs with the nearest unbraced if"),
            ],
        },
        {
            "num": 5, "title": "Compound Boolean Expressions", "blurb": "&&, ||, !, short-circuit",
            "lede": "Combine conditions with && and ||, negate with !. Short-circuit evaluation is the concept that turns into exam questions.",
            "points": [
                "<code>!a</code> is true when a is false. <code>a &amp;&amp; b</code> is true only when both are true. <code>a || b</code> is true when at least one is.",
                "Precedence: <code>!</code> first, then <code>&amp;&amp;</code>, then <code>||</code>. Relational operators bind tighter than all three. Use parentheses to be safe.",
                "<strong>Short-circuit evaluation:</strong> for <code>a &amp;&amp; b</code>, if a is false, b is <em>never evaluated</em>. For <code>a || b</code>, if a is true, b is never evaluated.",
                "Short-circuiting prevents errors: <code>if (s != null &amp;&amp; s.length() &gt; 0)</code> is safe because the length call is skipped when s is null. Reversed, it would crash.",
                "Also prevents division by zero: <code>if (d != 0 &amp;&amp; n / d &gt; 2)</code>.",
                "Compound conditions can replace nested ifs: <code>if (a) { if (b) { ... } }</code> ≡ <code>if (a &amp;&amp; b) { ... }</code> when there are no else branches.",
                "<code>!(x &gt; 5)</code> is <code>x &lt;= 5</code> — the negation includes the boundary.",
            ],
            "example": """
<pre class="code">int age = 17;
boolean permit = true;
boolean canDrive = age &gt;= 16 &amp;&amp; permit;              // true
boolean discount = age &lt; 13 || age &gt;= 65;              // false
boolean neither = !(age &lt; 13 || age &gt;= 65);            // true

String s = null;
if (s != null &amp;&amp; s.length() &gt; 3)   // safe: second part skipped
{
    ...
}</pre>""",
            "tip": "For \"which condition is safe\" questions, the null or zero check must come <em>first</em> in an <code>&amp;&amp;</code>. For evaluation questions, compute each relational part to true/false, then apply ! → &amp;&amp; → ||.",
            "questions": [
                {
                    "stem": "For which values of <code>x</code> is <code>x &gt; 3 &amp;&amp; x &lt; 10 || x == 0</code> true?",
                    "options": ["Only x from 4 to 9", "x from 4 to 9, or x equal to 0", "Only x equal to 0", "x from 3 to 10"],
                    "answer": "B",
                    "explanation": "&& binds tighter than ||: (x > 3 && x < 10) || x == 0. That's 4–9, or 0.",
                },
                {
                    "stem": "Consider <code>if (arr.length &gt; 0 &amp;&amp; arr[0] == 5)</code>. Which best explains why this is safe even when <code>arr</code> has zero elements?",
                    "options": ["Java checks all array indices at compile time.", "Because of short-circuit evaluation, <code>arr[0]</code> is never evaluated when <code>arr.length &gt; 0</code> is false.", "<code>arr[0]</code> returns 0 for empty arrays.", "The condition always evaluates both parts, so it is not safe."],
                    "answer": "B",
                    "explanation": "&& stops as soon as the left side is false, so the out-of-bounds access never happens.",
                },
            ],
            "vocab": [
                ("&& (and)", "true only when both operands are true"),
                ("|| (or)", "true when at least one operand is true"),
                ("! (not)", "negates a boolean"),
                ("Short-circuit evaluation", "the right operand of && or || is skipped when the left operand decides the result"),
            ],
        },
        {
            "num": 6, "title": "Comparing Boolean Expressions", "blurb": "equivalence, De Morgan's laws",
            "lede": "Two conditions can look different and mean the same thing. The exam asks which is equivalent — De Morgan's laws and truth tables are how you answer.",
            "points": [
                "Boolean expressions are <strong>equivalent</strong> if they evaluate to the same value for every possible input.",
                "<strong>De Morgan's laws:</strong> <code>!(a &amp;&amp; b)</code> ≡ <code>!a || !b</code>; <code>!(a || b)</code> ≡ <code>!a &amp;&amp; !b</code>. Negating flips the operator and negates each part.",
                "Negating a comparison flips it to include the boundary: <code>!(x &lt; 5)</code> ≡ <code>x &gt;= 5</code>; <code>!(x == y)</code> ≡ <code>x != y</code>.",
                "A <strong>truth table</strong> lists every combination of inputs and the result — the reliable way to prove equivalence when reasoning gets confusing.",
                "Simplifications: <code>a == true</code> ≡ <code>a</code>; <code>a == false</code> ≡ <code>!a</code>; <code>!!a</code> ≡ <code>a</code>.",
                "Two if/else structures are equivalent if every input takes the same action, regardless of how the conditions are written.",
            ],
            "example": """
<p>Is <code>!(x &gt; 10 || y &lt;= 0)</code> equivalent to <code>x &lt;= 10 &amp;&amp; y &gt; 0</code>?</p>
<p>De Morgan: <code>!(A || B)</code> = <code>!A &amp;&amp; !B</code>. <code>!(x &gt; 10)</code> = <code>x &lt;= 10</code>. <code>!(y &lt;= 0)</code> = <code>y &gt; 0</code>. So yes. Check one case: x = 3, y = 4 → original: !(false || false) = true; rewrite: true &amp;&amp; true = true. ✓</p>""",
            "tip": "Apply De Morgan mechanically: flip the operator, negate each side, and flip each comparison to its boundary-inclusive opposite. Then test one or two values. Options that negate the parts but keep the same &amp;&amp;/|| are the standard distractor.",
            "questions": [
                {
                    "stem": "Which expression is equivalent to <code>!(a &lt; 3 &amp;&amp; b != 7)</code>?",
                    "options": ["<code>a &gt;= 3 || b == 7</code>", "<code>a &gt;= 3 &amp;&amp; b == 7</code>", "<code>a &gt; 3 || b == 7</code>", "<code>a &lt; 3 || b != 7</code>"],
                    "answer": "A",
                    "explanation": "De Morgan: !(A && B) = !A || !B. !(a < 3) = a >= 3; !(b != 7) = b == 7.",
                },
                {
                    "stem": "Which of the following is equivalent to the code segment below?\n<pre class=\"code\">if (x &gt; 0)\n{\n    if (y &gt; 0)\n    {\n        return true;\n    }\n}\nreturn false;</pre>",
                    "options": ["<code>return x &gt; 0 || y &gt; 0;</code>", "<code>return x &gt; 0 &amp;&amp; y &gt; 0;</code>", "<code>return !(x &gt; 0 &amp;&amp; y &gt; 0);</code>", "<code>return x &gt; 0;</code>"],
                    "answer": "B",
                    "explanation": "true is returned only when both are positive — that's &&.",
                },
            ],
            "vocab": [
                ("Equivalent expressions", "expressions with the same value for all inputs"),
                ("De Morgan's laws", "rules for negating && and || expressions"),
                ("Truth table", "a table of all input combinations and their resulting values"),
            ],
        },
        {
            "num": 7, "title": "while Loops", "blurb": "condition-controlled repetition",
            "lede": "A while loop repeats as long as its condition is true. The exam asks how many iterations happen and what the variables hold when it stops.",
            "points": [
                "<code>while (condition) { body }</code> — the condition is checked <em>before</em> each iteration. If it's false initially, the body runs zero times.",
                "Something in the body must eventually make the condition false, or the loop is <strong>infinite</strong>.",
                "Typical structure: initialize before the loop; test; body; update. Forgetting the update is the classic infinite loop.",
                "After the loop, variables keep their final values. If a loop runs while <code>i &lt; 5</code> incrementing i, then <code>i</code> is 5 afterward.",
                "while loops are the choice when the number of iterations isn't known in advance (reading input until a sentinel, searching until found).",
                "An <code>if</code> inside a while with a <code>return</code> is a common way to exit a search loop early.",
            ],
            "example": """
<pre class="code">int n = 20;
int count = 0;
while (n &gt; 1)
{
    n = n / 2;
    count++;
}
System.out.println(n + " " + count);</pre>
<table class="trace"><tr><th>check n &gt; 1</th><th>n after</th><th>count</th></tr>
<tr><td>20: true</td><td>10</td><td>1</td></tr>
<tr><td>10: true</td><td>5</td><td>2</td></tr>
<tr><td>5: true</td><td>2</td><td>3</td></tr>
<tr><td>2: true</td><td>1</td><td>4</td></tr>
<tr><td>1: false → exit</td><td></td><td></td></tr></table>
<p>Output: <strong>1 4</strong>.</p>""",
            "tip": "Always trace with a table and include a row for the final failed check — that's where students stop one iteration early or late. And check whether the condition is true at the start; \"zero iterations\" is a real answer choice.",
            "questions": [
                {
                    "stem": "How many times is \"x\" printed?\n<pre class=\"code\">int k = 3;\nwhile (k &lt; 12)\n{\n    System.out.print(\"x\");\n    k += 4;\n}</pre>",
                    "options": ["2", "3", "4", "0"],
                    "answer": "B",
                    "explanation": "k = 3 (print), 7 (print), 11 (print), 15 (stop). Three times.",
                },
                {
                    "stem": "What is the value of <code>i</code> after the following loop?\n<pre class=\"code\">int i = 0;\nwhile (i * i &lt; 50)\n{\n    i++;\n}</pre>",
                    "options": ["7", "8", "49", "50"],
                    "answer": "B",
                    "explanation": "7 * 7 = 49 < 50, so i becomes 8. 8 * 8 = 64 is not < 50, so the loop stops with i = 8.",
                },
                {
                    "stem": "Which of the following loops runs forever?",
                    "options": ["<code>int x = 10; while (x &gt; 0) { x -= 3; }</code>", "<code>int x = 1; while (x != 10) { x += 2; }</code>", "<code>int x = 0; while (x &lt; 5) { x++; }</code>", "<code>int x = 8; while (x &gt; 1) { x /= 2; }</code>"],
                    "answer": "B",
                    "explanation": "x takes odd values 1, 3, 5, 7, 9, 11, … and never equals 10.",
                },
            ],
            "vocab": [
                ("while loop", "repeats its body as long as the condition is true; condition checked first"),
                ("Infinite loop", "a loop whose condition never becomes false"),
                ("Sentinel", "a special input value that signals a loop to stop"),
            ],
        },
        {
            "num": 8, "title": "for Loops", "blurb": "init; condition; update",
            "lede": "The for loop packages initialization, condition, and update into one header. It's equivalent to a while loop, and the exam expects you to convert between them.",
            "points": [
                "<code>for (init; condition; update) { body }</code>. Execution: init once → check condition → body → update → check condition → … until the condition is false.",
                "A variable declared in the init (<code>int i = 0</code>) exists <strong>only inside the loop</strong>. Using it after the loop is a compile error.",
                "<code>for (int i = 0; i &lt; n; i++)</code> runs exactly n times, i = 0 through n−1. <code>i &lt;= n</code> runs n + 1 times.",
                "Number of iterations for <code>i = a; i &lt; b; i++</code> is b − a (if b &gt; a). For <code>i &lt;= b</code>, it's b − a + 1.",
                "The update can be anything: <code>i += 2</code>, <code>i--</code>, <code>i *= 2</code>. Counting down: <code>for (int i = 10; i &gt; 0; i--)</code>.",
                "Any for loop can be rewritten as a while loop by moving the init above and the update to the end of the body. The difference: scope of the loop variable.",
                "Modifying the loop variable inside the body is legal but confusing and a source of trick questions.",
            ],
            "example": """
<pre class="code">for (int i = 2; i &lt;= 10; i += 3)
{
    System.out.print(i + " ");
}
// prints: 2 5 8
// i would be 11 after, but i doesn't exist outside the loop

// equivalent while loop:
int i = 2;
while (i &lt;= 10)
{
    System.out.print(i + " ");
    i += 3;
}
System.out.println(i);   // 11 — i is in scope here</pre>""",
            "tip": "Count iterations by listing the loop variable's values: start, add the step until the condition fails. Don't compute a formula unless the step is 1. And remember: <code>&lt;</code> vs <code>&lt;=</code> is one full extra iteration.",
            "questions": [
                {
                    "stem": "What is printed by the following code?\n<pre class=\"code\">for (int i = 10; i &gt; 0; i -= 4)\n{\n    System.out.print(i + \" \");\n}</pre>",
                    "options": ["10 6 2", "10 6 2 -2", "10 6", "6 2"],
                    "answer": "A",
                    "explanation": "10 (print), 6 (print), 2 (print), -2 fails i > 0.",
                },
                {
                    "stem": "How many times does the body of <code>for (int j = 3; j &lt;= 15; j++)</code> execute?",
                    "options": ["12", "13", "15", "14"],
                    "answer": "B",
                    "explanation": "j takes values 3 through 15 inclusive: 15 - 3 + 1 = 13.",
                },
                {
                    "stem": "Which of the following will cause a compile-time error?",
                    "options": ["<code>for (int i = 0; i &lt; 3; i++) { } System.out.println(i);</code>", "<code>int i; for (i = 0; i &lt; 3; i++) { } System.out.println(i);</code>", "<code>for (int i = 3; i &gt; 0; i--) { System.out.println(i); }</code>", "<code>for (int i = 0; i &lt; 10; i += 3) { }</code>"],
                    "answer": "A",
                    "explanation": "i declared in the for header is out of scope after the loop. Option B declares it outside, so it's fine.",
                },
            ],
            "vocab": [
                ("for loop", "a loop with initialization, condition, and update in its header"),
                ("Loop variable", "the counter declared in the for header; scoped to the loop"),
                ("Scope", "the region of code where a variable can be used"),
            ],
        },
        {
            "num": 9, "title": "Implementing Selection and Iteration Algorithms", "blurb": "standard patterns: sum, count, max, digits",
            "lede": "The CED lists specific algorithms you should be able to write and recognize. These are the shapes FRQ 1 is built from.",
            "points": [
                "<strong>Named algorithms the CED expects:</strong> compute a sum or average; count values meeting a condition; find the minimum or maximum; check whether a number is even/odd or divisible; compute the digits of an integer; determine whether a number is prime; find the frequency of a condition.",
                "<strong>Sum/count pattern:</strong> initialize to 0 before the loop, update inside. Average = sum ÷ count, cast to double if needed.",
                "<strong>Max/min pattern:</strong> initialize to the first value (or an extreme like <code>Integer.MIN_VALUE</code>), compare each value, replace if better.",
                "<strong>Digit extraction:</strong> <code>n % 10</code> is the last digit; <code>n / 10</code> removes it. Loop while <code>n &gt; 0</code>.",
                "<strong>Divisibility:</strong> <code>a % b == 0</code>. <strong>Prime:</strong> loop from 2 to n−1 (or √n) checking for a divisor; if none, prime.",
                "<strong>Early exit:</strong> a <code>return</code> inside the loop ends the method at the first match — used in \"is there any…\" checks.",
            ],
            "example": """
<pre class="code">// sum of the digits of a positive int
public static int digitSum(int n)
{
    int sum = 0;
    while (n &gt; 0)
    {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}
// digitSum(4712): 2, then 1, then 7, then 4 → 14

// is n prime?
public static boolean isPrime(int n)
{
    if (n &lt; 2) return false;
    for (int d = 2; d &lt; n; d++)
    {
        if (n % d == 0) return false;
    }
    return true;
}</pre>""",
            "tip": "On FRQ 1, the rubric gives separate points for the loop, the condition, the update, and the return. Even if the logic isn't perfect, a correctly structured loop with the right variable initialized earns credit. Write the skeleton first, then fill in the condition.",
            "questions": [
                {
                    "stem": "What does the following method return when called with <code>n = 3407</code>?\n<pre class=\"code\">public static int mystery(int n)\n{\n    int count = 0;\n    while (n &gt; 0)\n    {\n        if (n % 10 % 2 == 1)\n        {\n            count++;\n        }\n        n /= 10;\n    }\n    return count;\n}</pre>",
                    "options": ["2", "3", "4", "14"],
                    "answer": "A",
                    "explanation": "It counts odd digits. Digits 7, 0, 4, 3: odd ones are 7 and 3 → 2.",
                },
                {
                    "stem": "The following code is intended to find the largest value among <code>a</code>, <code>b</code>, and <code>c</code>.\n<pre class=\"code\">int max = 0;\nif (a &gt; max) max = a;\nif (b &gt; max) max = b;\nif (c &gt; max) max = c;</pre>For which inputs does it give the wrong answer?",
                    "options": ["When all three are positive", "When all three are negative", "When two values are equal", "It is always correct"],
                    "answer": "B",
                    "explanation": "If all values are negative, none exceed 0, so max stays 0 — wrong. Initialize to a first value instead.",
                },
            ],
            "vocab": [
                ("Accumulator", "a variable that collects a running total or count across iterations"),
                ("Digit extraction", "using % 10 and / 10 to process an integer's digits"),
            ],
        },
        {
            "num": 10, "title": "Implementing String Algorithms", "blurb": "loop over characters, count, reverse, find substrings",
            "lede": "Combine loops with substring and indexOf to process text. FRQs love \"count how many times,\" \"reverse,\" and \"find all occurrences.\"",
            "points": [
                "Iterate over characters with <code>for (int i = 0; i &lt; s.length(); i++)</code> and get each one as a String: <code>s.substring(i, i + 1)</code>.",
                "<strong>Named algorithms:</strong> count occurrences of a substring; find all positions of a substring; reverse a String; check for a palindrome; build a new String from selected characters.",
                "<strong>Counting substrings:</strong> loop i from 0 to <code>s.length() - sub.length()</code> (inclusive) and check <code>s.substring(i, i + sub.length()).equals(sub)</code>. The upper bound prevents an out-of-bounds substring call.",
                "<strong>Reverse:</strong> start with an empty String and prepend each character: <code>rev = s.substring(i, i + 1) + rev;</code>",
                "<strong>Building a String:</strong> start with <code>\"\"</code> and concatenate. Strings are immutable, so you're creating a new one each time — fine at exam scale.",
                "<code>indexOf</code> finds the <em>first</em> occurrence only. To find all, loop or use <code>substring</code> to search the remainder.",
            ],
            "example": """
<pre class="code">// count occurrences of sub in s (overlapping allowed)
public static int countOf(String s, String sub)
{
    int count = 0;
    for (int i = 0; i &lt;= s.length() - sub.length(); i++)
    {
        if (s.substring(i, i + sub.length()).equals(sub))
        {
            count++;
        }
    }
    return count;
}
// countOf("banana", "ana") → 2 (indices 1 and 3)

// reverse
String rev = "";
for (int i = 0; i &lt; s.length(); i++)
{
    rev = s.substring(i, i + 1) + rev;
}</pre>""",
            "tip": "The loop bound for substring searching is <code>i &lt;= s.length() - sub.length()</code> — get that off by one and you either miss the last match or throw an exception. Always use <code>.equals</code> inside the loop, never <code>==</code>.",
            "questions": [
                {
                    "stem": "What is printed by the following code?\n<pre class=\"code\">String s = \"abcde\";\nString r = \"\";\nfor (int i = 0; i &lt; s.length(); i += 2)\n{\n    r = s.substring(i, i + 1) + r;\n}\nSystem.out.println(r);</pre>",
                    "options": ["ace", "eca", "abcde", "edcba"],
                    "answer": "B",
                    "explanation": "i = 0, 2, 4 gives a, c, e; each is prepended: \"a\", \"ca\", \"eca\".",
                },
                {
                    "stem": "The method below is intended to return true if <code>s</code> contains the substring <code>\"ab\"</code>. Which loop condition is correct?\n<pre class=\"code\">for (int i = 0; /* condition */ ; i++)\n{\n    if (s.substring(i, i + 2).equals(\"ab\")) return true;\n}\nreturn false;</pre>",
                    "options": ["<code>i &lt; s.length()</code>", "<code>i &lt;= s.length()</code>", "<code>i &lt; s.length() - 1</code>", "<code>i &lt; s.length() - 2</code>"],
                    "answer": "C",
                    "explanation": "substring(i, i + 2) needs i + 2 ≤ length, so i ≤ length - 2, i.e., i < length - 1. Option A throws an exception on the last iteration; D misses a match at the end.",
                },
            ],
            "vocab": [
                ("Palindrome", "a String that reads the same forward and backward"),
                ("Substring search", "checking each window of a String against a target"),
            ],
        },
        {
            "num": 11, "title": "Nested Iteration", "blurb": "loops inside loops",
            "lede": "The inner loop runs completely for each pass of the outer loop. Count total iterations, and read the loop bounds carefully when the inner depends on the outer.",
            "points": [
                "In nested loops, the <strong>inner loop runs to completion</strong> every time the outer loop's body executes.",
                "Total body executions = (outer iterations) × (inner iterations) when the inner bounds are fixed.",
                "When the inner bound depends on the outer variable (<code>for (int j = 0; j &lt; i; j++)</code>), the count is a sum: 0 + 1 + 2 + … — triangular numbers.",
                "Output questions: track which loop controls rows vs. columns. A <code>println</code> after the inner loop ends the line.",
                "Nested loops are how you compare every pair of elements, print grids, or process 2D data (Unit 4).",
                "A <code>return</code> exits <em>both</em> loops (and the method). A <code>break</code> is not tested on the exam.",
            ],
            "example": """
<pre class="code">for (int r = 1; r &lt;= 3; r++)
{
    for (int c = 1; c &lt;= r; c++)
    {
        System.out.print("*");
    }
    System.out.println();
}
// *
// **
// ***
// Total stars: 1 + 2 + 3 = 6</pre>""",
            "tip": "Write the outer variable's value in the margin, then list the inner loop's values for that pass. Don't try to hold both counters in your head. For \"how many times\" with a dependent inner loop, write out the sum explicitly.",
            "questions": [
                {
                    "stem": "How many times is \"hi\" printed?\n<pre class=\"code\">for (int i = 0; i &lt; 4; i++)\n{\n    for (int j = 0; j &lt; 3; j++)\n    {\n        System.out.println(\"hi\");\n    }\n}</pre>",
                    "options": ["7", "12", "3", "4"],
                    "answer": "B",
                    "explanation": "4 outer × 3 inner = 12.",
                },
                {
                    "stem": "How many times is <code>count++</code> executed?\n<pre class=\"code\">for (int i = 1; i &lt;= 4; i++)\n{\n    for (int j = i; j &lt;= 4; j++)\n    {\n        count++;\n    }\n}</pre>",
                    "options": ["16", "10", "6", "4"],
                    "answer": "B",
                    "explanation": "i = 1: j runs 1–4 (4 times). i = 2: 3 times. i = 3: 2. i = 4: 1. Total 4 + 3 + 2 + 1 = 10.",
                },
                {
                    "stem": "What is printed by the following code?\n<pre class=\"code\">for (int i = 1; i &lt;= 2; i++)\n{\n    for (int j = 1; j &lt;= 3; j++)\n    {\n        System.out.print(i * j + \" \");\n    }\n}</pre>",
                    "options": ["1 2 3 2 4 6", "1 2 3 4 5 6", "1 2 2 4 3 6", "1 1 2 2 3 3"],
                    "answer": "A",
                    "explanation": "i = 1: 1 2 3. i = 2: 2 4 6.",
                },
            ],
            "vocab": [
                ("Nested loop", "a loop inside the body of another loop"),
                ("Inner loop", "the loop that runs to completion on each pass of the outer"),
            ],
        },
        {
            "num": 12, "title": "Informal Run-Time Analysis", "blurb": "counting statement executions",
            "lede": "Not Big-O — the exam asks you to count how many times a statement executes, and to compare two code segments by that count.",
            "points": [
                "<strong>Statement execution count</strong> is the number of times a particular statement runs. It's the exam's measure of efficiency.",
                "A single loop of n iterations executes its body n times. Nested loops multiply. Sequential loops add.",
                "Comparing algorithms: fewer executions for the same input size = more efficient. The exam gives two versions and asks which is better or by how much.",
                "Loops that halve their range each time (binary search) run about log₂ n times; loops that check every element run n times; comparing all pairs runs about n².",
                "Early exit (return when found) reduces the count in the best case but not the worst.",
                "The count can depend on the input, not just its size: searching for the first element takes 1 step; the last takes n.",
            ],
            "example": """
<pre class="code">// Version A
for (int i = 0; i &lt; n; i++)
{
    for (int j = 0; j &lt; n; j++)
    {
        count++;                // runs n * n times
    }
}
// Version B
for (int i = 0; i &lt; n; i++)
{
    count++;                    // runs n times
}
for (int j = 0; j &lt; n; j++)
{
    count++;                    // runs n times
}
// B runs 2n times total. For n = 100: A = 10,000, B = 200.</pre>""",
            "tip": "Read the loop headers, not the bodies. Nested with independent bounds → multiply. Nested with dependent bound → triangular sum (n(n+1)/2). Two loops in sequence → add. A question asking \"how many times is the statement executed when n = 5\" wants a number, so compute it.",
            "questions": [
                {
                    "stem": "How many times is <code>sum++</code> executed when <code>n = 6</code>?\n<pre class=\"code\">for (int i = 0; i &lt; n; i++)\n{\n    for (int j = 0; j &lt; n; j += 2)\n    {\n        sum++;\n    }\n}</pre>",
                    "options": ["12", "18", "36", "9"],
                    "answer": "B",
                    "explanation": "Outer: 6 iterations. Inner: j = 0, 2, 4 → 3 iterations. 6 × 3 = 18.",
                },
                {
                    "stem": "Two methods search a list of n items for a value. Method X checks every item and returns the count of matches. Method Y returns true as soon as the first match is found. Which statement is true about their execution counts?",
                    "options": ["Y always executes fewer statements than X.", "X always executes n comparisons; Y executes between 1 and n depending on where the match is.", "X and Y always execute the same number of statements.", "Y always executes exactly 1 comparison."],
                    "answer": "B",
                    "explanation": "X has no early exit. Y's count depends on the data — best case 1, worst case n.",
                },
            ],
            "vocab": [
                ("Statement execution count", "how many times a statement runs; the exam's measure of efficiency"),
                ("Run-time analysis", "estimating an algorithm's work as a function of input size"),
            ],
        },
    ],
}

# ----------------------------------------------------------------------
# UNIT 3 — Class Creation (10–18%)
# ----------------------------------------------------------------------

U3 = {
    "num": 3,
    "title": "Class Creation",
    "weight": "10–18%",
    "lede": "Writing your own classes: instance variables, constructors, methods, static members, scope, and this. FRQ 2 (Class Design) asks you to write an entire class from a description — every topic here is a rubric point.",
    "understandings": [
        "A class bundles data (private instance variables) with the methods that operate on it; encapsulation hides the data behind public methods.",
        "Constructors initialize objects; methods take parameters, may return values, and can modify objects passed by reference.",
        "Static members belong to the class rather than any object; scope determines which variables are visible where.",
        "Program design choices have impact on people, including privacy and accessibility.",
    ],
    "topics": [
        {
            "num": 1, "title": "Abstraction and Program Design", "blurb": "data and procedural abstraction, designing classes",
            "lede": "Before writing a class, decide what it represents and what it should be able to do. Abstraction is the discipline of hiding everything else.",
            "points": [
                "<strong>Abstraction</strong> means focusing on what something does and hiding how. <strong>Data abstraction</strong>: representing a concept as a class with attributes. <strong>Procedural abstraction</strong>: a method's name and header stand in for its implementation.",
                "Designing a class: identify the <strong>attributes</strong> (what it needs to remember — become instance variables) and the <strong>behaviors</strong> (what it needs to do — become methods).",
                "<strong>Encapsulation</strong> keeps instance variables <code>private</code> and exposes controlled access through <code>public</code> methods. Outside code can't corrupt the object's state.",
                "Breaking a program into classes and methods makes it easier to write, test, debug, and reuse — the same reasoning as for procedures.",
                "A class should represent one clear concept. Its public methods are its API to the rest of the program.",
                "Design happens before code: reading an FRQ 2 prompt, list attributes and behaviors first, then write.",
            ],
            "example": """
<p>Prompt: \"Write a class representing a bank account with an owner, a balance, deposits, withdrawals that can't overdraw, and a way to get the balance.\"</p>
<ul class="points">
<li><strong>Attributes:</strong> owner (String), balance (double) → private instance variables.</li>
<li><strong>Behaviors:</strong> deposit(amount), withdraw(amount) returning whether it succeeded, getBalance() → public methods.</li>
<li><strong>Constructor:</strong> takes owner and starting balance.</li>
</ul>
<p>That outline <em>is</em> the design. The code follows in 3.3–3.5.</p>""",
            "tip": "On FRQ 2, underline every noun that's a piece of state (becomes an instance variable) and every verb (becomes a method). The prompt tells you the class's design; your job is to translate it faithfully, not invent extras.",
            "questions": [
                {
                    "stem": "A programmer designs a <code>Playlist</code> class with a private list of songs and public methods <code>addSong</code>, <code>removeSong</code>, and <code>getSongCount</code>. Which of the following best describes this design choice?",
                    "options": ["Encapsulation: the data is hidden and accessed only through public methods.", "Inheritance: the class extends another class.", "Recursion: the methods call themselves.", "Overloading: the methods share a name."],
                    "answer": "A",
                    "explanation": "Private data with public methods controlling access is encapsulation.",
                },
                {
                    "stem": "Which of the following is an example of procedural abstraction?",
                    "options": ["Storing a student's grades in a private array", "Calling <code>Math.sqrt(x)</code> without knowing the algorithm it uses", "Declaring an instance variable as private", "Creating two objects from the same class"],
                    "answer": "B",
                    "explanation": "Using a method by its interface without knowing its implementation is procedural abstraction. Option A is data abstraction.",
                },
            ],
            "vocab": [
                ("Data abstraction", "modeling a concept as a class with attributes"),
                ("Procedural abstraction", "using a method without knowing its implementation"),
                ("Encapsulation", "keeping data private and controlling access through public methods"),
            ],
        },
        {
            "num": 2, "title": "Impact of Program Design", "blurb": "ethics, privacy, accessibility",
            "lede": "The CED's ethics topic for this unit: design decisions affect people. Short, but it appears on the exam.",
            "points": [
                "Programs are used by people, and design decisions can help or harm them. Programmers have a responsibility to consider effects on <strong>all</strong> potential users.",
                "<strong>Privacy:</strong> deciding what data to store, how long, and who can access it is a design choice. Storing less is safer.",
                "<strong>Security:</strong> keeping data private (encapsulation) and validating inputs reduces the chance of misuse.",
                "<strong>Accessibility and inclusion:</strong> programs should work for people with disabilities and across different devices, languages, and contexts. Assuming every user is like the developer produces exclusion.",
                "<strong>Bias:</strong> a program's logic and data can embed assumptions that treat groups unfairly; testing with diverse inputs and users helps surface it.",
                "Legal and ethical obligations include respecting intellectual property (citing code you use) and not collecting data without consent.",
                "These considerations apply during design, not as an afterthought.",
            ],
            "example": """
<p>A class <code>UserProfile</code> stores name, email, and — because it was convenient — full date of birth and home address, all with public getters. Reconsidered: date of birth is only needed to check age, so store a boolean <code>isAdult</code> instead; make the address private with no getter since nothing needs it. Same functionality, far less exposure if the data leaks. That's design impact.</p>""",
            "tip": "Questions here are scenario-based and the right answer usually involves collecting less data, validating before storing, considering users unlike the developer, or getting consent. Options that maximize data collection \"just in case\" are wrong.",
            "questions": [
                {
                    "stem": "A developer is designing a class to store user information for a fitness app. Which of the following is the most responsible design decision regarding user data?",
                    "options": ["Store every piece of data the user could possibly provide, in case it is useful later.", "Store only the data the app needs to function, and keep it private with controlled access.", "Make all instance variables public so other classes can access them easily.", "Share the data with third parties to improve the app."],
                    "answer": "B",
                    "explanation": "Minimizing collected data and encapsulating it protects privacy and security.",
                },
                {
                    "stem": "Which of the following best describes why a programmer should test a program with a diverse group of users?",
                    "options": ["To make the program run faster", "To discover assumptions in the design that exclude or disadvantage some users", "To reduce the number of classes", "To avoid needing documentation"],
                    "answer": "B",
                    "explanation": "Diverse testing surfaces bias and accessibility problems that the developer's own perspective misses.",
                },
            ],
            "vocab": [
                ("Data minimization", "collecting and storing only the data a program actually needs"),
                ("Accessibility", "designing so people with disabilities and varied contexts can use the program"),
            ],
        },
        {
            "num": 3, "title": "Anatomy of a Class", "blurb": "instance variables, private/public, structure",
            "lede": "The parts of a class in the order the exam expects them, and the access modifiers that make encapsulation work.",
            "points": [
                "A class declaration: <code>public class Name { ... }</code>. Inside, in conventional order: <strong>instance variables</strong>, <strong>constructors</strong>, <strong>methods</strong>.",
                "<strong>Instance variables</strong> hold each object's state. Declare them <code>private</code>: <code>private String name;</code> Each object gets its own copy.",
                "<code>private</code> members are accessible only inside the class. <code>public</code> members are accessible from anywhere. The exam expects private instance variables and public methods/constructors.",
                "Instance variables have <strong>default values</strong> if not initialized: 0 for int, 0.0 for double, false for boolean, <code>null</code> for references. Local variables have no defaults.",
                "Accessing a private variable from outside the class (<code>obj.name</code>) is a compile-time error. Use an accessor method instead.",
                "The class's data type name is the class name; you can declare variables of that type: <code>Student s;</code>",
                "<code>final</code> on an instance variable means it's set once (in the declaration or constructor) and never changed.",
            ],
            "example": """
<pre class="code">public class Student
{
    // instance variables — private, one set per object
    private String name;
    private int grade;
    private double gpa;

    // constructor(s) — 3.4
    public Student(String n, int g, double gp)
    {
        name = n;
        grade = g;
        gpa = gp;
    }

    // methods — 3.5
    public String getName()
    {
        return name;
    }
}</pre>""",
            "tip": "FRQ 2 rubrics award a point for declaring instance variables private. Forgetting <code>private</code> costs it every year. Also, a class with instance variables but no constructor is legal — Java provides a default one — but on the FRQ you'll be asked to write one.",
            "questions": [
                {
                    "stem": "Consider a class <code>Box</code> with <code>private int width;</code>. Which of the following statements outside the class will compile?",
                    "options": ["<code>Box b = new Box(); b.width = 5;</code>", "<code>Box b = new Box(); int w = b.width;</code>", "<code>Box b = new Box(); int w = b.getWidth();</code> where <code>getWidth</code> is a public method", "<code>Box b = new Box(); System.out.println(b.width);</code>"],
                    "answer": "C",
                    "explanation": "Private variables can't be accessed outside the class. A public accessor method is the correct route.",
                },
                {
                    "stem": "A class declares <code>private int count;</code> and has a constructor that does not assign to it. What is the value of <code>count</code> in a newly created object?",
                    "options": ["A compile-time error occurs", "0", "null", "Undefined; it must be assigned before use"],
                    "answer": "B",
                    "explanation": "Instance variables get default values; int defaults to 0. (Local variables are the ones that must be assigned first.)",
                },
            ],
            "vocab": [
                ("Instance variable", "a variable declared in a class that each object has its own copy of"),
                ("private", "accessible only within the class"),
                ("public", "accessible from any class"),
                ("Default value", "the automatic initial value of an instance variable: 0, 0.0, false, or null"),
            ],
        },
        {
            "num": 4, "title": "Constructors", "blurb": "initializing objects",
            "lede": "A constructor runs when new is called and sets up the object's initial state. Get the name, the missing return type, and the parameter-to-variable assignments right.",
            "points": [
                "A <strong>constructor</strong> has the class's exact name and <strong>no return type</strong> (not even void). <code>public Student(String n) { ... }</code>",
                "Its job is to initialize instance variables, usually from parameters. Every instance variable should get a value here, even if it's a default like 0 or an empty list.",
                "Constructors can be <strong>overloaded</strong>: a no-argument constructor that sets defaults and a full constructor that takes values.",
                "If a class has <em>no</em> constructor, Java supplies a default no-argument one. If you write <em>any</em> constructor, that default disappears.",
                "Parameters that are references (like a String or an array) are copied as references — the object's variable points to the same object the caller passed. For mutable objects this can be a problem; for Strings it's safe because they're immutable.",
                "A common convention: parameter names differ from instance variable names (<code>n</code> vs <code>name</code>), or use <code>this.name = name</code> (3.9).",
            ],
            "example": """
<pre class="code">public class Rectangle
{
    private double width;
    private double height;

    public Rectangle()                  // no-arg: defaults
    {
        width = 1.0;
        height = 1.0;
    }

    public Rectangle(double w, double h)   // full
    {
        width = w;
        height = h;
    }
}

Rectangle r1 = new Rectangle();         // 1.0 x 1.0
Rectangle r2 = new Rectangle(3, 4.5);   // 3.0 x 4.5</pre>""",
            "tip": "Two mistakes cost FRQ points every year: writing <code>public void Rectangle(...)</code> (the void makes it a method, not a constructor) and assigning parameters to nothing (<code>w = width;</code> backwards). Instance variable on the left, parameter on the right.",
            "questions": [
                {
                    "stem": "Which of the following is a correctly written constructor for a class named <code>Timer</code> with a <code>private int seconds</code> instance variable?",
                    "options": ["<code>public void Timer(int s) { seconds = s; }</code>", "<code>public Timer(int s) { seconds = s; }</code>", "<code>public Timer(int s) { s = seconds; }</code>", "<code>public int Timer(int s) { return s; }</code>"],
                    "answer": "B",
                    "explanation": "No return type, class name, instance variable assigned from the parameter. A has void (a method), C is backwards, D returns a value.",
                },
                {
                    "stem": "A class <code>Point</code> defines only the constructor <code>public Point(int x, int y)</code>. Which of the following will not compile?",
                    "options": ["<code>Point p = new Point(1, 2);</code>", "<code>Point p = new Point();</code>", "<code>Point p = new Point(0, 0);</code>", "<code>Point p = null;</code>"],
                    "answer": "B",
                    "explanation": "Once any constructor is defined, the default no-arg constructor no longer exists.",
                },
            ],
            "vocab": [
                ("Constructor", "a method with the class's name and no return type that initializes a new object"),
                ("No-argument constructor", "a constructor with no parameters that sets default values"),
                ("Default constructor", "the no-arg constructor Java provides only when a class defines none"),
            ],
        },
        {
            "num": 5, "title": "Methods: How to Write Them", "blurb": "void vs. return, accessors, mutators, toString",
            "lede": "Writing methods that read and change an object's state. The exam expects accessors, mutators, and a toString that returns — not prints — a String.",
            "points": [
                "Method structure: <code>public returnType name(parameters) { body }</code>. A non-void method must <code>return</code> a value of the declared type on every path.",
                "<strong>Accessors</strong> return an instance variable's value: <code>public int getCount() { return count; }</code>. They never change state.",
                "<strong>Mutators</strong> change instance variables and are usually <code>void</code>: <code>public void setCount(int c) { count = c; }</code>. They may validate first.",
                "<code>public String toString()</code> returns a String description of the object. <code>System.out.println(obj)</code> calls it automatically. It <em>returns</em>; it does not print.",
                "A method can call other methods of the same class by name, and can use instance variables directly.",
                "Reaching the end of a non-void method without a return is a compile-time error (\"missing return statement\"). A return inside an if isn't enough unless every branch returns.",
                "Parameters are local to the method; changing a primitive parameter doesn't affect the caller's variable.",
            ],
            "example": """
<pre class="code">public class Counter
{
    private int count;
    private String label;

    public Counter(String l) { label = l; count = 0; }

    public int getCount() { return count; }                 // accessor
    public void increment() { count++; }                    // mutator
    public void reset() { count = 0; }                      // mutator
    public boolean isPositive() { return count &gt; 0; }       // accessor
    public String toString()
    {
        return label + ": " + count;                        // returns, not prints
    }
}
Counter c = new Counter("clicks");
c.increment();
c.increment();
System.out.println(c);        // clicks: 2</pre>""",
            "tip": "If the prompt says \"returns,\" write <code>return</code>; if it says \"prints,\" write <code>System.out.println</code>. Mixing them up is a full rubric point. For toString, always return. For every non-void method, ask: does every possible path hit a return?",
            "questions": [
                {
                    "stem": "Which of the following methods will cause a compile-time error?",
                    "options": ["<code>public int f(int x) { if (x &gt; 0) { return 1; } return -1; }</code>", "<code>public int g(int x) { if (x &gt; 0) { return 1; } }</code>", "<code>public void h(int x) { if (x &gt; 0) { return; } }</code>", "<code>public boolean k(int x) { return x &gt; 0; }</code>"],
                    "answer": "B",
                    "explanation": "If x ≤ 0, g reaches the end without returning an int — missing return statement.",
                },
                {
                    "stem": "A class has the method <code>public String toString() { return \"Item: \" + name; }</code>. What does <code>System.out.println(item);</code> print, where <code>item</code> has name \"pen\"?",
                    "options": ["Item: pen", "A memory address", "pen", "Nothing; toString must be called explicitly"],
                    "answer": "A",
                    "explanation": "println calls toString on the object automatically.",
                },
            ],
            "vocab": [
                ("Accessor method", "returns the value of an instance variable without changing it"),
                ("Mutator method", "changes an instance variable; typically void"),
                ("toString", "a method returning a String representation of the object, called automatically by println"),
            ],
        },
        {
            "num": 6, "title": "Methods: Passing and Returning References of an Object", "blurb": "reference parameters, aliasing through methods",
            "lede": "When you pass an object to a method, you pass its address. The method can change the object — and the caller sees it. Primitives don't work that way.",
            "points": [
                "Java passes all arguments <strong>by value</strong>. For primitives, the value is the number. For objects, the value is the <strong>reference</strong> — so the parameter and the argument point to the <em>same object</em>.",
                "A method can <strong>modify the object</strong> a reference parameter points to (call its mutators, change array elements), and the caller sees the change.",
                "A method <strong>cannot</strong> make the caller's variable point to a different object. Reassigning the parameter (<code>p = new Thing()</code>) only changes the local copy of the reference.",
                "Changing a primitive parameter never affects the caller.",
                "Returning an object returns its reference. The caller can then modify that object through the returned reference.",
                "Returning a reference to a private instance variable that is a mutable object breaks encapsulation — outside code can change internal state. Strings are safe because they're immutable.",
            ],
            "example": """
<pre class="code">public static void bump(Counter c, int n)
{
    c.increment();      // affects the caller's object
    n++;                // affects only the local n
    c = new Counter("other");   // caller's variable still points to original
    c.increment();      // this increments the new local object only
}

Counter myC = new Counter("a");   // count 0
int myN = 5;
bump(myC, myN);
System.out.println(myC.getCount());   // 1
System.out.println(myN);              // 5</pre>""",
            "tip": "Draw the arrow. Parameter and argument arrows point to the same box; mutating the box is visible to both. Reassigning the parameter moves only the parameter's arrow. Primitives are just copied numbers.",
            "questions": [
                {
                    "stem": "Consider the following method, where <code>Score</code> has a mutator <code>add(int p)</code> and accessor <code>getPoints()</code>.\n<pre class=\"code\">public static void update(Score s, int pts)\n{\n    s.add(pts);\n    pts = 0;\n}</pre>After <code>Score sc = new Score(); int p = 10; update(sc, p);</code>, what are <code>sc.getPoints()</code> and <code>p</code>?",
                    "options": ["0 and 0", "10 and 10", "10 and 0", "0 and 10"],
                    "answer": "B",
                    "explanation": "s and sc share the object, so add(10) is visible: 10 points. pts is a local copy; setting it to 0 doesn't change p.",
                },
                {
                    "stem": "Consider the following.\n<pre class=\"code\">public static void reset(Counter c)\n{\n    c = new Counter(\"new\");\n}\nCounter x = new Counter(\"old\");\nx.increment();\nreset(x);\nSystem.out.println(x.getCount());</pre>What is printed?",
                    "options": ["0", "1", "null", "A compile-time error"],
                    "answer": "B",
                    "explanation": "reset only reassigns its local parameter. x still points to the original object with count 1.",
                },
            ],
            "vocab": [
                ("Pass by value", "Java copies the argument's value; for objects that value is a reference"),
                ("Reference parameter", "a parameter that holds the address of the caller's object"),
            ],
        },
        {
            "num": 7, "title": "Class Variables and Methods", "blurb": "static — shared by all objects",
            "lede": "static members belong to the class, not to any single object. One copy, shared by everyone, accessible without creating an object.",
            "points": [
                "A <strong>class variable</strong> (static variable) is declared with <code>static</code>: <code>private static int count;</code> There is <em>one</em> copy shared by all objects of the class.",
                "Common uses: counting how many objects have been created, or constants: <code>public static final double RATE = 0.05;</code>",
                "A <strong>class method</strong> (static method) is declared with <code>static</code> and called on the class: <code>ClassName.method()</code>. It can be called without any object existing.",
                "Static methods <strong>cannot</strong> access instance variables or call instance methods directly — there's no object to refer to. They can access static variables.",
                "Instance methods <em>can</em> access static variables and methods.",
                "Static variables are initialized when the class is first loaded, before any object is created. Their default values are the same as instance variables.",
                "Access a static variable from an instance method or from outside (if public) via the class name: <code>Student.count</code>.",
            ],
            "example": """
<pre class="code">public class Ticket
{
    private static int nextId = 1;        // shared by all tickets
    public static final double FEE = 2.50; // constant
    private int id;                        // each ticket has its own

    public Ticket()
    {
        id = nextId;
        nextId++;
    }
    public static int getNextId() { return nextId; }   // OK: static uses static
    public int getId() { return id; }
    // public static int getId() { return id; }  // ERROR: no object
}
Ticket a = new Ticket();   // id 1
Ticket b = new Ticket();   // id 2
System.out.println(Ticket.getNextId());   // 3</pre>""",
            "tip": "\"Which variable should be static?\" — anything that's the same for every object or tracks the class as a whole. \"Why won't this compile?\" — a static method touching an instance variable. Trace static variables as one shared cell, not one per object.",
            "questions": [
                {
                    "stem": "A class <code>Player</code> has <code>private static int numPlayers = 0;</code> incremented in its constructor. After creating three Player objects, what is <code>numPlayers</code>?",
                    "options": ["0", "1", "3", "Each object has its own value"],
                    "answer": "C",
                    "explanation": "One shared variable, incremented three times.",
                },
                {
                    "stem": "Which of the following will not compile inside a class with <code>private int size;</code> and <code>private static int total;</code>?",
                    "options": ["<code>public int getSize() { return size; }</code>", "<code>public static int getTotal() { return total; }</code>", "<code>public static int getSize() { return size; }</code>", "<code>public int getTotal() { return total; }</code>"],
                    "answer": "C",
                    "explanation": "A static method can't access an instance variable — there's no object.",
                },
            ],
            "vocab": [
                ("Class variable / static variable", "a single variable shared by all objects of a class"),
                ("Class method / static method", "a method called on the class that can't use instance variables"),
                ("Constant", "a static final variable whose value never changes"),
            ],
        },
        {
            "num": 8, "title": "Scope and Access", "blurb": "where variables are visible",
            "lede": "Where a variable can be used depends on where it was declared. Local variables shadow instance variables, and blocks end scope.",
            "points": [
                "<strong>Instance variables</strong> are in scope throughout the class's methods and constructors.",
                "<strong>Local variables</strong> (declared inside a method, including parameters) exist only within the block where they're declared — from the declaration to the closing brace.",
                "A variable declared inside a loop body or if block is gone after that block. A for loop's header variable is gone after the loop.",
                "<strong>Shadowing:</strong> a local variable or parameter with the same name as an instance variable hides it. Inside that method, the name refers to the local. Use <code>this.name</code> (3.9) to reach the instance variable.",
                "Two local variables with the same name in the same scope is a compile error. In separate scopes (two different methods) it's fine.",
                "<strong>Access modifiers</strong> control visibility across classes: <code>private</code> = this class only, <code>public</code> = everywhere.",
                "A method's parameter is a local variable initialized by the argument.",
            ],
            "example": """
<pre class="code">public class Demo
{
    private int x = 10;            // instance variable

    public void run(int x)         // parameter shadows instance x
    {
        System.out.println(x);     // prints the parameter
        int y = 5;
        if (x &gt; 0)
        {
            int z = 1;             // z only exists in this block
            y += z;
        }
        // System.out.println(z);  // ERROR: z out of scope
        System.out.println(y);     // 6
    }
}</pre>""",
            "tip": "Find the closing brace of the block a variable was declared in — that's the end of its life. If a question uses a variable after that brace, it's a compile error. For shadowing, the closest declaration wins.",
            "questions": [
                {
                    "stem": "Which of the following will cause a compile-time error?",
                    "options": ["<code>for (int i = 0; i &lt; 5; i++) { int sq = i * i; } </code>", "<code>int total = 0; for (int i = 0; i &lt; 5; i++) { total += i; } System.out.println(total);</code>", "<code>for (int i = 0; i &lt; 5; i++) { int sq = i * i; } System.out.println(sq);</code>", "<code>int n = 3; if (n &gt; 0) { int m = n * 2; System.out.println(m); }</code>"],
                    "answer": "C",
                    "explanation": "sq is declared inside the loop body and is out of scope after it.",
                },
                {
                    "stem": "A class has <code>private int value = 8;</code> and the method <code>public int get(int value) { return value; }</code>. What does <code>obj.get(3)</code> return?",
                    "options": ["8", "3", "11", "A compile-time error"],
                    "answer": "B",
                    "explanation": "The parameter shadows the instance variable, so value refers to the argument 3.",
                },
            ],
            "vocab": [
                ("Scope", "the region of code in which a variable is accessible"),
                ("Local variable", "a variable declared inside a method or block"),
                ("Shadowing", "a local variable or parameter hiding an instance variable of the same name"),
            ],
        },
        {
            "num": 9, "title": "this Keyword", "blurb": "the current object",
            "lede": "this refers to the object the method was called on. It resolves shadowing and lets an object pass itself to other methods.",
            "points": [
                "Inside an instance method or constructor, <code>this</code> is a reference to <strong>the current object</strong> — the one the method was called on.",
                "<code>this.name = name;</code> assigns the parameter to the instance variable when they share a name. Without <code>this</code>, the line would assign the parameter to itself.",
                "<code>this</code> can be passed as an argument: <code>other.compareTo(this)</code>, or used to return the current object.",
                "<code>this</code> cannot be used in a static method — there's no current object.",
                "Calling a method with no object prefix inside a class is the same as <code>this.method()</code>.",
                "Using <code>this</code> is optional when there's no shadowing; it's only required to disambiguate.",
            ],
            "example": """
<pre class="code">public class Book
{
    private String title;
    private int pages;

    public Book(String title, int pages)
    {
        this.title = title;      // instance ← parameter
        this.pages = pages;
    }

    public boolean isLongerThan(Book other)
    {
        return this.pages &gt; other.pages;
    }
}</pre>
<p>Without <code>this.</code> in the constructor, <code>title = title;</code> assigns the parameter to itself and the instance variable stays null.</p>""",
            "tip": "When a constructor's parameters share names with instance variables, look for <code>this.</code> on the left side. If it's missing, the instance variables are never set — a classic \"why does getTitle() return null\" question.",
            "questions": [
                {
                    "stem": "Consider the constructor below.\n<pre class=\"code\">public Cat(String name)\n{\n    name = name;\n}</pre>After <code>Cat c = new Cat(\"Tom\");</code>, what does <code>c.getName()</code> return (where the getter returns the instance variable <code>name</code>)?",
                    "options": ["\"Tom\"", "null", "\"\"", "A compile-time error"],
                    "answer": "B",
                    "explanation": "The parameter shadows the instance variable; the assignment is parameter-to-parameter. The instance variable keeps its default, null.",
                },
                {
                    "stem": "In which of the following can <code>this</code> not be used?",
                    "options": ["An instance method", "A constructor", "A static method", "An accessor method"],
                    "answer": "C",
                    "explanation": "Static methods have no current object, so this is meaningless there.",
                },
            ],
            "vocab": [
                ("this", "a reference to the object on which the current method or constructor was invoked"),
            ],
        },
    ],
}

# ----------------------------------------------------------------------
# UNIT 4 — Data Collections (30–40%)  part 1: 4.1 – 4.9
# ----------------------------------------------------------------------

U4_A = [
    {
        "num": 1, "title": "Ethical and Social Issues Around Data Collection", "blurb": "privacy, consent, bias in data",
        "lede": "Before the technical content, the CED's second ethics topic: collecting data at scale has consequences.",
        "points": [
            "Programs today collect and process enormous amounts of data about people. <strong>Personal data</strong> can identify someone directly or in combination with other data.",
            "<strong>Privacy:</strong> people have a reasonable expectation about how their data is used. Collecting more than needed, keeping it longer than needed, or sharing it without consent violates that.",
            "<strong>Security:</strong> stored data can be breached; the more collected, the greater the harm from a breach.",
            "<strong>Bias in data:</strong> a dataset that under-represents some groups leads to programs that serve them worse. Analysis is only as fair as the data.",
            "<strong>Consent and transparency:</strong> users should know what is collected and why. Terms buried in fine print are legally compliant but ethically weak.",
            "Programmers are responsible for the systems they build — including anticipating misuse and designing to limit it.",
        ],
        "example": """
<p>A school app records which students open which assignments and when. Useful for spotting who's struggling. But the same data could rank teachers, track students' late-night habits, or be sold to a tutoring company. Responsible design: collect only assignment-completion status, aggregate before sharing, tell students what's stored, and delete it at year end.</p>""",
        "tip": "Same rule as CSP's Big Idea 5: the correct answer minimizes collection, requires consent, considers who's harmed, and acknowledges bias. Absolute or one-sided options are distractors.",
        "questions": [
            {
                "stem": "A program analyzes purchase histories to recommend products. Which of the following is the most significant ethical concern?",
                "options": ["The program may run slowly on large datasets.", "Users' personal data is being collected and used in ways they may not have agreed to or expect.", "The recommendations may use an ArrayList instead of an array.", "The program requires an import statement."],
                "answer": "B",
                "explanation": "Data use without informed consent is the core privacy concern.",
            },
            {
                "stem": "A dataset used to train a medical program includes very few records from older patients. Which outcome is most likely?",
                "options": ["The program will run faster for older patients.", "The program may perform less accurately for older patients due to bias in the data.", "The program will refuse to run.", "The program will automatically correct for the missing data."],
                "answer": "B",
                "explanation": "Under-representation in data produces worse performance for that group — bias.",
            },
        ],
        "vocab": [
            ("Personal data", "information that identifies or could identify an individual"),
            ("Informed consent", "users agreeing to data collection after understanding what and why"),
        ],
    },
    {
        "num": 2, "title": "Introduction to Using Data Sets", "blurb": "what a data set is, cleaning, structure",
        "lede": "New in the revised course: a data set is a collection of related records, and programs process it as arrays, ArrayLists, or files.",
        "points": [
            "A <strong>data set</strong> is a collection of related data, often organized as records (one per item) with fields (attributes of each item) — like a spreadsheet's rows and columns.",
            "In Java, a data set is typically stored as an array or ArrayList of values, or of objects where each object is one record.",
            "Data may come from user input, a text file (4.6), or be built in code.",
            "Before analysis, data often needs <strong>cleaning</strong>: removing invalid or duplicate entries, standardizing formats, handling missing values.",
            "Common analyses: summary statistics (sum, average, max, min), filtering records that meet a condition, counting matches, sorting, and finding patterns.",
            "The structure of the data determines which collection to use: fixed-size known-length → array; growing/shrinking → ArrayList; grid → 2D array.",
        ],
        "example": """
<pre class="code">// a data set of daily temperatures as an array
double[] temps = {72.5, 68.0, 75.2, 71.8, 69.9};
double sum = 0;
for (double t : temps)
{
    sum += t;
}
double avg = sum / temps.length;   // 71.48

// a data set of records as an ArrayList of objects
ArrayList&lt;Student&gt; roster = new ArrayList&lt;Student&gt;();
roster.add(new Student("Ava", 92));
roster.add(new Student("Ben", 85));</pre>""",
        "tip": "Questions here are conceptual: which structure fits which data, and what step (cleaning, filtering, aggregating) a description refers to. The code for all of it comes in the following topics.",
        "questions": [
            {
                "stem": "A program must store the names of students who sign up for a club over the course of a semester; the number is not known in advance. Which structure is most appropriate?",
                "options": ["An int", "An array of fixed size", "An ArrayList", "A 2D array"],
                "answer": "C",
                "explanation": "Unknown, changing size means ArrayList.",
            },
            {
                "stem": "A data set of survey responses contains some entries with a blank age field. Removing or replacing these entries before computing the average age is an example of which step?",
                "options": ["Sorting", "Data cleaning", "Encapsulation", "Recursion"],
                "answer": "B",
                "explanation": "Handling invalid or missing values is data cleaning.",
            },
        ],
        "vocab": [
            ("Data set", "a collection of related records, each with fields"),
            ("Record", "one item in a data set, such as one row"),
            ("Data cleaning", "fixing or removing invalid, duplicate, or missing data before analysis"),
        ],
    },
    {
        "num": 3, "title": "Array Creation and Access", "blurb": "int[], indexing, length",
        "lede": "Arrays are fixed-size, indexed from 0. Off-by-one and out-of-bounds are the whole story.",
        "points": [
            "Declare and create: <code>int[] nums = new int[5];</code> — five ints, all initialized to <strong>0</strong>. <code>double[]</code> → 0.0, <code>boolean[]</code> → false, object arrays (<code>String[]</code>) → <strong>null</strong>.",
            "Initializer list: <code>int[] nums = {4, 8, 15};</code> creates and fills in one step.",
            "Access: <code>nums[i]</code>. Indices run from <strong>0</strong> to <strong><code>nums.length - 1</code></strong>. <code>length</code> is a field (no parentheses), unlike String's <code>length()</code>.",
            "Accessing index <code>length</code> or any negative index throws <strong>ArrayIndexOutOfBoundsException</strong> at run time.",
            "Array size is <strong>fixed</strong> once created. To \"grow\" you create a new, bigger array and copy.",
            "Arrays are objects: an array variable holds a reference. <code>int[] b = a;</code> makes b an alias of a — same array.",
            "An array of objects holds references; each element must be assigned an object before its methods are called, or you get a NullPointerException.",
        ],
        "example": """
<pre class="code">int[] a = new int[4];        // {0, 0, 0, 0}
a[0] = 7;
a[3] = 2;
a[a.length - 1] = 9;         // last element → 9
System.out.println(a[2]);    // 0
System.out.println(a.length);// 4
// a[4] = 1;                 // ArrayIndexOutOfBoundsException

String[] words = new String[2];
// words[0].length();        // NullPointerException — element is null
words[0] = "hi";
System.out.println(words[0].length());   // 2</pre>""",
        "tip": "Every array question: what's the first index (0), the last index (length − 1), and what's the default value? An index equal to length is the exam's favorite exception. And <code>length</code> without parentheses — with parentheses it won't compile.",
        "questions": [
            {
                "stem": "Which of the following will cause a run-time exception?\n<pre class=\"code\">int[] arr = new int[6];</pre>",
                "options": ["<code>arr[0] = 5;</code>", "<code>arr[5] = 5;</code>", "<code>arr[6] = 5;</code>", "<code>arr[arr.length - 1] = 5;</code>"],
                "answer": "C",
                "explanation": "Valid indices are 0–5. Index 6 is out of bounds.",
            },
            {
                "stem": "What is printed by the following code?\n<pre class=\"code\">int[] x = {3, 6, 9};\nint[] y = x;\ny[1] = 0;\nSystem.out.println(x[1]);</pre>",
                "options": ["6", "0", "3", "A compile-time error"],
                "answer": "B",
                "explanation": "y is an alias of x; they're the same array. Changing y[1] changes x[1].",
            },
            {
                "stem": "After <code>double[] d = new double[3];</code>, what is the value of <code>d[1]</code>?",
                "options": ["null", "0.0", "Undefined until assigned", "1.0"],
                "answer": "B",
                "explanation": "Numeric arrays are initialized to zero.",
            },
        ],
        "vocab": [
            ("Array", "a fixed-size, ordered collection of elements of one type"),
            ("Index", "an element's position, from 0 to length - 1"),
            ("length", "the field giving the number of elements in an array"),
            ("ArrayIndexOutOfBoundsException", "the run-time error from using an invalid index"),
        ],
    },
    {
        "num": 4, "title": "Array Traversals", "blurb": "for loops and enhanced for",
        "lede": "Visiting every element. The standard for loop gives you the index; the enhanced for loop gives you the element. Know when each is appropriate.",
        "points": [
            "<strong>Standard traversal:</strong> <code>for (int i = 0; i &lt; arr.length; i++)</code> with <code>arr[i]</code>. Use when you need the index — to modify elements, compare neighbors, or traverse backward or partially.",
            "<strong>Enhanced for (for-each):</strong> <code>for (int x : arr)</code> — x takes each element's value in order. Cleaner when you only read elements.",
            "In an enhanced for loop, <strong>assigning to the loop variable does not change the array</strong> — x is a copy of the element (for primitives). For objects, x is a copy of the reference, so calling mutators on it <em>does</em> affect the object in the array.",
            "Enhanced for can't skip elements, go backward, or access the index.",
            "<strong>Backward:</strong> <code>for (int i = arr.length - 1; i &gt;= 0; i--)</code>.",
            "Loop bound <code>i &lt;= arr.length</code> is the classic out-of-bounds bug.",
        ],
        "example": """
<pre class="code">int[] nums = {2, 4, 6};

for (int n : nums)            // enhanced: read only
{
    n = n * 10;               // does NOT change nums
}
// nums still {2, 4, 6}

for (int i = 0; i &lt; nums.length; i++)   // standard: can modify
{
    nums[i] = nums[i] * 10;
}
// nums now {20, 40, 60}</pre>""",
        "tip": "If the question modifies the array through the loop variable of an enhanced for loop, the array is unchanged — that's the trick. If it calls a mutator method on an object element, the object <em>is</em> changed. Index needed? Standard loop.",
        "questions": [
            {
                "stem": "What is printed by the following code?\n<pre class=\"code\">int[] a = {1, 2, 3};\nfor (int v : a)\n{\n    v += 10;\n}\nSystem.out.println(a[0] + a[1] + a[2]);</pre>",
                "options": ["6", "36", "16", "A compile-time error"],
                "answer": "A",
                "explanation": "v is a copy; modifying it leaves the array unchanged. 1 + 2 + 3 = 6.",
            },
            {
                "stem": "Which of the following correctly prints the elements of <code>arr</code> in reverse order?",
                "options": ["<code>for (int i = arr.length; i &gt; 0; i--) System.out.println(arr[i]);</code>", "<code>for (int i = arr.length - 1; i &gt;= 0; i--) System.out.println(arr[i]);</code>", "<code>for (int x : arr) System.out.println(x);</code>", "<code>for (int i = arr.length - 1; i &gt; 0; i--) System.out.println(arr[i]);</code>"],
                "answer": "B",
                "explanation": "Start at length - 1, go down to and including 0. A starts out of bounds; D skips index 0.",
            },
        ],
        "vocab": [
            ("Traversal", "visiting every element of an array"),
            ("Enhanced for loop", "for (type x : arr) — iterates over elements without an index"),
        ],
    },
    {
        "num": 5, "title": "Implementing Array Algorithms", "blurb": "sum, max, count, shift, reverse, find",
        "lede": "The CED names the array algorithms you should be able to write. These are FRQ building blocks — practice until they're reflexive.",
        "points": [
            "<strong>Named algorithms:</strong> find min/max; compute sum/average; count elements meeting a condition; determine if any/all elements satisfy a condition; find the mode (most frequent); check for duplicates; reverse the array; shift or rotate elements; check whether an array is sorted; find consecutive pairs.",
            "<strong>Any/all:</strong> \"any\" loops and returns true at the first match, false after the loop. \"All\" returns false at the first failure, true after.",
            "<strong>Reverse in place:</strong> swap <code>arr[i]</code> with <code>arr[arr.length - 1 - i]</code> for i from 0 to length/2.",
            "<strong>Shift left by one:</strong> <code>arr[i] = arr[i + 1]</code> for i from 0 to length − 2, then handle the last element. Direction of the loop matters to avoid overwriting.",
            "<strong>Consecutive elements:</strong> compare <code>arr[i]</code> and <code>arr[i + 1]</code> with the loop ending at <code>length - 1</code> (not length).",
            "<strong>Duplicates:</strong> nested loop comparing each pair (i, j with j &gt; i).",
        ],
        "example": """
<pre class="code">// are all elements positive?
public static boolean allPositive(int[] a)
{
    for (int x : a)
    {
        if (x &lt;= 0) return false;
    }
    return true;
}

// count adjacent equal pairs
int pairs = 0;
for (int i = 0; i &lt; a.length - 1; i++)
{
    if (a[i] == a[i + 1]) pairs++;
}

// reverse in place
for (int i = 0; i &lt; a.length / 2; i++)
{
    int tmp = a[i];
    a[i] = a[a.length - 1 - i];
    a[a.length - 1 - i] = tmp;
}</pre>""",
        "tip": "Any algorithm touching <code>arr[i + 1]</code> must stop at <code>length - 1</code>; touching <code>arr[i - 1]</code> must start at 1. For \"any\" vs \"all,\" the return inside the loop is the opposite of the return after it.",
        "questions": [
            {
                "stem": "What does the following method return for <code>{3, 3, 5, 5, 5, 2}</code>?\n<pre class=\"code\">public static int count(int[] a)\n{\n    int c = 0;\n    for (int i = 1; i &lt; a.length; i++)\n    {\n        if (a[i] == a[i - 1]) c++;\n    }\n    return c;\n}</pre>",
                "options": ["2", "3", "4", "5"],
                "answer": "B",
                "explanation": "Pairs (3,3), (5,5), (5,5) match → 3.",
            },
            {
                "stem": "The following method is intended to return true if any element of <code>arr</code> is negative.\n<pre class=\"code\">public static boolean hasNeg(int[] arr)\n{\n    for (int x : arr)\n    {\n        if (x &lt; 0) return true;\n        else return false;\n    }\n    return false;\n}</pre>Which best describes the error?",
                "options": ["It will not compile.", "It only checks the first element, because the else returns immediately.", "It throws an exception on an empty array.", "It works correctly."],
                "answer": "B",
                "explanation": "The else-return exits on the first element regardless. Remove the else so the loop continues.",
            },
        ],
        "vocab": [
            ("In-place", "modifying the array itself rather than building a new one"),
            ("Mode", "the value that appears most often"),
        ],
    },
    {
        "num": 6, "title": "Using Text Files", "blurb": "File, Scanner, hasNextLine, FileNotFoundException",
        "lede": "New in the revised course. Reading a text file uses the same Scanner methods as keyboard input, plus a File object and one exception you must declare.",
        "points": [
            "Open a file for reading: <code>Scanner in = new Scanner(new File(\"data.txt\"));</code>. Both <code>File</code> (java.io) and <code>Scanner</code> (java.util) need imports.",
            "Creating a Scanner on a File can throw <strong>FileNotFoundException</strong> (a checked exception). The method must declare <code>throws FileNotFoundException</code> in its header.",
            "Read line by line: <code>while (in.hasNextLine()) { String line = in.nextLine(); ... }</code>. Read tokens: <code>while (in.hasNext())</code> with <code>next()</code>, or <code>hasNextInt()</code> with <code>nextInt()</code>.",
            "Close the file when done: <code>in.close();</code>",
            "Lines of text often need parsing: <code>Integer.parseInt(str)</code> and <code>Double.parseDouble(str)</code> convert String tokens to numbers.",
            "The same nextInt/nextLine buffer trap from 1.4 applies to files.",
            "A common pattern: read each line into an ArrayList so the data can be processed after the file is closed.",
        ],
        "example": """
<pre class="code">import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public static ArrayList&lt;Integer&gt; readScores(String filename)
        throws FileNotFoundException
{
    Scanner in = new Scanner(new File(filename));
    ArrayList&lt;Integer&gt; scores = new ArrayList&lt;Integer&gt;();
    while (in.hasNextInt())
    {
        scores.add(in.nextInt());
    }
    in.close();
    return scores;
}</pre>""",
        "tip": "Three things the exam checks: the <code>throws FileNotFoundException</code> clause, the <code>hasNext…</code>/<code>next…</code> pair matching (hasNextLine with nextLine, hasNextInt with nextInt), and closing the Scanner. If a method opens a file and has no throws clause, it won't compile.",
        "questions": [
            {
                "stem": "A method creates <code>new Scanner(new File(\"in.txt\"))</code>. Which of the following must be true for the code to compile?",
                "options": ["The file must exist at compile time.", "The method must declare <code>throws FileNotFoundException</code>.", "The Scanner must be static.", "The file must contain only integers."],
                "answer": "B",
                "explanation": "FileNotFoundException is a checked exception; the method header must declare it.",
            },
            {
                "stem": "Which loop correctly reads every line of a text file using a Scanner <code>sc</code>?",
                "options": ["<code>while (sc.hasNext()) { String s = sc.nextLine(); }</code>", "<code>while (sc.hasNextLine()) { String s = sc.nextLine(); }</code>", "<code>while (sc.nextLine() != null) { }</code>", "<code>for (int i = 0; i &lt; sc.length(); i++) { String s = sc.nextLine(); }</code>"],
                "answer": "B",
                "explanation": "hasNextLine pairs with nextLine. Option A can throw on a trailing blank line; C throws at end of file; D doesn't compile.",
            },
        ],
        "vocab": [
            ("File", "a class representing a file on disk, passed to a Scanner to read it"),
            ("FileNotFoundException", "a checked exception thrown when a file can't be opened; must be declared"),
            ("hasNextLine()", "returns true if another line remains to be read"),
        ],
    },
    {
        "num": 7, "title": "Wrapper Classes", "blurb": "Integer, Double, autoboxing",
        "lede": "ArrayLists can't hold primitives, so Java wraps them in objects. Autoboxing makes this mostly invisible — except in the spots the exam tests.",
        "points": [
            "<code>Integer</code> and <code>Double</code> are <strong>wrapper classes</strong>: objects that hold one int or double. Needed because <code>ArrayList&lt;int&gt;</code> is illegal; you write <code>ArrayList&lt;Integer&gt;</code>.",
            "<strong>Autoboxing:</strong> Java automatically converts int → Integer when needed (<code>list.add(5)</code>). <strong>Unboxing:</strong> Integer → int (<code>int x = list.get(0)</code>).",
            "<code>Integer.MAX_VALUE</code> and <code>Integer.MIN_VALUE</code> — the int range limits, on the reference sheet. Useful as initial values for min/max algorithms.",
            "<code>Integer.parseInt(String)</code> and <code>Double.parseDouble(String)</code> convert text to numbers — essential for file input.",
            "Comparing two Integer objects with <code>==</code> compares references and is unreliable; use <code>.equals()</code> or unbox to ints first.",
            "Unboxing a <code>null</code> Integer throws a NullPointerException.",
            "Arithmetic on Integers unboxes automatically: <code>Integer a = 5; int b = a + 3;</code> works.",
        ],
        "example": """
<pre class="code">ArrayList&lt;Integer&gt; nums = new ArrayList&lt;Integer&gt;();
nums.add(7);                    // autobox int → Integer
int first = nums.get(0);        // unbox Integer → int
Integer big = Integer.MAX_VALUE;
int n = Integer.parseInt("42");   // 42
double d = Double.parseDouble("3.5");

int min = Integer.MAX_VALUE;     // start high for a min search
for (int x : nums)
{
    if (x &lt; min) min = x;
}</pre>""",
        "tip": "You can't write <code>ArrayList&lt;int&gt;</code> — that's a guaranteed compile-error question. Everywhere else, treat Integer like int and let autoboxing work, except: never compare Integers with <code>==</code>, and remember a null Integer crashes when unboxed.",
        "questions": [
            {
                "stem": "Which of the following declarations compiles?",
                "options": ["<code>ArrayList&lt;int&gt; a = new ArrayList&lt;int&gt;();</code>", "<code>ArrayList&lt;Integer&gt; a = new ArrayList&lt;Integer&gt;();</code>", "<code>ArrayList&lt;double&gt; a = new ArrayList&lt;double&gt;();</code>", "<code>ArrayList a = new ArrayList&lt;int&gt;();</code>"],
                "answer": "B",
                "explanation": "Generic type parameters must be classes; Integer is the wrapper for int.",
            },
            {
                "stem": "A method finds the largest value in a list of integers by starting with <code>int max = 0;</code>. For which input does this produce a wrong answer, and what initial value fixes it?",
                "options": ["Lists containing zero; use 1", "Lists of all negative values; use <code>Integer.MIN_VALUE</code>", "Lists of all positive values; use <code>Integer.MAX_VALUE</code>", "It is always correct"],
                "answer": "B",
                "explanation": "If every value is negative, none exceed 0. Starting at Integer.MIN_VALUE (or the first element) fixes it.",
            },
        ],
        "vocab": [
            ("Wrapper class", "an object type (Integer, Double) that holds a primitive value"),
            ("Autoboxing", "automatic conversion from a primitive to its wrapper"),
            ("Unboxing", "automatic conversion from a wrapper to its primitive"),
            ("Integer.parseInt", "converts a String to an int"),
        ],
    },
    {
        "num": 8, "title": "ArrayList Methods", "blurb": "add, get, set, remove, size",
        "lede": "A resizable list. Six methods on the reference sheet, and the index-shifting behavior of add and remove is where questions come from.",
        "points": [
            "Create: <code>ArrayList&lt;String&gt; names = new ArrayList&lt;String&gt;();</code> (empty, size 0). Import <code>java.util.ArrayList</code>.",
            "<code>size()</code> — number of elements (a method, with parentheses — unlike array <code>length</code>).",
            "<code>add(obj)</code> — appends to the end, returns true. <code>add(index, obj)</code> — inserts at index, shifting later elements <strong>right</strong>; size grows by 1.",
            "<code>get(index)</code> — returns the element. <code>set(index, obj)</code> — replaces the element at index, returns the <em>old</em> value; size unchanged.",
            "<code>remove(index)</code> — removes and returns the element at index, shifting later elements <strong>left</strong>; size shrinks by 1.",
            "Valid indices are 0 to <code>size() - 1</code>. <code>get(size())</code> throws <strong>IndexOutOfBoundsException</strong>. <code>add(size(), obj)</code> is legal (appends).",
            "ArrayList holds objects only — use wrapper types for numbers (4.7).",
        ],
        "example": """
<pre class="code">ArrayList&lt;String&gt; a = new ArrayList&lt;String&gt;();
a.add("x");              // [x]
a.add("y");              // [x, y]
a.add(1, "m");           // [x, m, y]   inserted, y shifted right
a.set(0, "z");           // [z, m, y]   replaced
String r = a.remove(1);  // [z, y]      r = "m"
System.out.println(a.size());     // 2
System.out.println(a.get(1));     // y
// a.get(2);             // IndexOutOfBoundsException</pre>""",
        "tip": "Rewrite the list in brackets after every call. <code>set</code> doesn't change size; <code>add(i, x)</code> and <code>remove(i)</code> do, and they shift everything after i. <code>remove</code> and <code>set</code> both return the element that was there — questions sometimes use that return value.",
        "questions": [
            {
                "stem": "What is printed by the following code?\n<pre class=\"code\">ArrayList&lt;Integer&gt; list = new ArrayList&lt;Integer&gt;();\nlist.add(10);\nlist.add(20);\nlist.add(30);\nlist.add(1, 15);\nlist.remove(2);\nSystem.out.println(list);</pre>",
                "options": ["[10, 15, 30]", "[10, 15, 20]", "[10, 20, 30]", "[15, 20, 30]"],
                "answer": "A",
                "explanation": "After add(1, 15): [10, 15, 20, 30]. remove(2) removes 20: [10, 15, 30].",
            },
            {
                "stem": "Given <code>ArrayList&lt;String&gt; w</code> with 4 elements, which of the following throws an exception?",
                "options": ["<code>w.add(4, \"e\")</code>", "<code>w.set(3, \"e\")</code>", "<code>w.get(4)</code>", "<code>w.remove(3)</code>"],
                "answer": "C",
                "explanation": "Valid get indices are 0–3. add(4, …) is legal because 4 == size (appends).",
            },
            {
                "stem": "What does <code>list.set(2, \"new\")</code> return, where <code>list</code> is <code>[a, b, c, d]</code>?",
                "options": ["\"new\"", "\"c\"", "2", "true"],
                "answer": "B",
                "explanation": "set returns the element that was replaced.",
            },
        ],
        "vocab": [
            ("ArrayList", "a resizable list of objects"),
            ("size()", "the number of elements in an ArrayList"),
            ("add(index, obj)", "inserts, shifting later elements right"),
            ("remove(index)", "removes and returns, shifting later elements left"),
            ("set(index, obj)", "replaces and returns the old element; size unchanged"),
        ],
    },
    {
        "num": 9, "title": "ArrayList Traversals", "blurb": "loops over ArrayLists, removing while traversing",
        "lede": "Same two loop styles as arrays, with one extra hazard: modifying the list's size while looping over it.",
        "points": [
            "<strong>Standard:</strong> <code>for (int i = 0; i &lt; list.size(); i++)</code> with <code>list.get(i)</code>. <strong>Enhanced:</strong> <code>for (String s : list)</code>.",
            "<strong>Removing during a forward loop skips elements.</strong> After <code>remove(i)</code>, the next element shifts into index i, then i++ jumps past it.",
            "Fixes: after removing, do <code>i--</code> (or don't increment); or traverse <strong>backward</strong> with <code>for (int i = list.size() - 1; i &gt;= 0; i--)</code>, where removals don't affect unvisited indices.",
            "<strong>Never add or remove inside an enhanced for loop</strong> — it throws <code>ConcurrentModificationException</code>.",
            "Enhanced for over an ArrayList of objects lets you call mutators on each element (the reference is shared); over <code>ArrayList&lt;Integer&gt;</code>, assigning to the loop variable does nothing to the list.",
            "The loop condition <code>i &lt; list.size()</code> is re-evaluated each iteration, so a shrinking list shortens the loop.",
        ],
        "example": """
<pre class="code">ArrayList&lt;Integer&gt; a = new ArrayList&lt;Integer&gt;();
// a = [4, 4, 7, 4]
// BUGGY: remove all 4s
for (int i = 0; i &lt; a.size(); i++)
{
    if (a.get(i) == 4) a.remove(i);
}
// result: [4, 7]  — second 4 was skipped

// CORRECT: backward
for (int i = a.size() - 1; i &gt;= 0; i--)
{
    if (a.get(i) == 4) a.remove(i);
}
// result: [7]</pre>""",
        "tip": "If a question removes elements in a forward loop, trace it literally — the answer usually has \"leftover\" elements that were skipped. If asked for the correct version, pick the backward loop or the one with <code>i--</code> after remove.",
        "questions": [
            {
                "stem": "What is the contents of <code>list</code> after the following code, where <code>list</code> starts as <code>[1, 2, 2, 3, 2]</code>?\n<pre class=\"code\">for (int i = 0; i &lt; list.size(); i++)\n{\n    if (list.get(i) == 2)\n    {\n        list.remove(i);\n    }\n}</pre>",
                "options": ["[1, 3]", "[1, 2, 3]", "[1, 2, 3, 2]", "[1, 3, 2]"],
                "answer": "B",
                "explanation": "i=1 removes the first 2 → [1, 2, 3, 2]; i=2 is 3 (the second 2 shifted to index 1 and was skipped); i=3 removes the last 2 → [1, 2, 3].",
            },
            {
                "stem": "Which of the following correctly removes every element equal to <code>target</code> from an <code>ArrayList&lt;Integer&gt; nums</code>?",
                "options": ["<code>for (Integer n : nums) { if (n == target) nums.remove(n); }</code>", "<code>for (int i = nums.size() - 1; i &gt;= 0; i--) { if (nums.get(i) == target) nums.remove(i); }</code>", "<code>for (int i = 0; i &lt; nums.size(); i++) { if (nums.get(i) == target) nums.remove(i); }</code>", "<code>for (int i = 0; i &lt;= nums.size(); i++) { if (nums.get(i) == target) nums.remove(i); }</code>"],
                "answer": "B",
                "explanation": "Backward traversal handles removals safely. A throws ConcurrentModificationException; C skips adjacent matches; D goes out of bounds.",
            },
        ],
        "vocab": [
            ("ConcurrentModificationException", "the error from modifying an ArrayList inside an enhanced for loop"),
            ("Backward traversal", "looping from size - 1 down to 0, safe for removals"),
        ],
    },
]

# ----------------------------------------------------------------------
# UNIT 4 part 2: 4.10 – 4.17
# ----------------------------------------------------------------------

U4_B = [
    {
        "num": 10, "title": "Implementing ArrayList Algorithms", "blurb": "FRQ 3 patterns",
        "lede": "The same algorithms as arrays, in ArrayList syntax, plus the ones that only make sense with a resizable list: insert in order, remove matches, build a filtered list.",
        "points": [
            "All the array algorithms (min/max, sum, count, any/all, duplicates, reverse) apply — swap <code>arr[i]</code> for <code>list.get(i)</code>, <code>length</code> for <code>size()</code>.",
            "<strong>Filter into a new list:</strong> create an empty ArrayList, traverse the original, <code>add</code> matches. The original is unchanged.",
            "<strong>Insert in sorted position:</strong> traverse until you find an element bigger than the new one, <code>add(i, value)</code> there; if none, <code>add(value)</code> at the end.",
            "<strong>Remove all matches:</strong> backward traversal with <code>remove(i)</code> (4.9).",
            "<strong>Traversing a list of objects:</strong> call accessors on each element (<code>list.get(i).getName()</code>). This is FRQ 3's shape: a class is given, and you process an ArrayList of its objects.",
            "Returning a new list vs. modifying the parameter: read the prompt. \"Returns a list of…\" → build and return a new one. \"Removes from the list…\" → mutate the parameter.",
        ],
        "example": """
<pre class="code">// FRQ 3-style: return names of students with gpa above a threshold
public static ArrayList&lt;String&gt; honorRoll(ArrayList&lt;Student&gt; roster, double min)
{
    ArrayList&lt;String&gt; result = new ArrayList&lt;String&gt;();
    for (Student s : roster)
    {
        if (s.getGpa() &gt;= min)
        {
            result.add(s.getName());
        }
    }
    return result;
}

// insert keeping ascending order
public static void insertSorted(ArrayList&lt;Integer&gt; list, int v)
{
    for (int i = 0; i &lt; list.size(); i++)
    {
        if (v &lt; list.get(i))
        {
            list.add(i, v);
            return;
        }
    }
    list.add(v);
}</pre>""",
        "tip": "FRQ 3 rubrics typically award: correct loop over the list, correct accessor call on each element, correct condition, correct add/remove/return. Write the enhanced for loop first, then the if, then what happens inside. Don't forget to return the new list.",
        "questions": [
            {
                "stem": "What does the following method return for the list <code>[5, 2, 8, 2, 9]</code>?\n<pre class=\"code\">public static int f(ArrayList&lt;Integer&gt; list)\n{\n    int r = list.get(0);\n    for (int i = 1; i &lt; list.size(); i++)\n    {\n        if (list.get(i) &lt; r) r = list.get(i);\n    }\n    return r;\n}</pre>",
                "options": ["9", "5", "2", "26"],
                "answer": "C",
                "explanation": "This is the min pattern. The smallest value is 2.",
            },
            {
                "stem": "A method should return a new ArrayList containing only the even values from <code>nums</code>, leaving <code>nums</code> unchanged. Which approach is correct?",
                "options": ["Traverse <code>nums</code> backward, removing odd values, and return <code>nums</code>.", "Create an empty ArrayList, add each even value from <code>nums</code> to it, and return the new list.", "Use <code>set</code> to replace odd values with 0 and return <code>nums</code>.", "Sort <code>nums</code> and return it."],
                "answer": "B",
                "explanation": "\"New list\" and \"unchanged original\" mean build and return a separate list.",
            },
        ],
        "vocab": [
            ("Filter", "building a new list from elements that meet a condition"),
            ("Insert in order", "adding an element at the position that keeps the list sorted"),
        ],
    },
    {
        "num": 11, "title": "2D Array Creation and Access", "blurb": "int[][], rows and columns",
        "lede": "A 2D array is an array of arrays. Row first, then column — and each row is itself a 1D array you can pass around.",
        "points": [
            "Declare and create: <code>int[][] grid = new int[3][4];</code> — 3 rows, 4 columns, all 0. <code>grid.length</code> is the number of <strong>rows</strong>; <code>grid[0].length</code> is the number of <strong>columns</strong>.",
            "Initializer: <code>int[][] g = {{1, 2, 3}, {4, 5, 6}};</code> — 2 rows, 3 columns.",
            "Access: <code>grid[row][col]</code>. <code>grid[1][2]</code> is row 1, column 2 (both from 0).",
            "<code>grid[r]</code> by itself is a 1D array — row r. You can pass it to a method that takes <code>int[]</code>.",
            "On the AP exam, 2D arrays are <strong>rectangular</strong> — every row has the same length. (Java allows ragged arrays, but they aren't tested.)",
            "Default values follow 1D rules: 0, 0.0, false, null.",
            "Out of bounds in either dimension throws ArrayIndexOutOfBoundsException.",
        ],
        "example": """
<pre class="code">int[][] m = {{1, 2, 3},
             {4, 5, 6}};
System.out.println(m.length);        // 2  (rows)
System.out.println(m[0].length);     // 3  (columns)
System.out.println(m[1][2]);         // 6
m[0][1] = 9;                         // row 0 becomes {1, 9, 3}
int[] secondRow = m[1];              // {4, 5, 6}
// m[2][0]                            // exception: no row 2</pre>""",
        "tip": "Read <code>m[a][b]</code> as \"row a, column b\" every time — never reverse it. <code>length</code> counts rows; <code>[0].length</code> counts columns. A question that flips these is the standard distractor.",
        "questions": [
            {
                "stem": "After <code>double[][] t = new double[4][6];</code>, what are <code>t.length</code> and <code>t[0].length</code>?",
                "options": ["4 and 6", "6 and 4", "24 and 1", "4 and 4"],
                "answer": "A",
                "explanation": "First dimension is rows (4), second is columns (6).",
            },
            {
                "stem": "What is printed by the following code?\n<pre class=\"code\">int[][] a = {{2, 4}, {6, 8}, {10, 12}};\nSystem.out.println(a[2][0] + a[0][1]);</pre>",
                "options": ["14", "12", "16", "8"],
                "answer": "A",
                "explanation": "a[2][0] is 10 (row 2, col 0); a[0][1] is 4. 10 + 4 = 14.",
            },
        ],
        "vocab": [
            ("2D array", "an array whose elements are arrays; rows of columns"),
            ("Row-major", "the convention that the first index is the row"),
            ("Rectangular array", "a 2D array where every row has the same length"),
        ],
    },
    {
        "num": 12, "title": "2D Array Traversals", "blurb": "nested loops, row-major vs. column-major",
        "lede": "Nested loops visit every cell. Which loop is outer determines the order — and the exam asks about that order.",
        "points": [
            "<strong>Row-major traversal:</strong> outer loop over rows, inner over columns. Visits row 0 left to right, then row 1, etc. This is the default.",
            "<strong>Column-major traversal:</strong> outer loop over columns, inner over rows. Visits column 0 top to bottom, then column 1.",
            "<strong>Nested enhanced for:</strong> <code>for (int[] row : grid) { for (int v : row) { ... } }</code> — row-major, read only.",
            "Use <code>grid.length</code> for the row bound and <code>grid[0].length</code> (or <code>grid[r].length</code>) for the column bound.",
            "Partial traversals: a single row (<code>grid[r][c]</code> for c), a single column (<code>grid[r][c]</code> for r), the diagonal (<code>grid[i][i]</code>), or a sub-region.",
            "Traversal order matters when output is printed in sequence or when elements are appended to a list.",
        ],
        "example": """
<pre class="code">int[][] g = {{1, 2, 3},
             {4, 5, 6}};

// row-major: 1 2 3 4 5 6
for (int r = 0; r &lt; g.length; r++)
{
    for (int c = 0; c &lt; g[0].length; c++)
    {
        System.out.print(g[r][c] + " ");
    }
}

// column-major: 1 4 2 5 3 6
for (int c = 0; c &lt; g[0].length; c++)
{
    for (int r = 0; r &lt; g.length; r++)
    {
        System.out.print(g[r][c] + " ");
    }
}</pre>""",
        "tip": "Look at which index the outer loop controls. Outer over r → row-major. Outer over c → column-major. When asked for the printed output, write out the grid and read it in that order.",
        "questions": [
            {
                "stem": "What is printed by the following code?\n<pre class=\"code\">int[][] m = {{1, 2}, {3, 4}, {5, 6}};\nfor (int c = 0; c &lt; m[0].length; c++)\n{\n    for (int r = 0; r &lt; m.length; r++)\n    {\n        System.out.print(m[r][c]);\n    }\n}</pre>",
                "options": ["123456", "135246", "246135", "654321"],
                "answer": "B",
                "explanation": "Column-major: column 0 (1, 3, 5) then column 1 (2, 4, 6).",
            },
            {
                "stem": "Which of the following computes the sum of the elements on the main diagonal of a square 2D array <code>sq</code>?",
                "options": ["<code>for (int i = 0; i &lt; sq.length; i++) sum += sq[i][i];</code>", "<code>for (int i = 0; i &lt; sq.length; i++) sum += sq[i][0];</code>", "<code>for (int i = 0; i &lt; sq.length; i++) sum += sq[0][i];</code>", "<code>for (int[] row : sq) sum += row[0];</code>"],
                "answer": "A",
                "explanation": "The main diagonal is where row == column: sq[i][i].",
            },
        ],
        "vocab": [
            ("Row-major traversal", "outer loop over rows, inner over columns"),
            ("Column-major traversal", "outer loop over columns, inner over rows"),
        ],
    },
    {
        "num": 13, "title": "Implementing 2D Array Algorithms", "blurb": "FRQ 4 patterns",
        "lede": "FRQ 4 is always a 2D array question. The algorithms are the 1D ones applied across rows, columns, or the whole grid.",
        "points": [
            "<strong>Named algorithms:</strong> sum/max/min of the whole grid, of a row, or of a column; count cells meeting a condition; find a value's position; check whether every element in a row/column meets a condition; find rows/columns with a property.",
            "<strong>Row operations:</strong> a method that takes <code>int[]</code> can be called with <code>grid[r]</code>. Reusing a 1D helper is common in FRQ 4.",
            "<strong>Column operations:</strong> there's no direct column array; loop over r with fixed c.",
            "<strong>Building a 2D array from a 1D array or list:</strong> fill in row-major (or column-major, if specified) order using a running index into the source.",
            "<strong>Searching:</strong> nested loops; return as soon as found (a return exits both loops).",
            "<strong>Modifying in place:</strong> nested loops with standard indices, assigning to <code>grid[r][c]</code>.",
        ],
        "example": """
<pre class="code">// FRQ 4-style: return the index of the row with the largest sum
public static int maxRow(int[][] g)
{
    int best = 0;
    int bestSum = rowSum(g[0]);
    for (int r = 1; r &lt; g.length; r++)
    {
        int s = rowSum(g[r]);
        if (s &gt; bestSum)
        {
            bestSum = s;
            best = r;
        }
    }
    return best;
}
public static int rowSum(int[] row)
{
    int sum = 0;
    for (int v : row) sum += v;
    return sum;
}

// fill a 2D array from a 1D array in row-major order
int k = 0;
for (int r = 0; r &lt; g.length; r++)
{
    for (int c = 0; c &lt; g[0].length; c++)
    {
        g[r][c] = source[k];
        k++;
    }
}</pre>""",
        "tip": "FRQ 4 part (a) is usually a 1D-style helper on one row or column; part (b) uses it across the grid. Write the nested loops with r and c named clearly and keep row bound = <code>length</code>, column bound = <code>[0].length</code>. If a return inside nested loops is needed, remember it exits everything.",
        "questions": [
            {
                "stem": "What does the following method return for <code>{{1, 5}, {3, 2}, {4, 4}}</code>?\n<pre class=\"code\">public static int count(int[][] g)\n{\n    int c = 0;\n    for (int r = 0; r &lt; g.length; r++)\n    {\n        if (g[r][0] &lt; g[r][1]) c++;\n    }\n    return c;\n}</pre>",
                "options": ["0", "1", "2", "3"],
                "answer": "B",
                "explanation": "Rows where the first is less than the second: {1,5} yes; {3,2} no; {4,4} no. Count = 1.",
            },
            {
                "stem": "Which of the following correctly computes the sum of column <code>c</code> of a 2D array <code>m</code>?",
                "options": ["<code>for (int i = 0; i &lt; m[0].length; i++) sum += m[c][i];</code>", "<code>for (int i = 0; i &lt; m.length; i++) sum += m[i][c];</code>", "<code>for (int v : m[c]) sum += v;</code>", "<code>for (int i = 0; i &lt; m.length; i++) sum += m[c][i];</code>"],
                "answer": "B",
                "explanation": "A column means fixed c and varying row index i from 0 to m.length - 1. Options A, C, D all treat c as a row.",
            },
        ],
        "vocab": [
            ("Helper method", "a method that handles one piece (like a single row) and is called from a larger algorithm"),
        ],
    },
    {
        "num": 14, "title": "Searching Algorithms", "blurb": "linear search, binary search",
        "lede": "Two searches: linear works on anything, binary needs sorted data and is much faster. The exam counts comparisons.",
        "points": [
            "<strong>Linear (sequential) search:</strong> check each element from the start until found or the end is reached. Returns the index or −1. Works on any array or ArrayList.",
            "Linear search worst case: <em>n</em> comparisons (element absent or last).",
            "<strong>Binary search:</strong> requires a <strong>sorted</strong> array. Compare the target to the middle; if equal, done; if smaller, search the left half; if larger, the right half. Repeat until found or the range is empty.",
            "Binary search implementation uses <code>low</code>, <code>high</code>, and <code>mid = (low + high) / 2</code>; adjust <code>high = mid - 1</code> or <code>low = mid + 1</code>; loop while <code>low &lt;= high</code>.",
            "Binary search worst case: about log₂ n comparisons — for 1,000 elements, about 10. The exam asks \"how many elements are examined\" for a given target: trace the mid values.",
            "Binary search on an unsorted array gives wrong answers, not an error.",
            "Both searches can be written for ArrayLists using <code>get</code> and <code>size</code>.",
        ],
        "example": """
<pre class="code">public static int binarySearch(int[] a, int target)
{
    int low = 0;
    int high = a.length - 1;
    while (low &lt;= high)
    {
        int mid = (low + high) / 2;
        if (a[mid] == target) return mid;
        else if (a[mid] &lt; target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
// a = {2, 5, 8, 12, 16, 23, 38}, target 23
// mid=3 (12) &lt; 23 → low=4; mid=5 (23) → found. 2 comparisons.</pre>""",
        "tip": "For \"how many times is the target compared,\" trace mid: write low, high, mid, and the element at mid on each pass. For \"which search should be used,\" unsorted → linear; sorted and large → binary. And binary search's <code>mid</code> uses integer division — truncation matters.",
        "questions": [
            {
                "stem": "A binary search is performed on the sorted array <code>{1, 4, 7, 10, 13, 16, 19, 22}</code> for the value 4. Which elements are compared to the target, in order?",
                "options": ["10, 4", "10, 7, 4", "13, 7, 4", "1, 4"],
                "answer": "A",
                "explanation": "low=0, high=7, mid=3 → 10. 4 < 10 → high=2. mid=1 → 4. Found. Two comparisons: 10, then 4.",
            },
            {
                "stem": "Which of the following is true about binary search?",
                "options": ["It works on any array regardless of order.", "It requires the array to be sorted and eliminates about half the remaining elements with each comparison.", "It always examines every element.", "It is slower than linear search for large arrays."],
                "answer": "B",
                "explanation": "Sorted input and halving are the two defining properties.",
            },
        ],
        "vocab": [
            ("Linear search", "checking elements one by one until the target is found"),
            ("Binary search", "repeatedly halving a sorted range to locate a target"),
        ],
    },
    {
        "num": 15, "title": "Sorting Algorithms", "blurb": "selection sort, insertion sort",
        "lede": "Two sorts to know by mechanism, not memorized code: what each pass does and what the array looks like after k passes.",
        "points": [
            "<strong>Selection sort:</strong> for each position i from 0, find the smallest element in the unsorted part (i to end) and swap it into position i. After k passes, the first k elements are the k smallest, in order.",
            "Selection sort always does the same number of comparisons regardless of input order: about n²/2. It does at most n − 1 swaps.",
            "<strong>Insertion sort:</strong> for each element from index 1 onward, shift it left past larger elements until it's in place among the already-sorted prefix. After k passes, the first k + 1 elements are sorted <em>relative to each other</em> (but may not be the k + 1 smallest overall).",
            "Insertion sort is fast on nearly-sorted data (few shifts) and slow on reverse-sorted data (many shifts).",
            "The exam shows an array after some number of passes and asks which algorithm produced it, or asks for the array state after a given pass.",
            "Both are O(n²) in the worst case; merge sort (4.17) is faster for large inputs.",
        ],
        "example": """
<p>Sort <code>{5, 2, 8, 1, 9}</code>:</p>
<table class="trace"><tr><th>Pass</th><th>Selection sort</th><th>Insertion sort</th></tr>
<tr><td>1</td><td>{1, 2, 8, 5, 9} — 1 swapped to front</td><td>{2, 5, 8, 1, 9} — 2 inserted before 5</td></tr>
<tr><td>2</td><td>{1, 2, 8, 5, 9} — 2 already in place</td><td>{2, 5, 8, 1, 9} — 8 already in place</td></tr>
<tr><td>3</td><td>{1, 2, 5, 8, 9} — 5 swapped in</td><td>{1, 2, 5, 8, 9} — 1 shifted to front</td></tr>
<tr><td>4</td><td>{1, 2, 5, 8, 9}</td><td>{1, 2, 5, 8, 9}</td></tr></table>
<p>Tell-tale: after pass k, selection has the k smallest at the front; insertion has the first k + 1 in order but not necessarily the smallest.</p>""",
        "tip": "Given a mid-sort snapshot: if the first few elements are the globally smallest values in order, it's selection sort. If the first few are in order but a smaller value still sits later in the array, it's insertion sort.",
        "questions": [
            {
                "stem": "The array <code>{6, 3, 9, 1, 7}</code> is being sorted in ascending order. After two passes it is <code>{1, 3, 9, 6, 7}</code>. Which algorithm is being used?",
                "options": ["Selection sort", "Insertion sort", "Binary search", "Merge sort"],
                "answer": "A",
                "explanation": "The two smallest values (1, 3) are in the first two positions — selection sort. Insertion sort after two passes would be {3, 6, 9, 1, 7}.",
            },
            {
                "stem": "Which of the following is true of insertion sort?",
                "options": ["It always performs the same number of comparisons regardless of input.", "It performs fewer shifts when the input is already nearly sorted.", "It requires the array to be sorted before it begins.", "It cannot be used on arrays of Strings."],
                "answer": "B",
                "explanation": "Insertion sort's work depends on how far each element must shift; nearly-sorted input needs few shifts.",
            },
        ],
        "vocab": [
            ("Selection sort", "repeatedly select the smallest remaining element and swap it into place"),
            ("Insertion sort", "insert each element into its correct position within the sorted prefix"),
            ("Pass", "one full iteration of the outer loop of a sort"),
        ],
    },
    {
        "num": 16, "title": "Recursion", "blurb": "base case, recursive call, tracing",
        "lede": "A method that calls itself. On the revised exam you trace recursion — you don't write it. Know the base case, count the calls, and follow the returns back up.",
        "points": [
            "A <strong>recursive method</strong> calls itself. It needs a <strong>base case</strong> (a condition where it returns without recursing) and a <strong>recursive call</strong> that moves toward the base case.",
            "Without a reachable base case, recursion never ends — a run-time stack overflow.",
            "Each call has its own copies of parameters and local variables. Changes in one call don't affect the others.",
            "<strong>Tracing:</strong> write each call with its argument, stop at the base case, then substitute return values back up the chain. Or draw the calls as a stack.",
            "<strong>Number of calls</strong> is a common question: count every invocation including the original.",
            "Any recursive method can be rewritten with a loop, and vice versa; recursion often mirrors the structure of the problem (factorial, sum of a list, string reversal).",
            "The revised CED says you will <em>trace</em> recursive code, not write it — FRQs won't require recursion.",
        ],
        "example": """
<pre class="code">public static int f(int n)
{
    if (n &lt;= 1) return 1;          // base case
    return n * f(n - 1);           // recursive call
}
// f(4) = 4 * f(3)
//      = 4 * (3 * f(2))
//      = 4 * (3 * (2 * f(1)))
//      = 4 * (3 * (2 * 1)) = 24
// Calls made: f(4), f(3), f(2), f(1) → 4 calls

public static void printDown(int n)
{
    if (n == 0) return;
    System.out.print(n + " ");
    printDown(n - 1);
}
// printDown(3) prints: 3 2 1</pre>""",
        "tip": "Write the calls in a column, arguments decreasing, until the base case returns a concrete value. Then fill in upward. For methods that print, note whether the print happens <em>before</em> or <em>after</em> the recursive call — that reverses the order of output.",
        "questions": [
            {
                "stem": "What is returned by <code>g(5)</code>?\n<pre class=\"code\">public static int g(int n)\n{\n    if (n == 0) return 0;\n    return n + g(n - 2);\n}</pre>",
                "options": ["9", "15", "5", "The method never terminates"],
                "answer": "D",
                "explanation": "g(5) calls g(3), which calls g(1), which calls g(-1). The base case checks n == 0 exactly, and n goes 5, 3, 1, -1, -3, … skipping 0 entirely. The base case is never reached, so the recursion never stops. (A base case of n <= 0 would fix it and return 9.)",
            },
            {
                "stem": "What is printed by <code>p(3)</code>?\n<pre class=\"code\">public static void p(int n)\n{\n    if (n &gt; 0)\n    {\n        p(n - 1);\n        System.out.print(n + \" \");\n    }\n}</pre>",
                "options": ["3 2 1", "1 2 3", "3 2 1 0", "0 1 2 3"],
                "answer": "B",
                "explanation": "The print happens after the recursive call, so the deepest call prints first: 1, then 2, then 3.",
            },
            {
                "stem": "How many times is the method <code>h</code> called (including the initial call) when <code>h(8)</code> is executed?\n<pre class=\"code\">public static int h(int n)\n{\n    if (n &lt; 1) return 0;\n    return 1 + h(n / 2);\n}</pre>",
                "options": ["3", "4", "5", "8"],
                "answer": "C",
                "explanation": "h(8) → h(4) → h(2) → h(1) → h(0). Five calls.",
            },
        ],
        "vocab": [
            ("Recursion", "a method calling itself"),
            ("Base case", "the condition under which a recursive method returns without recursing"),
            ("Recursive call", "the call to the same method with an argument closer to the base case"),
        ],
    },
    {
        "num": 17, "title": "Recursive Searching and Sorting", "blurb": "recursive binary search, merge sort",
        "lede": "Binary search written recursively, and merge sort — the divide-and-conquer sort that's faster than selection and insertion. Trace, don't write.",
        "points": [
            "<strong>Recursive binary search:</strong> the same halving as the loop version, but each half-search is a recursive call with updated <code>low</code>/<code>high</code>. Base case: <code>low &gt; high</code> (not found) or the middle matches.",
            "<strong>Merge sort:</strong> split the array in half, recursively sort each half, then <strong>merge</strong> the two sorted halves into one sorted array.",
            "The merge step walks through both halves with two indices, copying the smaller front element each time, then copying any leftovers.",
            "Merge sort's base case is a sub-array of one element (already sorted).",
            "Merge sort is <strong>faster</strong> than selection or insertion sort for large inputs — roughly n log n operations instead of n². It needs extra memory for the temporary merged array.",
            "The exam may show the array at some stage of merge sort (halves sorted, not yet merged) and ask which stage or which algorithm.",
            "Both algorithms illustrate <strong>divide and conquer</strong>: split, solve pieces recursively, combine.",
        ],
        "example": """
<pre class="code">public static int bs(int[] a, int t, int low, int high)
{
    if (low &gt; high) return -1;             // base: not found
    int mid = (low + high) / 2;
    if (a[mid] == t) return mid;          // base: found
    if (a[mid] &lt; t) return bs(a, t, mid + 1, high);
    return bs(a, t, low, mid - 1);
}

// merge sort on {8, 3, 5, 1}:
//   split → {8, 3} and {5, 1}
//   sort each → {3, 8} and {1, 5}
//   merge → compare 3 vs 1 → 1; 3 vs 5 → 3; 8 vs 5 → 5; leftover 8
//   result {1, 3, 5, 8}</pre>""",
        "tip": "For merge sort traces, the snapshot after the recursive sorts but before the final merge shows two independently sorted halves — that's the give-away. For recursive binary search, count the calls the same way as 4.14 counts comparisons.",
        "questions": [
            {
                "stem": "During a merge sort of <code>{7, 2, 9, 4, 6, 1}</code>, which of the following could be the state of the array just before the final merge?",
                "options": ["{2, 7, 9, 1, 4, 6}", "{1, 2, 4, 6, 7, 9}", "{2, 7, 9, 4, 6, 1}", "{1, 2, 4, 7, 9, 6}"],
                "answer": "A",
                "explanation": "Before the final merge, each half is sorted independently: {2, 7, 9} and {1, 4, 6}.",
            },
            {
                "stem": "Which of the following best describes why merge sort is preferred over selection sort for very large arrays?",
                "options": ["Merge sort uses less memory.", "Merge sort performs roughly n log n operations rather than n², so it is much faster as n grows.", "Merge sort does not require recursion.", "Selection sort only works on sorted arrays."],
                "answer": "B",
                "explanation": "The n log n vs n² gap is the reason. Merge sort actually uses more memory.",
            },
        ],
        "vocab": [
            ("Merge sort", "recursively sort halves, then merge them"),
            ("Merge", "combining two sorted sequences into one sorted sequence"),
            ("Divide and conquer", "split a problem into smaller instances, solve recursively, combine"),
        ],
    },
]

U4 = {
    "num": 4,
    "title": "Data Collections",
    "weight": "30–40%",
    "lede": "The biggest unit and the source of three of the four FRQs. Arrays, ArrayLists, 2D arrays, then searching, sorting, and recursion. If Unit 4 is solid, a 5 is realistic.",
    "understandings": [
        "Data sets are stored in arrays, ArrayLists, and 2D arrays, each with its own creation, access, and traversal rules.",
        "Standard algorithms — sum, max, count, filter, search, sort — are applied across all three structures.",
        "Text files are read with Scanner and File, and wrapper classes let numbers live in ArrayLists.",
        "Recursion is traced (not written), including recursive binary search and merge sort.",
    ],
    "topics": U4_A + U4_B,
}

UNITS = [U1, U2, U3, U4]
