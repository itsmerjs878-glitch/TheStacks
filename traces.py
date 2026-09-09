# -*- coding: utf-8 -*-
"""
The Stacks — interactive code traces.
Each trace = code lines + a list of steps recorded by actually
simulating the program in Python. A step is (line_index, vars, output, note).
Vars is a list of (name, value) so order is stable in the table.
"""
import json


def _v(**kw):
    return [(k, kw[k]) for k in kw]


def fmt(x):
    if isinstance(x, bool):
        return "true" if x else "false"
    if isinstance(x, float):
        return repr(x)
    if isinstance(x, list):
        return "[" + ", ".join(fmt(i) for i in x) + "]"
    if isinstance(x, str):
        return '"' + x + '"'
    return str(x)


class Rec:
    def __init__(self):
        self.steps = []
        self.out = ""

    def step(self, line, note="", **vars_):
        self.steps.append({
            "line": line,
            "vars": [[k, fmt(v)] for k, v in vars_.items()],
            "out": self.out,
            "note": note,
        })

    def print(self, s, newline=True):
        self.out += str(s) + ("\n" if newline else " ")


TRACES = {}


def add(tid, title, course, code, steps, intro=""):
    TRACES[tid] = {"id": tid, "title": title, "course": course, "code": code, "steps": steps, "intro": intro}


# ---------------------------------------------------------------- CSP
def t_csp_repeat_until():
    code = [
        "i ← 1",
        "sum ← 0",
        "REPEAT UNTIL (i > 4)",
        "{",
        "    sum ← sum + i",
        "    i ← i + 1",
        "}",
        "DISPLAY(sum)",
        "DISPLAY(i)",
    ]
    r = Rec()
    i = 1; r.step(0, "i starts at 1", i=i)
    s = 0; r.step(1, "sum starts at 0", i=i, sum=s)
    while True:
        r.step(2, f"check: is i > 4? {i} > 4 is {'true → stop' if i > 4 else 'false → run body'}", i=i, sum=s)
        if i > 4:
            break
        s += i; r.step(4, f"sum = {s - i} + {i}", i=i, sum=s)
        i += 1; r.step(5, f"i becomes {i}", i=i, sum=s)
    r.print(s, False); r.step(7, "display sum", i=i, sum=s)
    r.print(i, False); r.step(8, "display i — note it's 5, not 4", i=i, sum=s)
    add("csp-repeat-until", "REPEAT UNTIL — sum 1 through 4", "ap-csp", code, r.steps,
        "The loop runs while the condition is false. Watch the final check where i = 5.")


def t_csp_list_ops():
    code = [
        "a ← [10, 20, 30, 40]",
        "REMOVE(a, 2)",
        "APPEND(a, 50)",
        "INSERT(a, 1, 5)",
        "DISPLAY(a[3])",
        "DISPLAY(LENGTH(a))",
    ]
    r = Rec()
    a = [10, 20, 30, 40]; r.step(0, "four elements, indices 1–4", a=a)
    a.pop(1); r.step(1, "remove index 2 (the 20); later elements shift left", a=a)
    a.append(50); r.step(2, "append 50 to the end", a=a)
    a.insert(0, 5); r.step(3, "insert 5 at index 1; everything shifts right", a=a)
    r.print(a[2], False); r.step(4, "a[3] is the third element", a=a)
    r.print(len(a), False); r.step(5, "LENGTH is 5", a=a)
    add("csp-list-ops", "List operations — INSERT, REMOVE, APPEND", "ap-csp", code, r.steps,
        "AP pseudocode lists are 1-indexed. Rewrite the list after every operation.")


def t_csp_procedure():
    code = [
        "PROCEDURE double(n)",
        "{",
        "    RETURN (n * 2)",
        "}",
        "",
        "a ← 3",
        "b ← double(a) + double(5)",
        "DISPLAY(b)",
    ]
    r = Rec()
    a = 3; r.step(5, "a is 3", a=a)
    r.step(6, "evaluate right side: first call double(a) with n = 3", a=a)
    r.step(2, "inside double: n = 3, return 6", a=a, n=3)
    r.step(6, "double(a) = 6; now call double(5)", a=a)
    r.step(2, "inside double: n = 5, return 10", a=a, n=5)
    b = 16; r.step(6, "6 + 10 = 16 stored in b", a=a, b=b)
    r.print(b, False); r.step(7, "display 16; a is still 3", a=a, b=b)
    add("csp-procedure", "Calling a procedure twice", "ap-csp", code, r.steps,
        "Control jumps into the procedure and back. The parameter n gets a copy of each argument.")


def t_csp_max():
    code = [
        "nums ← [4, 9, 2, 7]",
        "biggest ← nums[1]",
        "FOR EACH n IN nums",
        "{",
        "    IF (n > biggest)",
        "    {",
        "        biggest ← n",
        "    }",
        "}",
        "DISPLAY(biggest)",
    ]
    r = Rec()
    nums = [4, 9, 2, 7]; r.step(0, "the list", nums=nums)
    big = nums[0]; r.step(1, "start with the first element", nums=nums, biggest=big)
    for n in nums:
        r.step(2, f"next element: n = {n}", nums=nums, biggest=big, n=n)
        r.step(4, f"is {n} > {big}? {'yes' if n > big else 'no'}", nums=nums, biggest=big, n=n)
        if n > big:
            big = n; r.step(6, f"new biggest: {big}", nums=nums, biggest=big, n=n)
    r.print(big, False); r.step(9, "loop done; display 9", nums=nums, biggest=big, n=n)
    add("csp-max", "Find the maximum with FOR EACH", "ap-csp", code, r.steps,
        "The standard max pattern. Note biggest is initialized to the first element, never to 0.")


# ---------------------------------------------------------------- CSA
def t_csa_while():
    code = [
        "int n = 20;",
        "int count = 0;",
        "while (n > 1)",
        "{",
        "    n = n / 2;",
        "    count++;",
        "}",
        "System.out.println(n + \" \" + count);",
    ]
    r = Rec()
    n = 20; r.step(0, "n starts at 20", n=n)
    c = 0; r.step(1, "count starts at 0", n=n, count=c)
    while True:
        r.step(2, f"check n > 1: {n} > 1 is {'true' if n > 1 else 'false → exit'}", n=n, count=c)
        if not n > 1:
            break
        old = n; n = n // 2; r.step(4, f"{old} / 2 = {n} (integer division)", n=n, count=c)
        c += 1; r.step(5, f"count becomes {c}", n=n, count=c)
    r.print(f"{n} {c}"); r.step(7, "print", n=n, count=c)
    add("csa-while", "while loop with integer division", "ap-csa", code, r.steps,
        "Integer division truncates. Count how many halvings it takes to get n to 1.")


def t_csa_nested():
    code = [
        "int count = 0;",
        "for (int i = 1; i <= 4; i++)",
        "{",
        "    for (int j = i; j <= 4; j++)",
        "    {",
        "        count++;",
        "    }",
        "}",
        "System.out.println(count);",
    ]
    r = Rec()
    c = 0; r.step(0, "count = 0", count=c)
    for i in range(1, 5):
        r.step(1, f"outer: i = {i}", count=c, i=i)
        for j in range(i, 5):
            r.step(3, f"inner: j = {j} (starts at i)", count=c, i=i, j=j)
            c += 1; r.step(5, f"count = {c}", count=c, i=i, j=j)
        r.step(3, f"j = {5} fails j <= 4; inner loop ends", count=c, i=i, j=5)
    r.step(1, "i = 5 fails i <= 4; outer loop ends", count=c, i=5)
    r.print(c); r.step(8, "4 + 3 + 2 + 1 = 10", count=c)
    add("csa-nested", "Nested loops where the inner bound depends on the outer", "ap-csa", code, r.steps,
        "The inner loop starts at i, so it runs 4, 3, 2, then 1 times.")


def t_csa_enhanced_for():
    code = [
        "int[] nums = {2, 4, 6};",
        "for (int v : nums)",
        "{",
        "    v = v * 10;",
        "}",
        "System.out.println(nums[0] + nums[1] + nums[2]);",
    ]
    r = Rec()
    nums = [2, 4, 6]; r.step(0, "the array", nums=nums)
    for v in nums:
        r.step(1, f"v gets a COPY of the next element: {v}", nums=nums, v=v)
        v2 = v * 10; r.step(3, f"v = {v2} — the array is unchanged", nums=nums, v=v2)
    r.print(sum(nums)); r.step(5, "2 + 4 + 6 = 12; the multiplications were lost", nums=nums)
    add("csa-enhanced-for", "Enhanced for loop does not modify the array", "ap-csa", code, r.steps,
        "v is a copy. Assigning to it never touches nums.")


def t_csa_arraylist_remove():
    code = [
        "// list = [1, 2, 2, 3, 2]",
        "for (int i = 0; i < list.size(); i++)",
        "{",
        "    if (list.get(i) == 2)",
        "    {",
        "        list.remove(i);",
        "    }",
        "}",
        "System.out.println(list);",
    ]
    r = Rec()
    lst = [1, 2, 2, 3, 2]; r.step(0, "starting list", list=lst)
    i = 0
    while True:
        r.step(1, f"check i < size: {i} < {len(lst)} is {'true' if i < len(lst) else 'false → exit'}", list=lst, i=i)
        if not i < len(lst):
            break
        val = lst[i]
        r.step(3, f"list.get({i}) is {val}; equals 2? {'yes' if val == 2 else 'no'}", list=lst, i=i)
        if val == 2:
            lst.pop(i); r.step(5, f"removed index {i}; elements after it shift LEFT", list=lst, i=i)
        i += 1; r.step(1, f"i++ → {i}" + (" — the element that shifted into the old index was skipped" if val == 2 and i < len(lst) else ""), list=lst, i=i)
    r.print(fmt(lst)); r.step(8, "a 2 survived because it was skipped", list=lst, i=i)
    add("csa-arraylist-remove", "Removing from an ArrayList in a forward loop (the bug)", "ap-csa", code, r.steps,
        "After a remove, the next element shifts into the current index — then i++ jumps past it.")


def t_csa_binary_search():
    code = [
        "// a = {1, 4, 7, 10, 13, 16, 19, 22}, target = 4",
        "int low = 0;",
        "int high = a.length - 1;",
        "while (low <= high)",
        "{",
        "    int mid = (low + high) / 2;",
        "    if (a[mid] == target) return mid;",
        "    else if (a[mid] < target) low = mid + 1;",
        "    else high = mid - 1;",
        "}",
        "return -1;",
    ]
    r = Rec()
    a = [1, 4, 7, 10, 13, 16, 19, 22]; t = 4
    low = 0; r.step(1, "low = 0", low=low)
    high = len(a) - 1; r.step(2, "high = 7", low=low, high=high)
    comparisons = 0
    while True:
        r.step(3, f"check low <= high: {low} <= {high}", low=low, high=high)
        if not low <= high:
            break
        mid = (low + high) // 2; r.step(5, f"mid = ({low} + {high}) / 2 = {mid}; a[mid] = {a[mid]}", low=low, high=high, mid=mid)
        comparisons += 1
        r.step(6, f"is a[{mid}] = {a[mid]} equal to {t}? {'yes → return ' + str(mid) if a[mid] == t else 'no'}", low=low, high=high, mid=mid, comparisons=comparisons)
        if a[mid] == t:
            break
        if a[mid] < t:
            low = mid + 1; r.step(7, f"{a[mid]} < {t}; search right half: low = {low}", low=low, high=high, mid=mid, comparisons=comparisons)
        else:
            high = mid - 1; r.step(8, f"{a[mid]} > {t}; search left half: high = {high}", low=low, high=high, mid=mid, comparisons=comparisons)
    add("csa-binary-search", "Binary search — tracking low, high, mid", "ap-csa", code, r.steps,
        "Count the comparisons: elements 10 then 4 were examined. Two steps to find the target.")


def t_csa_recursion():
    code = [
        "public static int f(int n)",
        "{",
        "    if (n <= 1) return 1;",
        "    return n * f(n - 1);",
        "}",
        "// call: f(4)",
    ]
    r = Rec()
    stack = []
    def go(n, depth):
        stack.append(f"f({n})")
        r.step(0, f"enter f({n})", call_stack=" → ".join(stack), n=n)
        r.step(2, f"is {n} <= 1? {'yes → return 1' if n <= 1 else 'no'}", call_stack=" → ".join(stack), n=n)
        if n <= 1:
            stack.pop()
            return 1
        r.step(3, f"need f({n - 1}) first; {n} * f({n - 1}) waits", call_stack=" → ".join(stack), n=n)
        sub = go(n - 1, depth + 1)
        res = n * sub
        r.step(3, f"f({n - 1}) returned {sub}; return {n} * {sub} = {res}", call_stack=" → ".join(stack), n=n, result=res)
        stack.pop()
        return res
    res = go(4, 0)
    r.step(5, f"f(4) = {res}", result=res)
    add("csa-recursion", "Recursion — factorial, calls and returns", "ap-csa", code, r.steps,
        "Each call waits for the one below it. Watch the call stack grow to f(1), then unwind.")


def t_csa_string():
    code = [
        "String s = \"banana\";",
        "int count = 0;",
        "for (int i = 0; i <= s.length() - 3; i++)",
        "{",
        "    if (s.substring(i, i + 3).equals(\"ana\"))",
        "    {",
        "        count++;",
        "    }",
        "}",
        "System.out.println(count);",
    ]
    r = Rec()
    s = "banana"; r.step(0, "length 6", s=s)
    c = 0; r.step(1, "count = 0", s=s, count=c)
    i = 0
    while True:
        r.step(2, f"check i <= 3: {i} <= 3 is {'true' if i <= 3 else 'false → exit'}", s=s, count=c, i=i)
        if i > 3:
            break
        sub = s[i:i + 3]
        r.step(4, f"substring({i}, {i + 3}) = \"{sub}\"; equals \"ana\"? {'yes' if sub == 'ana' else 'no'}", s=s, count=c, i=i, sub=sub)
        if sub == "ana":
            c += 1; r.step(6, f"count = {c}", s=s, count=c, i=i, sub=sub)
        i += 1
    r.print(c); r.step(9, "overlapping matches at 1 and 3", s=s, count=c)
    add("csa-string-count", "Counting substring occurrences", "ap-csa", code, r.steps,
        "The loop bound is length − 3 so substring(i, i+3) never goes out of bounds.")


for fn in (t_csp_repeat_until, t_csp_list_ops, t_csp_procedure, t_csp_max,
           t_csa_while, t_csa_nested, t_csa_enhanced_for, t_csa_arraylist_remove,
           t_csa_binary_search, t_csa_recursion, t_csa_string):
    fn()


def trace_json(tid):
    return json.dumps(TRACES[tid], ensure_ascii=False)


if __name__ == "__main__":
    for k, v in TRACES.items():
        print(k, len(v["steps"]), "steps")
