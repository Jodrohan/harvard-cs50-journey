# CS50P Week 8 – OOP Quick Revision Notes

## 1. Why OOP?
- Tuples → Immutable
- Lists → Mutable but index-based
- Dictionaries → Better with keys, but no validation
- **Classes** → Create your own data types with data + behavior.

---

## 2. Class & Object
- **Class** = Blueprint
- **Object** = Instance of a class

```python
class Student:
    pass

student = Student()
```

---

## 3. Constructor (`__init__`)
- Runs automatically when an object is created.
- Initializes attributes.
- `self` refers to the current object.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

## 4. `self`
- Represents the current object.
- Required as the first parameter of instance methods.

```python
student.name
```

---

## 5. `__str__`
- Controls how an object is displayed with `print()`.

```python
def __str__(self):
    return f"{self.name}"
```

---

## 6. Properties (`@property`)
Used to protect data and validate values.

```python
@property
def name(self):
    return self._name
```

Setter:

```python
@name.setter
def name(self, value):
    if not value:
        raise ValueError
    self._name = value
```

Remember:
- Getter → Read value
- Setter → Validate before changing

---

## 7. Class Variables
Shared by every object.

```python
class Student:
    houses = ["Gryffindor", "Ravenclaw"]
```

---

## 8. Class Methods (`@classmethod`)
- Works on the class (`cls`)
- Often used as an alternative constructor.

```python
@classmethod
def get(cls):
    return cls(name, house)
```

---

## 9. Static Methods (`@staticmethod`)
- Doesn't use `self` or `cls`
- Utility/helper function inside the class.

```python
@staticmethod
def generate_id():
    return 1234
```

---

## 10. Inheritance
Reuse code from another class.

```python
class Wizard:
    pass

class Student(Wizard):
    pass
```

Use:

```python
super().__init__(...)
```

to call the parent constructor.

---

## 11. Operator Overloading
Customize Python operators using dunder methods.

Common methods:

- `__str__` → `print(obj)`
- `__init__` → object creation
- `__add__` → `+`
- `__eq__` → `==`

Example:

```python
total = vault1 + vault2
```

calls

```python
vault1.__add__(vault2)
```

---

# Must Remember ⭐

- Class = Blueprint
- Object = Instance
- `self` = Current object
- `__init__` = Constructor
- `__str__` = String representation
- `@property` = Getter
- `@setter` = Validation
- `@classmethod` = Uses `cls`
- `@staticmethod` = Uses neither `self` nor `cls`
- `super()` = Call parent class
- Inheritance = Reuse code
- Dunder methods = Customize Python behavior (`__init__`, `__str__`, `__add__`, etc.)