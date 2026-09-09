# -*- coding: utf-8 -*-
"""
The Stacks — depth pass for AP CSP.
Keyed "unit.topic". Each entry adds:
  deeper   – points that go past the essential knowledge into the
             nuance, edge cases, and connections the exam actually tests
  mistakes – the specific errors students make on this topic, framed as
             what the wrong answer looks like and why it's wrong
  trace    – optional id of an interactive trace (see traces.py)
"""

DEPTH_CSP = {
    "1.1": {
        "deeper": [
            "The CED gives a specific list of what collaboration <em>reduces</em>: it reduces bias, reduces errors (more eyes on the code), and makes programs more usable by more people (more perspectives on who the users are). When an exam option lists one of these three, that's the signal it's correct.",
            "Collaboration works because of <strong>complementary skills</strong>: one person may be strong at algorithm design, another at interface design, another at testing. The exam frames this as \"different perspectives and skills\" — the phrase to look for.",
            "Communication isn't only talking: shared documents, code comments, commit messages, and issue trackers are all collaboration tools. A question describing a team using a shared repository with change tracking is describing collaboration infrastructure.",
            "Consensus building means the team agrees on decisions rather than one person dictating; conflict resolution means disagreements get worked through, not ignored. Both are named in the CED as things effective collaborators do.",
            "The Create Task is <em>individual</em> even though collaboration during development is allowed — you must be able to say exactly what you personally wrote. Collaborating on ideas is fine; submitting someone else's algorithm as your own is not.",
        ],
        "mistakes": [
            "<strong>Picking an option about performance.</strong> \"Collaboration makes the program run faster / use less memory\" is always wrong. Collaboration affects the development process and the quality of the design, not the program's execution.",
            "<strong>Confusing pair programming with splitting work.</strong> In pair programming both people work on the <em>same</em> code at the <em>same</em> time. If two people each write half the program separately, that's dividing labor, not pair programming.",
            "<strong>Assuming collaboration means more people = always better.</strong> The CED's claim is about diverse perspectives, not headcount. A team of ten identical thinkers doesn't get the benefit.",
        ],
    },
    "1.2": {
        "deeper": [
            "The CED distinguishes input types you should be able to name: <strong>tactile</strong> (keyboard, touchscreen), <strong>audio</strong> (microphone), <strong>visual</strong> (camera), and <strong>text</strong>. A sensor reading — temperature, GPS — is also input. Output can be tactile too (a phone vibrating).",
            "<strong>Event-driven programming</strong> is a distinct model from sequential: the program sets up handlers and then waits. Nothing happens until a click, key press, timer, or message arrives. Most apps you use are event-driven; most exam pseudocode is sequential. Know both.",
            "A program's <strong>purpose</strong> can be for the developer alone — to learn, to satisfy curiosity, to create art. The exam explicitly says a program \"can be developed for creative expression\" or \"to satisfy personal curiosity,\" and those are as legitimate as solving a business problem.",
            "\"Programs can generate new knowledge\" means the <em>output</em> teaches the programmer something they didn't know. Running a simulation of a coin flip 10,000 times and seeing the ratio converge is new knowledge even though you wrote the program.",
            "A <strong>code statement</strong> is a single instruction (<code>x ← 5</code>). A <strong>code segment</strong> is several statements together. An <strong>expression</strong> is something that evaluates to a value (<code>x + 1</code>) and isn't a complete statement on its own. The exam uses all three terms precisely.",
        ],
        "mistakes": [
            "<strong>Swapping purpose and function on the Create Task.</strong> Purpose = why the program exists (the problem or need). Function = what it does when it runs (inputs → processing → outputs). Writing \"the purpose is to display a menu\" describes function, not purpose.",
            "<strong>Calling an output an event.</strong> An event is something that <em>happens to</em> the program (user clicks). The display that results is output. In a question about a button that shows a quote, the click is the event and the quote is the output — not the reverse.",
            "<strong>Assuming every program must have user input.</strong> A program can take input from a file or sensor with no human involved, or take no input at all and still produce output.",
        ],
    },
    "1.3": {
        "deeper": [
            "The CED describes two development processes: <strong>iterative</strong> and <strong>incremental</strong>, and also notes that some processes are <em>unstructured or exploratory</em> — you try things and see what works. Exploratory development is legitimate, especially early; the exam won't call it wrong.",
            "The four phases — <strong>investigating and reflecting</strong>, <strong>designing</strong>, <strong>prototyping</strong>, <strong>testing</strong> — aren't strictly linear. Testing reveals design flaws, which sends you back to designing. That loop is what \"iterative\" means.",
            "<strong>Investigating</strong> includes understanding the <em>users</em>, not just the problem: who are they, what do they need, what constraints do they have? A program designed without investigating users tends to serve the developer's assumptions instead. This links to 5.3 (bias).",
            "<strong>Program specifications</strong> — a description of what the program must do — come out of the investigating phase. The exam may call them <em>requirements</em>. They can change during development, and accommodating change is part of the process, not a failure.",
            "Documentation serves <strong>future developers</strong>, <strong>collaborators</strong>, <strong>users</strong>, and <strong>your future self</strong>. The CED's specific claim: documentation is useful \"during development\" as well as after, because it helps you keep track of what you've done and why.",
            "Two kinds of abstraction appear in design: <strong>procedural</strong> (a named procedure stands in for its steps) and <strong>data</strong> (a list stands in for many values). Good design uses both to keep the program understandable.",
        ],
        "mistakes": [
            "<strong>Treating iterative and incremental as synonyms.</strong> The exam tests them separately. Iterative = repeating the phases to refine. Incremental = building in small working pieces. A team that builds a rough full version, tests, and refines it is iterating. A team that builds feature 1, tests, then feature 2 is being incremental.",
            "<strong>Thinking documentation is written only at the end.</strong> Options saying \"documentation is completed after the program is finished\" are wrong per the CED. It's throughout.",
            "<strong>Believing comments affect the program.</strong> Comments are ignored by the computer. Any option claiming comments make code faster, slower, or fix errors is a distractor.",
            "<strong>Skipping investigation on the Create Task.</strong> Students jump to coding, then can't answer the written response about their program's purpose for a specific user. Decide who it's for first.",
        ],
    },
    "1.4": {
        "deeper": [
            "The CED gives exactly four error types: <strong>syntax</strong>, <strong>logic</strong>, <strong>run-time</strong>, and <strong>overflow</strong>. Overflow is its own category — a number too large for the storage available. Some resources fold it into run-time errors; the exam lists it separately.",
            "A subtle point: a <strong>logic error</strong> can produce correct output for some inputs and wrong output for others. That's why it's dangerous — testing with one input can miss it. Boundary values (0, negative, empty, max) are where logic errors hide.",
            "<strong>Testing</strong> has a specific shape in the CED: choose inputs, predict the expected output, run, compare. If they don't match, there's an error. The prediction step is what students skip — without it, you can't tell whether output is right.",
            "<strong>Debugging by hand-tracing</strong> means executing the code mentally or on paper with a specific input, recording variable values at each step. It's slow but reliable, and it's the method the exam's own code-analysis questions require you to use anyway.",
            "<strong>Extra output statements</strong> (temporary DISPLAY calls showing a variable's value mid-program) are a legitimate, CED-named debugging technique. Remove them when done.",
            "Programs with syntax errors <em>cannot</em> be run, so their behavior is never \"wrong output\" — it's \"no output.\" A question describing a program that ran and did something has ruled out syntax errors by definition.",
        ],
        "mistakes": [
            "<strong>Calling a crash a logic error.</strong> If the program <em>stops</em> with an error message partway, it's run-time. Logic errors run to completion. The word \"terminates unexpectedly\" or \"crashes\" means run-time.",
            "<strong>Calling a wrong answer a syntax error.</strong> Syntax errors prevent running. If the program produced a value, its syntax was fine.",
            "<strong>Testing only typical inputs.</strong> The exam's \"which test case would reveal the error\" questions almost always have the answer at a boundary — the empty list, the value exactly equal to the threshold, zero.",
            "<strong>Assuming a program that ran without errors is correct.</strong> No error message means no syntax or run-time error. It says nothing about logic.",
        ],
    },
    "2.1": {
        "deeper": [
            "The CED asks you to understand <strong>place value</strong> in both bases, not just memorize conversions. In decimal, 352 = 3×100 + 5×10 + 2×1. In binary, 101 = 1×4 + 0×2 + 1×1. Same idea, different base.",
            "<strong>Analog vs. digital:</strong> analog data (sound waves, temperature) is continuous. Digital data is discrete. Converting analog to digital means <strong>sampling</strong> — measuring at regular intervals — and each sample is stored as a number. More samples per second and more bits per sample = higher fidelity and larger file.",
            "<strong>Bit width limits</strong> matter in real languages. An 8-bit unsigned integer holds 0–255; add 1 to 255 and it wraps to 0 (overflow). A 32-bit signed integer maxes at about 2.1 billion. AP pseudocode ignores this, but the concept is tested.",
            "<strong>Round-off error</strong> comes from real numbers: 1/3 can't be stored exactly in any finite number of bits, in any base. So 0.1 + 0.2 might not exactly equal 0.3 in a computer. This is why financial software often works in cents (integers) rather than dollars (decimals).",
            "Converting binary to decimal quickly: write the place values above the digits from the right (1, 2, 4, 8, 16, 32, 64, 128). Converting decimal to binary: subtract the largest power of 2 that fits, repeat. Or divide by 2 repeatedly and read the remainders bottom-up.",
            "The number of bits needed to represent N distinct values is the smallest n with 2<sup>n</sup> ≥ N. 100 values need 7 bits (2<sup>7</sup> = 128). 1,000 values need 10 bits.",
        ],
        "mistakes": [
            "<strong>Off-by-one on place values.</strong> The rightmost bit is worth 1, not 2. Students who start at 2 get every conversion wrong by a factor.",
            "<strong>Answering with the number of bits instead of the number of values.</strong> \"How many values can 5 bits represent?\" is 32, not 5. \"How many bits to represent 32 values?\" is 5.",
            "<strong>Thinking adding a bit adds a fixed number of values.</strong> It <em>doubles</em> them. 3 bits → 8, 4 bits → 16, 5 bits → 32.",
            "<strong>Confusing sampling rate with bit depth.</strong> Rate = how often you measure; depth = how many bits each measurement gets. Both affect quality and size, in different ways.",
        ],
    },
    "2.2": {
        "deeper": [
            "The CED says the choice between lossy and lossless depends on the <em>purpose</em>: is the goal to <strong>minimize size</strong> or to <strong>preserve every detail</strong>? Questions give you a purpose and expect the matching choice.",
            "Lossless compression exploits <strong>redundancy</strong> — patterns, repetition, predictable structure. Text has lots (common letters, repeated words), so it compresses well. Random data has none and barely compresses at all.",
            "Lossy compression exploits <strong>perception</strong>: humans can't hear very high frequencies or see tiny color differences between adjacent pixels, so that data can be dropped without a noticeable change. The \"loss\" is real but designed to be invisible.",
            "Lossy compression is <strong>irreversible</strong>. Decompressing a JPEG gives you an approximation of the original image, not the original. Compressing it again loses more. This is why editing workflows keep a lossless master.",
            "Compression ratio and quality trade off continuously — a lossy algorithm typically has a quality setting. Higher compression = smaller file = more loss. The exam may describe this as a slider or a percentage.",
            "Compression is about <strong>size</strong> (storage) and <strong>transmission time</strong> (bandwidth). It has nothing to do with security. Compressed data is not encrypted.",
        ],
        "mistakes": [
            "<strong>Choosing lossy for anything that must be exact.</strong> Text documents, program source code, financial records, medical scans for diagnosis, legal archives: lossless. If the stem says \"exactly,\" \"perfectly,\" \"identical,\" or \"no data lost,\" it's lossless.",
            "<strong>Assuming lossless always gives the smallest file.</strong> It's the opposite — lossy compresses far more. Lossless is the <em>safe</em> choice, not the <em>small</em> choice.",
            "<strong>Confusing compression with encryption.</strong> An option saying \"compress the file so it can't be read by others\" is wrong. Compression doesn't hide data.",
            "<strong>Thinking a decompressed lossy file is restored.</strong> It's not. The detail is gone permanently.",
        ],
    },
    "2.3": {
        "deeper": [
            "The CED separates <strong>data</strong> (raw facts) from <strong>information</strong> (what you learn from analyzing data) and <strong>knowledge</strong> (what you can do with that information). A list of temperatures is data. \"Average temperature rose 2° over ten years\" is information. \"We should plan for more cooling demand\" is knowledge.",
            "<strong>Metadata</strong> has a precise role in the CED: it helps <em>find, organize, and manage</em> data. A photo library sorted by date uses metadata; searching email by sender uses metadata. Changing metadata (renaming a file) doesn't change the data (the file's contents).",
            "Metadata is also a <strong>privacy vector</strong>. A photo's GPS metadata reveals where you were. An email's header metadata reveals who you talk to and when, even if the message is encrypted. This is why \"harmless\" metadata can matter.",
            "<strong>Scalability</strong> of data processing: as datasets grow to millions or billions of records, single computers can't hold or process them in reasonable time. This is where parallel and distributed computing (Big Idea 4) enters — the two Big Ideas connect here.",
            "<strong>Incomplete or invalid data</strong> can come from collection errors, sensor failures, people skipping survey questions, or data corruption. The exam's point: conclusions drawn from flawed data are flawed, no matter how good the analysis.",
            "Data can be <strong>biased at collection</strong> (who was surveyed), <strong>at cleaning</strong> (which records were removed), and <strong>at visualization</strong> (a chart with a truncated axis exaggerates differences). Each stage is a place bias can enter.",
            "Combining datasets can reveal patterns, but it can also <strong>de-anonymize</strong> people: individually harmless datasets, when joined, can identify individuals. This is a real privacy concern the CED expects you to recognize.",
        ],
        "mistakes": [
            "<strong>Accepting causation from correlation.</strong> The most common wrong answer in this topic. If two things trend together, the correct options say \"correlated\" or \"a third factor may explain it.\" Options saying \"X causes Y\" are wrong unless the question describes a controlled experiment.",
            "<strong>Thinking metadata is part of the data.</strong> The date a document was created isn't in the document's text. The exam treats them as separate.",
            "<strong>Assuming more data fixes bias.</strong> If the collection method is biased, more data from the same method is more biased data. The fix is a better method, not more volume.",
            "<strong>Reading a chart without checking the axes.</strong> Truncated or uneven axes are a named form of misleading visualization. If a question shows a chart, look at the scale before drawing conclusions.",
        ],
    },
    "2.4": {
        "deeper": [
            "This topic exists because the CED wants you to understand that <strong>programs, not people, do the work</strong> on large data. A human can't compute the average of ten million values; a five-line loop can. The value of computing is that it makes analysis of large datasets possible at all.",
            "<strong>Cleaning</strong> in the CED means making data <em>uniform</em> without changing its <em>meaning</em>: consistent capitalization, consistent date formats, consistent units, removing exact duplicates, deciding how to handle blanks. The \"without changing meaning\" clause is what separates cleaning from manipulation.",
            "<strong>Transformation</strong> derives new values from existing ones: converting Celsius to Fahrenheit, computing a per-student average from a list of scores, combining first and last name into one field. The original data is preserved; new columns are added.",
            "<strong>Filtering</strong> selects a subset by condition (only seniors, only scores above 80). <strong>Sorting</strong> orders by a field. <strong>Aggregating</strong> combines many records into a summary (count, sum, average, max). Most analyses chain these.",
            "<strong>Visualization</strong> choices matter: a bar chart for categories, a line chart for change over time, a scatter plot for relationships between two variables. The wrong chart type hides the pattern.",
            "The CED says data analysis can raise <em>new questions</em>, driving new collection. That iterative loop is the same idea as iterative development — investigate, analyze, refine, repeat.",
        ],
        "mistakes": [
            "<strong>Calling manipulation \"cleaning.\"</strong> If an option describes changing values to produce a desired conclusion (\"adjusting outliers upward to raise the average\"), that's not cleaning — it's falsification. Cleaning never changes meaning.",
            "<strong>Skipping cleaning and analyzing anyway.</strong> Questions that describe inconsistent data (\"NY\" and \"New York\") and ask what to do first want cleaning, not analysis.",
            "<strong>Choosing a visualization that hides the pattern.</strong> A pie chart for change over time, a line chart for unrelated categories. Match chart to question.",
        ],
    },
    "3.1": {
        "deeper": [
            "A variable's <strong>value can change</strong> (that's what makes it a variable) but its <strong>name and type</strong> don't. In AP pseudocode types aren't declared, but the exam still expects you to know what type a value is: 5 is a number, \"5\" is a string, true is a Boolean.",
            "Assignment is <strong>not symmetric</strong>. <code>a ← b</code> changes a and leaves b alone. <code>b ← a</code> is the opposite. Read the arrow: the value flows into the variable at the arrowhead's base.",
            "The <strong>order of statements</strong> is the order of evaluation. <code>x ← 5</code> then <code>x ← x * 2</code> gives 10. Reversed, x would be 5 (the first line would use whatever x was before). Sequencing questions test exactly this.",
            "Copying a value into a second variable creates an <em>independent</em> copy for simple values. Later changes to either don't affect the other. (Lists behave differently in some languages, but AP pseudocode questions generally treat list assignment as a copy too.)",
            "<strong>Swapping</strong> needs three assignments and a temporary. Two assignments (<code>a ← b</code>, <code>b ← a</code>) leave both variables with b's original value — the first line destroyed a's value before it was saved.",
            "Variable names should describe what the variable holds. The exam's own questions use descriptive names (<code>total</code>, <code>count</code>, <code>isFound</code>), and reading them tells you the algorithm's intent before you trace.",
        ],
        "mistakes": [
            "<strong>Tracing in your head.</strong> The single biggest source of wrong answers in Big Idea 3. A table with one row per statement takes 30 seconds and removes the errors.",
            "<strong>Reading ← as equals.</strong> <code>x ← x + 1</code> isn't a false equation; it's an instruction. Evaluate the right side with the current x, store the result in x.",
            "<strong>Assuming the copy updates.</strong> After <code>b ← a</code>, changing a does <em>not</em> change b. Students expect b to \"follow\" a. It doesn't.",
            "<strong>Botching the swap.</strong> If a question asks which code segment swaps two values, the answer uses a temp variable. Any two-line answer is wrong.",
        ],
        "trace": None,
    },
    "3.2": {
        "deeper": [
            "The CED phrase is that data abstraction \"provides a separation between the abstract properties of a data type and the concrete details of its representation.\" In plain terms: you think of <code>scores</code> as \"the list of scores\" and don't think about where each number lives in memory.",
            "A list can hold <strong>different types</strong> in AP pseudocode — numbers, strings, Booleans, even other lists — though most exam lists are one type. A list of lists is how you'd model a grid.",
            "The Create Task requires that your list (a) is used to <strong>store data</strong> and (b) that the program's <strong>functionality would be harder or impossible without it</strong>. The written response asks you to explain how the list manages complexity. The expected answer: without the list, you'd need a separate variable for each value, and code would have to change every time the number of values changed.",
            "<strong>Index starts at 1</strong> in AP pseudocode. <code>list[1]</code> is the first element, <code>list[LENGTH(list)]</code> is the last. Every real language you'll use starts at 0 — the exam is the exception, and it's deliberate: they test whether you read the reference sheet.",
            "Lists are <strong>ordered</strong>: the position of each element is meaningful and stable. Two lists with the same elements in different orders are different lists.",
            "A <strong>string</strong> is conceptually an ordered list of characters, but AP pseudocode doesn't let you index into strings the way you index lists. The exam defines any string operations it needs within the question.",
        ],
        "mistakes": [
            "<strong>Index 0.</strong> <code>list[0]</code> in AP pseudocode is an error. The first element is <code>list[1]</code>. This single fact is tested on nearly every exam.",
            "<strong>Explaining the list too vaguely on the Create Task.</strong> \"The list stores my data\" doesn't earn the point. You need: what the list holds, and why the program couldn't do its job without it (or would need many separate variables).",
            "<strong>Confusing data abstraction with procedural abstraction.</strong> A list is data abstraction. A procedure is procedural abstraction. Both \"manage complexity,\" but they're different mechanisms and the Create Task asks about them separately.",
        ],
    },
    "3.3": {
        "deeper": [
            "<strong>MOD's precedence</strong> is the same as multiplication and division — higher than addition and subtraction. <code>10 + 7 MOD 3</code> is <code>10 + 1 = 11</code>, not <code>17 MOD 3 = 2</code>. When operators are the same precedence, evaluate left to right.",
            "<strong>MOD for wraparound:</strong> if you're cycling through positions 1 to n and want to go from n back to 1, the formula is <code>(i MOD n) + 1</code>. Try it: i = n gives (0) + 1 = 1. i = 1 gives 2. This shows up in circular list and clock problems.",
            "<strong>MOD for digit extraction:</strong> <code>n MOD 10</code> is the last digit; <code>n MOD 100</code> is the last two digits. To get other digits you'd need division, and the exam may define an integer-division procedure for that purpose within a question.",
            "<strong>MOD with a smaller left operand:</strong> <code>3 MOD 7</code> is 3 — 7 goes in zero times, remainder 3. Students sometimes answer 0 or 4. The remainder of a small number divided by a bigger one is the small number itself.",
            "AP pseudocode's <code>/</code> is <strong>real division</strong>: <code>7 / 2</code> is 3.5. Unlike Java or Python 2, there's no integer division operator on the reference sheet. If a question needs integer division, it will define a procedure or use MOD to get the same effect.",
            "Expressions can nest: <code>((a + b) * c) MOD d</code>. Work inside-out, innermost parentheses first.",
        ],
        "mistakes": [
            "<strong>Applying MOD last.</strong> <code>a + b MOD c</code> means <code>a + (b MOD c)</code>. Students compute <code>(a + b) MOD c</code>. Same precedence as *, so it goes before +.",
            "<strong>Returning the quotient instead of the remainder.</strong> <code>17 MOD 5</code> is 2 (remainder), not 3 (quotient). MOD is always the leftover.",
            "<strong>Assuming / truncates.</strong> It doesn't in AP pseudocode. <code>9 / 2</code> is 4.5.",
            "<strong>Ignoring statement order.</strong> <code>x ← x + 1</code> then <code>x ← x * 2</code> is not the same as the reverse. Trace in order.",
        ],
    },
    "3.4": {
        "deeper": [
            "The CED's essential knowledge on strings is minimal: they're ordered sequences of characters, and you can <strong>concatenate</strong> and take <strong>substrings</strong>. Everything else — length, indexing, searching — the exam defines inside the question if it's needed.",
            "Concatenation with <code>+</code> works on strings in AP pseudocode. Combining a string and a number is <em>not</em> defined on the reference sheet; if a question does it, it will explain the behavior.",
            "A <strong>substring</strong> must be contiguous. \"cat\" is a substring of \"concatenate\" (positions 4–6). \"cnt\" is not, even though all three letters appear in order.",
            "The <strong>empty string</strong> <code>\"\"</code> is a valid string with zero characters. Concatenating it changes nothing. It's often the starting value when building a string in a loop.",
            "When a question defines a string procedure — say, <code>SUBSTRING(str, start, length)</code> or <code>SUBSTRING(str, start, end)</code> — the parameters matter enormously. One version takes a length, one takes an end index, and the end may or may not be inclusive. Read the definition every time.",
            "Building a string character by character in a loop is the standard pattern for reversing or filtering text: start with <code>\"\"</code>, add one character per iteration.",
        ],
        "mistakes": [
            "<strong>Adding a space that isn't there.</strong> <code>\"a\" + \"b\"</code> is <code>\"ab\"</code>. If a space is needed it must be concatenated explicitly.",
            "<strong>Treating a numeric string as a number.</strong> <code>\"4\" + \"2\"</code> is <code>\"42\"</code> if both are strings. Arithmetic isn't happening.",
            "<strong>Assuming a substring definition.</strong> Don't apply Java's or Python's rules. Use whatever the question says, including whether indices start at 1 and whether the end is inclusive.",
        ],
    },
    "3.5": {
        "deeper": [
            "<strong>Truth tables</strong> are the reliable tool. For two Booleans a and b there are four rows: TT, TF, FT, FF. Evaluate both expressions on each row; if all four match, they're equivalent. For three Booleans, eight rows. It's mechanical and it works.",
            "<strong>Short-circuit evaluation</strong> isn't formally in the CSP CED, but understanding that <code>false AND anything</code> is false and <code>true OR anything</code> is true speeds up evaluation and helps you see equivalences.",
            "<strong>De Morgan's laws in practice:</strong> to negate \"x is between 1 and 10\" — which is <code>x ≥ 1 AND x ≤ 10</code> — you get <code>x &lt; 1 OR x &gt; 10</code>. Flip AND to OR, flip each comparison to its opposite (including the boundary).",
            "The <strong>negation of a comparison</strong> flips to the opposite operator, which always includes the boundary the original excluded: NOT(&gt;) is ≤, NOT(≥) is &lt;, NOT(=) is ≠. Students who write NOT(x &gt; 5) as x &lt; 5 miss the case x = 5.",
            "Relational operators return a Boolean, so <code>x &gt; 5</code> by itself is a complete Boolean expression that can be assigned: <code>isBig ← x &gt; 5</code>. Then <code>IF (isBig)</code> works without writing <code>IF (isBig = true)</code>.",
            "Precedence: relational operators evaluate first, then NOT, then AND, then OR. So <code>NOT a AND b</code> is <code>(NOT a) AND b</code>. The exam uses parentheses generously, but knows students misgroup when it doesn't.",
        ],
        "mistakes": [
            "<strong>Dropping the boundary when negating.</strong> NOT(score ≥ 90) is score &lt; 90, not score ≤ 90 or score &lt; 89.",
            "<strong>De Morgan half-done.</strong> NOT(a AND b) becomes (NOT a) OR (NOT b). Students negate the parts but forget to flip AND to OR (giving NOT a AND NOT b, which is wrong).",
            "<strong>Treating OR as exclusive.</strong> <code>a OR b</code> is true when <em>both</em> are true, too. It's inclusive or.",
            "<strong>Grouping NOT loosely.</strong> <code>NOT a OR b</code> is <code>(NOT a) OR b</code>. NOT applies only to the thing right after it unless parentheses say otherwise.",
        ],
    },
    "3.6": {
        "deeper": [
            "An <code>IF</code> with no <code>ELSE</code> means \"maybe do this.\" An <code>IF/ELSE</code> means \"do exactly one of these two.\" The difference is whether there's a case where nothing in the structure runs.",
            "The condition is evaluated <strong>once</strong>, when the IF is reached. If the block changes variables that were in the condition, that doesn't re-trigger anything — the decision was already made.",
            "Two <code>IF</code> statements in sequence are <strong>independent</strong>. Both conditions are checked; zero, one, or both blocks may run. This is the most common structure the exam uses to test whether you understand independence vs. mutual exclusion.",
            "<code>IF/ELSE</code> can be rewritten as two <code>IF</code> statements with opposite conditions — <code>IF (x &gt; 5)</code> and <code>IF (x ≤ 5)</code> — and the behavior is identical <em>as long as the first block doesn't change x</em>. If it does, the second IF might see a different x. Equivalence questions exploit this.",
            "The exam's block-based pseudocode draws IF/ELSE as connected shapes. Read it the same way: one condition, two branches, exactly one runs.",
            "Selection combined with iteration — an IF inside a loop — is how counting, filtering, and finding patterns work. The IF picks which iterations \"count.\"",
        ],
        "mistakes": [
            "<strong>Reading two IFs as an IF/ELSE.</strong> If both conditions can be true for the same input, both blocks run. Count outputs accordingly.",
            "<strong>Reading an IF/ELSE as two IFs.</strong> Exactly one branch runs. If a question asks \"which values cause both DISPLAY statements to run\" and they're in an IF/ELSE, the answer is \"none.\"",
            "<strong>Forgetting execution continues after the conditional.</strong> Whatever's after the closing brace runs regardless of which branch was taken.",
        ],
    },
    "3.7": {
        "deeper": [
            "The rule for nested conditionals: an inner condition is <strong>only evaluated if execution reaches it</strong>. If the outer condition is false and the inner IF is inside the outer's true-block, the inner condition is never checked at all — not \"checked and found false,\" simply never checked.",
            "Nested IF/ELSE in ELSE branches builds a chain: check A; if not A, check B; if not B, check C; else D. Exactly one leaf runs. This is how grade ranges, tax brackets, and any multi-way categorization is expressed.",
            "<strong>Order in a chain matters</strong> when conditions overlap. Checking <code>score ≥ 70</code> before <code>score ≥ 90</code> sends a 95 down the 70 branch. Put the most restrictive condition first, or make them mutually exclusive with ranges.",
            "A nested IF inside another IF's true-block, with no ELSEs, is equivalent to a single IF with AND: <code>IF (a) { IF (b) { X } }</code> ≡ <code>IF (a AND b) { X }</code>. Adding ELSEs breaks this equivalence — then you need to think about all the paths.",
            "For \"which rewrite is equivalent\" questions, the technique is to enumerate paths: what inputs reach each DISPLAY or assignment in the original? Then check the candidate produces the same result for each.",
            "Deep nesting (three or more levels) is a readability problem the exam sometimes asks about — the fix is usually a compound condition or a chain.",
        ],
        "mistakes": [
            "<strong>Evaluating an inner condition that was never reached.</strong> If the outer branch didn't run, nothing inside it did. Cross it out entirely before looking at what's inside.",
            "<strong>Mis-pairing an ELSE.</strong> In block pseudocode the braces make it unambiguous, but students still attach an ELSE to the wrong IF when tracing quickly. Match each ELSE to the IF whose closing brace immediately precedes it.",
            "<strong>Assuming equivalence after a superficial check.</strong> Testing one input isn't proof. For equivalence questions, test an input for each branch of the original.",
        ],
    },
    "3.8": {
        "deeper": [
            "<code>REPEAT UNTIL</code> checks its condition <strong>before</strong> each iteration, including the first. If the condition is already true, the body runs zero times. (Some real languages have do-while loops that run the body at least once; AP pseudocode's REPEAT UNTIL does not.)",
            "The condition is a <strong>stopping</strong> condition: the loop continues while it's false and stops when it becomes true. Students used to \"while\" loops must mentally negate. <code>REPEAT UNTIL (i &gt; 4)</code> is the same as \"while i ≤ 4.\"",
            "<code>REPEAT n TIMES</code> runs exactly n times; there's no loop variable you can read. If you need a counter, declare and increment one yourself.",
            "<strong>Infinite loop detection:</strong> find the variables in the stopping condition, then check whether the body ever changes them in the direction that would make the condition true. If the condition is <code>i &gt; 10</code> and the body does <code>i ← i - 1</code>, it never stops (assuming i starts ≤ 10).",
            "The <strong>final value</strong> of a loop variable after the loop is the value that made the condition true — one step past the last iteration's value. If the body ran with i = 1, 2, 3, 4, then i is 5 afterward.",
            "The exam's block-based pseudocode draws REPEAT UNTIL as a shape with the condition on top. Same semantics.",
            "Combining a loop with an accumulator (<code>sum ← sum + i</code>) is how sums, counts, and products are computed. The accumulator must be initialized <em>before</em> the loop.",
        ],
        "mistakes": [
            "<strong>Running the body while the condition is true.</strong> REPEAT UNTIL is the opposite — body runs while false. This one flip is responsible for a large share of wrong loop answers.",
            "<strong>Forgetting the zero-iteration case.</strong> If the stopping condition is true before the loop starts, nothing inside runs. Check the initial state first.",
            "<strong>Reporting the last iteration's value instead of the final value.</strong> The variable's final value is the one that stopped the loop, which is one step beyond.",
            "<strong>Not initializing the accumulator.</strong> A <code>sum</code> that's never set to 0 before the loop is undefined. On the exam it's a logic error to spot.",
        ],
        "trace": "csp-repeat-until",
    },
    "3.9": {
        "deeper": [
            "The CED's definition of an algorithm has three properties: it's a <strong>finite</strong> set of instructions (it ends), the instructions are <strong>precise</strong> (no ambiguity), and following them <strong>accomplishes a task</strong>. \"Add salt to taste\" fails precision; \"count forever\" fails finiteness.",
            "Every algorithm can be built from the three control structures: <strong>sequencing</strong>, <strong>selection</strong>, and <strong>iteration</strong>. This is a theoretical result, and the exam treats it as a fact you should know. There's no fourth structure you need.",
            "The same algorithm can be written in <strong>many forms</strong> — natural language, flowchart, pseudocode, any programming language — and it's still the same algorithm. Questions may show a flowchart and ask which pseudocode matches, or vice versa.",
            "<strong>Different algorithms can solve the same problem.</strong> To find the maximum, you could scan once tracking the largest, or sort and take the last element. Both work; they differ in efficiency (3.17).",
            "<strong>Recognizing a pattern from its initialization:</strong> <code>x ← list[1]</code> before a loop with a comparison → finding min or max. <code>x ← 0</code> before a loop with <code>x ← x + …</code> → sum or count. <code>found ← false</code> before a loop → searching. Read the setup line first.",
            "<strong>Modifying an existing algorithm</strong> — changing &gt; to &lt; to find min instead of max, or changing a count into a sum — is a named skill. The exam gives working code and asks what single change achieves a new goal.",
            "The CED expects you to know these specific algorithms: finding max/min, computing sum/average, counting elements meeting a condition, determining whether a value is in a list, and combining or reordering lists. These appear as both \"what does this do\" and \"which code does this\" questions.",
        ],
        "mistakes": [
            "<strong>Initializing max to 0.</strong> Fails for lists of all negative numbers. Correct: initialize to the first element. The exam asks \"for which list does this algorithm fail\" — the answer is the all-negative list.",
            "<strong>Tracing with a realistic list.</strong> Use three elements. It's enough to see the pattern and short enough not to make arithmetic mistakes.",
            "<strong>Confusing count and sum.</strong> <code>count ← count + 1</code> counts. <code>sum ← sum + item</code> sums. Look at what's being added.",
            "<strong>Assuming a flowchart is a different algorithm.</strong> Form doesn't matter; logic does.",
        ],
        "trace": "csp-max",
    },
    "3.10": {
        "deeper": [
            "The complete list of operations on the AP reference sheet: <code>list[i]</code> (access), <code>list[i] ← value</code> (assign), <code>LENGTH(list)</code>, <code>APPEND(list, value)</code>, <code>INSERT(list, i, value)</code>, <code>REMOVE(list, i)</code>, and <code>FOR EACH</code>. That's all. Anything else is defined in the question.",
            "<strong>INSERT shifts right:</strong> the element at index i and everything after it moves to i + 1, i + 2, … and the new value goes at i. Length grows by 1. <strong>REMOVE shifts left:</strong> the element at i is gone, and everything after moves down. Length shrinks by 1. <strong>APPEND</strong> is INSERT at LENGTH + 1.",
            "After a REMOVE, the index you just removed now holds what <em>used to be</em> the next element. This causes the classic \"remove every matching element in a forward loop\" bug: matching elements adjacent to each other get skipped. (The Java version of this bug is in CSA 4.9.)",
            "<code>FOR EACH item IN list</code> visits every element in order. The variable <code>item</code> holds a copy of the current element. Changing <code>item</code> inside the loop does not change the list. To change list elements you need an index loop with <code>list[i] ← …</code>.",
            "<strong>Linear search</strong> — checking each element until you find the target — is the only search you can do on an unsorted list. It's O(n) in the worst case: n elements means up to n comparisons.",
            "<strong>Building a new list</strong> by filtering: start with an empty list, FOR EACH over the original, APPEND matches. The original is unchanged. This is how \"return a list of all elements that…\" is done.",
            "An <strong>empty list</strong> has LENGTH 0, and accessing any index is an error. Algorithms that read <code>list[1]</code> before checking length will fail on empty input — a testable edge case.",
        ],
        "mistakes": [
            "<strong>Not rewriting the list after each operation.</strong> Index shifts are invisible unless you write the list out. Do it every time.",
            "<strong>Reading the wrong index after INSERT/REMOVE.</strong> After <code>REMOVE(a, 2)</code>, what was <code>a[3]</code> is now <code>a[2]</code>. Questions are built around this.",
            "<strong>Modifying the FOR EACH variable and expecting the list to change.</strong> It won't.",
            "<strong>Using index 0.</strong> Still 1-based. Still tested.",
        ],
        "trace": "csp-list-ops",
    },
    "3.11": {
        "deeper": [
            "<strong>Why sorted is required:</strong> binary search decides which half to discard by comparing the middle element to the target. That decision is only valid if smaller values are all on one side and larger on the other — i.e., if the list is sorted. On unsorted data, the target could be in the discarded half.",
            "The <strong>maximum number of comparisons</strong> for n elements is the smallest k such that 2<sup>k</sup> &gt; n. This equals ⌊log₂ n⌋ + 1. Table: n = 7 → 3; n = 8 → 4; n = 15 → 4; n = 16 → 5; n = 100 → 7; n = 1000 → 10; n = 1,000,000 → 20.",
            "A question may give the actual list and target and ask which elements are <em>examined</em>. Trace it: middle first, then the middle of the remaining half, until found. Different rounding conventions for the middle (floor vs. ceiling) can change the exact elements; the exam usually specifies or uses a list where it doesn't matter.",
            "<strong>Linear vs. binary trade-off:</strong> linear needs no preparation but takes up to n steps. Binary needs a sorted list (sorting costs time) but takes log n steps. For one search on an unsorted list, linear wins. For many searches, sort once and use binary.",
            "Binary search is a <strong>selection + iteration</strong> algorithm: each iteration selects a half. Its efficiency is <strong>logarithmic</strong>, which the CED classifies as reasonable time — and it's the exam's main example of an algorithm that scales dramatically better than linear.",
            "Binary search generalizes: guessing a number between 1 and 1000 by always guessing the middle takes at most 10 guesses. Same algorithm, same log₂ bound.",
        ],
        "mistakes": [
            "<strong>Applying binary search to an unsorted list.</strong> If the stem doesn't say sorted, binary search isn't valid. That's frequently the entire question.",
            "<strong>Off-by-one on the step count.</strong> For n = 16, students say 4 (log₂ 16). The maximum is 5, because after four halvings you have one element left and still have to check it. Use \"smallest 2<sup>k</sup> greater than n.\"",
            "<strong>Assuming binary search is always better.</strong> If the list is unsorted and you search once, linear search is faster than sorting-then-binary.",
        ],
    },
    "3.12": {
        "deeper": [
            "A procedure call <strong>interrupts sequential execution</strong>: the program remembers where it was, jumps to the procedure, runs it, then returns to the line after the call. If that line was in the middle of an expression, the returned value is substituted in and evaluation continues.",
            "<strong>Parameters are local</strong> to the procedure. They're created when it's called, initialized to the argument values, and gone when it returns. Changing a parameter inside the procedure doesn't change the caller's variable (for simple values).",
            "A procedure can have <strong>zero parameters</strong> (called with empty parentheses) or several. Arguments are matched to parameters by <strong>position</strong>, not name: the first argument fills the first parameter.",
            "<code>RETURN</code> does two things: it provides the value the call evaluates to, and it <strong>ends the procedure immediately</strong>. Any code after a RETURN that executes is skipped. Multiple RETURNs in a procedure (one per branch) is normal; exactly one runs per call.",
            "A procedure without a RETURN produces no value — it's called for its <strong>side effect</strong> (displaying something, modifying a list). Using such a call in an expression (<code>x ← show(5) + 1</code>) is meaningless.",
            "Procedures can call other procedures, and can call themselves (recursion isn't on the CSP exam, but nested calls are). Trace each call to completion before continuing the caller.",
            "The AP reference sheet defines the syntax: <code>PROCEDURE name(parameter1, parameter2) { instructions }</code> and <code>RETURN (expression)</code>. Block-based pseudocode draws the same thing as shapes.",
        ],
        "mistakes": [
            "<strong>Continuing past a RETURN.</strong> Once RETURN executes, the procedure is done. Code below it on the same path never runs, even if it looks like it should.",
            "<strong>Losing your place.</strong> Write down the line number you'll return to before jumping into the procedure. Nested calls need a stack of these.",
            "<strong>Expecting the caller's variable to change.</strong> <code>double(a)</code> doesn't change a. Only the returned value matters — and only if it's stored.",
            "<strong>Matching arguments by name.</strong> Position is all that matters. If the procedure is <code>f(x, y)</code> and you call <code>f(y, x)</code>, the values are swapped.",
        ],
        "trace": "csp-procedure",
    },
    "3.13": {
        "deeper": [
            "<strong>Procedural abstraction</strong> in the CED: a procedure lets you use a computation by name without knowing (or re-reading) how it works. Once <code>isPrime(n)</code> is written and tested, you call it and trust it. That trust is the abstraction.",
            "The <strong>Create Task's procedure requirement</strong> is specific: a student-developed procedure with a name, a return type (or no return), and <strong>at least one parameter that has an effect on the procedure's functionality</strong>. The body must contain an algorithm with sequencing, selection, and iteration. And you must show a call to it.",
            "\"Parameter that has an effect\" means the parameter is actually used inside and changes what happens. A parameter that's received and ignored doesn't count.",
            "<strong>Generalization</strong> is the reason for parameters: <code>greetRam()</code> can only do one thing; <code>greet(name)</code> can do infinitely many. When code is duplicated with small variations, the variations become parameters and the code becomes one procedure.",
            "Procedures make programs <strong>easier to modify</strong> (change the body once), <strong>easier to test</strong> (test the procedure alone with known inputs), and <strong>easier to read</strong> (a good name explains the intent). The exam's \"why use a procedure\" questions want one of these.",
            "A procedure should have a <strong>single, clear purpose</strong> reflected in its name. <code>calculateAverage</code> should calculate an average and nothing else. Mixing responsibilities makes procedures harder to reuse.",
            "Procedures reduce <strong>duplicated code</strong>. Duplication is bad because a bug in duplicated code must be fixed everywhere it appears — and one copy inevitably gets missed.",
        ],
        "mistakes": [
            "<strong>A Create Task procedure with a parameter that isn't used.</strong> Doesn't meet the requirement. The parameter must affect behavior.",
            "<strong>Choosing an efficiency reason for using a procedure.</strong> Procedures don't make programs faster. They make them clearer and easier to maintain. Options claiming speed or memory benefits are distractors.",
            "<strong>Not showing the call.</strong> The Create Task needs the procedure <em>and</em> a call to it in your code. A defined-but-never-called procedure doesn't count.",
        ],
    },
    "3.14": {
        "deeper": [
            "A <strong>library</strong> is a collection of procedures (and sometimes data) that other programs can use. The procedures were written, tested, and documented by someone else — that's the value: you don't redo their work.",
            "An <strong>API</strong> specifies <em>how</em> to use a library: the procedure names, what to pass in, what comes back. You program <em>against</em> the API. The implementation behind it can change without your code changing, as long as the API stays the same.",
            "<strong>Documentation</strong> is the CED's emphasis: you can't use a library correctly without reading how each procedure behaves — what it expects, what it returns, what happens in edge cases. A question describing a developer who \"read the documentation to understand the parameters\" is describing correct library use.",
            "Libraries make development <strong>faster</strong> (don't rewrite tested code) and programs <strong>more reliable</strong> (widely-used libraries have had their bugs found). They also give access to capabilities you couldn't build yourself — graphics, networking, machine learning.",
            "Using a library is <strong>procedural abstraction at scale</strong>: you call <code>sortList(list)</code> without knowing whether it uses merge sort or quicksort. The abstraction is the whole point.",
            "Libraries are also a <strong>collaboration</strong> mechanism (1.1) — the people who wrote the library are, in effect, on your team.",
        ],
        "mistakes": [
            "<strong>Assuming you need the source code.</strong> You use a library through its API. Options saying \"the developer must understand the library's implementation\" are wrong.",
            "<strong>Claiming libraries guarantee correctness.</strong> They're usually well-tested, but calling them with the wrong arguments still produces wrong results — hence documentation.",
            "<strong>Confusing a library with a language feature.</strong> Built-in operators (+, MOD) aren't library calls. A library adds procedures beyond what the language provides.",
        ],
    },
    "3.15": {
        "deeper": [
            "<code>RANDOM(a, b)</code> returns an integer from a to b <strong>inclusive</strong>, each with equal probability. The count of possible values is <strong>b − a + 1</strong>. <code>RANDOM(1, 100)</code> has 100 outcomes; <code>RANDOM(0, 100)</code> has 101.",
            "<strong>Probability of a condition:</strong> count outcomes satisfying it, divide by total. <code>RANDOM(1, 20) &lt; 6</code> → outcomes 1–5, so 5/20 = 25%.",
            "<strong>Combining random calls:</strong> two dice is <code>RANDOM(1, 6) + RANDOM(1, 6)</code>, giving 2–12 but <em>not</em> uniformly — 7 is most likely. The exam may ask whether an expression produces each value equally often; sums of random values don't.",
            "<strong>Scaling and shifting:</strong> if you only have <code>RANDOM(1, 10)</code> and need even numbers 2–20, use <code>RANDOM(1, 10) * 2</code>. If you need multiples of 5 from 0 to 45, <code>(RANDOM(1, 10) - 1) * 5</code>.",
            "Random values make programs <strong>non-deterministic</strong>: the same program can produce different output each run. Questions about such programs ask what's <em>possible</em> or what <em>must</em> be true, not what \"the\" output is.",
            "Random values are essential to <strong>simulations</strong> (3.16) — they model the variation and uncertainty in real processes — and to games, sampling, and testing with varied inputs.",
        ],
        "mistakes": [
            "<strong>Excluding an endpoint.</strong> Both a and b are possible results. <code>RANDOM(1, 6)</code> can return 6.",
            "<strong>Counting outcomes as b − a.</strong> It's b − a + 1. Ten outcomes from 1 to 10, not nine.",
            "<strong>Assuming a sum of random values is uniform.</strong> It isn't. Middle values are more likely.",
            "<strong>Asking \"what is the output\" of a random program.</strong> There isn't one. The question will ask what's possible or what the probability is.",
        ],
    },
    "3.16": {
        "deeper": [
            "A simulation is an <strong>abstraction</strong> of a real-world process: it keeps the parts that matter for the question being asked and drops the rest. The CED's phrase is that simulations \"remove details\" and \"make assumptions\" to simplify.",
            "The reasons to simulate, per the CED: the real experiment is <strong>impossible</strong> (a future bridge), <strong>dangerous</strong> (a nuclear reaction), <strong>expensive</strong> (a rocket launch), <strong>too slow</strong> (centuries of climate), or <strong>too fast</strong> (a chemical reaction). Simulations are also <strong>repeatable</strong> with changed parameters.",
            "The core limitation: because details were removed, <strong>the simulation may not match reality</strong>. Results are only as good as the assumptions. A simulation that assumes every person has the same number of daily contacts will mispredict a disease that spreads through super-spreaders.",
            "<strong>Random values</strong> in a simulation model real-world variability. Running the simulation many times and looking at the distribution of results is how you get useful predictions from a random model — a single run tells you one possibility.",
            "<strong>Investigating with simulation:</strong> change one input, hold the others constant, observe the change in output. That's how simulations generate hypotheses about the real system.",
            "A simulation can be <strong>biased</strong> in the same ways data can: if the assumptions reflect one group's experience, the simulation predicts well for that group and poorly for others.",
            "Simulations can also be used <strong>as a testing tool</strong> for programs: simulate user input or network conditions to test a program without real users.",
        ],
        "mistakes": [
            "<strong>Claiming a simulation gives exact real-world results.</strong> It gives results under its assumptions. Any \"guarantees\" or \"exactly predicts\" option is wrong.",
            "<strong>Saying a simulation has no assumptions.</strong> Every simulation simplifies. That's the definition.",
            "<strong>Confusing a simulation with the real thing.</strong> A simulated crash test doesn't damage a car. That's the point — and the reason results need validation against real data eventually.",
        ],
    },
    "3.17": {
        "deeper": [
            "The CED defines efficiency by how an algorithm's resource use (steps or memory) <strong>grows with input size</strong>, and draws one line: <strong>polynomial</strong> growth (constant, linear, quadratic, cubic…) is <em>reasonable</em>; <strong>exponential</strong> (2<sup>n</sup>) or <strong>factorial</strong> (n!) growth is <em>unreasonable</em>.",
            "Why the line is there: doubling the input for a quadratic algorithm quadruples the work — manageable. Doubling the input for an exponential algorithm <em>squares</em> the work. At n = 50, 2<sup>n</sup> is a quadrillion. No hardware improvement fixes that.",
            "<strong>Recognizing growth from a table:</strong> steps double when n increases by 1 → exponential. Steps multiply by 4 when n doubles → quadratic. Steps double when n doubles → linear. Steps increase by 1 when n doubles → logarithmic.",
            "<strong>Reading growth from code:</strong> one loop over n items → linear. Nested loops each over n → quadratic. A loop that halves the range each time → logarithmic. Trying every subset or every ordering → exponential or factorial.",
            "<strong>Heuristics</strong> are for problems where the exact solution is unreasonable. A heuristic gives a good-enough answer fast, without guaranteeing the best. The traveling salesperson problem (shortest route through all cities) is the canonical example: exact = factorial time; nearest-neighbor heuristic = fast and usually decent.",
            "A problem can have both reasonable and unreasonable algorithms. Sorting by trying every ordering is factorial; sorting with merge sort is n log n. The problem isn't hard; the first algorithm is just bad.",
            "The CED explicitly says efficiency is <em>not</em> measured by running time on a specific computer — faster hardware changes the constant, not the growth. An unreasonable algorithm on a supercomputer is still unreasonable.",
        ],
        "mistakes": [
            "<strong>Calling quadratic \"unreasonable.\"</strong> It's polynomial, so it's reasonable per the CED. Slow for large n, but reasonable.",
            "<strong>Thinking a faster computer fixes exponential growth.</strong> It shifts the wall by a few units of n. It doesn't remove it.",
            "<strong>Expecting a heuristic to find the optimal answer.</strong> Heuristics trade optimality for speed. If an option says a heuristic \"always finds the best solution,\" it's wrong.",
            "<strong>Reading a steps table without computing ratios.</strong> Look at how steps change as n changes. That ratio is the growth type.",
        ],
    },
    "3.18": {
        "deeper": [
            "A <strong>decidable</strong> problem is one where an algorithm can be written that gives a correct yes/no answer for <em>every possible input</em>. An <strong>undecidable</strong> problem is one where no such algorithm can exist — this has been mathematically proven, not just not-yet-found.",
            "The <strong>halting problem</strong>: given any program and any input, will the program eventually stop? Alan Turing proved in 1936 that no algorithm can answer this for all programs. The proof constructs a program that does the opposite of whatever the supposed halting-detector predicts about it, creating a contradiction.",
            "Undecidability is <strong>not about difficulty or time</strong>. An unreasonable-time problem has an algorithm that's too slow. An undecidable problem has no algorithm at all, regardless of time. They're separate categories on the exam.",
            "An undecidable problem can still be <strong>solved for specific instances</strong>. You can tell that <code>DISPLAY(\"hi\")</code> halts and <code>REPEAT UNTIL (false)</code> doesn't. What's impossible is one algorithm that works for <em>every</em> program.",
            "Real consequences: no tool can perfectly detect all infinite loops, all bugs, or all malware — because each of those reduces to the halting problem. Tools use heuristics and catch most cases; the impossible part is catching all.",
            "This is one of the few places the CED touches theoretical computer science. The exam expects you to know: some problems are provably unsolvable by computers, the halting problem is the example, and this is a fundamental limit rather than a current-technology limit.",
        ],
        "mistakes": [
            "<strong>Saying an undecidable problem \"hasn't been solved yet.\"</strong> It's been proven unsolvable. \"Yet\" is wrong.",
            "<strong>Suggesting a faster computer or heuristic.</strong> Those address unreasonable time, not undecidability. No algorithm exists to speed up.",
            "<strong>Thinking undecidable means no instance can be solved.</strong> Specific cases often can. The claim is about a general algorithm for all cases.",
        ],
    },
    "4.1": {
        "deeper": [
            "The internet is <strong>decentralized</strong>: no single authority controls it. It's a network of independently-operated networks that agree to talk using common protocols. That's why it can't easily be \"turned off\" and why it scales — anyone can add a network.",
            "<strong>Packets</strong> carry a chunk of data plus <strong>metadata</strong>: source address, destination address, and a sequence number. The sequence number is what lets the receiver reassemble packets that arrive out of order. If a packet is missing, TCP asks for it again.",
            "<strong>Routing</strong> happens hop by hop. Each router looks at a packet's destination and forwards it toward the next router closer to that destination. No router knows the whole path; each knows the next step. Different packets of the same message can take different paths.",
            "<strong>IP</strong> handles addressing and routing — getting packets to the right machine. <strong>TCP</strong> sits on top and handles reliability — making sure they all arrive, in order, and asking for re-sends. <strong>UDP</strong> is TCP's faster, unreliable sibling used when speed matters more than perfection (live video, games).",
            "<strong>HTTP</strong> is the protocol web browsers and servers use to request and send pages. <strong>HTTPS</strong> is HTTP with encryption (via TLS), so intercepted traffic can't be read. The padlock icon means HTTPS.",
            "<strong>DNS</strong> is the internet's phone book: it maps names like <code>collegeboard.org</code> to IP addresses. Without DNS you'd type numbers. DNS itself is a distributed, hierarchical system — another example of scalability.",
            "<strong>IPv4</strong> addresses are 32 bits (four numbers 0–255, like 192.168.1.1) — about 4.3 billion, which ran out. <strong>IPv6</strong> uses 128 bits — enough for every device imaginable. The transition is ongoing.",
            "<strong>Bandwidth</strong> is capacity (bits per second); <strong>latency</strong> is delay (how long one packet takes to arrive). A satellite link can have high bandwidth and high latency. The CED focuses on bandwidth.",
            "The <strong>World Wide Web</strong> is one application built on the internet, alongside email, file transfer, streaming, and games. The web = HTTP + HTML + browsers. The internet = the underlying network. Different things.",
            "<strong>Open standards</strong> (the protocols are public, not owned) are why the internet works across every manufacturer and country. Anyone can implement TCP/IP; nobody needs permission.",
        ],
        "mistakes": [
            "<strong>Using internet and web interchangeably.</strong> The exam tests the distinction. Web is a service; internet is the network.",
            "<strong>Claiming packets take the same path or arrive in order.</strong> Neither is guaranteed. Sequence numbers and reassembly handle it.",
            "<strong>Assigning the wrong job to a protocol.</strong> IP = addressing/routing. TCP = reliable delivery. HTTP = web pages. DNS = names to addresses. Learn the four.",
            "<strong>Thinking a router knows the whole route.</strong> It knows the next hop. That's what makes rerouting around failures automatic.",
        ],
    },
    "4.2": {
        "deeper": [
            "<strong>Fault tolerance</strong> means a system keeps working <em>correctly</em> — not just stays on — when parts fail. The internet achieves it through <strong>redundancy</strong>: many paths between any two points, so losing one path doesn't cut the connection.",
            "The formal idea: a network is fault tolerant with respect to a component if removing that component still leaves every remaining node reachable from every other. The exam's diagram questions ask exactly this: which single link's removal would disconnect the network?",
            "<strong>Single point of failure</strong>: a component whose failure alone breaks the system. In a network diagram, a node connected by only one link is a single point of failure for itself. Adding a second link fixes it. The design goal is no single points of failure.",
            "Redundancy costs money — extra cables, routers, servers. The trade-off is reliability vs. expense. Critical systems (hospitals, financial networks) pay for more redundancy than a home network.",
            "Redundancy applies to <strong>data</strong> too: backups, mirrored drives, and data replicated across data centers are fault tolerance for storage. If one copy is lost, another exists.",
            "The internet's fault tolerance is a consequence of its design history: it was built to survive partial destruction. Packets automatically route around dead nodes because each router only needs to know the next hop, not the whole path.",
            "<strong>Scalability</strong> and fault tolerance reinforce each other: adding networks adds paths, which adds redundancy. A bigger internet is a more resilient internet.",
        ],
        "mistakes": [
            "<strong>Confusing redundancy with sending duplicate packets.</strong> Redundancy is extra <em>paths</em> (and backup components), not repeated transmissions. TCP re-sends packets that are lost, but that's error recovery, not redundancy.",
            "<strong>Not checking every link in a diagram.</strong> The question is usually \"which link's failure disconnects the network?\" Test each one by mentally removing it.",
            "<strong>Assuming a bigger network is more fragile.</strong> The opposite — more nodes means more alternative paths.",
        ],
    },
    "4.3": {
        "deeper": [
            "<strong>Sequential</strong>: one processor, one operation at a time. Time = sum of all operations. <strong>Parallel</strong>: multiple processors in one machine, operations that don't depend on each other run at the same time. <strong>Distributed</strong>: multiple <em>machines</em> over a network, each handling part of the problem.",
            "<strong>The speedup calculation</strong> the exam uses: find the operations that must run sequentially (they add up), find the operations that can run in parallel, distribute those to processors as evenly as possible, and the parallel phase takes as long as the <em>busiest</em> processor. Total time = sequential + max(parallel). Speedup = sequential time ÷ parallel time.",
            "<strong>Why speedup is limited:</strong> if 10% of a task must be sequential, then even with infinite processors, that 10% takes its full time. Maximum speedup is 10×. This is Amdahl's law in spirit; the CED just says the sequential portion limits speedup.",
            "<strong>Overhead</strong>: splitting work, coordinating, and combining results all take time. Two processors don't quite halve the time even for a perfectly divisible task.",
            "A task is <strong>parallelizable</strong> when its parts are independent — summing a list (each half can be summed separately then combined) is; a chain where each step needs the previous step's result (computing a running total step by step) is not.",
            "<strong>Distributed computing</strong> adds scalability (add more machines) and fault tolerance (one machine dying doesn't stop the job), at the cost of network communication overhead. It's how large-scale data processing (2.3) is actually done.",
            "Parallel programs must also handle <strong>synchronization</strong> — making sure results are combined correctly. The CED doesn't go deep here, but it's part of why parallel programming is harder than sequential.",
        ],
        "mistakes": [
            "<strong>Averaging parallel tasks instead of taking the max.</strong> If two processors run tasks of 40s and 20s, the parallel phase takes 40s, not 30s. The slower processor sets the pace.",
            "<strong>Forgetting the sequential part.</strong> Any step that needs all the parallel results must wait for them and then adds its own time.",
            "<strong>Claiming n processors give n× speedup.</strong> Only for a perfectly parallel task with no overhead — which doesn't exist. Real speedup is always less.",
            "<strong>Mixing up parallel and distributed.</strong> Multiple cores = parallel. Multiple computers = distributed.",
        ],
    },
    "5.1": {
        "deeper": [
            "A <strong>computing innovation</strong>, per the CED, \"includes a program as an integral part of its function.\" That covers apps, self-driving cars, medical devices, recommendation systems. A hammer isn't one; a smart thermostat is.",
            "<strong>Effects</strong> are the innovation's impact on society, economy, or culture. The exam wants you to categorize effects along two axes: <strong>beneficial vs. harmful</strong> and <strong>intended vs. unintended</strong>. All four combinations exist. An unintended benefit is just as real as an unintended harm.",
            "The classic examples: the internet was designed for research communication; its effect on commerce, entertainment, and politics was unintended. Social media was designed to connect friends; its effect on attention, mental health, and misinformation was unintended and, for many, harmful.",
            "<strong>Scale changes effects.</strong> A feature used by 100 people has small effects. The same feature used by a billion people changes how society works. Developers often can't foresee scale effects because they build for the small case.",
            "The CED says people create innovations \"for a purpose\" but they can be used \"in ways that are unintended\" — and it's not only bad actors. Ordinary users find uses developers didn't imagine. Sometimes those become the main use (SMS was an afterthought; it became the killer feature).",
            "<strong>Responsible development</strong> means thinking about potential harmful effects <em>during</em> design, not only after harm occurs. It's impossible to predict everything, so responsible developers also monitor effects after release and respond to them.",
            "Computing has <strong>changed work</strong>: new jobs (app developer, data scientist) exist that didn't; some jobs (travel agent, switchboard operator) have largely disappeared. The exam treats this as a mixed effect — beneficial for some, harmful for others, both true.",
            "Computing has changed <strong>access to information</strong> (nearly unlimited, but also unfiltered), <strong>communication</strong> (instant, global, but also surveilled), and <strong>privacy expectations</strong> (what was private is now routinely collected). Every one of these is a two-sided effect.",
            "The <strong>Explore Task</strong> (a former exam component whose vocabulary persists in the CED) asked students to analyze a computing innovation's purpose, function, effects, and data use. Questions on this topic often mirror that structure.",
        ],
        "mistakes": [
            "<strong>Picking the one-sided option.</strong> \"This innovation is only beneficial\" or \"has no harmful effects\" is essentially never correct. The CED's whole point is that effects are mixed.",
            "<strong>Confusing unintended with harmful.</strong> Unintended effects can be good. The two axes are independent.",
            "<strong>Assuming the developer is responsible for every use.</strong> The CED presents this as a tension, not a settled rule. Options that assign all responsibility to one party are usually distractors.",
            "<strong>Ignoring who is affected.</strong> A strong answer says <em>which group</em> benefits and <em>which group</em> is harmed. \"Society benefits\" is too vague when the harm falls on a specific group.",
        ],
    },
    "5.2": {
        "deeper": [
            "The <strong>digital divide</strong> is unequal access to computing and the internet. The CED names causes: <strong>socioeconomic status</strong>, <strong>geographic location</strong>, <strong>demographic characteristics</strong> (age, disability, education), and <strong>government or institutional policy</strong> (censorship, lack of investment).",
            "It exists at every scale: between countries (broadband penetration varies enormously), within countries (rural vs. urban), within cities (neighborhood by neighborhood), and within households (who gets the one device).",
            "The divide is about more than hardware: <strong>digital literacy</strong> (knowing how to use technology), <strong>affordability</strong> of ongoing service (not just a device), <strong>reliability</strong> of connection, <strong>language</strong> (most content is in a few languages), and <strong>accessibility</strong> for people with disabilities are all dimensions.",
            "<strong>Why it matters more over time:</strong> as essential services move online — school, job applications, healthcare portals, government benefits, banking — lacking access stops being an inconvenience and becomes exclusion from society's basic functions. The divide compounds other inequalities.",
            "Developers contribute to the divide when they <strong>assume their users are like them</strong>: fast connections, new devices, large screens, fluent English. A site that requires 50 MB of JavaScript excludes people on slow connections. This connects to 5.3 (bias) and to 1.3 (investigating users during design).",
            "Actions that reduce the divide: public infrastructure investment, subsidized service, community access points (libraries, schools), low-cost devices, and — for developers — building things that work on old devices and slow connections, in multiple languages, with accessibility features.",
            "The digital divide can also refer to <strong>generational</strong> differences: older people may have less familiarity even with access. And it can be <strong>policy-driven</strong>: some governments restrict internet access deliberately.",
        ],
        "mistakes": [
            "<strong>Treating it as only an international issue.</strong> Questions set entirely in one country — even one city — can be about the digital divide.",
            "<strong>Treating it as a matter of choice.</strong> Someone who prefers paper isn't part of the digital divide. Someone who can't afford broadband is.",
            "<strong>Assuming a device solves it.</strong> A laptop with no internet, or internet with no skills to use it, doesn't close the gap. It's multi-dimensional.",
            "<strong>Picking options that widen the gap.</strong> \"Require the latest phone,\" \"raise prices,\" \"use high-resolution video only\" — these are wrong answers to \"how would you reduce the divide.\"",
        ],
    },
    "5.3": {
        "deeper": [
            "<strong>Computing bias</strong> is when a system produces systematically unfair results for certain groups. The CED's key claim: bias in a computing innovation reflects the biases in its <strong>data</strong>, its <strong>design</strong>, and its <strong>developers</strong> — and it can be unintentional.",
            "<strong>Bias from data:</strong> systems trained on historical data learn historical patterns, including unfair ones. A hiring tool trained on past hires learns past discrimination. A facial recognition system trained mostly on one demographic works worse on others. The data doesn't have to be labeled \"biased\" — it just has to be unrepresentative.",
            "<strong>Bias from design:</strong> defaults, categories, and assumptions encode the designers' worldview. A form with only two gender options, a voice assistant tested only with one accent, a health app that assumes a particular body type — each excludes people the designers didn't picture.",
            "<strong>Bias from developers:</strong> teams that lack diversity have blind spots. This is why 1.1 emphasizes diverse collaboration — it's a direct countermeasure to bias.",
            "Bias can exist at <strong>every level</strong>: which problem to solve (whose needs matter?), what data to collect, how to clean it, what to test, who to test with, and how to interpret results. It's not one step you can check off.",
            "<strong>Amplification at scale:</strong> a biased human decision affects one person. A biased algorithm used for millions of decisions affects millions — consistently and invisibly. That's why algorithmic bias is treated as more dangerous than individual bias.",
            "<strong>Reducing bias</strong> is an active responsibility: audit data for representation, test outcomes across groups, involve affected communities, build diverse teams, and be willing to not ship something that can't be made fair. The CED says programmers \"should take action to reduce bias.\"",
            "Bias is often <strong>invisible from inside</strong>: developers who share the blind spot don't see the problem. External testing and diverse perspectives are how it gets found.",
        ],
        "mistakes": [
            "<strong>Thinking bias requires intent.</strong> Most computing bias is unintentional. \"The developers didn't mean to\" doesn't make a system unbiased.",
            "<strong>Believing a better algorithm alone fixes biased data.</strong> If the data is unrepresentative, the algorithm learns from unrepresentative data. The data must be fixed.",
            "<strong>Assuming computers are objective.</strong> \"An algorithm can't be biased because it's math\" is a common belief and a wrong answer. Algorithms encode human choices.",
            "<strong>Missing the connection to collaboration.</strong> \"Why would a diverse team reduce bias?\" — because they catch each other's blind spots. This links 5.3 back to 1.1.",
        ],
    },
    "5.4": {
        "deeper": [
            "<strong>Crowdsourcing</strong> uses the internet to gather contributions — data, labor, ideas, funding — from a large, distributed group. The CED's point is that the internet makes this possible at a scale and speed that didn't exist before.",
            "<strong>Citizen science</strong> is crowdsourcing for research: the public collects or classifies data. Examples: counting birds, classifying galaxy images, recording rainfall, identifying protein structures in a game. The volume of data and geographic coverage would be impossible for professional researchers alone.",
            "Crowdsourcing enables <strong>new business models</strong>: crowdfunding (many small contributions fund a project), gig platforms (work distributed to many independent people), and collaborative products (an encyclopedia written by volunteers).",
            "<strong>Quality control</strong> is the challenge: contributors vary in skill and care. Solutions include having multiple people do the same task and comparing, reputation systems, expert review of samples, and designing tasks to be simple enough to do reliably.",
            "Crowdsourcing inherits contributors' <strong>biases</strong>: if the crowd is mostly one demographic, the data reflects that demographic. This connects to 5.3.",
            "Crowdsourcing is distinct from <strong>distributed computing</strong> (4.3): crowdsourcing is many <em>people</em> contributing; distributed computing is many <em>machines</em>. Volunteer computing projects that run on people's home computers blur the line but are technically distributed computing with crowdsourced hardware.",
            "The CED links crowdsourcing to the broader theme of the internet enabling <strong>collaboration</strong> among people who never meet — the same idea as 1.1, at planetary scale.",
        ],
        "mistakes": [
            "<strong>Confusing crowdsourcing with distributed computing.</strong> People vs. machines. If humans are contributing effort or data, it's crowdsourcing.",
            "<strong>Assuming crowdsourced data is accurate.</strong> It needs verification. Options claiming crowdsourcing guarantees accuracy are wrong.",
            "<strong>Missing citizen science.</strong> Any scenario where the public helps with scientific data collection is citizen science, even if the word \"crowdsourcing\" doesn't appear.",
        ],
    },
    "5.5": {
        "deeper": [
            "<strong>Intellectual property</strong> covers creative and inventive work: software, music, images, writing, inventions. The creator has legal rights to control its use. On the internet, IP is easy to copy and hard to protect, which creates constant legal and ethical tension.",
            "<strong>Copyright</strong> is automatic — a work is copyrighted the moment it's created, with or without a notice. Using copyrighted material without permission is infringement. \"I found it online\" is not permission. \"It didn't have a copyright symbol\" is not permission.",
            "<strong>Creative Commons</strong> licenses let creators pre-grant specific permissions: attribution required, non-commercial only, share-alike (derivatives must use the same license), no derivatives. Each license is a different bundle. CC doesn't mean \"free for anything\" — read which one.",
            "<strong>Open source</strong> software makes its source code available under a license that permits use, modification, and redistribution — often with conditions (attribution, or that derivatives also be open). It's still copyrighted; the license grants rights that copyright would otherwise reserve.",
            "<strong>Open access</strong> is the research-publication equivalent: papers and data freely available rather than behind paywalls. It's a movement about who gets to read science.",
            "The <strong>Create Task</strong> requires you to cite code you didn't write — in comments, with the source. Using others' code is allowed; presenting it as your own is plagiarism and can invalidate your score.",
            "<strong>Ethical concerns</strong> the CED names: computing innovations can be used in ways their creators find objectionable (a face-recognition tool used for surveillance), and computing raises questions about <strong>privacy</strong>, <strong>ownership of data</strong>, <strong>misinformation</strong>, and <strong>who bears responsibility</strong> for harm.",
            "<strong>Legal concerns</strong>: laws differ by country and change slowly. Something legal in one jurisdiction may not be in another. And laws lag technology — a new capability may be legal simply because no law addresses it yet, which doesn't make it ethical.",
            "The exam distinguishes <strong>legal</strong> from <strong>ethical</strong>: something can be legal and unethical (collecting data users don't understand they're giving), or illegal and arguably ethical (civil disobedience). Questions may ask you to identify which kind of concern a scenario raises.",
        ],
        "mistakes": [
            "<strong>Treating \"no license\" as \"free to use.\"</strong> It means all rights reserved. Default copyright is the strictest state.",
            "<strong>Assuming Creative Commons or open source means no rules.</strong> Both are licenses with conditions. Attribution is almost always required.",
            "<strong>Not citing code on the Create Task.</strong> Uncited code from any source — a tutorial, a classmate, an AI — is plagiarism under College Board policy.",
            "<strong>Conflating legal with ethical.</strong> The exam treats them as separate questions. Legal ≠ right.",
        ],
    },
    "5.6": {
        "deeper": [
            "<strong>PII</strong> — personally identifiable information — includes name, address, SSN, date of birth, phone, email, biometrics, medical and financial records, and anything that in combination can identify a person. The CED emphasizes <em>combination</em>: ZIP code + birthdate + gender identifies most Americans uniquely.",
            "PII is collected through <strong>search history</strong>, <strong>location data</strong>, <strong>cookies</strong> (small files sites store in your browser to recognize you), <strong>app permissions</strong>, purchase records, and social media activity. Much of it is collected automatically and combined by data brokers.",
            "The CED's concern: PII can be used to <strong>enhance the user experience</strong> (personalization) but also to <strong>stalk</strong>, <strong>steal identities</strong>, and <strong>manipulate</strong> (targeted ads, targeted misinformation). Once information is public, it's essentially impossible to remove.",
            "<strong>Authentication</strong> verifies identity. Three factor types: something you <strong>know</strong> (password, PIN), something you <strong>have</strong> (phone, hardware key), something you <strong>are</strong> (fingerprint, face). <strong>Multifactor authentication</strong> uses two or more <em>different</em> types. Two passwords = one factor.",
            "<strong>Strong passwords</strong> are long, not reused across sites, and not based on personal information. Length matters more than complexity. Password managers exist because humans can't remember dozens of unique long passwords.",
            "<strong>Encryption</strong> transforms data so it's unreadable without a key. <strong>Symmetric</strong>: one shared key encrypts and decrypts — fast, but you have to get the key to the other party securely. <strong>Public key (asymmetric)</strong>: a public key (shared freely) encrypts; only the matching private key decrypts. Solves the key-exchange problem.",
            "<strong>Public key in practice:</strong> your browser gets a website's public key, encrypts a message only the site can read, and they use that to set up a fast symmetric session. That's HTTPS. <strong>Certificate authorities</strong> vouch that the public key really belongs to that site, so an attacker can't substitute their own.",
            "<strong>Attacks to distinguish:</strong> <strong>malware</strong> is the umbrella (software intended to harm). A <strong>virus</strong> is malware that attaches to other programs and spreads when they run. <strong>Phishing</strong> tricks the user into giving up information via fake messages or sites. <strong>Keylogging</strong> records keystrokes to capture passwords. A <strong>rogue access point</strong> is a fake Wi-Fi network that intercepts everything you send. <strong>Unencrypted traffic</strong> on any network can be read by anyone on that network.",
            "<strong>Software updates</strong> matter because they patch known vulnerabilities. An unpatched system has holes that attackers know about. Delaying updates is a security decision.",
            "<strong>Free services</strong> are typically paid for with your data. Reading what an app collects, limiting permissions, and being skeptical of unexpected requests for information are the user-side defenses the CED expects you to know.",
            "Security is a <strong>cost-benefit</strong> question, not absolute. No system is perfectly secure; the goal is to make attacks expensive enough that they're not worth attempting for the value at stake.",
        ],
        "mistakes": [
            "<strong>Calling two passwords multifactor.</strong> Same factor type. Multifactor needs different types: know + have, know + are, etc.",
            "<strong>Sharing the private key.</strong> In public key encryption, the private key is never shared. The public key is the one you give out.",
            "<strong>Mislabeling attacks.</strong> Fake email asking for your password = phishing. Software recording keystrokes = keylogging. Fake Wi-Fi = rogue access point. Each has one definition.",
            "<strong>Thinking encryption is compression.</strong> Encryption hides; compression shrinks. Different goals, different tools.",
            "<strong>Assuming individual data points are harmless.</strong> The exam's point is that combination identifies. ZIP + birthday + gender is PII in combination.",
        ],
    },
}
