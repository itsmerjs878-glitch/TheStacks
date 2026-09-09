# -*- coding: utf-8 -*-
"""
The Stacks — AP CSP content.
Structure follows the College Board Course and Exam Description (CED):
5 Big Ideas, 35 topics. Edit here, then run `python3 build.py`.
All notes, examples, and practice questions are original.
"""

COURSE = {
    "title": "AP Computer Science Principles",
    "intro": """
<p>Everything on the AP CSP exam, organized exactly the way the College Board's Course and Exam Description (CED) organizes it: five Big Ideas, 35 numbered topics. Each topic page has the essential knowledge, a worked example, an exam tip, practice questions in the real exam's style, and the vocabulary you'll be tested on.</p>
""",
    "exam_format": """
<section class="block">
  <h2>How the exam works</h2>
  <ul class="points">
    <li><strong>Section I — End-of-course multiple choice.</strong> 70 questions, 120 minutes, 70% of your score. Every question has 4 options. Most are single-select; a handful are multi-select where you must pick <em>two</em> correct answers to get credit.</li>
    <li><strong>Section II — Create Performance Task.</strong> 30% of your score. You build a program during the year (at least 12 hours of class time), submit the code and a video, then answer written-response prompts about it on exam day.</li>
    <li>There is no penalty for guessing on multiple choice — answer every question.</li>
    <li>All code on the exam is in <strong>AP pseudocode</strong> (text-based and block-based). A reference sheet is provided, but you're expected to read it fluently, not learn it during the test.</li>
    <li>Roughly 25% of questions are code-analysis: given a snippet, predict output, find the bug, or pick the equivalent code. Practice tracing by hand, line by line, with a table of variable values.</li>
  </ul>
</section>
""",
    "five_tips": """
<section class="block">
  <h2>What separates a 5 from a 3</h2>
  <ul class="points">
    <li><strong>Trace code with a variable table.</strong> The most common lost points are careless tracing errors in Big Idea 3 — writing each variable's value after every line catches them.</li>
    <li><strong>Know the exam's vocabulary precisely.</strong> Lossy vs. lossless, procedural vs. data abstraction, parallel vs. distributed, sequential vs. selection vs. iteration — many questions are essentially "which term describes this scenario."</li>
    <li><strong>Weigh both sides in Big Idea 5.</strong> Impact questions reward answers that acknowledge an innovation can be beneficial for one group and harmful for another; extreme, one-sided options are usually wrong.</li>
    <li><strong>Read the whole stem.</strong> Distractors are built from a partial reading. Underline what is actually being asked (output? number of iterations? which change preserves behavior?).</li>
    <li><strong>Spend proportionally.</strong> Big Idea 3 (30–35%) and Big Idea 5 (21–26%) are over half the multiple choice. Study time should mirror that.</li>
  </ul>
</section>
""",
}

# ----------------------------------------------------------------------
# BIG IDEA 1
# ----------------------------------------------------------------------

BI1 = {
    "num": 1,
    "title": "Creative Development",
    "weight": "10–13%",
    "lede": "This Big Idea is about the process of making software: collaborating, defining a program's purpose, designing and iterating, and hunting down errors. It's the smallest slice of the multiple choice, but its vocabulary is exactly what the Create Task written responses are graded on.",
    "understandings": [
        "Collaboration produces better programs than one person working alone, and effective collaboration is a skill with specific practices.",
        "Every program has a purpose, and programs can produce results beyond that purpose — including new knowledge for the person who wrote it.",
        "Developers use an iterative, incremental process with planning tools, documentation, and testing, rather than writing everything at once.",
        "Errors are a normal part of development; there are distinct types of errors and systematic ways to find and fix them.",
    ],
    "topics": [
        {
            "num": 1, "title": "Collaboration", "blurb": "teams, pair programming",
            "lede": "Programs get built by people working together. The CED cares about why collaboration helps and what makes it work.",
            "points": [
                "Collaboration brings together people with <strong>different perspectives, skills, and experiences</strong>, which produces programs that are more innovative, more accurate, and less biased than solo work.",
                "It helps at <em>every</em> stage: planning, designing, coding, testing, and reviewing. Collaboration is not only for splitting up work.",
                "<strong>Pair programming</strong> is the CED's named example: two people share one workstation. The <strong>driver</strong> writes code; the <strong>navigator</strong> reviews each line and thinks ahead. Roles switch regularly.",
                "Effective collaboration requires <strong>communication, consensus building, conflict resolution, and negotiation</strong> — the exam treats these as real skills, not soft filler.",
                "Feedback from users, teachers, and peers is part of collaboration. Incorporating it makes the final product better match what people actually need.",
                "Online tools (shared repositories, version control, messaging) let people collaborate without being in the same room.",
            ],
            "example": """
<p>A team of three is building a study-timer app. One student likes minimal interfaces, one has strong design skills, one has used timers that annoyed them with too many alerts. Because they combine perspectives, the final design has a clean interface with a single, adjustable alert — something none of them would have built alone. That "different perspectives → better product" logic is what an exam question about collaboration is fishing for.</p>""",
            "tip": "When a question asks why collaboration helped, the correct option almost always mentions <em>diverse perspectives</em>, <em>reduced bias</em>, or <em>catching errors earlier</em>. Options claiming collaboration makes programs run faster or use less memory are distractors — collaboration is about the people process, not program performance.",
            "questions": [
                {
                    "stem": "Two students are working on a program together. One student types code while the other watches, reviews each line, and suggests improvements. After twenty minutes they switch roles. Which of the following best describes this practice?",
                    "options": ["Pair programming", "Iterative development", "Code documentation", "Procedural abstraction"],
                    "answer": "A",
                    "explanation": "One person writing (driver) while the other reviews (navigator), with roles swapping, is the definition of pair programming.",
                },
                {
                    "stem": "Which of the following is a benefit of developing a program with a diverse team rather than alone?",
                    "options": ["The program will always run more efficiently.", "The team is less likely to build in unintentional bias, because members bring different perspectives.", "The program will require less testing.", "Documentation becomes unnecessary."],
                    "answer": "B",
                    "explanation": "The CED explicitly ties diverse collaboration to reduced bias and better design. Efficiency, testing needs, and documentation are unaffected.",
                },
            ],
            "vocab": [
                ("Pair programming", "two programmers share one workstation; one writes (driver) while the other reviews (navigator), switching regularly"),
                ("Collaboration", "working together throughout development to combine perspectives and skills"),
            ],
        },
        {
            "num": 2, "title": "Program Function and Purpose", "blurb": "why programs exist, inputs and outputs",
            "lede": "Every program is written to do something for someone. This topic covers how to describe a program's purpose, function, and its inputs and outputs — vocabulary that comes straight back in the Create Task.",
            "points": [
                "A <strong>program</strong> (or software) is a collection of statements executed by a computer to complete a task.",
                "Programs are written to solve problems, express creativity, satisfy personal curiosity, or generate new knowledge. The CED distinguishes the program's <strong>purpose</strong> (what problem/need it addresses) from its <strong>function</strong> (what it actually does when it runs).",
                "<strong>Inputs</strong> are data the program receives — from a user (tactile, audio, visual, text), from a file, from a sensor, or from another program. <strong>Outputs</strong> are what it produces: text, graphics, audio, or data sent elsewhere.",
                "An <strong>event</strong> is an action (mouse click, key press, sensor reading) that triggers a specific program response. Event-driven programs run code in response to events rather than in a fixed sequence.",
                "Program behavior is defined by how it responds to inputs; the same program can produce different outputs given different inputs.",
                "A <strong>code segment</strong> is a portion of a larger program. A <strong>code statement</strong> is one complete instruction. The exam uses both terms.",
            ],
            "example": """
<p>A weather program's <strong>purpose</strong> is to help someone decide what to wear. Its <strong>function</strong> is: take a ZIP code as input, request a forecast from a weather service, and display the high, low, and chance of rain. The user typing a ZIP code is an <strong>input</strong>; the displayed forecast is an <strong>output</strong>; pressing "refresh" is an <strong>event</strong> that triggers a new request. On the Create Task you must describe your own program in exactly these terms.</p>""",
            "tip": "The Create Task written response asks you to state your program's purpose and its function separately. Purpose = the human problem it addresses. Function = the behavior when it runs. Practice writing both in one sentence each for any program you look at.",
            "questions": [
                {
                    "stem": "A student writes a program that displays a random motivational quote each time the user clicks a button. Which of the following best describes the role of the button click in this program?",
                    "options": ["An output of the program", "A procedure that must be defined by the user", "An event that triggers the program to run a segment of code", "A data abstraction that stores the quotes"],
                    "answer": "C",
                    "explanation": "A user action that causes the program to respond is an event. The quote displayed is the output; the click is the trigger.",
                },
                {
                    "stem": "Which of the following best distinguishes the purpose of a program from its function?",
                    "options": ["Purpose is what the program does when it runs; function is the problem it solves.", "Purpose is the problem or need the program addresses; function is how the program behaves when it runs.", "Purpose refers to the program's inputs; function refers to its outputs.", "Purpose is defined by the computer; function is defined by the user."],
                    "answer": "B",
                    "explanation": "This is the CED's definition and the exact distinction the Create Task asks you to write about.",
                },
            ],
            "vocab": [
                ("Program", "a collection of statements a computer executes to accomplish a task"),
                ("Input", "data a program receives from a user, file, sensor, or another program"),
                ("Output", "data or behavior a program produces, such as text, graphics, or audio"),
                ("Event", "an action, such as a click or key press, that triggers a program response"),
                ("Code segment", "a portion of a program's code"),
            ],
        },
        {
            "num": 3, "title": "Program Design and Development", "blurb": "iteration, documentation, abstraction",
            "lede": "The CED describes a specific development process: investigate, design, prototype, test, repeat. Knowing the vocabulary for each piece — and what documentation is for — is worth several exam questions.",
            "points": [
                "A <strong>development process</strong> can be ordered and structured or exploratory, but good ones share phases: <strong>investigating</strong> and reflecting, <strong>designing</strong>, <strong>prototyping</strong>, and <strong>testing</strong>.",
                "<strong>Iterative development</strong> means going through those phases repeatedly, improving with each cycle. <strong>Incremental development</strong> means building and testing one small piece at a time and adding to what already works.",
                "The <em>investigating</em> phase includes understanding the users: surveys, interviews, observation, and gathering requirements about what the program needs to do and for whom.",
                "The <em>designing</em> phase includes brainstorming, planning the user interface, and using tools such as <strong>flowcharts</strong> or <strong>pseudocode</strong> to lay out an algorithm before writing real code.",
                "<strong>Program documentation</strong> — comments inside the code plus external descriptions — explains what a program does and how, so it can be understood, maintained, and reused later by the author or others. Documentation should be written during development, not only at the end.",
                "<strong>Comments</strong> are the in-code form of documentation; the computer ignores them. Good comments explain <em>why</em> and <em>what</em>, not just restate the line.",
                "<strong>Abstraction</strong> underpins good design: managing complexity by focusing on what something does rather than how. Using a procedure or a list is a form of abstraction.",
                "Requirements can change during development — that's normal, and iteration is how developers accommodate it.",
            ],
            "example": """
<p>Building a grade-calculator: (1) <em>Investigate</em> — ask three classmates what they want; they all want weighted categories. (2) <em>Design</em> — sketch the screen and write pseudocode for the weighted average. (3) <em>Prototype</em> — code just the average for one category and confirm it's right. (4) <em>Test</em> — try zero grades, a 100, a missing category. Then loop back: add the second category, test again. Each loop is an <em>iteration</em>; adding one category at a time is <em>incremental</em>. The comments you write during step 3 are <em>documentation</em>.</p>""",
            "tip": "If a question describes a team that repeatedly revisits earlier phases after testing, the answer is <em>iterative</em>. If it describes adding features one working piece at a time, the answer is <em>incremental</em>. They often happen together, but the exam tests them as separate terms.",
            "questions": [
                {
                    "stem": "A programmer builds a small working version of a game with one level, tests it, then adds a second level and tests again, continuing until all levels are done. Which development approach does this best illustrate?",
                    "options": ["Incremental development", "Sequential execution", "Data abstraction", "Fault-tolerant design"],
                    "answer": "A",
                    "explanation": "Building and testing one piece at a time on top of working code is incremental development.",
                },
                {
                    "stem": "Which of the following is the primary reason to include comments in program code?",
                    "options": ["Comments make the program execute faster.", "Comments are required for the program to compile.", "Comments help programmers understand the purpose and behavior of code when they return to it later.", "Comments prevent runtime errors."],
                    "answer": "C",
                    "explanation": "Comments are documentation for humans. They have no effect on execution or errors.",
                },
            ],
            "vocab": [
                ("Iterative development", "repeatedly cycling through design, build, and test phases to refine a program"),
                ("Incremental development", "building a program in small pieces, testing each before adding the next"),
                ("Prototype", "an early, partial version of a program used to test ideas"),
                ("Documentation", "written descriptions and comments that explain what a program does and how it works"),
                ("Comment", "a note inside code intended for humans and ignored by the computer"),
                ("Requirements", "a description of what a program must do, often gathered from users"),
            ],
        },
        {
            "num": 4, "title": "Identifying and Correcting Errors", "blurb": "syntax, logic, runtime, overflow",
            "lede": "The exam names four kinds of errors and expects you to classify a scenario into the right one, then know how to find and fix it.",
            "points": [
                "<strong>Syntax error:</strong> the code violates the rules of the language (missing parenthesis, misspelled keyword). The program cannot run at all until it's fixed.",
                "<strong>Logic error:</strong> the code runs and finishes, but the result is wrong because the reasoning is flawed — e.g., using <code>&lt;</code> where <code>&le;</code> was intended, or an off-by-one loop bound.",
                "<strong>Run-time error:</strong> the code is syntactically valid but hits a problem while executing — dividing by zero, accessing index 0 or index beyond a list's length — and stops.",
                "<strong>Overflow error:</strong> the result of a calculation is too large for the computer to store in the fixed number of bits available for it. Related: <strong>round-off error</strong>, where real numbers can't be represented exactly.",
                "<strong>Testing</strong> means running the program with chosen inputs and comparing the actual output to the expected output. Good test cases include normal values, boundary values, and invalid or empty inputs.",
                "<strong>Debugging</strong> is the process of finding and fixing errors. Common strategies: <strong>hand-tracing</strong> (executing line by line on paper with a variable table), adding <strong>extra output statements</strong> to see intermediate values, and <strong>testing with different inputs</strong> to isolate the failing case.",
                "Some errors can be caught before running (syntax); most logic errors are only found by testing.",
            ],
            "example": """
<pre class="code">count ← 0
FOR EACH score IN scores
{
    IF (score > 90)
    {
        count ← count + 1
    }
}
DISPLAY(count)</pre>
<p>Intended purpose: count scores of 90 or above. This runs with no error message, but a score of exactly 90 isn't counted because the condition uses <code>&gt;</code> instead of <code>&ge;</code>. That's a <strong>logic error</strong>. You'd only catch it by testing with a score of 90 — which is why boundary values belong in every test set.</p>""",
            "tip": "Classify by symptom. Won't run at all → syntax. Runs, then crashes partway → run-time. Runs to the end with the wrong answer → logic. Result is a nonsense huge/tiny number → overflow. The exam rarely asks you to name the error type without giving you one of these symptoms.",
            "questions": [
                {
                    "stem": "A program is intended to calculate the average of a list of numbers. It runs to completion and displays a value, but the value is incorrect because the program divides by the wrong count. Which type of error is this?",
                    "options": ["Syntax error", "Logic error", "Run-time error", "Overflow error"],
                    "answer": "B",
                    "explanation": "The program runs and finishes but produces the wrong result, which is the signature of a logic error.",
                },
                {
                    "stem": "A program attempts to access the element at index 8 of a list that contains only 5 elements. The program stops executing and reports an error. Which type of error occurred?",
                    "options": ["Syntax error", "Logic error", "Run-time error", "Overflow error"],
                    "answer": "C",
                    "explanation": "The code was valid, but a problem during execution (an out-of-range index) caused it to stop — a run-time error.",
                },
                {
                    "stem": "Which of the following is the most effective way to determine whether a program's loop produces the intended result for boundary values?",
                    "options": ["Read the code once quickly.", "Hand-trace the program with test inputs at the boundaries, recording each variable's value.", "Remove all comments from the program.", "Rename the variables."],
                    "answer": "B",
                    "explanation": "Hand-tracing with specific test inputs is the CED's named debugging technique for exactly this situation.",
                },
            ],
            "vocab": [
                ("Syntax error", "a mistake in the code's structure that prevents it from running"),
                ("Logic error", "a mistake in the algorithm that produces incorrect output while the program still runs"),
                ("Run-time error", "an error that occurs during execution and stops the program"),
                ("Overflow error", "a result too large to be represented in the available bits"),
                ("Round-off error", "an error from real numbers that cannot be represented exactly in binary"),
                ("Hand-tracing", "stepping through code manually, tracking each variable's value"),
                ("Debugging", "finding and fixing errors in a program"),
            ],
        },
    ],
}

# ----------------------------------------------------------------------
# BIG IDEA 2
# ----------------------------------------------------------------------

BI2 = {
    "num": 2,
    "title": "Data",
    "weight": "17–22%",
    "lede": "How computers represent, store, compress, and extract meaning from data. Students underrate this Big Idea because the topics seem simple, then lose points on the precise distinctions — lossy vs. lossless, correlation vs. causation, data vs. information.",
    "understandings": [
        "Everything a computer stores is binary, and the number of bits determines how many distinct values can be represented.",
        "Compression trades file size against fidelity; lossless keeps everything, lossy discards some.",
        "Data by itself is not information — information comes from processing, filtering, combining, and interpreting data in context.",
        "Programs are what make large-scale data analysis possible, and cleaning data is a real, necessary step.",
    ],
    "topics": [
        {
            "num": 1, "title": "Binary Numbers", "blurb": "bits, bytes, base conversion",
            "lede": "All data on a computer is stored as sequences of bits. You need to convert between binary and decimal fluently and understand how the number of bits limits what can be represented.",
            "points": [
                "A <strong>bit</strong> is a single binary digit: 0 or 1. A <strong>byte</strong> is 8 bits.",
                "Binary is <strong>base 2</strong>: each place value is a power of 2 (from the right: 1, 2, 4, 8, 16, 32, 64, 128 …). Decimal is <strong>base 10</strong>, with place values that are powers of 10.",
                "<strong>Binary → decimal:</strong> add the place values where there's a 1. <code>1101</code> = 8 + 4 + 0 + 1 = 13.",
                "<strong>Decimal → binary:</strong> repeatedly subtract the largest power of 2 that fits. 22 → 16 (leaves 6) → 4 (leaves 2) → 2 (leaves 0), so 22 = <code>10110</code>.",
                "<em>n</em> bits can represent <strong>2<sup>n</sup></strong> distinct values. 8 bits → 256 values (0–255). Adding one bit <em>doubles</em> the number of possible values.",
                "Numbers, text, images, and sound are all stored as binary once encoded. Text uses a scheme that maps each character to a number (ASCII, Unicode); an image maps each pixel to numbers for its color; audio is <strong>sampled</strong> at regular intervals and each sample stored as a number.",
                "A <strong>fixed number of bits</strong> for a value means a maximum representable size — the source of overflow errors. Some languages use a fixed size; others (and AP pseudocode) treat integers as arbitrary-size, so overflow is a real-world issue rather than a pseudocode one.",
                "Real numbers are stored with limited precision, so calculations can produce small <strong>round-off errors</strong>.",
            ],
            "example": """
<p><strong>Convert <code>10011</code> to decimal.</strong> Place values from the right: 1, 2, 4, 8, 16. Ones are in the 16, 2, and 1 places → 16 + 2 + 1 = <strong>19</strong>.</p>
<p><strong>Convert 45 to binary.</strong> 32 fits (13 left) → 8 fits (5 left) → 4 fits (1 left) → 1 fits (0 left). Bits set: 32, 8, 4, 1 → <code>101101</code>. Check: 32 + 8 + 4 + 1 = 45.</p>
<p><strong>How many colors can 3 bits represent?</strong> 2<sup>3</sup> = 8. With 4 bits, 16. Each added bit doubles the count.</p>""",
            "tip": "Write the place values above the bits (…32 16 8 4 2 1) before converting — it removes almost every arithmetic slip. For \"how many values\" questions, the answer is always a power of 2 equal to 2 raised to the number of bits, not the number of bits itself.",
            "questions": [
                {
                    "stem": "What is the decimal value of the binary number 101110?",
                    "options": ["42", "44", "46", "48"],
                    "answer": "C",
                    "explanation": "Place values 32, 16, 8, 4, 2, 1 with bits 1,0,1,1,1,0 → 32 + 8 + 4 + 2 = 46.",
                },
                {
                    "stem": "A game stores each player's level using 4 bits. The developers want to allow more than 16 levels. What is the minimum number of bits needed to represent 20 distinct levels?",
                    "options": ["4", "5", "10", "20"],
                    "answer": "B",
                    "explanation": "4 bits gives 2⁴ = 16 values, not enough. 5 bits gives 2⁵ = 32 values, which covers 20. The answer is the smallest n with 2ⁿ ≥ 20.",
                },
                {
                    "stem": "Which of the following is a true statement about how computers represent data?",
                    "options": ["Only numbers can be stored as binary; text and images require a different representation.", "Each additional bit used to store a value halves the number of possible values.", "Text, images, and sound are all represented as binary sequences after being encoded as numbers.", "A byte can represent 8 different values."],
                    "answer": "C",
                    "explanation": "All data types are ultimately binary. Adding a bit doubles (not halves) values, and a byte represents 256 values, not 8.",
                },
            ],
            "vocab": [
                ("Bit", "a single binary digit, 0 or 1"),
                ("Byte", "8 bits"),
                ("Binary (base 2)", "a number system with two digits, where each place is a power of 2"),
                ("Decimal (base 10)", "the everyday number system, where each place is a power of 10"),
                ("Overflow error", "a value exceeds what its fixed number of bits can hold"),
                ("Sampling", "measuring an analog signal, like sound, at regular intervals to store it digitally"),
            ],
        },
        {
            "num": 2, "title": "Data Compression", "blurb": "lossless vs. lossy",
            "lede": "The single most-tested distinction in this Big Idea. Compression shrinks data; the question is always whether the original can be rebuilt.",
            "points": [
                "<strong>Data compression</strong> reduces the number of bits needed to store or transmit data. Fewer bits means less storage and faster transfer.",
                "<strong>Lossless compression</strong> reduces size while allowing <em>complete reconstruction</em> of the original. Used where every bit matters: text, program code, spreadsheets, and formats like PNG and ZIP. It typically achieves smaller savings.",
                "<strong>Lossy compression</strong> permanently removes some data to achieve <em>much greater</em> size reduction. The original cannot be exactly rebuilt, but the loss may be imperceptible. Used for JPEG images, MP3 audio, and streaming video.",
                "The <strong>trade-off:</strong> lossy gives smaller files at the cost of fidelity. The right choice depends on whether exact reconstruction is required and how much quality loss is acceptable.",
                "The amount of compression possible depends on the data: highly repetitive data compresses well losslessly (e.g., long runs of the same value); already-random data barely compresses.",
                "Decisions about compression are made based on the purpose: archiving a legal document → lossless; sending a photo to a friend → lossy is fine.",
            ],
            "example": """
<p>The text <code>AAAAAAABBBBBCCC</code> can be stored losslessly as <code>7A5B3C</code> — the original is exactly recoverable from the counts. That's the idea behind <em>run-length encoding</em>, a simple lossless technique. A photo, by contrast, might have thousands of nearly-identical blue-sky pixels; a lossy scheme averages them into fewer values, saving far more space, but the exact original pixels are gone.</p>""",
            "tip": "If the stem says the file must be \"exactly\" or \"perfectly\" restored, or involves text/code/financial records, answer lossless. If it emphasizes minimizing size or transmission time and the data is an image, video, or audio where small quality loss is acceptable, answer lossy. Also remember: compression is about size and speed — not security.",
            "questions": [
                {
                    "stem": "A hospital needs to store patient X-ray images so that every detail can be recovered exactly for later diagnosis, even if the files take more storage. Which compression approach is most appropriate?",
                    "options": ["Lossy compression, because it reduces file size the most", "Lossless compression, because the original image can be fully reconstructed", "No compression is possible for image data", "Encryption, because it makes the file smaller"],
                    "answer": "B",
                    "explanation": "Exact reconstruction is required, so lossless. Encryption is about security, not size.",
                },
                {
                    "stem": "Which of the following best describes a trade-off of using lossy compression for a video that will be streamed over a slow connection?",
                    "options": ["The video will be larger but higher quality.", "The video will be smaller and faster to transmit, but some detail is permanently lost.", "The video can be perfectly reconstructed, but only after transmission completes.", "The video cannot be played until decompressed by the sender."],
                    "answer": "B",
                    "explanation": "Lossy = big size reduction (good for slow connections) at the cost of irrecoverable detail.",
                },
            ],
            "vocab": [
                ("Data compression", "reducing the number of bits needed to represent data"),
                ("Lossless compression", "compression from which the original data can be completely reconstructed"),
                ("Lossy compression", "compression that permanently discards some data for greater size reduction"),
            ],
        },
        {
            "num": 3, "title": "Extracting Information from Data", "blurb": "data vs. information, metadata, correlation",
            "lede": "Raw data isn't knowledge. This topic is about the steps between a pile of records and an actual conclusion — and the traps along the way.",
            "points": [
                "<strong>Information</strong> is the collection of facts and patterns extracted from data. Data becomes information when it's processed, organized, and interpreted.",
                "Programs make it possible to find patterns in datasets far too large for a person to read — this is why computing transformed fields from medicine to sports.",
                "<strong>Metadata</strong> is data about data: a photo's timestamp and location, a file's author, an email's routing headers. Metadata can be used to organize, search, and filter data, and changing or deleting it does not change the underlying data.",
                "Common operations for extracting information: <strong>filtering</strong> (keeping records that meet a condition), <strong>sorting</strong>, <strong>searching</strong>, <strong>aggregating</strong> (sum, average, count), and <strong>visualizing</strong> (charts, graphs) to make patterns visible.",
                "Combining data from <strong>multiple sources</strong> can reveal relationships not visible in any single source.",
                "<strong>Correlation is not causation.</strong> Two things trending together doesn't mean one causes the other. The exam tests this directly.",
                "Data can be <strong>incomplete, invalid, or biased</strong> — from how it was collected, who was included, or how it was cleaned. Conclusions inherit those flaws.",
                "The <strong>scale</strong> of data matters: large datasets may need distributed or parallel processing, and challenges include storage size, transfer time, and cleaning.",
                "<strong>Privacy concerns</strong> arise because metadata and combined datasets can identify or track people even when no single record seems sensitive.",
            ],
            "example": """
<p>A school's attendance system stores 40,000 rows: student ID, date, period, present/absent. That's <em>data</em>. A program filters to first period, groups by day of week, and computes the absence rate — revealing Mondays have 30% more absences. That's <em>information</em>. If someone then claims \"Monday <em>causes</em> absences,\" that's the correlation/causation trap; a sports schedule or bus route could be the real driver. The row's timestamp and the ID of the device that recorded it are <em>metadata</em>.</p>""",
            "tip": "When a question presents a dataset and a conclusion, ask: does the data actually support that, or could something else explain it? Options that claim causation from a correlation are wrong. Options that say more data or a controlled comparison is needed are usually right.",
            "questions": [
                {
                    "stem": "A study finds that cities with more ice cream shops also have higher rates of sunburn. Which of the following is the most reasonable conclusion?",
                    "options": ["Ice cream shops cause sunburn.", "Sunburn causes people to open ice cream shops.", "There is a correlation, likely explained by a third factor such as warm, sunny weather.", "The data must be incorrect."],
                    "answer": "C",
                    "explanation": "This is the classic correlation-not-causation setup. A shared cause (weather) explains both.",
                },
                {
                    "stem": "A photograph file contains information about the date it was taken, the camera model, and the GPS location. Which of the following best describes this information?",
                    "options": ["Lossy compression", "Metadata", "An algorithm", "A run-time error"],
                    "answer": "B",
                    "explanation": "Data describing the photo, rather than the photo's pixels themselves, is metadata.",
                },
                {
                    "stem": "Which of the following best explains how a program can help extract information from a dataset of millions of customer purchases?",
                    "options": ["The program can filter, sort, and aggregate the records to reveal patterns too large for a person to find by hand.", "The program guarantees the data contains no bias.", "The program converts the data into a smaller file so it can be read manually.", "The program removes the need for data cleaning."],
                    "answer": "A",
                    "explanation": "Filtering, sorting, and aggregating at scale is exactly what programs add. They do not remove bias or the need to clean data.",
                },
            ],
            "vocab": [
                ("Information", "facts and patterns extracted from data through processing and interpretation"),
                ("Metadata", "data that describes other data, such as a file's creation date or location"),
                ("Correlation", "two variables tending to change together, which does not by itself prove one causes the other"),
                ("Filtering", "selecting only the records that meet a condition"),
                ("Cleaning data", "fixing or removing incomplete, invalid, or inconsistent records"),
            ],
        },
        {
            "num": 4, "title": "Using Programs with Data", "blurb": "cleaning, transforming, visualizing",
            "lede": "This topic closes the loop: programs are the tool for turning large datasets into answers, and that means handling messy data and asking well-formed questions.",
            "points": [
                "Programs can process data to <strong>discover information and generate new knowledge</strong> — automating what would be impossible manually at scale.",
                "<strong>Data cleaning</strong> is a necessary, real step: making data uniform (same date formats, consistent capitalization), removing duplicates, and handling missing or invalid values, all <em>without changing the meaning</em> of the data.",
                "Programs can <strong>transform</strong> data — reformat, combine, or derive new values — to make analysis possible (e.g., converting temperatures to one unit, computing an average per row).",
                "<strong>Visualization</strong> (charts, graphs, maps) communicates information in a dataset in a way that's much easier to interpret than the raw table.",
                "Extracting information requires asking a question first, then choosing which data, transformations, and tools answer it. Not every question can be answered by the data available.",
                "Tools include spreadsheets, purpose-built programs, and code; the process is the same regardless of tool.",
                "The knowledge gained from data can raise <strong>new questions</strong>, driving another round of collection and analysis (iteration again).",
            ],
            "example": """
<p>You export a class survey to a spreadsheet. Some students typed \"yes\", others \"Yes\", others \"Y\". A program that normalizes all of these to <code>yes</code> is <em>cleaning</em>. Adding a column that converts \"hours per week\" from text like \"3h\" to the number 3 is <em>transforming</em>. Plotting hours-studied against grade is <em>visualizing</em>. Only after all three can you ask whether studying correlates with grades — and remember 2.3's warning about what a correlation does and doesn't show.</p>""",
            "tip": "A question about \"making data uniform so a program can process it\" wants the answer <em>cleaning</em>. Cleaning never changes what the data means — if an option describes altering values to get a desired result, that's data manipulation, not cleaning, and it's wrong.",
            "questions": [
                {
                    "stem": "A dataset of survey responses contains the values \"NY\", \"New York\", and \"new york\" for the same state. A programmer writes code to change all three to \"New York\" before analysis. Which of the following best describes this step?",
                    "options": ["Lossy compression", "Data cleaning", "Encryption", "Creating metadata"],
                    "answer": "B",
                    "explanation": "Making inconsistent values uniform without changing their meaning is data cleaning.",
                },
                {
                    "stem": "Which of the following is most likely to help a researcher communicate a pattern found in a large dataset to a general audience?",
                    "options": ["Displaying the full raw table of every record", "Creating a visualization such as a chart or graph of the pattern", "Compressing the dataset with a lossless algorithm", "Removing all metadata from the dataset"],
                    "answer": "B",
                    "explanation": "Visualization exists to make information in data interpretable. The other options don't communicate a pattern.",
                },
            ],
            "vocab": [
                ("Data cleaning", "making data uniform and valid without changing its meaning"),
                ("Data transformation", "reformatting or deriving values from data to enable analysis"),
                ("Visualization", "representing data graphically to make patterns easier to interpret"),
            ],
        },
    ],
}

# ----------------------------------------------------------------------
# BIG IDEA 3 (part 1: 3.1 – 3.9)
# ----------------------------------------------------------------------

BI3_TOPICS_A = [
    {
        "num": 1, "title": "Variables and Assignments", "blurb": "storing and updating values",
        "lede": "The foundation of every code-tracing question. A variable holds one value at a time, and assignment replaces it.",
        "points": [
            "A <strong>variable</strong> is a named abstraction for a value stored in memory. It holds <em>one</em> value at a time; assigning a new value replaces the old one.",
            "AP pseudocode uses <code>a ← expression</code> for assignment. The right side is evaluated <em>first</em>, then the result is stored in the variable on the left.",
            "Because the right side is evaluated first, <code>x ← x + 1</code> means \"take the current value of x, add 1, store it back in x.\"",
            "<strong>Data types</strong> matter: numbers, Booleans (true/false), strings (text), and lists. Operations behave differently depending on type.",
            "Assigning a variable's value to another variable <em>copies</em> the value at that moment. Later changes to one don't affect the other.",
            "Good variable names (<code>totalScore</code>, not <code>t</code>) are a form of documentation and reduce logic errors.",
            "Swapping two values requires a third, temporary variable: <code>temp ← a</code>, <code>a ← b</code>, <code>b ← temp</code>.",
        ],
        "example": """
<pre class="code">a ← 5
b ← a
a ← a + 3
DISPLAY(a)
DISPLAY(b)</pre>
<p>Trace it: <code>a</code> = 5. <code>b</code> gets a copy of 5. Then <code>a</code> becomes 5 + 3 = 8. <code>b</code> is still 5 — copying happened before <code>a</code> changed. Output: <strong>8 5</strong>. (<code>DISPLAY</code> outputs its value followed by a space.)</p>""",
        "tip": "On any tracing question, draw a two-column table: variable name, current value. Update one row per line of code. Nearly every wrong answer on these questions comes from doing the update in your head and slipping.",
        "questions": [
            {
                "stem": "Consider the following code segment.\n<pre class=\"code\">x ← 10\ny ← x\nx ← 20\nDISPLAY(y)</pre>What is displayed?",
                "options": ["10", "20", "30", "Nothing; the code has an error"],
                "answer": "A",
                "explanation": "y received a copy of x's value (10) at the time of assignment. Changing x afterward does not change y.",
            },
            {
                "stem": "Which of the following code segments correctly swaps the values of variables <code>a</code> and <code>b</code>?",
                "options": ["<code>a ← b</code><br><code>b ← a</code>", "<code>temp ← a</code><br><code>a ← b</code><br><code>b ← temp</code>", "<code>a ← b</code><br><code>b ← temp</code>", "<code>b ← a</code><br><code>a ← b</code>"],
                "answer": "B",
                "explanation": "Without a temporary variable, the first assignment overwrites one of the values before it can be copied. Option B saves a first.",
            },
        ],
        "vocab": [
            ("Variable", "a named storage location that holds one value at a time"),
            ("Assignment", "storing the result of an expression in a variable, written with ← in AP pseudocode"),
            ("Data type", "the kind of value a variable holds: number, Boolean, string, or list"),
        ],
    },
    {
        "num": 2, "title": "Data Abstraction", "blurb": "lists as a way to manage complexity",
        "lede": "A list lets one name refer to many related values. That's data abstraction, and it's one of the two abstraction types the Create Task explicitly grades.",
        "points": [
            "<strong>Data abstraction</strong> provides a separation between the abstract properties of a data type and the concrete details of its representation. Practically: a <strong>list</strong> lets you treat a whole collection as one thing.",
            "A list is an <strong>ordered sequence</strong> of elements. Each element is referenced by its <strong>index</strong>. In AP pseudocode, indexing starts at <strong>1</strong>, so the first element is <code>list[1]</code> and the last is <code>list[LENGTH(list)]</code>.",
            "Lists <strong>manage complexity</strong>: instead of <code>score1</code>, <code>score2</code>, … <code>score30</code>, you use one list <code>scores</code> and loop over it. Adding a 31st score requires no code changes.",
            "The Create Task requires you to identify a list in your program and explain how it manages complexity — this exact phrase. The answer is about handling many values with one name and code that works regardless of how many there are.",
            "A <strong>string</strong> is also an ordered sequence (of characters), and a list can contain strings, numbers, Booleans, or even other lists.",
            "Using a list in place of many separate variables makes the program <em>easier to develop, maintain, and read</em>.",
        ],
        "example": """
<p>Without a list, averaging five test scores means five variables and a formula that must be rewritten if a sixth test is added. With a list:</p>
<pre class="code">scores ← [88, 92, 79, 95, 84]
total ← 0
FOR EACH s IN scores
{
    total ← total + s
}
DISPLAY(total / LENGTH(scores))</pre>
<p>Add a sixth score to the list and nothing else changes. That's the \"manages complexity\" argument the Create Task wants.</p>""",
        "tip": "Index questions are a constant source of lost points. AP pseudocode is 1-indexed. <code>list[0]</code> is an error. If a question shows real-language code (Python-style), it will say so — otherwise assume 1-based.",
        "questions": [
            {
                "stem": "In AP pseudocode, what is displayed by the following code?\n<pre class=\"code\">names ← [\"Ava\", \"Ben\", \"Cy\", \"Dee\"]\nDISPLAY(names[3])</pre>",
                "options": ["Ava", "Ben", "Cy", "Dee"],
                "answer": "C",
                "explanation": "Indexing starts at 1, so names[3] is the third element, \"Cy\".",
            },
            {
                "stem": "A student's program stores each of 40 book titles in a separate variable. Which of the following changes would best manage the complexity of the program?",
                "options": ["Rename each variable with a shorter name.", "Store the titles in a single list and use a loop to process them.", "Add a comment above each variable.", "Convert the titles to uppercase."],
                "answer": "B",
                "explanation": "Replacing many variables with one list is the CED's definition of how data abstraction manages complexity.",
            },
        ],
        "vocab": [
            ("Data abstraction", "using a structure like a list so a collection of values can be treated as one unit"),
            ("List", "an ordered sequence of elements, each accessed by index"),
            ("Element", "a single value in a list"),
            ("Index", "the position of an element in a list; starts at 1 in AP pseudocode"),
        ],
    },
    {
        "num": 3, "title": "Mathematical Expressions", "blurb": "arithmetic and MOD",
        "lede": "Arithmetic in pseudocode follows normal order of operations, with one operator — MOD — that shows up constantly.",
        "points": [
            "Operators: <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, and <code>MOD</code>. Standard precedence applies: parentheses first, then <code>*</code> <code>/</code> <code>MOD</code> left to right, then <code>+</code> <code>-</code> left to right.",
            "<code>a MOD b</code> is the <strong>remainder</strong> when <code>a</code> is divided by <code>b</code>. <code>17 MOD 5</code> = 2, <code>20 MOD 4</code> = 0, <code>3 MOD 10</code> = 3 (if a &lt; b, the result is a).",
            "<strong>MOD uses:</strong> <code>n MOD 2 = 0</code> tests for even; <code>n MOD 10</code> gets the last digit; <code>i MOD LENGTH(list)</code> wraps an index around; <code>seconds MOD 60</code> converts to minutes and seconds.",
            "<code>/</code> in AP pseudocode is regular division that can produce decimals (<code>7 / 2</code> = 3.5). There is no integer-division operator on the reference sheet.",
            "A <strong>sequence</strong> of statements executes in order, one after another. The order changes the result: <code>x ← x * 2</code> then <code>x ← x + 1</code> is not the same as the reverse.",
            "Arithmetic on values of the wrong type (e.g., adding a number to a string) is an error in most languages.",
        ],
        "example": """
<pre class="code">a ← 17
b ← a MOD 5
c ← a / 5
d ← (a + 3) MOD 4
DISPLAY(b)
DISPLAY(c)
DISPLAY(d)</pre>
<p><code>b</code> = 17 MOD 5 = 2. <code>c</code> = 17 / 5 = 3.4. <code>d</code> = 20 MOD 4 = 0. Output: <strong>2 3.4 0</strong>.</p>""",
        "tip": "Whenever you see MOD, ask \"what's the remainder?\" and do the long division. For expressions mixing MOD with other operators, put parentheses around the MOD part mentally — MOD has the same precedence as multiplication, so <code>a + b MOD c</code> computes the MOD first.",
        "questions": [
            {
                "stem": "What is the value of the expression <code>25 MOD 7</code>?",
                "options": ["3", "4", "18", "3.57"],
                "answer": "B",
                "explanation": "7 goes into 25 three times (21), leaving a remainder of 4.",
            },
            {
                "stem": "Which of the following expressions evaluates to true exactly when the variable <code>n</code> holds an odd integer?",
                "options": ["<code>n MOD 2 = 0</code>", "<code>n MOD 2 = 1</code>", "<code>n / 2 = 1</code>", "<code>n MOD 1 = 0</code>"],
                "answer": "B",
                "explanation": "Odd numbers leave a remainder of 1 when divided by 2.",
            },
            {
                "stem": "What is displayed by the following code?\n<pre class=\"code\">x ← 4\nx ← x * 3\nx ← x + 2\nDISPLAY(x MOD 5)</pre>",
                "options": ["0", "2", "4", "14"],
                "answer": "C",
                "explanation": "x becomes 12, then 14. 14 MOD 5 = 4.",
            },
        ],
        "vocab": [
            ("MOD", "the remainder after integer division; a MOD b"),
            ("Expression", "a combination of values, variables, and operators that evaluates to a single value"),
            ("Sequencing", "executing statements in order, one after another"),
        ],
    },
    {
        "num": 4, "title": "Strings", "blurb": "text, concatenation, substrings",
        "lede": "Strings are ordered sequences of characters. The exam tests the concept — concatenation and substrings — rather than specific string functions.",
        "points": [
            "A <strong>string</strong> is an ordered sequence of characters (letters, digits, spaces, symbols), written in quotes: <code>\"Hello\"</code>.",
            "<strong>Concatenation</strong> joins strings end to end. <code>\"AP\" + \"CSP\"</code> → <code>\"APCSP\"</code>. Note there's no automatic space.",
            "A <strong>substring</strong> is any contiguous run of characters within a string. <code>\"Comp\"</code> is a substring of <code>\"Computer\"</code>; <code>\"Cptr\"</code> is not.",
            "Strings can be compared, searched, and have their length measured. The exact operation names vary by language; the CED expects the concepts, not a specific syntax.",
            "A string containing digits, like <code>\"42\"</code>, is text, not a number — concatenating <code>\"4\" + \"2\"</code> gives <code>\"42\"</code>, not 6.",
            "Strings are <em>immutable</em> in many languages: operations produce a new string rather than changing the original.",
        ],
        "example": """
<pre class="code">first ← "Grace"
last ← "Hopper"
full ← first + " " + last
DISPLAY(full)</pre>
<p>Concatenation with an explicit space in the middle → <strong>Grace Hopper</strong>. Without the <code>+ " " +</code>, the output would be <code>GraceHopper</code>. Questions love that missing space.</p>""",
        "tip": "When the exam shows string operations, it defines them in the question (e.g., \"the procedure SUBSTRING(str, start, end) returns…\"). Read that definition carefully — in particular, whether the end index is included — and apply it literally rather than assuming a language you know.",
        "questions": [
            {
                "stem": "The variable <code>word</code> holds the string <code>\"program\"</code>. Which of the following is a substring of <code>word</code>?",
                "options": ["\"pgm\"", "\"gram\"", "\"margorp\"", "\"prog ram\""],
                "answer": "B",
                "explanation": "A substring must be a contiguous run of the original characters. \"gram\" is the last four characters in order.",
            },
            {
                "stem": "What is displayed by the following code?\n<pre class=\"code\">a ← \"12\"\nb ← \"3\"\nDISPLAY(a + b)</pre>",
                "options": ["15", "123", "36", "An error, because strings cannot be added"],
                "answer": "B",
                "explanation": "Both values are strings, so + concatenates them: \"12\" followed by \"3\" is \"123\".",
            },
        ],
        "vocab": [
            ("String", "an ordered sequence of characters"),
            ("Concatenation", "joining two strings end to end"),
            ("Substring", "a contiguous sequence of characters within a string"),
        ],
    },
    {
        "num": 5, "title": "Boolean Expressions", "blurb": "true/false, AND, OR, NOT",
        "lede": "Every conditional and loop depends on a Boolean expression. You have to evaluate them exactly, including the ones designed to be misread.",
        "points": [
            "A <strong>Boolean</strong> value is either <code>true</code> or <code>false</code>. A Boolean expression evaluates to one of those two.",
            "<strong>Relational operators</strong> compare values: <code>=</code>, <code>≠</code>, <code>&gt;</code>, <code>&lt;</code>, <code>≥</code>, <code>≤</code>. Note: in AP pseudocode <code>=</code> is comparison, not assignment (assignment is <code>←</code>).",
            "<strong>Logical operators:</strong> <code>NOT a</code> is true when a is false. <code>a AND b</code> is true only when both are true. <code>a OR b</code> is true when at least one is true (including both).",
            "Precedence: <code>NOT</code> is evaluated before <code>AND</code>, which is before <code>OR</code>. Use parentheses when in doubt — the exam does.",
            "<strong>De Morgan's laws</strong> show up as \"equivalent expression\" questions: <code>NOT (a AND b)</code> = <code>(NOT a) OR (NOT b)</code>, and <code>NOT (a OR b)</code> = <code>(NOT a) AND (NOT b)</code>.",
            "Two Boolean expressions are <strong>equivalent</strong> if they have the same value for every combination of inputs. A truth table proves it.",
            "The negation of <code>x &gt; 5</code> is <code>x ≤ 5</code>, not <code>x &lt; 5</code>. Missing the boundary case is a classic distractor.",
        ],
        "example": """
<p>Let <code>age ← 16</code> and <code>hasLicense ← false</code>.</p>
<ul class="points">
<li><code>age ≥ 16 AND hasLicense</code> → true AND false → <strong>false</strong></li>
<li><code>age ≥ 16 OR hasLicense</code> → true OR false → <strong>true</strong></li>
<li><code>NOT (age &lt; 18)</code> → NOT true → <strong>false</strong></li>
<li><code>NOT (age ≥ 16 AND hasLicense)</code> → NOT false → <strong>true</strong>, which by De Morgan equals <code>age &lt; 16 OR NOT hasLicense</code> → false OR true → true. ✓</li>
</ul>""",
        "tip": "For \"which expression is equivalent\" questions, don't reason abstractly — plug in all four combinations of true/false (or a few boundary numbers) and compare outputs. It takes 30 seconds and is essentially error-proof.",
        "questions": [
            {
                "stem": "Which of the following expressions is equivalent to <code>NOT (x &gt; 10 AND y = 3)</code>?",
                "options": ["<code>x ≤ 10 AND y ≠ 3</code>", "<code>x ≤ 10 OR y ≠ 3</code>", "<code>x &lt; 10 OR y ≠ 3</code>", "<code>x &gt; 10 OR y = 3</code>"],
                "answer": "B",
                "explanation": "De Morgan: NOT (A AND B) = (NOT A) OR (NOT B). NOT (x > 10) is x ≤ 10 (include the boundary), NOT (y = 3) is y ≠ 3.",
            },
            {
                "stem": "The variables <code>a</code> and <code>b</code> are Boolean. For which values is the expression <code>(a OR b) AND (NOT a)</code> true?",
                "options": ["a = true, b = true", "a = true, b = false", "a = false, b = true", "a = false, b = false"],
                "answer": "C",
                "explanation": "NOT a requires a = false. Then (a OR b) requires b = true. Only option C satisfies both.",
            },
        ],
        "vocab": [
            ("Boolean", "a value that is either true or false"),
            ("Relational operator", "an operator that compares two values, such as = or <"),
            ("Logical operator", "NOT, AND, or OR — combines or negates Boolean values"),
            ("Equivalent expressions", "expressions that evaluate to the same value for every possible input"),
        ],
    },
    {
        "num": 6, "title": "Conditionals", "blurb": "IF and IF/ELSE, selection",
        "lede": "Selection means the program chooses which code to run based on a condition. IF and IF/ELSE are how it does that.",
        "points": [
            "<strong>Selection</strong> is one of the three building blocks of algorithms (with sequencing and iteration). It lets a program take different paths.",
            "<code>IF (condition) { block }</code> runs the block only when the condition is true; otherwise it skips it and continues.",
            "<code>IF (condition) { block1 } ELSE { block2 }</code> runs exactly one of the two blocks — block1 if true, block2 if false. Never both, never neither.",
            "After the conditional finishes, execution continues with the next statement in sequence regardless of which branch ran.",
            "Two separate <code>IF</code> statements are independent — both conditions are checked and both blocks can run. An <code>IF/ELSE</code> is mutually exclusive. This difference is a frequent exam trap.",
            "The condition must be a Boolean expression. Everything from 3.5 applies.",
        ],
        "example": """
<pre class="code">temp ← 72
IF (temp > 80)
{
    DISPLAY("hot")
}
IF (temp > 60)
{
    DISPLAY("warm")
}
ELSE
{
    DISPLAY("cold")
}</pre>
<p>First IF: 72 &gt; 80 is false → nothing. Second IF/ELSE: 72 &gt; 60 is true → <strong>warm</strong>, and the ELSE is skipped. Output: <code>warm</code>. Had the first IF been true, both \"hot\" and \"warm\" would display, because they're independent statements.</p>""",
        "tip": "Count the IFs. Independent IFs can each fire; an IF/ELSE chain fires exactly one branch. When a question asks \"how many lines are displayed,\" this distinction is usually the whole question.",
        "questions": [
            {
                "stem": "What is displayed by the following code?\n<pre class=\"code\">score ← 85\nIF (score ≥ 90)\n{\n    DISPLAY(\"A\")\n}\nELSE\n{\n    IF (score ≥ 80)\n    {\n        DISPLAY(\"B\")\n    }\n    ELSE\n    {\n        DISPLAY(\"C\")\n    }\n}</pre>",
                "options": ["A", "B", "C", "B C"],
                "answer": "B",
                "explanation": "85 ≥ 90 is false, so the ELSE runs. Inside, 85 ≥ 80 is true, so \"B\" is displayed and the inner ELSE is skipped.",
            },
            {
                "stem": "Consider the following code, where <code>n</code> is a positive integer.\n<pre class=\"code\">IF (n MOD 2 = 0)\n{\n    DISPLAY(\"even\")\n}\nIF (n > 10)\n{\n    DISPLAY(\"big\")\n}</pre>For which value of <code>n</code> are two words displayed?",
                "options": ["7", "8", "11", "12"],
                "answer": "D",
                "explanation": "Both independent IFs must be true: even AND greater than 10. Only 12 qualifies.",
            },
        ],
        "vocab": [
            ("Selection", "choosing which code to execute based on a Boolean condition"),
            ("Conditional statement", "an IF or IF/ELSE statement"),
        ],
    },
    {
        "num": 7, "title": "Nested Conditionals", "blurb": "conditionals inside conditionals",
        "lede": "A conditional can live inside another conditional's block. The inner one is only reached if the outer path leads there — tracing them carefully is the entire skill.",
        "points": [
            "<strong>Nested conditionals</strong> are conditional statements placed inside the block of another conditional.",
            "The inner condition is only <em>evaluated</em> when the outer branch containing it executes. If the outer condition is false, the inner one never runs at all.",
            "Nesting lets you express \"if A, then check B\" logic — multiple criteria that depend on one another.",
            "Nested IF/ELSE inside ELSE branches builds a multi-way choice (like grade ranges A/B/C/D/F). Only one leaf branch ever executes.",
            "Many nested conditionals can be rewritten using <code>AND</code>/<code>OR</code>, and vice versa. The exam asks which rewrite is <em>equivalent</em>. Check with test values.",
            "Deep nesting is hard to read; matching the braces to the correct IF is where tracing errors happen. Indentation in the exam's code is reliable — use it.",
        ],
        "example": """
<pre class="code">IF (isMember)
{
    IF (total > 50)
    {
        discount ← 20
    }
    ELSE
    {
        discount ← 10
    }
}
ELSE
{
    discount ← 0
}</pre>
<p>Members with a total over 50 get 20; other members get 10; non-members get 0. An equivalent flat version: <code>IF (isMember AND total > 50)</code> → 20, <code>ELSE IF (isMember)</code> → 10, <code>ELSE</code> → 0. Same outputs for every input, so they're equivalent.</p>""",
        "tip": "Trace nested conditionals from the outside in. Decide the outer condition, cross out the branch that doesn't run, and only then look at what's inside the surviving branch. Never evaluate an inner condition before you've confirmed its outer branch runs.",
        "questions": [
            {
                "stem": "What is displayed by the following code?\n<pre class=\"code\">x ← 5\ny ← 12\nIF (x > 3)\n{\n    IF (y &lt; 10)\n    {\n        DISPLAY(\"one\")\n    }\n    ELSE\n    {\n        DISPLAY(\"two\")\n    }\n}\nELSE\n{\n    DISPLAY(\"three\")\n}</pre>",
                "options": ["one", "two", "three", "two three"],
                "answer": "B",
                "explanation": "x > 3 is true, so the outer IF branch runs. Inside, y < 10 is false, so the inner ELSE displays \"two\". The outer ELSE never runs.",
            },
            {
                "stem": "Which of the following is equivalent to the code below?\n<pre class=\"code\">IF (a > 0)\n{\n    IF (b > 0)\n    {\n        DISPLAY(\"yes\")\n    }\n}</pre>",
                "options": ["<code>IF (a > 0 OR b > 0) { DISPLAY(\"yes\") }</code>", "<code>IF (a > 0 AND b > 0) { DISPLAY(\"yes\") }</code>", "<code>IF (NOT (a > 0)) { DISPLAY(\"yes\") }</code>", "<code>IF (a > 0) { DISPLAY(\"yes\") }</code>"],
                "answer": "B",
                "explanation": "\"yes\" appears only when both a > 0 and b > 0 — that's AND.",
            },
        ],
        "vocab": [
            ("Nested conditional", "a conditional statement placed inside the block of another conditional"),
        ],
    },
    {
        "num": 8, "title": "Iteration", "blurb": "REPEAT n TIMES, REPEAT UNTIL, loops",
        "lede": "Iteration repeats code. The exam's favorite questions: how many times does the loop run, and what's the final value when it stops?",
        "points": [
            "<strong>Iteration</strong> (looping) is the third building block of algorithms. The code inside the loop is the <strong>loop body</strong>.",
            "<code>REPEAT n TIMES { body }</code> runs the body exactly <em>n</em> times.",
            "<code>REPEAT UNTIL (condition) { body }</code> checks the condition <em>before each pass</em>. If the condition is already true at the start, the body runs <strong>zero times</strong>. Otherwise it runs, then re-checks, until the condition becomes true.",
            "<code>FOR EACH item IN list { body }</code> runs the body once per element, in order, with <code>item</code> holding the current element (covered more in 3.10).",
            "An <strong>infinite loop</strong> occurs when a REPEAT UNTIL condition can never become true. The exam asks you to spot the variable that never changes.",
            "The typical pattern: initialize a counter or accumulator before the loop, update it inside, and use it after. Tracing = table with one row per iteration.",
            "Loop variables retain their final value after the loop ends. If a REPEAT UNTIL stops when <code>i = 5</code>, <code>i</code> is 5 afterward.",
        ],
        "example": """
<pre class="code">i ← 1
sum ← 0
REPEAT UNTIL (i > 4)
{
    sum ← sum + i
    i ← i + 1
}
DISPLAY(sum)
DISPLAY(i)</pre>
<table class="trace"><tr><th>check i &gt; 4?</th><th>sum</th><th>i after</th></tr>
<tr><td>1 &gt; 4 false</td><td>1</td><td>2</td></tr>
<tr><td>2 &gt; 4 false</td><td>3</td><td>3</td></tr>
<tr><td>3 &gt; 4 false</td><td>6</td><td>4</td></tr>
<tr><td>4 &gt; 4 false</td><td>10</td><td>5</td></tr>
<tr><td>5 &gt; 4 true → stop</td><td></td><td></td></tr></table>
<p>Output: <strong>10 5</strong>. Four iterations; <code>i</code> ends at 5, not 4.</p>""",
        "tip": "REPEAT UNTIL runs while the condition is <em>false</em>. Students constantly flip this. Read it as \"keep going until this becomes true.\" And always check the initial condition — a loop that's already satisfied runs zero times.",
        "questions": [
            {
                "stem": "How many times is \"hi\" displayed by the following code?\n<pre class=\"code\">count ← 10\nREPEAT UNTIL (count &lt; 4)\n{\n    DISPLAY(\"hi\")\n    count ← count - 2\n}</pre>",
                "options": ["3", "4", "5", "The loop never ends"],
                "answer": "B",
                "explanation": "count goes 10 → 8 → 6 → 4 → 2. The body runs while count ≥ 4: for values 10, 8, 6, 4 — four times. When count is 2, the condition is true and the loop stops.",
            },
            {
                "stem": "Which of the following loops will never terminate?",
                "options": ["<code>x ← 0</code><br><code>REPEAT UNTIL (x ≥ 5) { x ← x + 1 }</code>", "<code>x ← 10</code><br><code>REPEAT UNTIL (x = 0) { x ← x - 2 }</code>", "<code>x ← 3</code><br><code>REPEAT UNTIL (x > 100) { x ← x * 2 }</code>", "<code>x ← 1</code><br><code>REPEAT UNTIL (x = 0) { x ← x + 1 }</code>"],
                "answer": "D",
                "explanation": "In D, x starts at 1 and only increases, so x = 0 can never become true. Option B does terminate: 10, 8, 6, 4, 2, 0.",
            },
            {
                "stem": "What is the value of <code>total</code> after the following code runs?\n<pre class=\"code\">total ← 0\nREPEAT 3 TIMES\n{\n    total ← total + 5\n    total ← total * 2\n}</pre>",
                "options": ["30", "50", "70", "150"],
                "answer": "C",
                "explanation": "Pass 1: 0+5=5, ×2=10. Pass 2: 15, ×2=30. Pass 3: 35, ×2=70.",
            },
        ],
        "vocab": [
            ("Iteration", "repeating a block of code"),
            ("Loop body", "the statements inside a loop that are repeated"),
            ("REPEAT UNTIL", "a loop that runs while its condition is false and stops once it becomes true"),
            ("Infinite loop", "a loop whose exit condition is never met"),
        ],
    },
    {
        "num": 9, "title": "Developing Algorithms", "blurb": "building blocks, common patterns",
        "lede": "An algorithm is a finite set of instructions that solves a problem. This topic is about how the three building blocks combine and the standard patterns you're expected to recognize on sight.",
        "points": [
            "An <strong>algorithm</strong> is a finite sequence of precise instructions that accomplishes a task. It must end.",
            "Every algorithm is built from <strong>sequencing</strong>, <strong>selection</strong>, and <strong>iteration</strong>. The exam asks you to identify which one a code fragment illustrates.",
            "Algorithms can be expressed in natural language, flowcharts, pseudocode, or code — the same algorithm in different forms is still the same algorithm.",
            "Different algorithms can solve the same problem; they may differ in efficiency or clarity but produce the same result.",
            "<strong>Standard patterns to recognize:</strong> finding the <em>max/min</em> (track the best so far), computing a <em>sum or average</em> (accumulator), <em>counting</em> items that meet a condition, checking whether a value is <em>present</em> in a list, and building a new list from filtered elements.",
            "Existing algorithms can be <strong>combined or modified</strong> to solve new problems — you don't start from scratch every time.",
            "Reading an algorithm: identify what's initialized, what changes each iteration, and what's true when it stops. That reveals its purpose.",
        ],
        "example": """
<p><strong>Find the largest value in a list</strong> — the canonical pattern:</p>
<pre class="code">biggest ← nums[1]
FOR EACH n IN nums
{
    IF (n > biggest)
    {
        biggest ← n
    }
}
DISPLAY(biggest)</pre>
<p>Initialize to the first element (never to 0 — that fails for all-negative lists), compare each element, keep the winner. Swap <code>&gt;</code> for <code>&lt;</code> and it finds the minimum. Replace the IF with <code>total ← total + n</code> and it sums. Recognizing these variants is faster than re-deriving them.</p>""",
        "tip": "When asked \"what does this algorithm do,\" don't trace with random values — trace with a tiny list of 3 items and watch what the tracked variable equals at the end. The initialization line usually tells you the pattern before you've read anything else.",
        "questions": [
            {
                "stem": "What does the following code display, where <code>vals ← [4, 9, 2, 7]</code>?\n<pre class=\"code\">count ← 0\nFOR EACH v IN vals\n{\n    IF (v > 5)\n    {\n        count ← count + 1\n    }\n}\nDISPLAY(count)</pre>",
                "options": ["2", "4", "16", "22"],
                "answer": "A",
                "explanation": "This is the counting pattern. Values greater than 5 are 9 and 7 → count = 2.",
            },
            {
                "stem": "A programmer wants to modify the algorithm below so it finds the smallest value instead of the largest.\n<pre class=\"code\">best ← list[1]\nFOR EACH x IN list\n{\n    IF (x > best)\n    {\n        best ← x\n    }\n}</pre>Which single change accomplishes this?",
                "options": ["Change <code>best ← list[1]</code> to <code>best ← 0</code>", "Change <code>x > best</code> to <code>x < best</code>", "Change <code>best ← x</code> to <code>x ← best</code>", "Remove the IF statement"],
                "answer": "B",
                "explanation": "Flipping the comparison makes it track the smallest value seen. Initializing to 0 would break the algorithm for lists of positive numbers.",
            },
        ],
        "vocab": [
            ("Algorithm", "a finite set of precise instructions that accomplishes a task"),
            ("Sequencing", "statements executed in order"),
            ("Selection", "choosing a path with a conditional"),
            ("Iteration", "repeating with a loop"),
            ("Accumulator", "a variable that builds up a result, such as a running total, across iterations"),
        ],
    },
]

# ----------------------------------------------------------------------
# BIG IDEA 3 (part 2: 3.10 – 3.18)
# ----------------------------------------------------------------------

BI3_TOPICS_B = [
    {
        "num": 10, "title": "Lists", "blurb": "list operations, traversal",
        "lede": "The reference sheet gives you a small set of list operations. Combined with FOR EACH, they're behind a big share of the code questions.",
        "points": [
            "AP pseudocode list operations (all 1-indexed): <code>list[i]</code> accesses element i; <code>list[i] ← value</code> assigns it; <code>LENGTH(list)</code> gives the number of elements.",
            "<code>APPEND(list, value)</code> adds to the end and increases length by 1. <code>INSERT(list, i, value)</code> puts value at index i, shifting later elements right. <code>REMOVE(list, i)</code> deletes the element at i, shifting later elements left.",
            "After INSERT or REMOVE, indices of later elements <em>change</em>. A question that removes index 2 and then reads index 3 is reading what used to be index 4.",
            "<strong>Traversal</strong> means visiting every element. <code>FOR EACH item IN list</code> is the complete traversal; a REPEAT UNTIL with an index can do partial traversals.",
            "Common list algorithms: linear search (check each element until found), filtering into a new list, counting, sum/average, min/max, reversing, checking for duplicates.",
            "A list can be empty: <code>[]</code>, with LENGTH 0. Accessing <code>list[1]</code> on an empty list is a run-time error.",
            "Lists can contain lists, allowing grids or tables — but the CED keeps most questions to one dimension.",
        ],
        "example": """
<pre class="code">a ← [10, 20, 30, 40]
REMOVE(a, 2)
APPEND(a, 50)
INSERT(a, 1, 5)
DISPLAY(a[3])
DISPLAY(LENGTH(a))</pre>
<p>Step through: start <code>[10,20,30,40]</code> → REMOVE index 2 → <code>[10,30,40]</code> → APPEND 50 → <code>[10,30,40,50]</code> → INSERT 5 at index 1 → <code>[5,10,30,40,50]</code>. Then <code>a[3]</code> = 30, LENGTH = 5. Output: <strong>30 5</strong>.</p>""",
        "tip": "Rewrite the list after every INSERT/REMOVE/APPEND — literally write it out with brackets. Tracking index shifts in your head is where these go wrong. And in a FOR EACH loop, changing the loop variable does <em>not</em> change the list.",
        "questions": [
            {
                "stem": "What is displayed after the following code runs?\n<pre class=\"code\">nums ← [3, 8, 1, 6]\nINSERT(nums, 2, 9)\nREMOVE(nums, 4)\nDISPLAY(nums)</pre>",
                "options": ["[3, 9, 8, 6]", "[3, 9, 8, 1]", "[9, 3, 8, 6]", "[3, 8, 9, 6]"],
                "answer": "A",
                "explanation": "INSERT 9 at index 2 → [3, 9, 8, 1, 6]. REMOVE index 4 (the 1) → [3, 9, 8, 6].",
            },
            {
                "stem": "The following procedure is intended to return true if <code>target</code> appears in <code>list</code>.\n<pre class=\"code\">PROCEDURE contains(list, target)\n{\n    FOR EACH item IN list\n    {\n        IF (item = target)\n        {\n            RETURN true\n        }\n    }\n    RETURN false\n}</pre>Which best describes the algorithm used?",
                "options": ["Binary search", "Linear search", "Sorting", "Data compression"],
                "answer": "B",
                "explanation": "Checking each element in order until a match is found is a linear (sequential) search.",
            },
            {
                "stem": "The list <code>data</code> has 7 elements. After <code>REMOVE(data, 1)</code> and then <code>APPEND(data, 100)</code>, what is <code>LENGTH(data)</code>?",
                "options": ["6", "7", "8", "9"],
                "answer": "B",
                "explanation": "Remove one (6), append one (7).",
            },
        ],
        "vocab": [
            ("Traversal", "visiting each element of a list, usually with FOR EACH"),
            ("APPEND", "adds a value to the end of a list"),
            ("INSERT", "places a value at a given index, shifting later elements right"),
            ("REMOVE", "deletes the element at a given index, shifting later elements left"),
            ("Linear search", "checking elements one by one until the target is found or the list ends"),
        ],
    },
    {
        "num": 11, "title": "Binary Search", "blurb": "halving a sorted list",
        "lede": "Binary search finds a value in a sorted list by repeatedly cutting the search space in half. It's dramatically faster than linear search — but only on sorted data.",
        "points": [
            "<strong>Binary search</strong> requires the list to be <strong>sorted</strong>. On unsorted data it doesn't work at all. This is the single most-tested fact.",
            "Procedure: look at the middle element. If it's the target, done. If the target is smaller, discard the upper half; if larger, discard the lower half. Repeat on the remaining half.",
            "Each step <strong>halves</strong> the number of elements left to check. A list of 1,000 elements takes at most about 10 checks (2<sup>10</sup> = 1,024); a million takes about 20.",
            "<strong>Linear search</strong> checks elements one at a time and may need to check every element — up to <em>n</em> checks for <em>n</em> items.",
            "The exam asks: given a sorted list of N items, what's the maximum number of checks binary search needs? Answer: the smallest k where 2<sup>k</sup> <em>&gt;</em> N. For 15 items that's 4 (2<sup>4</sup> = 16 &gt; 15); for 64 items it's 7 (2<sup>7</sup> = 128 &gt; 64). Roughly log₂ N, rounded down, plus one for the final check.",
            "Binary search is a <em>selection + iteration</em> algorithm: repeated comparison and narrowing.",
            "Trade-off: sorting has a cost. If you only search once, sorting then binary searching may not beat a single linear search. If you search many times, sort first.",
        ],
        "example": """
<p>Sorted list: <code>[2, 5, 9, 14, 21, 30, 44, 51, 63]</code>, target 44.</p>
<ol class="points">
<li>Middle (index 5) is 21. 44 &gt; 21 → keep the right half: <code>[30, 44, 51, 63]</code>.</li>
<li>Middle is 44 (or 51 depending on rounding; either way one more step). Found at step 2 or 3.</li>
</ol>
<p>Linear search would have needed 7 checks to reach 44. With 9 elements, binary search never needs more than 4 (2<sup>4</sup> = 16 ≥ 9).</p>""",
        "tip": "If a question about binary search doesn't say the list is sorted, that's the answer: binary search can't be used. If it asks for the maximum number of checks, find the smallest power of 2 that is <em>greater</em> than the list size and use that exponent: 8 items → 4, 15 → 4, 16 → 5, 64 → 7, 100 → 7, 1000 → 10.",
        "questions": [
            {
                "stem": "A list of 64 numbers is sorted in ascending order. What is the maximum number of elements that must be examined to find a target value using binary search?",
                "options": ["6", "7", "32", "64"],
                "answer": "B",
                "explanation": "Each check halves what remains: 64 → 32 → 16 → 8 → 4 → 2 → 1 takes six checks to get down to a single element, and a seventh check examines that element. The smallest power of 2 greater than 64 is 2⁷ = 128, so the maximum is 7.",
            },
            {
                "stem": "Which of the following is a requirement for binary search to be used on a list?",
                "options": ["The list must contain only unique values.", "The list must be sorted.", "The list must have an even number of elements.", "The list must contain only integers."],
                "answer": "B",
                "explanation": "Binary search relies on ordering to decide which half to discard.",
            },
            {
                "stem": "Which of the following best describes the advantage of binary search over linear search?",
                "options": ["Binary search works on unsorted lists.", "Binary search always finds the value in one step.", "Binary search eliminates half of the remaining elements with each comparison, so it needs far fewer steps on large lists.", "Binary search uses less memory."],
                "answer": "C",
                "explanation": "The halving is the whole reason binary search scales so well.",
            },
        ],
        "vocab": [
            ("Binary search", "a search on a sorted list that repeatedly halves the range being examined"),
            ("Sorted list", "elements arranged in order, required for binary search"),
        ],
    },
    {
        "num": 12, "title": "Calling Procedures", "blurb": "arguments, parameters, return values",
        "lede": "Calling a procedure hands control to it, possibly with values, and gets control (and maybe a result) back. The vocabulary here is precise and tested.",
        "points": [
            "A <strong>procedure</strong> is a named group of instructions that can be executed by calling its name. Other languages call these functions or methods.",
            "<strong>Parameters</strong> are the variables listed in the procedure's definition. <strong>Arguments</strong> are the actual values passed in when it's called. The first argument goes into the first parameter, and so on.",
            "When a procedure is called, the program <strong>jumps</strong> into the procedure, runs it, and then <strong>returns</strong> to the line after the call. That interrupts normal sequential flow.",
            "<code>RETURN (expression)</code> ends the procedure immediately and sends the value back to the caller. Code after a RETURN in the same path never runs.",
            "A procedure with a RETURN can be used inside an expression: <code>x ← square(4) + 1</code>. A procedure without a RETURN (one that just DISPLAYs or changes things) is called as a statement.",
            "The same procedure can be called many times with different arguments — that's the point.",
            "<strong>Modularity:</strong> breaking a program into procedures makes each piece easier to write, test, and reuse.",
        ],
        "example": """
<pre class="code">PROCEDURE double(n)
{
    RETURN (n * 2)
}

a ← 3
b ← double(a) + double(5)
DISPLAY(b)</pre>
<p><code>double(a)</code> passes the argument 3 into parameter <code>n</code>, returns 6. <code>double(5)</code> returns 10. <code>b</code> = 16. Output: <strong>16</strong>. Note that <code>a</code> is still 3 — the procedure got a copy.</p>""",
        "tip": "Track \"where am I\" during a trace. When you hit a procedure call, write down the line you'll return to, go execute the procedure with the arguments substituted for the parameters, and come back. RETURN means you stop reading the procedure instantly — even if there are lines below it.",
        "questions": [
            {
                "stem": "Consider the following procedure.\n<pre class=\"code\">PROCEDURE mystery(a, b)\n{\n    IF (a > b)\n    {\n        RETURN (a - b)\n    }\n    RETURN (b - a)\n}</pre>What is displayed by <code>DISPLAY(mystery(4, 9))</code>?",
                "options": ["-5", "5", "13", "Nothing is displayed"],
                "answer": "B",
                "explanation": "4 > 9 is false, so the first RETURN is skipped. The second RETURN gives 9 - 4 = 5.",
            },
            {
                "stem": "In the call <code>calculate(7, \"kg\")</code> to a procedure defined as <code>PROCEDURE calculate(amount, unit)</code>, which of the following is true?",
                "options": ["<code>amount</code> and <code>unit</code> are arguments; 7 and \"kg\" are parameters.", "<code>amount</code> and <code>unit</code> are parameters; 7 and \"kg\" are arguments.", "7 is a parameter and \"kg\" is an argument.", "The terms parameter and argument are interchangeable on the exam."],
                "answer": "B",
                "explanation": "Parameters are the names in the definition; arguments are the values in the call.",
            },
        ],
        "vocab": [
            ("Procedure", "a named block of code that can be called; also called a function or method"),
            ("Parameter", "a variable in a procedure's definition that receives a value when called"),
            ("Argument", "the actual value passed to a procedure when it is called"),
            ("Return value", "the value a procedure sends back to the code that called it"),
            ("Modularity", "dividing a program into separate procedures that each handle one task"),
        ],
    },
    {
        "num": 13, "title": "Developing Procedures", "blurb": "procedural abstraction",
        "lede": "Writing your own procedures is where procedural abstraction happens — and the Create Task requires you to have one with a parameter, selection, and iteration.",
        "points": [
            "<strong>Procedural abstraction</strong> lets a programmer use a procedure by knowing <em>what</em> it does without knowing <em>how</em>. The name and parameters are the interface; the body is hidden detail.",
            "Benefits: reduces <strong>duplicated code</strong>, makes programs easier to read and maintain, and lets you fix a bug in one place instead of many.",
            "<strong>Parameters generalize</strong> a procedure. A procedure that only works on one hardcoded value is far less useful than one that takes that value as a parameter.",
            "Good procedure names describe the task (<code>calculateTax</code>, <code>isValidEmail</code>). Like variable names, they're documentation.",
            "<strong>Create Task requirement:</strong> a student-developed procedure with at least one parameter that affects its behavior, and whose body includes an algorithm with sequencing, selection, and iteration. You must show the procedure being <em>called</em>, too.",
            "Procedures can call other procedures, building larger behavior from smaller verified pieces.",
            "A procedure should do one clearly defined thing. If you're describing it with \"and,\" it may be two procedures.",
        ],
        "example": """
<p>Without a procedure, computing a letter grade three times means the IF/ELSE chain appears three times. With one:</p>
<pre class="code">PROCEDURE letterGrade(score)
{
    IF (score ≥ 90) { RETURN ("A") }
    IF (score ≥ 80) { RETURN ("B") }
    IF (score ≥ 70) { RETURN ("C") }
    RETURN ("F")
}
DISPLAY(letterGrade(91))
DISPLAY(letterGrade(74))</pre>
<p>Output: <strong>A C</strong>. If the school changes the B cutoff, you edit one line. That's the maintenance benefit the CED describes.</p>""",
        "tip": "When a question asks why a programmer should turn repeated code into a procedure, the right answer is about <em>reducing duplication and making changes easier</em>. Answers about making the program run faster or use less memory are distractors — procedures don't do that.",
        "questions": [
            {
                "stem": "A program contains the same 8-line block of code in five different places, differing only in the number used on the first line. Which of the following is the best improvement?",
                "options": ["Add a comment above each copy explaining that it is repeated.", "Write a procedure with a parameter for the differing number and call it in each of the five places.", "Combine the five copies into one very long block.", "Rename the variables in each copy so they are distinct."],
                "answer": "B",
                "explanation": "Duplicated logic with one varying value is exactly what a parameterized procedure is for.",
            },
            {
                "stem": "Which of the following best describes procedural abstraction?",
                "options": ["Storing many values in a list so they can be processed together", "Using a procedure by knowing its name and what it does, without needing to know how it is implemented", "Writing a program without any procedures", "Compressing code so it takes less space"],
                "answer": "B",
                "explanation": "Procedural abstraction hides implementation behind an interface. Option A describes data abstraction.",
            },
        ],
        "vocab": [
            ("Procedural abstraction", "using a procedure without needing to know how its internal code works"),
            ("Generalization", "using parameters so a procedure works for many inputs, not one fixed case"),
        ],
    },
    {
        "num": 14, "title": "Libraries", "blurb": "reusing code, APIs",
        "lede": "Libraries are collections of procedures written by someone else. Using them well means reading documentation and understanding what an API promises.",
        "points": [
            "A <strong>software library</strong> is a collection of procedures that can be used in other programs — often written and tested by other developers.",
            "Benefits: save development time, reuse code that's already been debugged, and gain capabilities (graphics, networking, math) you'd otherwise have to build yourself.",
            "An <strong>API (application programming interface)</strong> specifies how a library's procedures are called: their names, parameters, and what they return. It's the contract between your code and the library.",
            "<strong>Documentation</strong> is essential for using a library correctly — it explains what each procedure does, what it needs, and how it behaves in edge cases. You can't use a library well without it.",
            "Using a library is procedural abstraction in practice: you call <code>sort(list)</code> without knowing the sorting algorithm inside.",
            "Libraries are typically imported into a program before their procedures can be called.",
        ],
        "example": """
<p>Suppose a math library's documentation says: <code>ROUND(x, places)</code> returns x rounded to the given number of decimal places. You never see the rounding code; you just call <code>ROUND(3.14159, 2)</code> and get 3.14. If the documentation had said the second parameter is the number of <em>significant figures</em>, the same call would return 3.1. Reading the API, not guessing, is the skill.</p>""",
        "tip": "Questions here are usually scenario-based: a developer wants to add a map to an app. The correct reasoning is \"use a library to avoid rewriting tested code,\" and the correct next step is \"read its documentation/API.\" Any option suggesting you must understand the library's internal implementation is wrong.",
        "questions": [
            {
                "stem": "A programmer wants to display a bar chart in their program. Rather than writing the drawing code from scratch, they use a charting library. Which of the following is the most important reason this approach is effective?",
                "options": ["The library's procedures have already been developed and tested, saving time and reducing errors.", "Programs that use libraries are always shorter.", "Libraries eliminate the need for documentation.", "Using a library guarantees the program has no bugs."],
                "answer": "A",
                "explanation": "Reusing tested code is the core benefit. Libraries don't guarantee bug-free programs or remove the need for documentation.",
            },
            {
                "stem": "Which of the following best describes an API?",
                "options": ["A type of lossy compression", "The set of procedures, their parameters, and return values that a library makes available for other programs to call", "The internal source code of a library", "A list used to store data"],
                "answer": "B",
                "explanation": "An API is the interface — what you can call and how — not the implementation.",
            },
        ],
        "vocab": [
            ("Software library", "a collection of pre-written procedures that other programs can use"),
            ("API", "the specification of how to use a library: its procedures, parameters, and return values"),
            ("Documentation", "written explanation of how a library's procedures behave"),
        ],
    },
    {
        "num": 15, "title": "Random Values", "blurb": "RANDOM(a, b)",
        "lede": "One procedure, one rule: RANDOM(a, b) returns a random integer from a to b, inclusive. Nearly every question is about that inclusivity or about probability.",
        "points": [
            "<code>RANDOM(a, b)</code> returns a random integer between <strong>a and b, inclusive</strong>. <code>RANDOM(1, 6)</code> simulates a die: 1, 2, 3, 4, 5, or 6.",
            "Each call is independent. Calling it twice can give the same value or different values — the program can't predict which.",
            "Number of possible outcomes = b − a + 1. <code>RANDOM(1, 10)</code> has 10 outcomes; <code>RANDOM(0, 10)</code> has 11.",
            "Each outcome is equally likely. Probability of a specific value = 1 / (b − a + 1). Probability that <code>RANDOM(1, 10)</code> ≤ 3 is 3/10.",
            "Random values are used in games, simulations (3.16), sampling, and testing.",
            "To scale or shift randomness, combine with arithmetic: <code>RANDOM(1, 6) + RANDOM(1, 6)</code> simulates two dice (2–12, not uniformly distributed).",
            "A program that uses random values will generally produce <em>different output</em> each time it runs — a question may ask which statements are possible rather than certain.",
        ],
        "example": """
<pre class="code">x ← RANDOM(1, 4)
IF (x ≤ 1)
{
    DISPLAY("rare")
}
ELSE
{
    DISPLAY("common")
}</pre>
<p>Possible values: 1, 2, 3, 4 (four outcomes). \"rare\" displays only when x = 1 → probability 1/4 = 25%. \"common\" displays 75% of the time.</p>""",
        "tip": "Count outcomes as b − a + 1, then count how many satisfy the condition. Students forget that both endpoints are included and get 1/9 instead of 1/10. If a question describes wanting a value \"from 1 to 100,\" the call is <code>RANDOM(1, 100)</code>, not <code>RANDOM(0, 100)</code>.",
        "questions": [
            {
                "stem": "What is the probability that the following code displays \"win\"?\n<pre class=\"code\">n ← RANDOM(1, 5)\nIF (n > 3)\n{\n    DISPLAY(\"win\")\n}</pre>",
                "options": ["1/5", "2/5", "3/5", "1/2"],
                "answer": "B",
                "explanation": "Outcomes 1–5 (five total). n > 3 is true for 4 and 5 → 2/5.",
            },
            {
                "stem": "Which of the following code segments simulates flipping a fair coin, displaying \"heads\" or \"tails\" with equal probability?",
                "options": ["<code>IF (RANDOM(1, 2) = 1) { DISPLAY(\"heads\") } ELSE { DISPLAY(\"tails\") }</code>", "<code>IF (RANDOM(0, 2) = 1) { DISPLAY(\"heads\") } ELSE { DISPLAY(\"tails\") }</code>", "<code>IF (RANDOM(1, 3) = 1) { DISPLAY(\"heads\") } ELSE { DISPLAY(\"tails\") }</code>", "<code>IF (RANDOM(1, 2) > 2) { DISPLAY(\"heads\") } ELSE { DISPLAY(\"tails\") }</code>"],
                "answer": "A",
                "explanation": "RANDOM(1, 2) has exactly two equally likely outcomes. B and C have three outcomes (not 50/50); D can never be true.",
            },
        ],
        "vocab": [
            ("RANDOM(a, b)", "returns a random integer from a to b, inclusive, each equally likely"),
        ],
    },
    {
        "num": 16, "title": "Simulations", "blurb": "modeling the real world",
        "lede": "A simulation is a program that models a real or imagined situation. The exam tests why we simulate and what's lost when we do.",
        "points": [
            "A <strong>simulation</strong> is an abstraction of a more complex object or phenomenon, used to investigate it in a controlled way.",
            "<strong>Why simulate:</strong> the real thing may be too dangerous (crash tests), too expensive, too slow (climate over centuries), too fast, or simply impossible to observe (a bridge that isn't built yet). Simulations can be run many times and with varied parameters.",
            "Simulations <strong>remove details</strong> and make <strong>simplifying assumptions</strong>. That's what makes them tractable — and what limits their accuracy. Every simulation question wants you to notice this trade-off.",
            "Because of simplifications, a simulation's results may not match reality; conclusions must account for what was left out.",
            "Simulations often use <strong>random values</strong> (3.15) to model uncertainty or variation, and are run repeatedly to see the range of outcomes.",
            "Investigating a simulation: change one parameter at a time and observe the effect. That's how simulations generate hypotheses.",
            "A simulation is a model, not an experiment on the real system — but it can guide which real experiments are worth running.",
        ],
        "example": """
<p>A city wants to know whether adding a traffic light reduces accidents. Building the light and waiting a year is slow and risks real crashes. A simulation models cars arriving at random intervals, the light cycling, and drivers' reaction times. It ignores weather, driver distraction, and road conditions — simplifications. Running it 10,000 times shows accidents drop 40% <em>in the model</em>. That's useful for deciding to try the light, but the 40% number shouldn't be quoted as a real-world prediction.</p>""",
        "tip": "Two answer patterns dominate. \"Why use a simulation?\" → safety, cost, time, or impossibility of the real thing. \"What's a limitation?\" → simplifying assumptions mean results may not reflect reality. If an option says a simulation gives \"exact\" or \"guaranteed\" real-world results, it's wrong.",
        "questions": [
            {
                "stem": "An engineer uses a computer simulation to test how a bridge design responds to earthquakes of different strengths. Which of the following is the most likely reason for using a simulation instead of a physical test?",
                "options": ["Simulations always produce perfectly accurate results.", "Testing a real bridge under real earthquakes would be dangerous, expensive, and impractical, while a simulation can be run many times safely.", "Simulations do not require any assumptions about the bridge.", "A physical test would require less time."],
                "answer": "B",
                "explanation": "Safety, cost, and repeatability are the core reasons to simulate. Simulations still rely on assumptions and are not perfectly accurate.",
            },
            {
                "stem": "A simulation of disease spread assumes every person has the same number of daily contacts. Which of the following best describes the effect of this assumption?",
                "options": ["It makes the simulation impossible to run.", "It is a simplification that may cause the simulation's results to differ from real-world spread.", "It guarantees the simulation matches real data.", "It eliminates the need for random values."],
                "answer": "B",
                "explanation": "Simplifying assumptions make simulations feasible but limit accuracy. The exam wants you to name that trade-off.",
            },
        ],
        "vocab": [
            ("Simulation", "a program that models a real-world or hypothetical process as an abstraction"),
            ("Simplifying assumption", "a detail intentionally left out or held constant to make a model tractable"),
        ],
    },
    {
        "num": 17, "title": "Algorithmic Efficiency", "blurb": "reasonable vs. unreasonable time, heuristics",
        "lede": "How does the work an algorithm does grow as the input grows? The CED draws one line — polynomial vs. exponential — and everything here follows from it.",
        "points": [
            "<strong>Efficiency</strong> is measured by how the number of steps (or memory) an algorithm needs grows as the <strong>input size</strong> grows — not by a stopwatch on one computer.",
            "An algorithm runs in <strong>reasonable time</strong> if its steps grow <em>polynomially</em> with input size: constant, linear (n), quadratic (n²), cubic, etc.",
            "An algorithm runs in <strong>unreasonable time</strong> if its steps grow <em>exponentially</em> (2<sup>n</sup>) or <em>factorially</em> (n!). Doubling the input can square or worse the time — these become impossible for even modest inputs.",
            "Comparing algorithms: count the operations as a function of n. Linear search is about n steps; binary search about log₂ n; comparing every pair of items is about n².",
            "Some problems have <strong>no known</strong> reasonable-time algorithm. For these, a <strong>heuristic</strong> — an approach that finds a good-enough, not necessarily optimal, solution quickly — is used instead.",
            "Heuristic example: the traveling salesperson problem (shortest route visiting every city). Checking all routes is factorial time; \"always go to the nearest unvisited city\" is a fast heuristic that gives a decent route.",
            "Efficiency often involves a trade-off with simplicity or memory. The most efficient algorithm isn't always the best choice for a small, one-time task.",
        ],
        "example": """
<p>Two algorithms check whether a list of n names contains any duplicate.</p>
<ul class="points">
<li><strong>Algorithm A:</strong> compare every name to every other name. For n = 10 that's about 45 comparisons; for n = 1,000, about 500,000. Steps grow roughly as n² — polynomial, so reasonable.</li>
<li><strong>Algorithm B:</strong> try every possible ordering of the list looking for a pattern. For n = 10 that's 3.6 million orderings; for n = 20, over 2 quintillion. Factorial — unreasonable.</li>
</ul>
<p>A is slower than a smarter approach but fine; B is unusable past tiny inputs no matter how fast the computer is.</p>""",
        "tip": "If a question gives a table of input size vs. steps, check the growth: steps doubling when n increases by 1 = exponential = unreasonable. Steps multiplying by 4 when n doubles = n² = reasonable. When the stem says \"no efficient algorithm exists\" or \"the solution doesn't have to be perfect,\" the answer involves a heuristic.",
        "questions": [
            {
                "stem": "The table shows the number of steps an algorithm takes for different input sizes.\n<table class=\"trace\"><tr><th>Input size</th><th>Steps</th></tr><tr><td>10</td><td>1,024</td></tr><tr><td>11</td><td>2,048</td></tr><tr><td>12</td><td>4,096</td></tr></table>Which of the following best describes the algorithm?",
                "options": ["It runs in reasonable time because the steps increase for each input size.", "It runs in unreasonable time because the steps double with each additional input, indicating exponential growth.", "It runs in constant time.", "It runs in linear time."],
                "answer": "B",
                "explanation": "Steps double each time n increases by 1 — that's 2ⁿ, exponential, unreasonable.",
            },
            {
                "stem": "A delivery company must plan a route through 50 cities. Checking every possible route would take longer than the age of the universe. Which approach is most appropriate?",
                "options": ["Use a heuristic that finds a good route quickly, even if it is not guaranteed to be the shortest.", "Buy a faster computer so that all routes can be checked.", "Use binary search to find the shortest route.", "Reduce the problem to one city."],
                "answer": "A",
                "explanation": "When the exact algorithm is unreasonable, a heuristic gives a usable answer in reasonable time. A faster computer doesn't overcome factorial growth.",
            },
        ],
        "vocab": [
            ("Efficiency", "how an algorithm's required steps or memory grow with input size"),
            ("Reasonable time", "polynomial growth in steps (n, n², n³ …) as input grows"),
            ("Unreasonable time", "exponential or factorial growth in steps as input grows"),
            ("Heuristic", "a technique that finds a good-enough solution quickly when an optimal one is impractical"),
        ],
    },
    {
        "num": 18, "title": "Undecidable Problems", "blurb": "problems no algorithm can solve",
        "lede": "Some problems can't be solved by any algorithm — not slow, not hard, impossible. The exam expects you to know the distinction and the famous example.",
        "points": [
            "A <strong>decidable problem</strong> is one for which an algorithm exists that gives a correct yes/no answer for <em>every</em> possible input. \"Is this number even?\" is decidable.",
            "An <strong>undecidable problem</strong> is one for which no such algorithm can exist. It's not that we haven't found one — it has been proven that none can exist.",
            "Undecidable ≠ unreasonable time. An unreasonable-time problem <em>has</em> an algorithm, just a slow one. An undecidable problem has no algorithm that works for all inputs.",
            "The classic example is the <strong>halting problem</strong>: no general algorithm can determine, for every possible program and input, whether that program will eventually stop or run forever.",
            "An algorithm may solve <em>some instances</em> of an undecidable problem (you can tell that <code>DISPLAY(\"hi\")</code> halts), but no single algorithm solves all instances.",
            "This is a theoretical limit of computing — a boundary that faster hardware or cleverer programming cannot move.",
        ],
        "example": """
<p>Someone claims to have written <code>willHalt(program, input)</code> that returns true if the program stops and false if it loops forever. Sure, it works on simple cases. But it can be shown that any such procedure must fail on at least one input — a program constructed to do the opposite of whatever <code>willHalt</code> predicts about it. That contradiction is why the halting problem is undecidable. The takeaway for the exam is just the conclusion: no general solution exists.</p>""",
        "tip": "Three categories, don't mix them: (1) reasonable time — has a fast algorithm; (2) unreasonable time — has an algorithm, but too slow, so use a heuristic; (3) undecidable — no algorithm can exist for all cases. If the stem says \"no algorithm can ever\" or mentions determining whether an arbitrary program halts, it's undecidable.",
        "questions": [
            {
                "stem": "Which of the following best describes an undecidable problem?",
                "options": ["A problem that can be solved, but only in unreasonable time", "A problem for which no algorithm can be constructed that always gives a correct yes/no answer for every input", "A problem that requires a heuristic", "A problem that has not yet been solved but eventually will be"],
                "answer": "B",
                "explanation": "Undecidable means provably no general algorithm exists — not slow, not unsolved-so-far.",
            },
            {
                "stem": "A programmer says, \"I can write a program that, given any other program and its input, will always correctly determine whether that program eventually stops.\" Which of the following is true?",
                "options": ["This is possible with a sufficiently fast computer.", "This is possible using binary search.", "This is impossible; determining whether an arbitrary program halts is an undecidable problem.", "This is possible but would take unreasonable time."],
                "answer": "C",
                "explanation": "This is the halting problem. No algorithm solves it for all programs, regardless of speed.",
            },
        ],
        "vocab": [
            ("Decidable problem", "a problem for which an algorithm exists that correctly answers every input"),
            ("Undecidable problem", "a problem for which no algorithm can correctly answer every input"),
            ("Halting problem", "the undecidable problem of determining whether an arbitrary program will stop or run forever"),
        ],
    },
]

BI3 = {
    "num": 3,
    "title": "Algorithms and Programming",
    "weight": "30–35%",
    "lede": "The largest Big Idea by far, and the one that's mostly code. Variables, expressions, conditionals, loops, lists, procedures, then algorithm efficiency and its limits. Every topic here builds on the one before it — read them in order the first time.",
    "understandings": [
        "Programs store and manipulate values with variables, expressions, and lists; data abstraction manages complexity.",
        "Algorithms are built from sequencing, selection, and iteration, and can be expressed in many forms.",
        "Procedures with parameters provide procedural abstraction, and libraries let programmers reuse others' procedures.",
        "Randomness and simulation let programs model uncertain and real-world processes.",
        "Algorithms differ in efficiency; some problems have no reasonable-time solution, and some have no solution at all.",
    ],
    "topics": BI3_TOPICS_A + BI3_TOPICS_B,
}

# ----------------------------------------------------------------------
# BIG IDEA 4
# ----------------------------------------------------------------------

BI4 = {
    "num": 4,
    "title": "Computer Systems and Networks",
    "weight": "11–15%",
    "lede": "How the internet moves data, why it keeps working when parts of it fail, and how splitting work across processors speeds things up. Three topics, dense with vocabulary.",
    "understandings": [
        "The internet is a network of networks that moves data in packets using shared protocols, and it's designed so no single failure takes it down.",
        "Fault tolerance comes from redundancy — multiple paths and backups.",
        "Parallel and distributed computing split work across processors or machines, with a speedup limited by the parts that can't be split.",
    ],
    "topics": [
        {
            "num": 1, "title": "The Internet", "blurb": "packets, protocols, routing",
            "lede": "A network of networks, connected by agreed-upon rules. The exam wants precise definitions and an understanding of how data actually travels.",
            "points": [
                "A <strong>computer network</strong> is a group of interconnected computing devices that can send and receive data. The <strong>internet</strong> is a network of networks connected by shared standards — no single organization owns or controls it.",
                "<strong>Routing</strong> is finding a path from sender to receiver. Data can take many different paths; <strong>routers</strong> pass packets toward their destination.",
                "Data is sent in <strong>packets</strong>: small chunks that each contain the data plus <strong>metadata</strong> (source and destination addresses, sequence number). Packets from one message may travel different routes and arrive out of order; they're <strong>reassembled</strong> at the destination using the sequence numbers.",
                "Every device has an <strong>IP address</strong> — a unique numeric identifier used for routing. IPv4 uses 32 bits (about 4 billion addresses, now exhausted); IPv6 uses 128 bits.",
                "<strong>Protocols</strong> are agreed rules that specify how data is formatted, addressed, transmitted, and received. Because they're <strong>open standards</strong>, any device following them can communicate with any other.",
                "Key protocols: <strong>IP</strong> (addressing and routing packets), <strong>TCP</strong> (reliable delivery — checks all packets arrive, requests re-sends, reorders), <strong>UDP</strong> (faster, no delivery guarantee — used for streaming), <strong>HTTP/HTTPS</strong> (requesting and sending web pages; HTTPS adds encryption).",
                "<strong>DNS</strong> (Domain Name System) translates human-readable names like <code>example.com</code> into IP addresses.",
                "<strong>Bandwidth</strong> is the maximum data-transfer rate of a connection, measured in bits per second. Higher bandwidth = more data per second.",
                "The <strong>World Wide Web</strong> is a system of linked pages and resources <em>that runs on</em> the internet. They aren't the same thing: the internet is the network; the web is one service using it.",
                "The internet's <strong>scalability</strong> — its ability to keep working as it grows — comes from its layered, standardized, decentralized design.",
            ],
            "example": """
<p>You type <code>example.com</code> and press Enter. Your browser asks a <strong>DNS</strong> server for that name's <strong>IP address</strong>. It then sends an <strong>HTTPS</strong> request. That request is split into <strong>packets</strong>, each stamped with your IP, the server's IP, and a sequence number. <strong>Routers</strong> forward each packet along whatever path is available — packet 3 might go through Denver while packet 4 goes through Dallas. The server's <strong>TCP</strong> layer collects them, puts them in order, and asks for any that are missing. Then it sends the page back the same way.</p>""",
            "tip": "Two distinctions the exam loves: internet vs. World Wide Web (network vs. a service on it), and TCP vs. UDP (reliable/ordered vs. fast/unguaranteed). And if an option says packets must travel the same route or arrive in order, it's wrong — they don't, and reassembly handles it.",
            "questions": [
                {
                    "stem": "Which of the following best explains how a large file is transmitted over the internet?",
                    "options": ["The file is sent as one continuous stream along a single fixed path.", "The file is divided into packets that may travel different routes and are reassembled in order at the destination.", "The file is converted to a single IP address and sent to the router.", "The file is compressed into one packet to guarantee delivery."],
                    "answer": "B",
                    "explanation": "Packet switching: split into packets, independently routed, reassembled using sequence data.",
                },
                {
                    "stem": "Which of the following best describes the relationship between the internet and the World Wide Web?",
                    "options": ["They are two names for the same thing.", "The internet is a network of networks; the World Wide Web is a system of linked resources that uses the internet.", "The World Wide Web is the physical hardware; the internet is the software.", "The internet is a subset of the World Wide Web."],
                    "answer": "B",
                    "explanation": "The web is one of many services (with email, streaming, etc.) that run over the internet.",
                },
                {
                    "stem": "Why are open protocols important to the functioning of the internet?",
                    "options": ["They allow devices made by different manufacturers to communicate using shared rules.", "They encrypt all data automatically.", "They guarantee that no packets are ever lost.", "They assign every user the same IP address."],
                    "answer": "A",
                    "explanation": "Interoperability through shared, public standards is the point of open protocols.",
                },
            ],
            "vocab": [
                ("Computer network", "interconnected devices that can send and receive data"),
                ("Internet", "a global network of networks using open protocols"),
                ("Packet", "a small unit of data with metadata for routing and reassembly"),
                ("Router", "a device that forwards packets toward their destination"),
                ("IP address", "a unique numeric address for a device on a network"),
                ("Protocol", "an agreed set of rules for formatting and transmitting data"),
                ("TCP", "a protocol that ensures reliable, ordered delivery of packets"),
                ("DNS", "the system that translates domain names into IP addresses"),
                ("Bandwidth", "the maximum rate of data transfer, in bits per second"),
                ("World Wide Web", "a system of linked resources accessed over the internet via HTTP"),
            ],
        },
        {
            "num": 2, "title": "Fault Tolerance", "blurb": "redundancy, resilience",
            "lede": "The internet keeps working when parts of it break. The reason is redundancy, and the exam wants you to explain it in those terms.",
            "points": [
                "<strong>Fault tolerance</strong> is a system's ability to continue functioning correctly when some components fail.",
                "The internet is fault tolerant because of <strong>redundancy</strong>: there are many possible paths between any two points. If a router or cable fails, packets are re-routed through another path.",
                "Redundant routing means <strong>no single point of failure</strong> — the internet doesn't depend on any one connection.",
                "Redundancy has a cost: extra hardware and connections. The trade-off is reliability versus expense.",
                "The <strong>scalability</strong> of the internet is tied to this design: adding new networks adds more paths, increasing rather than decreasing resilience.",
                "Fault tolerance applies beyond networks — backup servers, mirrored data, and duplicated power supplies are the same idea.",
                "A network is more fault tolerant when the removal of any one node still leaves every other node connected. Exam questions often show a diagram and ask which connection's failure would disconnect part of the network.",
            ],
            "example": """
<p>Picture five routers A–E where A connects to B and C, B connects to D, C connects to D, and D connects to E. If the A–B link fails, traffic from A to E still flows A→C→D→E. The network is fault tolerant for that failure. But D–E is the <em>only</em> link to E: if it fails, E is cut off entirely. D–E is a single point of failure; adding a C–E link would fix it. That's exactly the kind of diagram question the exam uses.</p>""",
            "tip": "For network-diagram questions, count paths. Ask: for each connection, if I delete it, can every device still reach every other? A connection whose removal isolates a device is the vulnerability. The answer to \"how do we improve fault tolerance\" is always \"add another path.\"",
            "questions": [
                {
                    "stem": "Which of the following best explains why the internet is considered fault tolerant?",
                    "options": ["Every packet is sent multiple times to guarantee delivery.", "There are multiple paths between devices, so data can be rerouted if a connection fails.", "All data is stored in a single central location.", "Routers never fail."],
                    "answer": "B",
                    "explanation": "Redundant paths allow rerouting around failures. That's the definition of the internet's fault tolerance.",
                },
                {
                    "stem": "A small network has four devices. Device P connects only to device Q. Devices Q, R, and S are each connected to the other two. Which of the following is true?",
                    "options": ["The network has no single point of failure.", "If the connection between Q and R fails, S can no longer reach P.", "If the connection between P and Q fails, P is disconnected from the rest of the network.", "The network is fully fault tolerant."],
                    "answer": "C",
                    "explanation": "P has exactly one connection. Losing it isolates P. Q, R, and S have redundant links to each other.",
                },
            ],
            "vocab": [
                ("Fault tolerance", "the ability of a system to keep working when components fail"),
                ("Redundancy", "having multiple copies or paths so a single failure isn't fatal"),
                ("Single point of failure", "a component whose failure would bring down the system"),
            ],
        },
        {
            "num": 3, "title": "Parallel and Distributed Computing", "blurb": "speedup, sequential vs. parallel",
            "lede": "Splitting a task across processors or machines. The exam's signature question here is computing the speedup — and understanding why it's never as much as you'd hope.",
            "points": [
                "<strong>Sequential computing</strong> executes one operation at a time, in order. Total time = sum of all operations.",
                "<strong>Parallel computing</strong> breaks a task into parts that run <em>simultaneously</em> on multiple processors (cores) in one computer.",
                "<strong>Distributed computing</strong> uses multiple <em>separate</em> computers, connected by a network, working together on one problem — often for tasks too large for a single machine.",
                "Parallel solutions are generally faster than sequential ones, <strong>but only if the task can be divided</strong>. Parts that depend on each other's results must still run in order.",
                "<strong>Speedup</strong> = sequential time ÷ parallel time. The exam gives you operation times and asks for the minimum time on a given number of processors.",
                "Speedup is limited by the <strong>sequential portion</strong>: if 20% of a task can't be parallelized, no number of processors gets you more than a 5× speedup.",
                "There's also <strong>overhead</strong> — the cost of coordinating between processors — so real speedup is always less than the ideal.",
                "Distributed computing's advantages: scales beyond one machine's limits, and can be more fault tolerant (one machine failing doesn't stop the whole job).",
            ],
            "example": """
<p>A program has three independent tasks taking 40, 30, and 20 seconds, plus a final step of 10 seconds that needs all three results.</p>
<ul class="points">
<li><strong>Sequential:</strong> 40 + 30 + 20 + 10 = <strong>100 seconds</strong>.</li>
<li><strong>Two processors:</strong> put the 40 on one processor, the 30 and 20 (= 50) on the other. The parallel phase takes 50 seconds (the longer of the two). Then the 10-second step. Total: <strong>60 seconds</strong>.</li>
<li><strong>Three processors:</strong> 40, 30, 20 each on its own → 40 seconds (the max), plus 10 → <strong>50 seconds</strong>.</li>
</ul>
<p>Speedup with three processors = 100 ÷ 50 = 2×, not 3×, because of the 10-second sequential step and the uneven task sizes.</p>""",
            "tip": "For the timing calculation: (1) list tasks that <em>must</em> be sequential — they add up; (2) for parallel tasks, distribute them to balance the processors and take the <em>longest</em> processor's total; (3) add the two. The answer is never the average of parallel tasks — it's the maximum.",
            "questions": [
                {
                    "stem": "A program has four independent tasks that take 8, 6, 4, and 2 seconds. Using two processors that can each run one task at a time, what is the minimum time to complete all tasks?",
                    "options": ["8 seconds", "10 seconds", "12 seconds", "20 seconds"],
                    "answer": "B",
                    "explanation": "Sequential would be 20. Balance: processor 1 runs 8 + 2 = 10, processor 2 runs 6 + 4 = 10. Minimum time is 10 seconds.",
                },
                {
                    "stem": "Which of the following best describes distributed computing?",
                    "options": ["Running a single task on one processor as fast as possible", "Using multiple processors within one computer to run parts of a task simultaneously", "Using multiple computers connected by a network to work together on a problem", "Compressing a program so it uses less memory"],
                    "answer": "C",
                    "explanation": "Multiple separate machines over a network = distributed. Multiple cores in one machine = parallel.",
                },
                {
                    "stem": "A task consists of a 30-second step that must run first, followed by parts that can run in parallel. Even with an unlimited number of processors, the task cannot complete in less than 30 seconds. Which of the following best explains why?",
                    "options": ["Parallel computing always takes longer than sequential computing.", "The sequential portion of a task limits the total speedup that parallelization can achieve.", "Processors cannot run at the same time.", "The task has a run-time error."],
                    "answer": "B",
                    "explanation": "The non-parallelizable part sets a floor on total time. This is the core limit of parallel speedup.",
                },
            ],
            "vocab": [
                ("Sequential computing", "operations executed one after another on a single processor"),
                ("Parallel computing", "splitting a task across multiple processors running at the same time"),
                ("Distributed computing", "multiple networked computers cooperating on one problem"),
                ("Speedup", "sequential time divided by parallel time"),
            ],
        },
    ],
}

# ----------------------------------------------------------------------
# BIG IDEA 5
# ----------------------------------------------------------------------

BI5 = {
    "num": 5,
    "title": "Impact of Computing",
    "weight": "21–26%",
    "lede": "The second-largest Big Idea, and mostly reading comprehension plus vocabulary. Every innovation has effects — good, bad, intended, unintended — and the exam rewards answers that see more than one side.",
    "understandings": [
        "Computing innovations have beneficial and harmful effects, often at the same time, and effects at scale weren't always intended.",
        "Access to computing is unequal, and that inequality (the digital divide) matters more as more of life moves online.",
        "Bias enters computing systems through data and design, and it can be identified and reduced.",
        "Crowdsourcing and citizen science let large groups solve problems and gather data.",
        "Computing raises legal and ethical questions about intellectual property, privacy, and access to information.",
        "Personal data can be collected, combined, and exploited; security practices protect it.",
    ],
    "topics": [
        {
            "num": 1, "title": "Beneficial and Harmful Effects", "blurb": "intended vs. unintended",
            "lede": "The framing question for the whole Big Idea: who does an innovation help, who does it hurt, and did anyone plan for that?",
            "points": [
                "A <strong>computing innovation</strong> includes a program as an integral part of its function — a physical device, a system, or an app. Its <strong>effect</strong> is the impact it has on society, economy, or culture.",
                "Effects can be <strong>beneficial</strong> or <strong>harmful</strong>, and the same innovation is often both — for different people or in different contexts.",
                "<strong>Intended effects</strong> are what the innovation was designed to do. <strong>Unintended effects</strong> are consequences nobody planned — and these can be positive or negative.",
                "Innovations designed for one purpose get used in ways their creators never imagined, and sometimes those uses become the main thing (the web was built for sharing physics papers).",
                "Effects at <strong>scale</strong> differ from effects on one person: a feature that's harmless for one user can reshape behavior when a billion people have it.",
                "Responsible developers consider potential harmful effects <em>during</em> development, not after. It's impossible to predict everything, which is why monitoring effects after release matters.",
                "Advances in computing have generated new careers and ended others, changed how people communicate and access information, and altered privacy expectations.",
            ],
            "example": """
<p>Ride-sharing apps. <em>Intended:</em> easier, cheaper rides. <em>Beneficial:</em> more transportation options, flexible income for drivers. <em>Harmful:</em> reduced income for taxi drivers, congestion, precarious work with no benefits. <em>Unintended:</em> changes in city parking demand and public transit ridership. A strong exam answer names at least one effect on each side and notes that the harms fall on different groups than the benefits.</p>""",
            "tip": "Options that are absolute — \"only beneficial,\" \"has no negative effects,\" \"all users are affected the same way\" — are almost always wrong. The correct option acknowledges that effects vary by group and that unintended consequences exist.",
            "questions": [
                {
                    "stem": "A social media platform introduces a feature that shows users posts their friends have liked. Which of the following is most likely an unintended harmful effect?",
                    "options": ["Users see content from friends.", "Users spend more time on the platform than they intended, affecting sleep and productivity.", "The platform's servers store more data.", "Users can like posts."],
                    "answer": "B",
                    "explanation": "The feature was intended to increase engagement; harming sleep and productivity is an unintended consequence at scale.",
                },
                {
                    "stem": "Which of the following statements about the effects of a computing innovation is most accurate?",
                    "options": ["An innovation is either beneficial or harmful, never both.", "The same innovation can be beneficial to some groups and harmful to others.", "Developers can predict all effects of an innovation before release.", "Unintended effects are always harmful."],
                    "answer": "B",
                    "explanation": "This is the CED's core framing. Effects are mixed and depend on who is affected.",
                },
            ],
            "vocab": [
                ("Computing innovation", "a device, system, or app that uses a program as an essential part of how it works"),
                ("Intended effect", "an impact the innovation was designed to produce"),
                ("Unintended effect", "a consequence not planned by the creators, which can be positive or negative"),
            ],
        },
        {
            "num": 2, "title": "Digital Divide", "blurb": "unequal access",
            "lede": "Not everyone has the same access to computing. The exam wants the causes, the consequences, and the recognition that it happens both between and within countries.",
            "points": [
                "The <strong>digital divide</strong> is the gap between people who have reliable access to computing devices and the internet and people who don't.",
                "Contributing factors: <strong>socioeconomic status</strong> (cost of devices and service), <strong>geographic location</strong> (rural areas without infrastructure), <strong>demographics</strong> (age, disability, education), and <strong>government policy</strong> (censorship, investment).",
                "The divide exists <strong>between countries</strong> and <strong>within a single country</strong> — including within a single city.",
                "Consequences compound: as school, jobs, healthcare, banking, and government services move online, lacking access means being excluded from essential parts of society.",
                "Access isn't only devices and bandwidth — it includes digital literacy (knowing how to use technology) and the availability of content in one's language.",
                "Actions that reduce the divide: public infrastructure investment, low-cost devices, community access points (libraries), and designing software to work on older devices and slow connections.",
                "Developers contribute to the divide when they assume all users have fast connections and new hardware.",
            ],
            "example": """
<p>During remote schooling, two students in the same district get the same assignments. One has home broadband and a laptop; the other shares a phone with two siblings and uses a fast-food parking lot's Wi-Fi. Same curriculum, wildly different outcomes — that's the digital divide operating within one town. A school that lends laptops and pays for hotspots is acting to narrow it.</p>""",
            "tip": "The digital divide is about <em>access</em>, not attitude. Options describing people who \"choose\" not to use technology are distractors. And it's not only an international issue — a question set entirely within the US can still be about the digital divide.",
            "questions": [
                {
                    "stem": "Which of the following is an example of the digital divide?",
                    "options": ["Two students use different brands of laptop.", "Students in a rural area lack broadband access and cannot complete online homework, while students in a nearby city can.", "A student prefers paper books to e-books.", "A website is available in multiple languages."],
                    "answer": "B",
                    "explanation": "Unequal access based on geography that affects opportunity is the definition of the digital divide.",
                },
                {
                    "stem": "Which of the following actions would most directly help reduce the digital divide?",
                    "options": ["Requiring all websites to use high-resolution video", "Providing free public internet access and affordable devices in underserved communities", "Increasing the price of internet service", "Designing apps that only run on the newest phones"],
                    "answer": "B",
                    "explanation": "Reducing cost and infrastructure barriers directly expands access. The other options widen the gap.",
                },
            ],
            "vocab": [
                ("Digital divide", "the gap between those with reliable access to computing and the internet and those without"),
                ("Digital literacy", "the skills needed to use computing technology effectively"),
            ],
        },
        {
            "num": 3, "title": "Computing Bias", "blurb": "bias in data and design",
            "lede": "Programs reflect the data they're built on and the assumptions of the people who built them. Bias is often unintentional, which is exactly why it needs to be looked for.",
            "points": [
                "<strong>Computing bias</strong> occurs when a computing innovation systematically produces unfair or skewed outcomes for certain groups.",
                "Bias can enter through the <strong>data</strong>: if training data underrepresents a group, the system performs worse for that group (e.g., facial recognition trained mostly on one demographic).",
                "Bias can enter through <strong>design choices</strong>: which features are included, what the defaults are, what's considered \"normal\" — reflecting the assumptions of the developers.",
                "Bias can be <strong>intentional or unintentional</strong>. Most exam scenarios are unintentional — a well-meaning team that didn't test with diverse users.",
                "Bias may exist at <strong>every level</strong> of development, from problem selection to data collection to testing.",
                "Programmers should <strong>take action to reduce bias</strong>: audit data for representativeness, test with diverse users, involve diverse teams (this is why 1.1 emphasizes diverse collaboration), and examine outcomes by group.",
                "Bias in a system used at scale — hiring, lending, policing — can amplify existing inequality dramatically.",
            ],
            "example": """
<p>A company builds a résumé-screening tool by training it on a decade of past hiring decisions. Those past decisions favored one gender for engineering roles. The tool learns the pattern and down-ranks résumés with signals associated with the other gender. Nobody at the company <em>intended</em> that — the bias was in the historical data. Detecting it required checking the tool's outcomes by group, and fixing it required different data, not just different code.</p>""",
            "tip": "Look for the source. If the scenario mentions training data, the bias came from the data. If it mentions who was on the team or what they assumed, it's design. Options claiming bias can be eliminated by \"using more advanced algorithms\" alone are wrong — you have to address the data and the assumptions.",
            "questions": [
                {
                    "stem": "A voice assistant was tested only with speakers of one regional accent and performs poorly for users with other accents. Which of the following best describes this situation?",
                    "options": ["A syntax error in the program", "Computing bias resulting from unrepresentative data and testing", "An example of the digital divide", "Lossy compression of audio"],
                    "answer": "B",
                    "explanation": "Underrepresentation in data/testing leading to worse performance for a group is computing bias.",
                },
                {
                    "stem": "Which of the following is the most effective way for a development team to reduce bias in a program that recommends loan approvals?",
                    "options": ["Use a larger number of processors.", "Examine the training data for underrepresented groups and test outcomes across demographic groups before deployment.", "Remove all comments from the code.", "Compress the data before analysis."],
                    "answer": "B",
                    "explanation": "Auditing data and testing outcomes by group directly targets the sources of bias.",
                },
            ],
            "vocab": [
                ("Computing bias", "systematic unfairness in a computing system's outcomes toward certain groups"),
                ("Training data", "the data used to build a system's behavior; unrepresentative data produces biased results"),
            ],
        },
        {
            "num": 4, "title": "Crowdsourcing", "blurb": "citizen science, distributed effort",
            "lede": "Using the internet to gather help, data, or money from a large, distributed group. Short topic, reliable points.",
            "points": [
                "<strong>Crowdsourcing</strong> obtains input, ideas, services, or funding from a large group of people, typically online.",
                "<strong>Citizen science</strong> is crowdsourced scientific research: members of the public collect or classify data (bird counts, galaxy classification) that researchers couldn't gather alone.",
                "The internet makes crowdsourcing possible by connecting large numbers of people cheaply and letting them contribute in small pieces.",
                "Benefits: <strong>scale</strong> (thousands of contributors), <strong>speed</strong>, <strong>diversity</strong> of input, and lower cost. Some problems are only solvable this way.",
                "Examples: collaborative encyclopedias, funding platforms, mapping projects, distributed volunteer computing, product reviews, and bug-finding contests.",
                "Limitations: contributions can be inconsistent in quality, contributors may share biases, and results need verification.",
                "Crowdsourcing also enables new business and creative models that didn't exist before widespread connectivity.",
            ],
            "example": """
<p>Astronomers have millions of telescope images of galaxies and need each classified by shape. A program can't do it reliably, and one lab would take decades. They post the images online with a simple tutorial; hundreds of thousands of volunteers classify them, each image getting several independent classifications that are compared for agreement. That's citizen science: the crowd provides the labor, the design provides the quality control.</p>""",
            "tip": "If a scenario involves many members of the public contributing data or effort over the internet toward a shared goal, the answer is crowdsourcing (or citizen science if it's research). Don't confuse it with distributed computing — that's machines sharing work, not people.",
            "questions": [
                {
                    "stem": "A research group asks the public to photograph and upload pictures of local insects, which the researchers use to track species populations. This is best described as an example of which of the following?",
                    "options": ["Citizen science", "Distributed computing", "The digital divide", "Data compression"],
                    "answer": "A",
                    "explanation": "Public participation in gathering scientific data is citizen science, a form of crowdsourcing.",
                },
                {
                    "stem": "Which of the following is a benefit of crowdsourcing that would be difficult to achieve otherwise?",
                    "options": ["Guaranteed accuracy of every contribution", "Collecting data or ideas from a very large and diverse group of people quickly and at low cost", "Elimination of all bias", "Faster processor speeds"],
                    "answer": "B",
                    "explanation": "Scale and diversity at low cost is the distinctive benefit. Accuracy and bias still need managing.",
                },
            ],
            "vocab": [
                ("Crowdsourcing", "gathering input, work, or funding from a large group of people, usually online"),
                ("Citizen science", "scientific research that relies on public volunteers to collect or analyze data"),
            ],
        },
        {
            "num": 5, "title": "Legal and Ethical Concerns", "blurb": "intellectual property, licenses, open source",
            "lede": "Who owns code and content, what you're allowed to do with it, and where computing raises ethical questions that don't have settled answers.",
            "points": [
                "<strong>Intellectual property (IP)</strong> is work or an invention that results from creativity and to which someone has rights — including software, images, music, and text.",
                "<strong>Copyright</strong> protects creative works; using someone's material without permission is a violation. Software, artwork, and writing found online are copyrighted by default even without a notice.",
                "<strong>Creative Commons</strong> licenses let creators grant specific permissions in advance (e.g., free to use with attribution, or free for non-commercial use), so others can reuse work without asking.",
                "<strong>Open source</strong> software makes its source code freely available to use, study, modify, and distribute, under a license that sets the terms. <strong>Open access</strong> refers to freely available research and publications.",
                "The <strong>Create Task</strong> requires you to cite any code you didn't write yourself. Using others' code is fine; failing to credit it is not.",
                "Ethical concerns raised by computing: <strong>privacy</strong> and surveillance, <strong>algorithmic decision-making</strong> in high-stakes areas, the spread of <strong>misinformation</strong>, and access to technology that can be used for harm as well as good.",
                "Legal concerns include <strong>plagiarism</strong>, <strong>piracy</strong>, <strong>hacking</strong> and unauthorized access, and misuse of personal data. Laws vary by country and lag behind technology.",
                "Computing innovations can be used in ways their creators find objectionable — the exam asks whether the developer, the user, or society bears responsibility, and expects nuance.",
            ],
            "example": """
<p>You find a JavaScript animation library on the web with no license file. You can look at it, but copying it into your project is a copyright question — no license means all rights reserved. Another library uses an open-source license that permits reuse with attribution. You use that one and credit it in your code comments. On the Create Task, the credited library is fine; uncredited copied code is treated as plagiarism.</p>""",
            "tip": "\"No license\" does not mean \"free to use\" — it means default copyright. Open source and Creative Commons both <em>grant</em> permissions; they don't remove copyright. On ethics questions, the correct answer usually recognizes competing interests rather than declaring one side simply right.",
            "questions": [
                {
                    "stem": "A student finds a photograph online with a Creative Commons license that permits reuse with attribution. Which of the following is an appropriate use of the photo?",
                    "options": ["Using the photo without credit, since it is Creative Commons", "Using the photo in a project and crediting the photographer as the license requires", "Claiming the photo as the student's own work", "Selling the photo under the student's name"],
                    "answer": "B",
                    "explanation": "Creative Commons licenses grant specific permissions with conditions; attribution is the condition here.",
                },
                {
                    "stem": "Which of the following best describes open source software?",
                    "options": ["Software that has no copyright", "Software whose source code is freely available to use, modify, and share under the terms of its license", "Software that is free to download but whose code is hidden", "Software created by the government"],
                    "answer": "B",
                    "explanation": "Open source = available source code under a license. It is still copyrighted; the license grants rights.",
                },
            ],
            "vocab": [
                ("Intellectual property", "creative work or inventions to which a person or organization holds rights"),
                ("Copyright", "legal protection of a creative work that restricts copying and reuse"),
                ("Creative Commons", "licenses that let creators pre-authorize specific kinds of reuse"),
                ("Open source", "software whose source code is freely available under a license permitting use and modification"),
                ("Plagiarism", "presenting someone else's work as your own"),
            ],
        },
        {
            "num": 6, "title": "Safe Computing", "blurb": "PII, security, encryption, attacks",
            "lede": "The longest topic in the Big Idea and a frequent source of questions: what data is at risk, how it gets stolen, and how it's protected.",
            "points": [
                "<strong>Personally identifiable information (PII)</strong> is information that can be used to identify a person: name, address, Social Security number, date of birth, biometric data, medical and financial records, and more.",
                "PII is collected through <strong>search history, location, cookies, and app activity</strong>. Combining seemingly harmless pieces can identify someone. Once online, information is hard to remove.",
                "PII enables useful personalization but can be used for <strong>stalking, identity theft, and targeted manipulation</strong>. It is often collected and sold without users' full awareness.",
                "<strong>Authentication</strong> proves identity. <strong>Strong passwords</strong> are long and not reused. <strong>Multifactor authentication</strong> requires two or more of: something you <em>know</em> (password), something you <em>have</em> (phone, key), something you <em>are</em> (fingerprint).",
                "<strong>Encryption</strong> scrambles data so it's unreadable without a key. <strong>Symmetric</strong> encryption uses one shared key for both encrypting and decrypting. <strong>Public key (asymmetric)</strong> encryption uses a public key to encrypt and a private key to decrypt — anyone can send you a secret message, only you can read it.",
                "<strong>Certificate authorities</strong> issue digital certificates that verify a website's public key really belongs to that site. This is what makes HTTPS trustworthy.",
                "<strong>Attacks to know:</strong> <strong>malware</strong> (software designed to damage or gain unauthorized access), <strong>virus</strong> (malware that attaches to other programs and spreads), <strong>phishing</strong> (fake messages that trick people into revealing information), <strong>keylogging</strong> (recording keystrokes), <strong>rogue access points</strong> (fake Wi-Fi that intercepts traffic).",
                "Data traveling over an unsecured network can be intercepted; encryption (like HTTPS) protects it in transit.",
                "<strong>Software updates</strong> patch known security vulnerabilities — running old versions leaves known holes open.",
                "Users should read what data an app collects, limit permissions, and recognize that free services are often paid for with personal data.",
            ],
            "example": """
<p><strong>Public key encryption in one paragraph:</strong> Alice publishes her public key anywhere. Bob uses it to encrypt a message. Only Alice's private key — which she never shares — can decrypt it. Even if someone intercepts the message and has Alice's public key, they can't read it, because the public key only <em>locks</em>. That asymmetry is what lets strangers communicate securely over an open network without first meeting to share a password.</p>
<p><strong>Multifactor in one line:</strong> password (know) + code texted to your phone (have) = two factors. Two passwords is still one factor.</p>""",
            "tip": "Vocabulary questions dominate here. Phishing is the person being tricked; keylogging is the keystrokes being recorded; a virus spreads by attaching to programs; a rogue access point is a fake network. For encryption: symmetric = one shared key; public key = a public lock and a private unlock. And multifactor means different <em>categories</em>, not just multiple steps.",
            "questions": [
                {
                    "stem": "A user receives an email that appears to be from their bank, asking them to click a link and enter their password to \"verify their account.\" The link leads to a fake site. This is an example of which of the following?",
                    "options": ["Keylogging", "Phishing", "A rogue access point", "A virus"],
                    "answer": "B",
                    "explanation": "Deceptive messages that trick people into giving up information are phishing.",
                },
                {
                    "stem": "Which of the following is an example of multifactor authentication?",
                    "options": ["Entering a password and then a second, different password", "Entering a password and then a code sent to the user's phone", "Entering the same password twice", "Choosing a very long password"],
                    "answer": "B",
                    "explanation": "Password (something you know) + phone code (something you have) uses two different factor categories.",
                },
                {
                    "stem": "In public key encryption, which of the following is true?",
                    "options": ["The same key is used to encrypt and decrypt a message.", "The public key is used to encrypt, and only the corresponding private key can decrypt.", "The private key must be shared with anyone who wants to send a message.", "Public key encryption cannot be used over the internet."],
                    "answer": "B",
                    "explanation": "Asymmetric encryption: public key locks, private key unlocks, and the private key is never shared.",
                },
                {
                    "stem": "Which of the following is considered personally identifiable information (PII)?",
                    "options": ["The current temperature in a city", "A person's date of birth combined with their home address", "The number of users of a website", "A public domain image"],
                    "answer": "B",
                    "explanation": "Information that can identify a specific individual — especially in combination — is PII.",
                },
            ],
            "vocab": [
                ("PII", "personally identifiable information — data that can identify an individual"),
                ("Multifactor authentication", "verifying identity with two or more categories of evidence: know, have, are"),
                ("Encryption", "converting data into a form unreadable without a key"),
                ("Symmetric encryption", "one shared key encrypts and decrypts"),
                ("Public key encryption", "a public key encrypts; only the matching private key decrypts"),
                ("Certificate authority", "a trusted organization that verifies a site's public key via a digital certificate"),
                ("Malware", "software designed to damage a system or gain unauthorized access"),
                ("Virus", "malware that attaches to programs and spreads when they run"),
                ("Phishing", "tricking people into revealing information through fake messages or sites"),
                ("Keylogging", "secretly recording a user's keystrokes"),
                ("Rogue access point", "a fake wireless network set up to intercept traffic"),
            ],
        },
    ],
}

BIG_IDEAS = [BI1, BI2, BI3, BI4, BI5]
