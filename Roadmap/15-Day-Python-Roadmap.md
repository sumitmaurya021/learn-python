# 🐍 15-Day Complete Python Roadmap (Beginner → Strong Practical Level)

## 📌 Kaise Use Karein Yeh Roadmap
- Har din **3–4 hours** dedicate karo (Theory + Practical + Practice + Revision).
- Sirf padhna nahi hai — **har code khud type karke run karo**, copy-paste mat karo.
- Har din ke end ka "Coding Challenge" **bina Google kiye** solve karne ki koshish karo.
- Agar koi din miss ho jaye, agle din pehle usko cover karo, phir aage badho.
- Priority tags samajh lo:
  - ⭐ **Must Learn** — bina iske aage nahi badh sakte
  - 🔥 **Important** — job-ready banata hai
  - 💡 **Good to Know** — bonus knowledge, later bhi seekh sakte ho

## ⚠️ Honest Disclaimer (Important)
15 din mein Python ka **poora universe** cover karna possible nahi hai — aur main aapko fake promise nahi dunga.
Yeh roadmap aapko **strong practical foundation + OOP + file handling + basic API/JSON** tak le jayega, jisse aap khud se programs bana sakoge aur backend development (Flask/Django/FastAPI) seekhne ke liye ready ho jaoge.

**15 din ke baad (Day 16 se) continue karne wale advanced topics:**
- Decorators & Closures (advanced) 🔥
- Advanced OOP (abstract classes, metaclasses) 💡
- Regular Expressions (regex) 🔥
- Multithreading / Multiprocessing 💡
- Unit Testing (pytest) 🔥
- Advanced generators & context managers 💡
- Web frameworks: Flask / Django / FastAPI ⭐ (agla goal)
- Database connectivity (SQL with Python) 🔥
- Async programming (asyncio) 💡

Yeh sab is roadmap ka **natural next step** hai — inko rush karke half-baked nahi seekhna hai.

---

# Day 1 – Python Basics & Syntax ⭐

## 🎯 Day Goal:
Aaj Python install karna, samajhna ki Python kaam kaise karta hai, aur apna **first real program** likhna hai. Indentation aur syntax rules pakka karne hain kyunki poora Python isi pe based hai.

## 📚 Theory:

### 1. Python Kya Hai Aur Kyun Seekhein? ⭐
Python ek **high-level, interpreted programming language** hai — matlab aap English jaisi readable language likhte ho, aur Python interpreter usko machine ke liye translate karta hai line-by-line (compile karne ki zarurat nahi).

**Real-world example:** Jaise aap ek waiter (interpreter) ko Hindi mein order dete ho aur woh kitchen (computer) tak translate karke pahunchata hai — waise hi Python interpreter aapka code samajh kar computer ko batata hai kya karna hai.

Python ka use: Web development (Django, Flask), Data Science (Pandas, NumPy), AI/ML, Automation, Scripting — bahut jagah hota hai.

### 2. Installation & Setup ⭐
- Python.org se latest Python (3.12+) install karo, ya VS Code + Python extension use karo.
- Terminal mein check karo: `python --version` ya `python3 --version`

### 3. Python Interpreter vs Script Mode 🔥
- **Interactive mode:** Terminal mein `python` type karke ek-ek line turant run kar sakte ho (testing ke liye great).
- **Script mode:** `.py` file banake poora program ek saath run karte ho — real projects isi tarah likhe jaate hain.

### 4. Indentation — Python ki Jaan ⭐
Python mein `{}` braces nahi hote code block define karne ke liye — **indentation (spaces)** use hota hai. Agar indentation galat hui to `IndentationError` aayega.

**Real-world analogy:** Jaise ek essay mein paragraph ka structure hota hai (introduction, body, conclusion alag-alag indent/spacing mein), waise hi Python mein har block (if, loop, function) ka apna indent level hota hai.

### 5. Comments ⭐
Comments code ko explain karne ke liye hote hain, interpreter unko ignore karta hai.
- Single line: `# yeh comment hai`
- Multi-line: triple quotes `""" ... """`

### 6. print() Function ⭐
Output screen par dikhane ke liye.

## 💻 Practical:

### Example 1: Hello World Program
```python
# Yeh mera pehla Python program hai
print("Hello, World!")
print("Mera naam Python Learner hai")
```
**Line-by-line explanation:**
- Line 1: `#` se shuru hone wali line comment hai, ignore ho jaati hai.
- Line 2 & 3: `print()` function jo bhi quotes ke andar hai use screen par output karta hai.

### Example 2: Indentation Samajhna
```python
age = 20

if age >= 18:
    print("Aap adult ho")   # yeh 4 spaces indent hai
    print("Voting kar sakte ho")
else:
    print("Aap minor ho")
```
**Explanation:** `if` ke andar dono print statements 4 spaces indent hain — isliye woh `if` block ka part hain. Indentation change karo to error aa jayega.

### Example 3: Comments Aur Multi-line String
```python
"""
Yeh multi-line comment hai
Program: Basic Info Display
Author: Learner
"""
print("Python seekhna shuru!")  # inline comment
```

## 🧠 Practice Questions:
1. Apna naam, age, aur city print karne wala 3-line program likho.
2. Ek program likho jo `IndentationError` intentionally create kare (galat indentation dekar), phir usse fix karo.
3. Terminal mein interactive mode open karke `2+2` aur `print("test")` run karo.
4. 5 alag print statements likho jo ek chhota "about me" paragraph banayein.
5. Comment likho jo explain kare ki tumhara program kya karta hai (bina code likhe, sirf comment structure banao).

## 🔥 Coding Challenge:
Ek Python script banao jo terminal par ek **ASCII art ya simple banner** print kare tumhare naam ke saath (use multiple print statements), aur saath mein 2 comments ho jo explain karein program kya kar raha hai.

## 🎤 Interview Questions:
1. Python interpreted language hai ya compiled? Farak batao.
2. Python mein indentation itna important kyun hai?
3. `print()` function ka kaam kya hai?
4. Single-line aur multi-line comment mein farak batao.
5. Python interactive mode aur script mode mein kya difference hai?

## ✅ Day-End Checklist:
- [ ] Python install ho gaya aur version check kar liya
- [ ] Pehla `.py` file bana kar run kar liya
- [ ] Indentation ka concept clear hai
- [ ] Comments likhna aata hai
- [ ] print() confidently use kar sakte ho

## ⏱️ Suggested Time:
Theory: 45 min | Practical: 60 min | Practice: 45 min | Revision: 30 min

---

# Day 2 – Variables, Data Types & Input/Output ⭐

## 🔄 Quick Revision (Day 1):
Kal humne seekha: Python installation, `print()`, indentation, aur comments. Aaj hum data ko **store aur handle** karna seekhenge.

## 🎯 Day Goal:
Variables banana, Python ke core data types samajhna, type conversion, aur user se input lena — taaki dynamic programs likh sako.

## 📚 Theory:

### 1. Variables ⭐
Variable ek **naam (label)** hai jo memory mein kisi value ko store karta hai. Python mein type declare karne ki zarurat nahi (dynamically typed).

**Real-world analogy:** Variable ek **container/box** hai jispe label lagi hai — box ke andar tum kuch bhi rakh sakte ho (number, text, list), aur baad mein badal bhi sakte ho.

```python
name = "Rahul"      # box "name" mein string
age = 25             # box "age" mein number
```

**Naming Rules 🔥:**
- Letter ya underscore se start hona chahiye (number se nahi)
- Case-sensitive hai (`Name` aur `name` alag hain)
- Reserved keywords use nahi kar sakte (`if`, `for`, `class` etc.)
- Convention: `snake_case` use karo (e.g., `user_name`)

### 2. Data Types ⭐
| Type | Example | Real-world use |
|---|---|---|
| `int` | `25` | Age, count |
| `float` | `25.5` | Price, weight |
| `str` | `"Rahul"` | Name, text |
| `bool` | `True/False` | Yes/No decisions |
| `complex` | `2+3j` | Scientific calc (rare) |

### 3. type() Function ⭐
Kisi bhi variable ka data type check karne ke liye.

### 4. Type Conversion (Casting) 🔥
Ek type se doosre type mein convert karna: `int()`, `float()`, `str()`, `bool()`.

**Real-world example:** Jab user form fill karta hai, input hamesha **text (string)** aata hai — agar age pe calculation karni hai to usse `int()` mein convert karna padega.

### 5. Input/Output ⭐
`input()` function se user se data lete hain — **hamesha string return karta hai.**

## 💻 Practical:

### Example 1: Variables & Data Types
```python
name = "Priya"          # str
age = 22                # int
height = 5.4             # float
is_student = True        # bool

print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>
print(type(is_student))  # <class 'bool'>
```
**Explanation:** `type()` batata hai variable kis data type ka hai — debugging ke liye bahut useful hai.

### Example 2: Type Casting
```python
age_str = "25"          # yeh string hai
age_int = int(age_str)  # ab yeh number ban gaya

print(age_int + 5)      # 30 (ab addition possible hai)
# print(age_str + 5)    # yeh ERROR dega - string + int nahi ho sakta
```

### Example 3: Taking Input from User
```python
name = input("Aapka naam kya hai? ")
age = input("Aapki age kya hai? ")

age = int(age)  # string ko int mein convert kiya

print("Hello", name, "! Aap", age, "saal ke ho.")
print(f"Agle saal aap {age + 1} saal ke honge.")  # f-string
```
**Explanation:** 
- `input()` hamesha string return karta hai, isliye age ko `int()` se convert kiya.
- `f"..."` (f-string) modern aur clean way hai variables ko string ke andar insert karne ka — ⭐ **Must Learn** best practice.

## 🧠 Practice Questions:
1. Apna naam, age, city store karke ek formatted sentence print karo using f-string.
2. User se do numbers input lo aur unka sum print karo (type conversion zaroor use karo).
3. `bool()` conversion try karo: `bool(0)`, `bool(1)`, `bool("")`, `bool("hello")` — output predict karo phir verify karo.
4. Ek variable ki value ka type check karo `type()` se, phir usse doosre type mein convert karo.
5. User se unki height (cm mein) lo aur usse meters mein convert karke print karo (float use hoga).

## 🔥 Coding Challenge:
Ek **"Simple Profile Card Generator"** banao jo user se naam, age, city, aur favourite hobby poochhe, aur phir ek nicely formatted profile print kare using f-strings.

## 🎤 Interview Questions:
1. Python dynamically typed language hai — iska matlab kya hai?
2. `int()`, `float()`, `str()` conversion kab fail ho sakti hai? Example do.
3. `input()` function hamesha kya return karta hai?
4. Variable naming ke 3 rules batao.
5. `type()` function ka use kya hai?
6. f-string kya hai aur yeh `.format()` se better kyun hai?

## ✅ Day-End Checklist:
- [ ] Variables confidently create kar sakte ho
- [ ] 5 core data types pehchan sakte ho
- [ ] Type conversion samajh aa gaya
- [ ] input() se user input le sakte ho
- [ ] f-strings use karna aata hai

## ⏱️ Suggested Time:
Theory: 40 min | Practical: 60 min | Practice: 50 min | Revision: 30 min

---

# Day 3 – Operators ⭐

## 🔄 Quick Revision (Day 1-2):
Indentation, print, variables, data types, type casting, input() — sab ka mix banake ek chhota program mentally revise karo.

## 🎯 Day Goal:
Saare operators (arithmetic, comparison, logical, assignment) samajhna aur unse decisions/calculations wale programs likhna.

## 📚 Theory:

### 1. Arithmetic Operators ⭐
`+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (power)

**Real-world example:** Bill split karte time `%` (modulus) se pata chalta hai kitna extra bacha, aur `//` se poore parts.

### 2. Comparison Operators ⭐
`==`, `!=`, `>`, `<`, `>=`, `<=` — yeh hamesha `True`/`False` (bool) return karte hain.

⚠️ **Common Mistake:** `=` (assignment) aur `==` (comparison) ko confuse karna — beginners ki sabse common galti hai.

### 3. Logical Operators ⭐
`and`, `or`, `not` — multiple conditions combine karne ke liye.

**Real-world analogy:** "Mujhe umbrella chahiye **agar** baarish ho rahi hai **AND** mujhe bahar jaana hai" — dono conditions true honi chahiye.

### 4. Assignment Operators 🔥
`=`, `+=`, `-=`, `*=`, `/=` etc. — shortcut hain value update karne ke.

### 5. Membership & Identity Operators 💡
`in`, `not in` (kisi sequence mein element hai ya nahi), `is`, `is not` (same object hai ya nahi).

### 6. Operator Precedence 🔥
Jaise maths mein BODMAS hota hai, Python mein bhi operators ka ek order hota hai jisme woh evaluate hote hain (`**` sabse pehle, phir `*,/`, phir `+,-`).

## 💻 Practical:

### Example 1: Arithmetic Operators
```python
a = 17
b = 5

print(a + b)   # 22
print(a - b)   # 12
print(a * b)   # 85
print(a / b)   # 3.4 (float division)
print(a // b)  # 3 (floor division - decimal hata deta hai)
print(a % b)   # 2 (remainder)
print(a ** b)  # 1419857 (17 ki power 5)
```

### Example 2: Comparison + Logical Operators Together
```python
age = 20
has_id = True

can_vote = age >= 18 and has_id
print(can_vote)  # True

is_teen = age >= 13 and age <= 19
print(is_teen)  # False, kyunki age 20 hai
```
**Explanation:** `and` ke dono sides True hone chahiye tabhi result True aayega.

### Example 3: Assignment Operators (Shortcut)
```python
score = 10
score += 5   # score = score + 5  -> 15
score *= 2   # score = score * 2  -> 30
print(score)  # 30
```

## 🧠 Practice Questions:
1. Do numbers input lo aur unpar sabhi arithmetic operators apply karke result print karo.
2. Ek number even hai ya odd, `%` operator use karke check karo.
3. `and`, `or`, `not` use karke ek condition banao: "user login kar sakta hai agar age >= 18 AND password correct hai".
4. `+=`, `-=` operators use karke ek counter program banao.
5. Predict karo output: `10 > 5 and 3 < 1` — phir run karke verify karo.

## 🔥 Coding Challenge:
Ek **"Bill Split Calculator"** banao — total bill amount aur number of friends input lo, phir batao har person kitna dega (`//`) aur kitna extra bacha (`%`).

## 🎤 Interview Questions:
1. `/` aur `//` mein kya farak hai?
2. `==` aur `=` mein kya farak hai? Ek galti se dono mix ho jaye to kya hoga?
3. `and` aur `or` operator kab True return karte hain?
4. `%` operator ka ek real-world use case batao.
5. Operator precedence kya hoti hai? Example do.

## ✅ Day-End Checklist:
- [ ] Saare arithmetic operators use kar sakte ho
- [ ] Comparison operators se conditions bana sakte ho
- [ ] Logical operators (and/or/not) samajh gaye
- [ ] `=` vs `==` ka farak clear hai
- [ ] Assignment shortcut operators (`+=` etc.) aate hain

## ⏱️ Suggested Time:
Theory: 35 min | Practical: 55 min | Practice: 50 min | Revision: 30 min

---

# Day 4 – Strings (Deep Dive) 🔥

## 🔄 Quick Revision (Day 1-3):
Variables, data types, operators — ab tak ek calculator jaisa logic bana sakte ho. Aaj text (string) data pe deep dive karenge, jo real projects mein bahut use hota hai.

## 🎯 Day Goal:
Strings ko manipulate karna seekhna — indexing, slicing, common string methods, aur formatting.

## 📚 Theory:

### 1. String Kya Hai ⭐
String characters ka ek sequence hai, `'single'` ya `"double"` quotes mein likha jaata hai.

### 2. Indexing & Slicing ⭐
Har character ka ek position (index) hota hai, **0 se start** hota hai.

**Real-world analogy:** String ek train hai jisme har coach (character) ki ek seat number (index) hai — 0 se ginti shuru hoti hai.

```python
name = "Python"
# P  y  t  h  o  n
# 0  1  2  3  4  5   (positive index)
#-6 -5 -4 -3 -2 -1   (negative index)
```

### 3. String Immutability ⭐
Strings **immutable** hote hain — ek baar bann jaane ke baad unka koi character change nahi kar sakte, naya string banana padta hai.

### 4. Common String Methods 🔥
`.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.join()`, `.find()`, `.count()`, `len()`

### 5. String Formatting ⭐
f-strings (best practice), `.format()`, `%` formatting (old style, avoid karo)

### 6. Common Mistake ⚠️
Beginners strings ko list ki tarah modify karne ki koshish karte hain: `name[0] = 'J'` — yeh **error** dega kyunki strings immutable hain.

## 💻 Practical:

### Example 1: Indexing & Slicing
```python
name = "Python Programming"

print(name[0])        # P
print(name[-1])        # g
print(name[0:6])       # Python  (0 se 5 tak, 6 exclude)
print(name[7:])        # Programming
print(name[::-1])      # gnimmargorP nohtyP (reverse trick!)
```
**Explanation:** Slicing syntax `[start:stop:step]` hai — `stop` index exclude hota hai. `[::-1]` step -1 use karke string reverse kar deta hai.

### Example 2: String Methods
```python
text = "  Hello World  "

print(text.strip())        # "Hello World" (extra spaces hata diye)
print(text.upper())        # "  HELLO WORLD  "
print(text.lower())        # "  hello world  "
print(text.strip().replace("World", "Python"))  # "Hello Python"

words = "python,java,c++".split(",")
print(words)   # ['python', 'java', 'c++']

joined = "-".join(words)
print(joined)  # python-java-c++
```

### Example 3: String Formatting
```python
name = "Anjali"
marks = 92.5

# f-string (Best Practice ⭐)
print(f"{name} ne {marks} marks score kiye")

# .format() method
print("{} ne {} marks score kiye".format(name, marks))

# f-string with expressions
print(f"Agle saal marks ho sakte hain: {marks + 5}")
```

## 🧠 Practice Questions:
1. Ek string lo aur uska first aur last character alag-alag print karo.
2. User se full name lo aur usko `.split()` se first name aur last name mein alag karo.
3. Ek sentence mein kisi particular word ko `.replace()` se replace karo.
4. `len()` use karke check karo user ka password kam se kam 8 characters ka hai ya nahi.
5. Ek string palindrome hai ya nahi check karo (e.g., "madam") — slicing trick use karo.

## 🔥 Coding Challenge:
Ek **"Username Generator"** banao — user se full name lo, aur automatically ek username generate karo (e.g., first 4 letters of first name + last name lowercase + random 2 digit number placeholder). String methods aur slicing ka use karo.

## 🎤 Interview Questions:
1. Strings immutable kyun hote hain? Iska fayda kya hai?
2. Positive aur negative indexing mein kya farak hai?
3. `split()` aur `join()` ka use kab karte hain?
4. Slicing syntax `[start:stop:step]` explain karo.
5. f-string aur `.format()` mein kya difference hai?

## ✅ Day-End Checklist:
- [ ] Indexing aur slicing confidently use kar sakte ho
- [ ] Common string methods yaad hain
- [ ] String immutability samajh gaye
- [ ] f-strings use karna aata hai

## ⏱️ Suggested Time:
Theory: 40 min | Practical: 60 min | Practice: 50 min | Revision: 30 min

---

## 🏗️ MINI PROJECT #1 (Day 1-4 Concepts Combined) 🔥

### Project: "Personal Info & Bio Card Generator"
**Requirement:** 
- User se naam, age, city, favourite quote input lo.
- Type conversion, f-strings, aur string methods (`.upper()`, `.title()`) use karke ek nicely formatted "Bio Card" print karo.
- Bonus: Quote ko `.title()` case mein convert karo aur ek border banao `"="*40` use karke.

```python
print("=" * 40)
name = input("Naam: ").strip().title()
age = int(input("Age: "))
city = input("City: ").strip().title()

print("=" * 40)
print(f"| Naam  : {name}")
print(f"| Age   : {age}")
print(f"| City  : {city}")
print("=" * 40)
```
Ismein tumhe input, type casting, string methods, aur f-strings — sab combine karke use karna hai. Isse khud se extend karke aur fields add karo.

---

# Day 5 – Lists & Tuples ⭐

## 🔄 Quick Revision (Day 1-4):
Variables, operators, aur strings — ab tak hum single values ke saath kaam kar rahe the. Aaj se **multiple values ek saath store karna** seekhenge.

## 🎯 Day Goal:
Lists aur Tuples samajhna — kab kya use karna hai, aur unpar common operations karna.

## 📚 Theory:

### 1. List Kya Hai ⭐
List ek **ordered, mutable (changeable)** collection hai jisme multiple values store ho sakti hain, `[]` mein likhte hain.

**Real-world analogy:** List ek **shopping cart** hai — items add/remove/reorder kar sakte ho, aur alag-alag types ki cheezein (fruits, electronics) ek saath rakh sakte ho.

```python
fruits = ["apple", "banana", "mango"]
mixed = [1, "hello", 3.14, True]  # different types allowed
```

### 2. List Operations 🔥
Indexing/slicing strings jaisi hi hoti hai. Plus:
- `.append()` — end mein add
- `.insert()` — specific position pe add
- `.remove()` — value se delete
- `.pop()` — index se delete (aur return karta hai)
- `.sort()`, `.reverse()`
- `len()`

### 3. List Mutability ⭐
Lists **mutable** hote hain — string ke ulat, list ke elements directly change ho sakte hain: `fruits[0] = "orange"`

### 4. Tuple Kya Hai ⭐
Tuple bhi list jaisa hai, lekin **immutable** hai — ek baar bana to change nahi kar sakte. `()` mein likhte hain.

**Real-world analogy:** Tuple ek **fixed coordinate (latitude, longitude)** jaisa hai — yeh change nahi hona chahiye, isliye tuple use hota hai. Ya kisi ka **date of birth (day, month, year)** — fixed rehta hai.

```python
coordinates = (28.6139, 77.2090)  # Delhi ki lat, long
```

### 5. List vs Tuple — Kab Kya Use Karein? 🔥
| List | Tuple |
|---|---|
| Mutable (change ho sakti hai) | Immutable (fix rehti hai) |
| Slower (thoda) | Faster |
| `[]` | `()` |
| Data jo change hoga (cart items) | Data jo fixed hai (coordinates, RGB colors) |

### 6. Nested Lists 💡
List ke andar list bhi ho sakti hai — 2D data (matrix, grid) ke liye useful.

## 💻 Practical:

### Example 1: List Operations
```python
fruits = ["apple", "banana", "mango"]

fruits.append("orange")        # end mein add
print(fruits)  # ['apple', 'banana', 'mango', 'orange']

fruits.insert(1, "grapes")     # index 1 pe insert
print(fruits)  # ['apple', 'grapes', 'banana', 'mango', 'orange']

fruits.remove("banana")        # value se remove
print(fruits)

fruits.sort()                  # alphabetically sort
print(fruits)

print(len(fruits))             # total items count
```

### Example 2: List Indexing, Slicing, Looping Preview
```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])     # 10
print(numbers[-1])    # 50
print(numbers[1:4])   # [20, 30, 40]

numbers[0] = 100       # list mutable hai, change ho sakti hai
print(numbers)         # [100, 20, 30, 40, 50]

total = sum(numbers)
print(f"Total: {total}, Max: {max(numbers)}, Min: {min(numbers)}")
```

### Example 3: Tuples
```python
person = ("Rahul", 25, "Mumbai")  # (name, age, city)

print(person[0])   # Rahul
# person[0] = "Amit"  # yeh ERROR dega - tuple immutable hai!

name, age, city = person   # tuple unpacking - bahut useful trick
print(f"{name} is {age} years old from {city}")
```
**Explanation:** Tuple unpacking se ek line mein multiple variables assign ho jaate hain — real projects mein bahut common pattern hai.

## 🧠 Practice Questions:
1. Ek list banao 5 numbers ki, phir usme ek naya number append karo aur ek delete karo.
2. List ka sabse bada aur chhota number `max()`, `min()` se nikaalo.
3. Ek tuple banao apne 3 favourite movies ka, aur unpacking use karke print karo.
4. Ek list ko `.sort()` aur `.reverse()` dono se manipulate karo, difference dekho.
5. Nested list banao (2x2 matrix jaisi) aur specific element access karo.

## 🔥 Coding Challenge:
Ek **"To-Do List Manager"** banao (basic version, loop ke bina) — ek list mein 5 tasks add karo, ek task complete hone par `.remove()` karo, aur final pending list print karo.

## 🎤 Interview Questions:
1. List aur Tuple mein main difference kya hai?
2. Tuple immutable hone ka fayda kya hai?
3. `.append()` aur `.insert()` mein farak batao.
4. `.remove()` aur `.pop()` mein kya difference hai?
5. Tuple unpacking kya hai? Example do.

## ✅ Day-End Checklist:
- [ ] List create aur modify kar sakte ho
- [ ] Common list methods yaad hain
- [ ] Tuple ka use-case samajh gaye
- [ ] List vs Tuple ka farak clear hai
- [ ] Tuple unpacking aata hai

## ⏱️ Suggested Time:
Theory: 45 min | Practical: 60 min | Practice: 50 min | Revision: 30 min

---

# Day 6 – Sets & Dictionaries ⭐

## 🔄 Quick Revision (Day 1-5):
List aur Tuple seekh liye. Aaj do aur important collections seekhenge — Sets (unique values) aur Dictionaries (key-value pairs), jo real projects mein bahut zyada use hote hain.

## 🎯 Day Goal:
Sets aur Dictionaries ka use samajhna aur unpar operations karna.

## 📚 Theory:

### 1. Set Kya Hai 🔥
Set ek **unordered collection of unique values** hai — duplicates automatically remove ho jaate hain. `{}` mein likhte hain (bina key-value ke).

**Real-world analogy:** Set ek **guest list** jaisa hai jisme koi naam repeat nahi ho sakta — agar same naam do baar add karo, woh ek hi baar count hoga.

```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3}  - duplicates automatically gone
```

### 2. Set Operations 💡
`.add()`, `.remove()`, union (`|`), intersection (`&`), difference (`-`) — mathematical set operations jaise school mein padhe the.

### 3. Dictionary Kya Hai ⭐
Dictionary **key-value pairs** store karta hai — real-world data represent karne ka sabse natural tareeka.

**Real-world analogy:** Dictionary ek **phone contact list** jaisi hai — naam (key) se number (value) dhoondte ho, index se nahi. Jaise real dictionary mein word (key) se meaning (value) milta hai.

```python
student = {
    "name": "Aarav",
    "age": 21,
    "city": "Delhi"
}
```

### 4. Dictionary Operations ⭐
- Access: `student["name"]` ya safer `student.get("name")`
- Add/Update: `student["grade"] = "A"`
- Delete: `del student["age"]` ya `.pop("age")`
- `.keys()`, `.values()`, `.items()`

### 5. Common Mistake ⚠️
`dict["key"]` agar key exist nahi karti to **KeyError** deta hai. `dict.get("key")` safer hai — nahi milne par `None` return karta hai, error nahi.

### 6. Nested Dictionaries 🔥
Real-world data (jaise JSON/API responses) mein dictionaries ke andar dictionaries hote hain — yeh Day 15 (API/JSON) ke liye important foundation hai.

## 💻 Practical:

### Example 1: Sets
```python
fruits_set = {"apple", "banana", "apple", "mango"}
print(fruits_set)  # {'apple', 'banana', 'mango'} - duplicate gone

fruits_set.add("orange")
print(fruits_set)

set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a | set_b)   # union: {1, 2, 3, 4}
print(set_a & set_b)   # intersection: {2, 3}
print(set_a - set_b)   # difference: {1}
```
**Real use-case:** Do lists ke common elements nikalne ke liye sets bahut fast aur clean tareeka hain (e.g., common friends between two users).

### Example 2: Dictionary Basics
```python
student = {
    "name": "Aarav",
    "age": 21,
    "marks": [85, 90, 78]
}

print(student["name"])          # Aarav
print(student.get("grade"))     # None (safe, error nahi aayega)

student["grade"] = "A"          # naya key-value add
student["age"] = 22             # existing update
print(student)

for key, value in student.items():
    print(f"{key}: {value}")
```
**Explanation:** `.items()` se dictionary ki har key-value pair ek tuple ki tarah milti hai, jisse loop mein use karna easy hota hai.

### Example 3: Nested Dictionary (Real-world Data)
```python
users = {
    "user1": {"name": "Priya", "age": 25},
    "user2": {"name": "Rohan", "age": 30}
}

print(users["user1"]["name"])   # Priya
print(users["user2"]["age"])    # 30
```
**Real-world connection:** Yehi structure APIs se JSON data aane par milta hai (Day 15 mein detail se seekhenge).

## 🧠 Practice Questions:
1. Ek list ko set mein convert karke duplicates remove karo.
2. Do sets ka union aur intersection nikaalo (apni 2 favourite subjects lists banao).
3. Apna profile ek dictionary mein banao (naam, age, city, hobbies-list) aur print karo.
4. Dictionary mein ek key update karo aur ek naya key-value pair add karo.
5. `.get()` use karke ek non-existent key access karo — dekho error nahi aata.

## 🔥 Coding Challenge:
Ek **"Student Record System"** (single student, loop ke bina) banao — dictionary mein naam, roll number, aur 3 subjects ke marks (nested list/dict) store karo, phir total aur average nikaal kar print karo.

## 🎤 Interview Questions:
1. Set aur List mein main difference kya hai?
2. Dictionary mein key duplicate ho sakti hai kya?
3. `dict["key"]` aur `dict.get("key")` mein kya farak hai?
4. Set ke union, intersection, difference operations kab useful hote hain?
5. Nested dictionary kya hoti hai? Real-world example do.

## ✅ Day-End Checklist:
- [ ] Set ka use-case aur operations samajh gaye
- [ ] Dictionary create, access, update, delete kar sakte ho
- [ ] `.get()` vs `[]` ka farak clear hai
- [ ] Nested dictionary access kar sakte ho

## ⏱️ Suggested Time:
Theory: 45 min | Practical: 65 min | Practice: 50 min | Revision: 30 min

---

# Day 7 – Conditional Statements ⭐

## 🔄 Quick Revision (Day 1-6):
Variables, operators, strings, lists, tuples, sets, dictionaries — data store karna aa gaya. Ab **decisions lena** seekhenge — yeh programming ki asli "logic building" shuru hoti hai.

## 🎯 Day Goal:
if-elif-else statements se apne program ko "decisions" lena sikhana.

## 📚 Theory:

### 1. if Statement ⭐
Condition True hone par hi block execute hota hai.

**Real-world analogy:** "Agar traffic light red hai, to ruk jao" — condition check hoti hai, phir action.

### 2. if-else ⭐
Do options mein se ek choose karna — condition True ya False.

### 3. if-elif-else ⭐
Multiple conditions check karne ke liye — jaise ek exam mein grade decide karna (A, B, C, F).

### 4. Nested Conditions 🔥
if ke andar if — complex decisions ke liye, lekin zyada nesting code ko messy bana deti hai (best practice: avoid deep nesting jahan possible ho).

### 5. Ternary (One-line if-else) 💡
```python
result = "Pass" if marks >= 40 else "Fail"
```
Short conditions ke liye clean way, lekin complex logic ke liye normal if-else better hai (readability).

### 6. Truthy & Falsy Values 🔥
Python mein `0`, `""`, `[]`, `{}`, `None`, `False` — sab **falsy** treat hote hain conditions mein. Baaki sab **truthy**.

```python
if []:
    print("yeh nahi chalega")  # empty list falsy hai
```

### 7. Common Mistake ⚠️
`if x = 5:` likhna (assignment vs comparison confuse karna) — Python yeh error de dega, lekin logic samajhna zaroori hai. Sahi: `if x == 5:`

## 💻 Practical:

### Example 1: Basic if-elif-else (Grading System)
```python
marks = int(input("Apke marks batao: "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print(f"Aapka grade: {grade}")
```
**Explanation:** Python top se bottom conditions check karta hai — pehli True condition milte hi baaki skip ho jaati hain.

### Example 2: Nested Conditions (Login System Logic)
```python
username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "1234":
        print("Login Successful!")
    else:
        print("Galat password!")
else:
    print("User exist nahi karta")
```

### Example 3: Truthy/Falsy + Ternary
```python
cart = []  # empty cart

if cart:
    print("Cart mein items hain")
else:
    print("Cart khaali hai")   # yeh print hoga, kyunki empty list falsy hai

marks = 45
status = "Pass" if marks >= 40 else "Fail"
print(status)
```

## 🧠 Practice Questions:
1. User se age lo aur batao "Child", "Teenager", "Adult", "Senior Citizen" (multiple elif use karo).
2. Ek number positive, negative ya zero hai — check karo.
3. Teen numbers input lekar sabse bada number nikaalo (nested if ya elif se).
4. Ek year leap year hai ya nahi check karo (`%` aur logical operators combine karo).
5. Ternary operator use karke ek number even/odd check karo.

## 🔥 Coding Challenge:
Ek **"Simple ATM Login System"** banao (loop ke bina, single attempt) — correct PIN pe balance dikhao, galat PIN pe error message do, aur agar balance check karne ke baad withdraw amount balance se zyada hai to "Insufficient Funds" bhi handle karo (nested condition).

## 🎤 Interview Questions:
1. if-elif-else ka flow kaise kaam karta hai?
2. Truthy aur Falsy values kya hoti hain? 3 examples do.
3. Ternary operator kab use karna chahiye aur kab nahi?
4. Nested conditions ka disadvantage kya hai?
5. `if x = 5` likhne par kya hoga aur kyun?

## ✅ Day-End Checklist:
- [ ] if-elif-else confidently likh sakte ho
- [ ] Nested conditions samajh gaye
- [ ] Truthy/Falsy concept clear hai
- [ ] Ternary operator use kar sakte ho

## ⏱️ Suggested Time:
Theory: 40 min | Practical: 55 min | Practice: 55 min | Revision: 30 min

---

# Day 8 – Loops ⭐

## 🔄 Quick Revision (Day 1-7):
Conditions se decisions lena seekh liya. Ab **repetition (baar-baar kaam karna)** seekhenge — loops se hi real automation aur data processing hoti hai.

## 🎯 Day Goal:
for loop, while loop, aur unke control statements (break, continue) master karna.

## 📚 Theory:

### 1. for Loop ⭐
Kisi sequence (list, string, range) ke har element pe ek-ek karke kaam karta hai.

**Real-world analogy:** For loop ek **teacher** hai jo class ke har student (list ke har item) ko ek-ek karke check karta hai — jab tak sab check na ho jayein.

### 2. range() Function ⭐
`range(start, stop, step)` — numbers ki sequence generate karta hai loop ke liye.

```python
range(5)        # 0,1,2,3,4
range(1, 6)     # 1,2,3,4,5
range(0, 10, 2) # 0,2,4,6,8
```

### 3. while Loop ⭐
Jab tak condition True hai, tab tak loop chalta rehta hai. Jab **kitni baar loop chalega pata na ho**, tab while use karo (for loop tab use karo jab count fixed ho).

**Real-world analogy:** While loop ek **security guard** jaisa hai — "jab tak gate khula hai, andar check karte raho" — pehle se pata nahi hota kitni baar check karna padega.

### 4. break & continue 🔥
- `break` — loop ko turant rok deta hai
- `continue` — current iteration skip karke agli iteration pe jaata hai

### 5. Nested Loops 🔥
Loop ke andar loop — patterns aur 2D data ke liye use hota hai.

### 6. Infinite Loop ⚠️ (Common Mistake)
`while True:` likh ke agar `break` condition nahi lagayi to program hang ho jaayega — beginners ki common galti.

### 7. else with Loop 💡
Python mein loops ke saath `else` bhi ho sakta hai — jab loop `break` na ho tab execute hota hai (rarely used, but good to know).

## 💻 Practical:

### Example 1: for Loop with range()
```python
for i in range(1, 6):
    print(f"Number: {i}")

# Output: Number: 1, Number: 2 ... Number: 5
```

### Example 2: for Loop over List/String + while Loop
```python
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(f"I like {fruit}")

# while loop example - countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")
```

### Example 3: break, continue, aur Nested Loop (Pattern)
```python
# break example: find first number divisible by 7
for num in range(1, 100):
    if num % 7 == 0:
        print(f"Mila: {num}")
        break

# continue example: skip even numbers
for num in range(1, 10):
    if num % 2 == 0:
        continue
    print(num)   # sirf odd numbers print honge

# nested loop - pattern printing
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()   # nayi line
```
**Explanation:** Outer loop ek baar chalta hai, uske andar inner loop poora chalta hai — isliye total `3*3=9` combinations print hongi.

## 🧠 Practice Questions:
1. `for` loop se 1 se 20 tak sirf even numbers print karo.
2. `while` loop se koi number entered hone tak (0 tak) sum calculate karo.
3. `break` use karke ek list mein pehla negative number dhoondo.
4. `continue` use karke 1-50 mein sirf 3 se divisible numbers print karo.
5. Nested loop se ek simple star pattern print karo (triangle shape).

## 🔥 Coding Challenge:
Ek **"Number Guessing Game"** banao — computer ek fixed number soche (e.g., 7), user `while True` loop mein guess kare, har galat guess pe "High" ya "Low" hint mile, aur sahi guess pe loop `break` ho jaye with attempts count.

## 🎤 Interview Questions:
1. `for` loop aur `while` loop mein kab kaunsa use karte hain?
2. `break` aur `continue` mein kya farak hai?
3. Infinite loop kya hota hai? Kaise avoid karein?
4. `range(1, 10, 2)` kya output degi?
5. Nested loops ka time complexity pe kya impact hota hai?

## ✅ Day-End Checklist:
- [ ] for loop with range() confidently use kar sakte ho
- [ ] while loop ka sahi use-case samajh gaye
- [ ] break aur continue ka farak clear hai
- [ ] Nested loops se pattern bana sakte ho
- [ ] Infinite loop avoid karna aata hai

## ⏱️ Suggested Time:
Theory: 40 min | Practical: 65 min | Practice: 55 min | Revision: 30 min

---

## 🏗️ MINI PROJECT #2 (Day 5-8 Concepts Combined) 🔥

### Project: "Contact Book (In-Memory, List of Dictionaries)"
**Requirement:**
- Dictionary ki list banao contacts store karne ke liye.
- Loop se saare contacts print karo (formatted).
- Conditions se ek specific naam search karo.
- List, dict, loop, conditions — sab combine hoga.

```python
contacts = [
    {"name": "Riya", "phone": "9876543210", "city": "Pune"},
    {"name": "Aman", "phone": "9123456780", "city": "Delhi"},
    {"name": "Sneha", "phone": "9988776655", "city": "Mumbai"}
]

print("===== Contact Book =====")
for contact in contacts:
    print(f"Name: {contact['name']} | Phone: {contact['phone']} | City: {contact['city']}")

search_name = input("\nSearch contact by name: ").strip().title()
found = False
for contact in contacts:
    if contact["name"] == search_name:
        print(f"Found -> {contact}")
        found = True
        break

if not found:
    print("Contact nahi mila")
```
Isko extend karo — user se naya contact `.append()` se add karwao, aur delete bhi implement karo.

---

# Day 9 – Functions ⭐

## 🔄 Quick Revision (Day 1-8):
Data types, conditions, loops — humne code likhna seekh liya. Ab code ko **reusable aur organized** banana seekhenge — Functions se hi "clean code" likhna shuru hota hai.

## 🎯 Day Goal:
Functions define karna, arguments/parameters ka concept, return values, aur default/keyword/variable arguments samajhna.

## 📚 Theory:

### 1. Function Kya Hai Aur Kyun ⭐
Function code ka ek **reusable block** hai jo specific kaam karta hai. Isse code **DRY (Don't Repeat Yourself)** rehta hai.

**Real-world analogy:** Function ek **recipe** jaisa hai — ek baar recipe (function) likh do, jab bhi khana banana ho (call karo), same steps follow ho jaate hain, bina dobara likhe.

```python
def greet():
    print("Hello!")

greet()   # call karne par hi execute hoga
```

### 2. Parameters vs Arguments 🔥
- **Parameter:** function definition mein variable name (`def greet(name):`)
- **Argument:** function call karte time actual value (`greet("Rahul")`)

### 3. return Statement ⭐
Function se value **wapas bhejne** ke liye — `print()` sirf dikhata hai, `return` value ko aage use karne ke liye deta hai.

⚠️ **Common Mistake:** `print()` aur `return` confuse karna. Function jo `return` nahi karta, woh `None` return karta hai by default.

### 4. Default Parameters 🔥
Agar argument na diya jaye to default value use hoti hai.

```python
def greet(name="Guest"):
    print(f"Hello {name}")

greet()          # Hello Guest
greet("Priya")   # Hello Priya
```

### 5. *args aur **kwargs 🔥
- `*args` — variable number ke **positional arguments** (tuple ki tarah)
- `**kwargs` — variable number ke **keyword arguments** (dict ki tarah)

**Real-world example:** Jab tumhe nahi pata user kitne items order karega, `*args` use karke unlimited items accept kar sakte ho.

### 6. Local vs Global Variables (Preview) 💡
Function ke andar bane variables sirf usi function mein exist karte hain (detail Day 10 mein).

## 💻 Practical:

### Example 1: Basic Function with Parameters & Return
```python
def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 10)
print(total)   # 15

# Without return - direct print (bad practice for reusability)
def show_sum(a, b):
    print(a + b)   # yeh value ko aage use nahi kar sakte
```
**Explanation:** `return` wali value ko variable mein store karke aage use kar sakte ho — `print()` sirf output dikhata hai, kuch return nahi karta.

### Example 2: Default Parameters & Keyword Arguments
```python
def create_profile(name, age=18, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

create_profile("Riya")                          # defaults use honge
create_profile("Aman", 25, "Delhi")               # positional
create_profile(name="Sneha", city="Mumbai", age=22)  # keyword args - order matter nahi karta
```

### Example 3: *args and **kwargs
```python
def total_marks(*scores):
    return sum(scores)

print(total_marks(85, 90, 78))       # 253
print(total_marks(60, 70))            # 130 - kitne bhi arguments chalein

def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Kabir", age=20, city="Jaipur")
```
**Explanation:** `*args` sab positional arguments ko ek tuple mein collect kar leta hai, `**kwargs` sab keyword arguments ko ek dictionary mein.

## 🧠 Practice Questions:
1. Ek function banao jo do numbers ka average nikaale aur return kare.
2. Ek function banao `is_even(number)` jo True/False return kare.
3. Default parameter wala function banao jo interest calculate kare (default rate = 5%).
4. `*args` use karke ek function banao jo kisi bhi count ke numbers ka max nikaale.
5. `**kwargs` use karke ek function banao jo student ki saari details ek formatted string mein return kare.

## 🔥 Coding Challenge:
Ek **"Simple Calculator"** banao using functions — `add()`, `subtract()`, `multiply()`, `divide()` alag-alag functions ho, aur ek main function user se operation choose karwaye aur result print kare (division mein zero-division bhi handle karo simple if se).

## 🎤 Interview Questions:
1. Parameter aur Argument mein kya farak hai?
2. `return` aur `print()` mein kya difference hai?
3. `*args` aur `**kwargs` kab use karte hain? Example do.
4. Default parameters ka use-case kya hai?
5. Agar function mein `return` statement na ho to kya hoga?
6. Function ko reusable banane ka kya fayda hai?

## ✅ Day-End Checklist:
- [ ] Function define aur call karna aata hai
- [ ] Parameters aur return values ka farak clear hai
- [ ] Default parameters use kar sakte ho
- [ ] *args aur **kwargs samajh gaye

## ⏱️ Suggested Time:
Theory: 45 min | Practical: 65 min | Practice: 55 min | Revision: 30 min

---

# Day 10 – Scope, Modules & Packages 🔥

## 🔄 Quick Revision (Day 1-9):
Functions se code reusable banana seekh liya. Aaj seekhenge variables kahan "accessible" hote hain (scope), aur apna code multiple files mein kaise organize karte hain (modules).

## 🎯 Day Goal:
Variable scope (local/global) samajhna, aur Python modules/packages import karke use karna.

## 📚 Theory:

### 1. Local vs Global Scope ⭐
- **Local variable:** function ke andar bana, sirf usi function mein accessible.
- **Global variable:** function ke bahar bana, poore program mein accessible.

**Real-world analogy:** Local variable ek **office ka internal memo** hai — sirf us department (function) mein valid hai. Global variable **company-wide announcement** hai — sab jagah dikhta hai.

```python
x = 10  # global

def show():
    y = 5   # local
    print(x)   # global access ho sakta hai
    print(y)

show()
# print(y)  # ERROR - y function ke bahar exist nahi karta
```

### 2. global Keyword 🔥
Function ke andar se global variable ko modify karne ke liye `global` keyword chahiye (best practice: isse avoid karo jahan possible ho, kyunki debugging mushkil karta hai).

### 3. Modules Kya Hain ⭐
Module ek `.py` file hai jisme functions/classes/variables hoti hain, jisse hum **import** karke reuse kar sakte hain.

**Real-world analogy:** Module ek **toolbox** hai — tumhe har cheez khud banane ki zarurat nahi, existing tools (`math`, `random` modules) import karke use kar sakte ho.

### 4. Common Built-in Modules ⭐
```python
import math
import random
from datetime import datetime
```

### 5. Packages 💡
Package modules ka ek collection (folder) hai jisme `__init__.py` hota hai. Bade projects multiple modules ko packages mein organize karte hain.

### 6. pip & Virtual Environments (Preview) 🔥
`pip` Python ka package manager hai jisse third-party libraries install karte hain (`pip install requests`). Detail Day 15 mein.

## 💻 Practical:

### Example 1: Local vs Global Scope
```python
counter = 0   # global

def increment():
    global counter   # bina isके counter modify nahi ho sakta
    counter += 1

increment()
increment()
print(counter)   # 2
```
**Explanation:** `global` keyword batata hai Python ko ki hum function ke andar bhi outer/global `counter` ko hi modify kar rahe hain, naya local variable nahi bana rahe.

### Example 2: Using Built-in Modules
```python
import math
print(math.sqrt(25))     # 5.0
print(math.pi)            # 3.14159...
print(math.ceil(4.3))     # 5
print(math.floor(4.7))    # 4

import random
print(random.randint(1, 10))    # random number 1-10 ke beech
print(random.choice(["A", "B", "C"]))  # random selection

from datetime import datetime
now = datetime.now()
print(now.strftime("%d-%m-%Y %H:%M"))
```

### Example 3: Creating Your Own Module
```python
# file: my_utils.py
def greet(name):
    return f"Hello, {name}!"

def square(n):
    return n * n
```
```python
# file: main.py
import my_utils

print(my_utils.greet("Riya"))
print(my_utils.square(5))

# ya specific function import karo:
from my_utils import square
print(square(4))
```
**Explanation:** Apna code multiple files mein todkar organize karna large projects mein essential hai — yeh real-world software development ka standard practice hai.

## 🧠 Practice Questions:
1. Ek global counter banao jo function calls se increment ho.
2. `math` module use karke ek circle ka area nikaalo (radius input lekar).
3. `random` module se ek "dice roll simulator" banao (1-6 random number).
4. `datetime` module se aaj ki date aur time print karo formatted way mein.
5. Apna ek chhota module banao (`calculator_utils.py`) jisme 2 functions ho, aur usse main file mein import karke use karo.

## 🔥 Coding Challenge:
Ek **"OTP Generator"** banao `random` module use karke — 6-digit random OTP generate kare, aur isse ek separate module (`otp_utils.py`) mein function ki tarah likho, phir main file se import karke use karo.

## 🎤 Interview Questions:
1. Local aur Global variable mein kya farak hai?
2. `global` keyword ka use kab karte hain?
3. Module aur Package mein kya farak hai?
4. `import module` aur `from module import function` mein kya difference hai?
5. Kuch built-in Python modules ke naam batao jo aapne use kiye.

## ✅ Day-End Checklist:
- [ ] Local vs Global scope ka farak clear hai
- [ ] Built-in modules (math, random, datetime) use kar sakte ho
- [ ] Apna module bana kar import kar sakte ho
- [ ] Module vs Package samajh gaye

## ⏱️ Suggested Time:
Theory: 40 min | Practical: 60 min | Practice: 50 min | Revision: 30 min

---

# Day 11 – Exception Handling ⭐

## 🔄 Quick Revision (Day 1-10):
Functions aur modules seekh liye. Aaj seekhenge **errors ko gracefully handle karna** — real-world programs crash nahi hone chahiye, unhe errors ko "catch" karke handle karna chahiye.

## 🎯 Day Goal:
try-except-else-finally samajhna aur apne programs ko crash-proof banana.

## 📚 Theory:

### 1. Exception Kya Hai ⭐
Exception ek **error hai jo program run hote time (runtime) aata hai** aur agar handle na ho to program crash ho jaata hai.

**Real-world analogy:** Jaise driving karte time achanak tyre puncture ho jaye — agar spare tyre (exception handling) ready hai to safar rukta nahi, warna gaadi wahi ruk jaati hai (crash).

### 2. Common Exceptions ⭐
- `ZeroDivisionError` — kisi number ko 0 se divide karna
- `ValueError` — galat type ki value (e.g., `int("abc")`)
- `TypeError` — incompatible types operate karna (e.g., `"5" + 5`)
- `IndexError` — list ka out-of-range index access karna
- `KeyError` — dictionary mein non-existent key access karna
- `FileNotFoundError` — file exist na karna

### 3. try-except Block ⭐
Risky code `try` block mein likhte hain, aur agar error aaye to `except` block usse "catch" kar leta hai.

### 4. Multiple except Blocks 🔥
Different types ke errors ko alag-alag handle kar sakte ho.

### 5. else aur finally 🔥
- `else` — sirf tab chalta hai jab try mein **koi error na aaye**
- `finally` — **hamesha** chalta hai, error aaye ya na aaye (cleanup ke liye, jaise file close karna)

### 6. raise Statement 💡
Khud se custom exception "throw" karne ke liye.

### 7. Common Mistake ⚠️
Bare `except:` (bina exception type specify kiye) use karna — yeh **sab errors ko silently hide** kar deta hai, jo debugging ko mushkil bana deta hai. Hamesha specific exception type catch karo.

## 💻 Practical:

### Example 1: Basic try-except
```python
try:
    num = int(input("Number daalo: "))
    result = 10 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: 0 se divide nahi kar sakte!")
except ValueError:
    print("Error: Sirf number daalo, text nahi!")
```
**Explanation:** Agar user "0" daalta hai to `ZeroDivisionError` catch hoga, aur agar text daalta hai to `ValueError` catch hoga — program crash nahi hoga.

### Example 2: else and finally
```python
try:
    num = int(input("Number daalo: "))
    result = 100 / num
except ZeroDivisionError:
    print("Zero se divide nahi kar sakte")
except ValueError:
    print("Valid number nahi hai")
else:
    print(f"Success! Result: {result}")   # sirf tab chalega jab error na aaye
finally:
    print("Program execution complete")   # hamesha chalega
```

### Example 3: Custom Exception with raise
```python
def check_age(age):
    if age < 0:
        raise ValueError("Age negative nahi ho sakti!")
    if age < 18:
        raise Exception("Aap minor ho, entry allowed nahi")
    return "Entry Allowed"

try:
    print(check_age(-5))
except ValueError as e:
    print(f"ValueError aaya: {e}")
except Exception as e:
    print(f"Exception aaya: {e}")
```
**Explanation:** `raise` se hum khud custom conditions pe error create kar sakte hain, aur `as e` se error message access kar sakte hain.

## 🧠 Practice Questions:
1. Ek program banao jo user se do numbers lekar divide kare, aur `ZeroDivisionError` handle kare.
2. Ek list ka index access karo jo exist nahi karta, `IndexError` handle karo.
3. Dictionary mein non-existent key access karke `KeyError` handle karo.
4. `try-except-else-finally` — sab use karke ek complete program banao.
5. `raise` use karke ek function banao jo negative number pass karne pe custom error de.

## 🔥 Coding Challenge:
Ek **"Safe Calculator"** banao jo user se do numbers aur operation (+, -, *, /) le, aur saare possible errors (ZeroDivisionError, ValueError, invalid operation) ko gracefully handle kare bina crash hue.

## 🎤 Interview Questions:
1. Exception handling ka main purpose kya hai?
2. `try-except` aur `if-else` mein kya farak hai (kab kya use karein)?
3. `finally` block kab use karte hain? Example do.
4. Bare `except:` use karna kyun bad practice hai?
5. `raise` keyword ka use kya hai?
6. 3 common built-in exceptions ke naam batao.

## ✅ Day-End Checklist:
- [ ] try-except confidently use kar sakte ho
- [ ] Multiple exceptions handle kar sakte ho
- [ ] else aur finally ka farak clear hai
- [ ] Custom exceptions raise karna aata hai

## ⏱️ Suggested Time:
Theory: 40 min | Practical: 60 min | Practice: 55 min | Revision: 30 min

---

# Day 12 – File Handling 🔥

## 🔄 Quick Revision (Day 1-11):
Exception handling se programs crash-proof bana liye. Aaj seekhenge data ko **permanently store** karna (files mein) — kyunki abhi tak program band hote hi saara data khatam ho jaata tha.

## 🎯 Day Goal:
Files ko read, write, aur append karna, aur `with` statement (context manager) ka best-practice use samajhna.

## 📚 Theory:

### 1. File Handling Kyun Zaroori Hai ⭐
Abhi tak jo bhi data humne store kiya (list, dict), woh program band hote hi **RAM se delete** ho jaata hai. Files se data **permanently disk pe save** hota hai.

**Real-world analogy:** Program ki memory (RAM) ek **whiteboard** jaisi hai — mitao to sab khatam. File ek **notebook** jaisi hai — likha hua permanently rehta hai, dobara khol kar padh sakte ho.

### 2. File Modes ⭐
| Mode | Matlab |
|---|---|
| `'r'` | Read (default) — file exist na ho to error |
| `'w'` | Write — naya file banata hai, agar exist karti hai to **overwrite** kar deta hai (purana data delete!) |
| `'a'` | Append — end mein add karta hai, purana data safe rehta hai |
| `'r+'` | Read aur write dono |

⚠️ **Common Mistake:** `'w'` mode use karke accidentally purana important data overwrite kar dena — hamesha soch samajh kar mode choose karo.

### 3. open() aur close() 🔥
```python
file = open("data.txt", "r")
content = file.read()
file.close()   # yeh MANUALLY close karna padta hai, bhoolna common mistake hai
```

### 4. with Statement (Best Practice) ⭐
`with` statement automatically file ko close kar deta hai, chahe error aaye ya na aaye — isliye yeh **hamesha use karna chahiye**, manual `close()` ki jagah.

```python
with open("data.txt", "r") as file:
    content = file.read()
# yahan automatically file close ho chuki hai
```

### 5. Reading Methods 🔥
- `.read()` — poori file ek string mein
- `.readline()` — ek line
- `.readlines()` — saari lines ek list mein

### 6. Working with CSV-like / structured text 💡
Basic text files ke saath JSON (Day 15) aur CSV bhi common real-world formats hain.

## 💻 Practical:

### Example 1: Writing to a File
```python
with open("notes.txt", "w") as file:
    file.write("Yeh mera pehla note hai.\n")
    file.write("File handling seekh raha hoon.\n")

# file automatically close ho gayi with block khatam hote hi
```
**Explanation:** `'w'` mode se agar `notes.txt` exist nahi karti to naya banega, agar exist karti hai to overwrite ho jayegi.

### Example 2: Reading a File
```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

with open("notes.txt", "r") as file:
    for line in file:              # file lines pe directly loop kar sakte ho
        print(line.strip())        # .strip() se extra newline hat jaata hai
```

### Example 3: Appending to a File
```python
with open("notes.txt", "a") as file:
    file.write("Yeh naya line hai, purana data safe hai.\n")

with open("notes.txt", "r") as file:
    print(file.read())
```

### Example 4: Handling File Errors (Combining Day 11!)
```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File exist nahi karti!")
```

## 🧠 Practice Questions:
1. Ek file banao aur usme apni 5 favourite movies likho (ek line ek movie).
2. Us file ko read karke lines ko ek list mein store karo.
3. File mein 2 naye tasks append karo bina purana data delete kiye.
4. Ek file read karne ki koshish karo jo exist nahi karti — `FileNotFoundError` handle karo.
5. Ek text file se saari lines padho aur count karo total kitne words hain.

## 🔥 Coding Challenge:
Ek **"Simple To-Do List App (File-based)"** banao jisme:
- User task add kar sake (file mein append ho)
- Saare tasks file se read karke print ho sakein
- (Bonus) Ek specific task delete karne ka logic socho — poori file read karo, filter karo, phir `'w'` mode se rewrite karo.

## 🎤 Interview Questions:
1. `'w'` aur `'a'` mode mein kya farak hai?
2. `with` statement kyun use karte hain, manual `open()`/`close()` ki jagah?
3. `.read()`, `.readline()`, `.readlines()` mein kya farak hai?
4. File handling mein `FileNotFoundError` kab aata hai?
5. Agar file close karna bhool jaayein to kya problem ho sakti hai?

## ✅ Day-End Checklist:
- [ ] File read, write, append confidently kar sakte ho
- [ ] `with` statement ka best practice use samajh gaye
- [ ] File modes (r, w, a) ka farak clear hai
- [ ] File errors handle kar sakte ho

## ⏱️ Suggested Time:
Theory: 40 min | Practical: 65 min | Practice: 55 min | Revision: 30 min

---

## 🏗️ MINI PROJECT #3 (Day 9-12 Concepts Combined) 🔥🔥

### Project: "Persistent To-Do List Application"
**Requirement:** Functions + Exception Handling + File Handling — sab combine karke ek proper CLI (command-line) app banao.

```python
import os

FILENAME = "todo.txt"

def add_task(task):
    with open(FILENAME, "a") as file:
        file.write(task + "\n")
    print(f"Task added: {task}")

def view_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("Koi task nahi hai!")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("Abhi tak koi task add nahi hui hai.")

def delete_task(task_number):
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number!")
            return

        tasks.pop(task_number - 1)   # list se remove

        with open(FILENAME, "w") as file:   # rewrite entire file
            file.writelines(tasks)
        print("Task deleted successfully!")
    except FileNotFoundError:
        print("Koi task list exist nahi karti.")

# Simple menu-driven interaction
while True:
    print("\n1. Add Task  2. View Tasks  3. Delete Task  4. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        num = int(input("Enter task number to delete: "))
        delete_task(num)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again")
```
**Note:** Isme `enumerate()` function use hua hai (list ko index ke saath loop karna) — yeh ek chhota naya concept hai jo practically bahut use hota hai, isse explore karo.

Yeh project functions, loops, conditions, file handling, aur exception handling — **sabko real application** mein combine karta hai. Isse khud extend karo (jaise "mark as complete" feature add karo).

---

# Day 13 – Object-Oriented Programming (OOP) Part 1 ⭐

## 🔄 Quick Revision (Day 1-12):
Functions, files, exceptions — humne "procedural" style mein code likha (steps ki tarah). Aaj se **OOP (Object-Oriented Programming)** shuru — real-world entities ko code mein represent karna seekhenge, jo professional software development ka core hai.

## 🎯 Day Goal:
Classes, objects, `__init__` constructor, aur instance methods samajhna.

## 📚 Theory:

### 1. OOP Kya Hai Aur Kyun ⭐
OOP ek programming style hai jisme hum real-world cheezon (Car, Student, BankAccount) ko **Class** (blueprint) aur **Object** (actual cheez) se represent karte hain.

**Real-world analogy:** **Class** ek **blueprint/naksha** hai ghar banane ka. **Object** actual **ghar** hai jo us blueprint se bana. Ek blueprint se multiple ghar (objects) ban sakte hain, har ghar ka apna address/color (data) hoga lekin structure same hoga.

### 2. Class Define Karna ⭐
```python
class Car:
    pass   # empty class
```

### 3. `__init__` Constructor ⭐
Jab bhi object banta hai, `__init__` automatically call hota hai — yeh object ki **initial properties (attributes)** set karta hai.

### 4. `self` Keyword ⭐
`self` current object ko refer karta hai — har method ka pehla parameter `self` hota hai, taaki class ko pata chale kis specific object pe kaam ho raha hai.

**Real-world analogy:** `self` ek "yeh wala" pointer hai — jaise 10 cars hain (objects), `self` batata hai "**is** specific car" ki baat ho rahi hai, doosri cars ki nahi.

### 5. Instance Attributes vs Methods 🔥
- **Attributes:** object ka data (`self.color`, `self.brand`)
- **Methods:** object ka behavior/function (`self.start_engine()`)

### 6. Creating Multiple Objects ⭐
Ek class se multiple independent objects ban sakte hain, har ek ka apna data hoga.

## 💻 Practical:

### Example 1: Basic Class with Constructor
```python
class Student:
    def __init__(self, name, age, marks):
        self.name = name       # attribute
        self.age = age
        self.marks = marks

    def display(self):          # method
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

s1 = Student("Riya", 20, 85)
s2 = Student("Aman", 22, 78)

s1.display()   # Name: Riya, Age: 20, Marks: 85
s2.display()   # Name: Aman, Age: 22, Marks: 78
```
**Explanation:** `__init__` har naye object ke liye automatically chalta hai jab `Student("Riya", 20, 85)` call hota hai. `self.name` object ke andar data store karta hai.

### Example 2: Methods that Modify Data (Real-world: Bank Account)
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

account = BankAccount("Priya", 1000)
account.deposit(500)      # New balance: 1500
account.withdraw(2000)    # Insufficient balance!
account.withdraw(800)     # New balance: 700
```

### Example 3: Multiple Objects, Independent Data
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Tesla", "Model 3")
car2 = Car("Toyota", "Fortuner")

print(car1.brand, car1.model)   # Tesla Model 3
print(car2.brand, car2.model)   # Toyota Fortuner
# car1 aur car2 completely independent hain
```

## 🧠 Practice Questions:
1. Ek `Person` class banao (name, age attributes) aur ek method jo "introduce" kare.
2. `BankAccount` class ko extend karo — ek `check_balance()` method add karo.
3. Ek `Rectangle` class banao jisme `length`, `width` ho, aur `area()` aur `perimeter()` methods.
4. 3 alag `Student` objects banao aur ek loop se sabka data print karo.
5. Ek `Book` class banao (title, author, price) aur ek method jo discount apply kare.

## 🔥 Coding Challenge:
Ek **"Library Management (Basic OOP)"** banao — `Book` class banao (title, author, is_available), aur methods `borrow_book()` aur `return_book()` jo availability status update karein.

## 🎤 Interview Questions:
1. Class aur Object mein kya farak hai?
2. `__init__` method kya karta hai aur kab call hota hai?
3. `self` keyword ka use kya hai?
4. Attribute aur Method mein kya farak hai?
5. Ek class se multiple objects banana kya demonstrate karta hai?

## ✅ Day-End Checklist:
- [ ] Class aur Object ka concept clear hai
- [ ] `__init__` constructor samajh gaye
- [ ] `self` ka use samajh gaye
- [ ] Methods define aur call kar sakte ho
- [ ] Multiple independent objects bana sakte ho

## ⏱️ Suggested Time:
Theory: 50 min | Practical: 65 min | Practice: 55 min | Revision: 30 min

---

# Day 14 – OOP Part 2 + Comprehensions + Lambda/Map/Filter ⭐

## 🔄 Quick Revision (Day 1-13):
Kal classes aur objects seekhe. Aaj OOP ke 2 important pillars (Inheritance, Encapsulation) + kuch **Pythonic shortcuts** (comprehensions, lambda) seekhenge jo clean, professional code likhne ke liye zaroori hain.

## 🎯 Day Goal:
Inheritance, encapsulation basics, list/dict comprehensions, aur lambda/map/filter/reduce samajhna.

## 📚 Theory:

### 1. Inheritance ⭐
Ek class (child) doosri class (parent) ki properties/methods **inherit (le sakti)** hai — code reuse ka powerful tareeka.

**Real-world analogy:** Jaise beta apne parents ke kuch traits inherit karta hai, lekin apne khud ke bhi traits add kar sakta hai — waise hi child class parent ki cheezein use kar sakti hai aur naya bhi add kar sakti hai.

```python
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):    # Dog inherits from Animal
    def bark(self):
        print("Barking...")

d = Dog()
d.eat()    # Animal se inherited
d.bark()   # Dog ka apna
```

### 2. Encapsulation (Basics) 🔥
Data ko **protect** karna — Python mein `_variable` (protected, convention) aur `__variable` (private, name-mangled) use hota hai.

**Real-world analogy:** ATM machine ka internal circuit (private data) tum directly touch nahi kar sakte — sirf buttons (public methods) se interact karte ho.

### 3. `super()` 💡
Child class se parent class ka method/constructor call karne ke liye.

### 4. List Comprehension ⭐
Ek line mein list banane ka **Pythonic** (clean, fast) tareeka — normal loop se short aur readable.

```python
squares = [x**2 for x in range(5)]
# equivalent to:
squares = []
for x in range(5):
    squares.append(x**2)
```

### 5. Dict Comprehension 🔥
Same concept dictionaries ke liye.

### 6. Lambda Functions 🔥
Ek chhota **anonymous (bina naam ka) function**, single expression ke liye — jab function itna chhota ho ki poora `def` likhna overkill lage.

```python
square = lambda x: x**2
print(square(5))   # 25
```

### 7. map(), filter(), reduce() 🔥
- `map()` — har element pe function apply karta hai
- `filter()` — condition True honay wale elements select karta hai
- `reduce()` (from `functools`) — sabko combine karke ek single value banata hai

### 8. Iterators & Generators (Intro) 💡
- **Iterator:** object jo `next()` se ek-ek value deta hai
- **Generator:** `yield` keyword use karke memory-efficient tareeke se values generate karta hai (poori list memory mein nahi rakhta) — bade datasets ke liye important.

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)   # 1,2,3,4,5 - ek-ek karke generate hote hain
```

## 💻 Practical:

### Example 1: Inheritance & Encapsulation
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # private attribute (encapsulation)

    def show_salary(self):
        print(f"{self.name}'s salary: {self.__salary}")

class Manager(Employee):          # inheritance
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # parent constructor call
        self.team_size = team_size

    def show_team(self):
        print(f"{self.name} manages {self.team_size} people")

m = Manager("Rohan", 80000, 5)
m.show_salary()   # inherited method
m.show_team()      # own method
# print(m.__salary)  # ERROR - private attribute directly access nahi ho sakta
```

### Example 2: List & Dict Comprehension
```python
numbers = [1, 2, 3, 4, 5, 6]

squares = [n**2 for n in numbers]
print(squares)   # [1, 4, 9, 16, 25, 36]

evens = [n for n in numbers if n % 2 == 0]   # with condition
print(evens)      # [2, 4, 6]

square_dict = {n: n**2 for n in numbers}
print(square_dict)   # {1: 1, 2: 4, 3: 9, ...}
```

### Example 3: Lambda, map, filter, reduce
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map - har element ko square karo
squared = list(map(lambda x: x**2, numbers))
print(squared)   # [1, 4, 9, 16, 25]

# filter - sirf even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4]

# reduce - sabko multiply karke ek value
product = reduce(lambda x, y: x * y, numbers)
print(product)   # 120 (1*2*3*4*5)
```
**Explanation:** `map`/`filter` list comprehensions ke alternative hain — modern Python mein comprehensions zyada preferred (readable) hain, lekin `map`/`filter`/`reduce` samajhna bhi important hai (interviews mein poocha jaata hai).

## 🧠 Practice Questions:
1. Ek `Vehicle` parent class banao, aur `Car`, `Bike` child classes banao inheritance se.
2. Encapsulation use karke ek `Account` class banao jisme balance private ho.
3. List comprehension se 1-50 mein sirf prime-check ke bina, multiples of 5 nikaalo.
4. Dict comprehension se ek list of words ki length ka dictionary banao.
5. `lambda` aur `map()` use karke ek list ke saare numbers ko double karo.
6. Generator function banao jo Fibonacci series generate kare.

## 🔥 Coding Challenge:
Ek **"Shape Hierarchy"** banao — parent class `Shape` (with `area()` method placeholder), aur child classes `Circle`, `Rectangle`, `Triangle` jo apna `area()` calculate karein (yeh polymorphism ka bhi preview hai — same method name, different behavior).

## 🎤 Interview Questions:
1. Inheritance kya hai? Real-world example do.
2. `super()` ka use kya hai?
3. Python mein "private" variable ka concept kaise implement hota hai?
4. List comprehension normal loop se better kyun hai?
5. Lambda function normal function se kaise different hai?
6. Generator aur normal function mein kya farak hai? `yield` kya karta hai?

## ✅ Day-End Checklist:
- [ ] Inheritance implement kar sakte ho
- [ ] Encapsulation ka basic concept clear hai
- [ ] List/dict comprehension confidently likh sakte ho
- [ ] Lambda, map, filter, reduce use kar sakte ho
- [ ] Generator function ka basic idea clear hai

## ⏱️ Suggested Time:
Theory: 55 min | Practical: 70 min | Practice: 55 min | Revision: 30 min

---

# Day 15 – Virtual Environments, APIs/JSON, Debugging & FINAL PROJECT ⭐🔥

## 🔄 Quick Revision (Day 1-14):
Congratulations — tum yahan tak pahunch gaye ho! Poore 14 din ka content ek baar mentally scan karo: variables → data types → operators → strings → collections → conditions → loops → functions → modules → exceptions → files → OOP → comprehensions. Aaj sab kuch ek **real project** mein combine hoga.

## 🎯 Day Goal:
Virtual environments/pip recap karna, JSON data aur APIs ke saath kaam karna, debugging best practices seekhna, aur ek **complete final project** banana jo multiple concepts combine kare.

## 📚 Theory:

### 1. Virtual Environments Kyun Zaroori Hain ⭐
Virtual environment ek **isolated Python environment** hai — har project ki apni alag libraries/versions hoti hain, taaki ek project ki dependencies doosre project se clash na karein.

**Real-world analogy:** Virtual environment alag-alag **kitchen** jaisa hai har recipe (project) ke liye — taaki ek dish ke ingredients doosri dish mein galti se mix na ho jaayein.

```bash
python -m venv myenv        # environment banao
myenv\Scripts\activate      # Windows activate
source myenv/bin/activate   # Mac/Linux activate
pip install requests        # ab isi environment mein install hoga
deactivate                  # environment se bahar aao
```

### 2. pip — Package Manager ⭐
`pip` se third-party libraries install karte hain jo Python ke saath by-default nahi aatin (jaise `requests`, `pandas`).

```bash
pip install requests
pip list                    # installed packages dekho
pip freeze > requirements.txt   # sab dependencies file mein save karo
```

### 3. JSON Kya Hai ⭐
JSON (JavaScript Object Notation) data exchange ka **universal format** hai — APIs almost hamesha JSON mein data bhejti hain. JSON structure Python dictionary jaisa hi dikhta hai.

```json
{
    "name": "Riya",
    "age": 25,
    "skills": ["Python", "SQL"]
}
```

### 4. Python's json Module 🔥
- `json.loads()` — JSON string ko Python dict mein convert karta hai
- `json.dumps()` — Python dict ko JSON string mein convert karta hai

### 5. Working with APIs 🔥
API (Application Programming Interface) se hum internet se real-time data le sakte hain (weather, news, etc.). Python mein `requests` library (pip se install) use hoti hai.

**Real-world analogy:** API ek **waiter** hai restaurant mein — tum order (request) do, woh kitchen (server) se data laakar deta hai (response), bina tumhe kitchen ke andar jaane diye.

### 6. Debugging Best Practices ⭐
- `print()` statements se variable values track karo (quick debugging)
- Error messages **poori padhо** — Python bataata hai exact line aur error type
- Code ko chhote pieces mein test karo, ek saath poora complex code mat likho
- Meaningful variable/function names use karo
- Comments likho jahan logic complex ho

### 7. Clean Code Best Practices 🔥
- Functions chhote aur single-purpose rakho
- DRY principle (Don't Repeat Yourself)
- Consistent naming (`snake_case`)
- Magic numbers avoid karo (constants use karo)

## 💻 Practical:

### Example 1: JSON Basics
```python
import json

# Python dict -> JSON string
data = {"name": "Aarav", "age": 21, "skills": ["Python", "Java"]}
json_string = json.dumps(data, indent=4)
print(json_string)

# JSON string -> Python dict
json_data = '{"name": "Riya", "age": 25}'
python_dict = json.loads(json_data)
print(python_dict["name"])   # Riya

# JSON file se read/write
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
```

### Example 2: Calling a Real API
```python
import requests   # pip install requests karna padega pehle

response = requests.get("https://api.github.com/users/octocat")

if response.status_code == 200:
    data = response.json()   # JSON response ko Python dict mein convert
    print(f"Name: {data['name']}")
    print(f"Public Repos: {data['public_repos']}")
else:
    print(f"Error: {response.status_code}")
```
**Explanation:** `requests.get()` API ko call karta hai, `.json()` response ko directly Python dictionary mein convert kar deta hai — yehi wo skill hai jo backend/frontend integration mein daily use hoti hai.

### Example 3: Debugging Example
```python
def calculate_discount(price, discount_percent):
    print(f"DEBUG: price={price}, discount_percent={discount_percent}")  # debug line
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    print(f"DEBUG: final_price={final_price}")   # debug line
    return final_price

result = calculate_discount(1000, 20)
print(f"Final Price: {result}")
```
**Explanation:** Temporary `print("DEBUG: ...")` statements se pata chalta hai variables mein kya values hain, kaunse step pe cheezein galat ho rahi hain — production code mein baad mein remove kar dete hain ya proper `logging` module use karte hain (advanced topic).

## 🧠 Practice Questions:
1. Ek Python dictionary banao aur usse JSON file mein save karo.
2. Us JSON file ko wapas read karke Python dict mein load karo.
3. `requests` library install karke koi bhi free public API call karo (e.g., `https://api.github.com/users/<username>`).
4. Ek function mein intentionally bug daalo, phir debug print statements se usse dhoondo aur fix karo.
5. Apne Day 12 wale To-Do project ko JSON file use karne ke liye modify karo (text file ki jagah).

---

## 🏆 FINAL PROJECT (Day 15) — "Student Management System" 🔥⭐

Yeh project combine karta hai: **OOP, File Handling, JSON, Exception Handling, Functions, Loops, Conditions, Comprehensions** — poora roadmap ek jagah.

### Requirements:
1. `Student` class banao (OOP) — name, roll_no, marks (dict of subjects).
2. Students ka data JSON file mein permanently store ho (File Handling + JSON).
3. User menu-driven options se: Add Student, View All Students, Search Student, Calculate Average (Functions + Loops + Conditions).
4. Saare invalid inputs exception handling se safely handle hon.

```python
import json
import os

FILENAME = "students.json"

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks   # dict: {"Math": 90, "Science": 85}

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def to_dict(self):
        return {"name": self.name, "roll_no": self.roll_no, "marks": self.marks}


def load_students():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_students(students):
    with open(FILENAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    name = input("Student ka naam: ").strip().title()
    try:
        roll_no = int(input("Roll number: "))
    except ValueError:
        print("Invalid roll number!")
        return

    marks = {}
    num_subjects = int(input("Kitne subjects hain? "))
    for i in range(num_subjects):
        subject = input(f"Subject {i+1} ka naam: ").strip().title()
        try:
            score = float(input(f"{subject} mein marks: "))
            marks[subject] = score
        except ValueError:
            print("Invalid marks, skip kar diya")

    student = Student(name, roll_no, marks)
    students = load_students()
    students.append(student.to_dict())
    save_students(students)
    print(f"Student {name} add ho gaya!")


def view_students():
    students = load_students()
    if not students:
        print("Koi student record nahi hai")
        return
    print("\n===== All Students =====")
    for s in students:
        avg = sum(s["marks"].values()) / len(s["marks"]) if s["marks"] else 0
        print(f"Roll No: {s['roll_no']} | Name: {s['name']} | Average: {avg:.2f}")


def search_student():
    students = load_students()
    try:
        roll_no = int(input("Search karne ke liye roll number: "))
    except ValueError:
        print("Invalid input!")
        return

    found = [s for s in students if s["roll_no"] == roll_no]   # list comprehension!

    if found:
        s = found[0]
        print(f"Found -> Name: {s['name']}, Marks: {s['marks']}")
    else:
        print("Student nahi mila")


def main_menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll No")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Dhanyawad! Program band ho raha hai.")
            break
        else:
            print("Invalid choice, dobara try karo")


if __name__ == "__main__":
    main_menu()
```

**Isme use hue concepts:**
- ✅ OOP (Student class, methods)
- ✅ File Handling + JSON (persistent storage)
- ✅ Exception Handling (invalid inputs safely handled)
- ✅ Functions (modular, reusable code)
- ✅ Loops & Conditions (menu system)
- ✅ List Comprehension (search function mein)
- ✅ f-strings, string methods

### Extend Karne Ke Liye Ideas (Khud Try Karo):
- "Delete Student" aur "Update Marks" features add karo
- Sorting add karo (students ko average marks ke hisaab se sort karo)
- Grade calculate karo (A/B/C) average ke basis pe
- Input validation aur zyada robust banao

## 🎤 Interview Questions (Final Day):
1. Virtual environment ka use kya hai aur yeh kyun important hai?
2. JSON kya hai aur yeh APIs mein kyun use hota hai?
3. `requests.get()` se API call karne ka basic flow explain karo.
4. Debugging ke liye kaunse tareeke use kar sakte ho?
5. Apne final project mein kaunse-kaunse OOP concepts use kiye, explain karo.
6. `json.dumps()` aur `json.dump()` mein kya farak hai? (Hint: string vs file)

## ✅ Day-End Checklist (Aur Poore 15 Din Ka):
- [ ] Virtual environment bana aur activate kar sakte ho
- [ ] JSON data ko read/write kar sakte ho
- [ ] Real API call karke response handle kar sakte ho
- [ ] Debugging ka basic approach aata hai
- [ ] Final project independently samajh kar likha/modify kiya
- [ ] Ab main khud se ek naya Python program **bina reference dekhe** plan aur likh sakta hoon

## ⏱️ Suggested Time:
Theory: 45 min | Final Project Building: 120 min | Testing/Debugging: 45 min | Revision (poore 15 din ka): 30 min

---

# 🎓 Congratulations — 15 Days Complete!

Agar tumne yeh poora roadmap follow kiya hai — har din ka code khud likha hai, challenges khud solve kiye hain — to ab tum:
- Python ki **core language** confidently use kar sakte ho
- **Real logic building** aur problem solving kar sakte ho
- OOP se **structured, maintainable code** likh sakte ho
- Files, JSON, aur basic APIs ke saath kaam kar sakte ho
- Apne khud ke chhote-medium projects independently bana sakte ho

## 🚀 Next Steps (Day 16 Onwards):
1. **Regular Expressions (regex)** 🔥 — text pattern matching ke liye
2. **Decorators & Closures (advanced)** 🔥 — clean, reusable code patterns
3. **Unit Testing (pytest)** 🔥 — professional developers ka must-have skill
4. **SQL + Python (databases)** ⭐ — real apps mein data permanently SQL databases mein store hota hai
5. **Web Framework (Flask ya Django ya FastAPI)** ⭐ — backend development ka agla natural step
6. **Git & GitHub** ⭐ — version control, agar abhi nahi seekha to turant seekho
7. **Multithreading/Async Programming** 💡 — performance-heavy applications ke liye

**Suggestion:** Ab **5-10 chhote projects** khud se socho aur bina kisi roadmap ke banao (e.g., Expense Tracker, Quiz App, Weather App using API, Password Generator) — yehi practice tumhe **truly independent Python developer** banayegi.

Good luck! 🐍🔥
