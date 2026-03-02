# 🐍 Ultimate Python OOP Mastery Course

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Level-Intermediate-FF6B6B?style=for-the-badge" alt="Level">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Duration-8h-yellow?style=for-the-badge" alt="Duration">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Exercises-5-green?style=for-the-badge&logo=check" alt="Exercises">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License">
  </a>
</p>

---

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGl4aWR6Nnl6Z3BtcW1yYnJ4aGR6Y3BtcW1yYnJ4aGR6eGl4aWR6Nnl6ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4FGuhL4U2WyjdkaY/giphy.gif" width="300" alt="Python Programming GIF"/>
</p>

---

## 📑 Table of Contents

1. [🏠 Home](#home)
2. [🎯 Objectives](#objectives)
3. [💻 Environment](#environment)
4. [📂 Structure](#structure)
5. [📖 Methodology](#methodology)
6. [🧠 OOP Theory](#oop-theory)
7. [📝 Exercises](#exercises)
8. [▶️ Run Code](#run-code)
9. [📊 Results](#results)
10. [💡 Reference](#reference)
11. [🎬 Videos](#videos)
12. [❓ Help](#help)
13. [📚 Resources](#resources)

---

## 🏠 Home

### Welcome Banner

```mermaid
flowchart TB
    subgraph Banner[🐍 WELCOME TO PYTHON OOP MASTER COURSE!]
        direction TB
        Title["🎓 Master Object-Oriented Programming<br/>from Beginner to Expert"]:::title
        Learn["✨ What you'll learn:"]:::subtitle
        L1["✓ Classes & Objects creation"]:::item
        L2["✓ Encapsulation & Data Protection"]:::item
        L3["✓ Inheritance & Code Reuse"]:::item
        L4["✓ Polymorphism & Operator Overloading"]:::item
        L5["✓ Multiple Inheritance & MRO"]:::item
        L6["✓ Complete Project Architecture"]:::item
        
        Learn --> L1
        Learn --> L2
        Learn --> L3
        Learn --> L4
        Learn --> L5
        Learn --> L6
    end
    
    style Banner fill:#1a237e,color:#fff
    style Title fill:#7c4dff,color:#fff,font-size:20px
    style Learn fill:#7c4dff,color:#fff,font-size:16px
    style L1 fill:#00e676,color:#000
    style L2 fill:#00e676,color:#000
    style L3 fill:#00e676,color:#000
    style L4 fill:#00e676,color:#000
    style L5 fill:#00e676,color:#000
    style L6 fill:#00e676,color:#000
```

### Course Flow

```mermaid
flowchart TB
    subgraph Course[📚 Course Journey]
        direction LR
        E1[🏦 Exercise 1<br/>Encapsulation] --> E2[➗ Exercise 2<br/>Operators]
        E2 --> E3[🎓 Exercise 3<br/>Inheritance]
        E3 --> E4[🚗 Exercise 4<br/>Multi-Inherit]
        E4 --> EP[📚 Final Project<br/>Library]
    end
    
    style Course fill:#1a237e,color:#fff
    style E1 fill:#4caf50,color:#fff
    style E2 fill:#2196f3,color:#fff
    style E3 fill:#9c27b0,color:#fff
    style E4 fill:#ff5722,color:#fff
    style EP fill:#f44336,color:#fff
```

---

## 🎯 Objectives

### Learning Goals Mind Map

```mermaid
mindmap
  root((🎯 OBJECTIVES))
    Master Class Design
      Create classes
      Define constructors
      Object instantiation
    Encapsulation
      Data protection
      Private attributes
      Public methods
    Inheritance
      Single inheritance
      Multiple inheritance
      super() usage
    Polymorphism
      Operator overloading
      Dunder methods
      Method overriding
    Build Projects
      Architecture design
      Complete systems
      Best practices
```

---

## 💻 Environment

### System Requirements

```mermaid
graph LR
    subgraph Req[🖥️ System Requirements]
        R1[📋 Component] --> R2[📋 Minimum]
        R2 --> R3[⚡ Recommended]
    end
    
    style Req fill:#263238,color:#fff
```

| 🖥️ Component | 📋 Minimum | ⚡ Recommended |
|--------------|------------|----------------|
| **Python** | 3.8 | 3.12+ |
| **RAM** | 4 GB | 8 GB |
| **Storage** | 1 GB | 5 GB |
| **OS** | Windows/Mac/Linux | Win 11/Mac/Ubuntu |

---

## 📂 Structure

### Project Files Tree

```mermaid
graph TD
    subgraph Structure[📂 Project Structure]
        Root[📦 Python-Practical-Works/] --> Readme[📄 README.md]
        Root --> Ex1[📄 Exercise 1.py]
        Root --> Ex2[📄 Exercise 2.py]
        Root --> Ex3[📄 Exercise 3.py]
        Root --> Ex4[📄 Exercise 4.py]
        Root --> Final[📄 Exercise .py]
        
        Ex1 --> Ex1Cont[🏦 Bank Account]
        Ex2 --> Ex2Cont[➗ Vector2D]
        Ex3 --> Ex3Cont[🎓 School System]
        Ex4 --> Ex4Cont[🚗 Vehicles]
        Final --> FinalCont[📚 Library]
    end
    
    style Root fill:#1a237e,color:#fff
    style Readme fill:#4caf50,color:#fff
    style Ex1 fill:#2196f3,color:#fff
    style Ex2 fill:#9c27b0,color:#fff
    style Ex3 fill:#ff9800,color:#fff
    style Ex4 fill:#e91e63,color:#fff
    style Final fill:#f44336,color:#fff
```

---

## 📖 Methodology

### 6-Step Learning System

```mermaid
flowchart TD
    subgraph Steps[📖 Learning Steps]
        Step1[📚 STEP 1<br/>Read Theory]:::step
        Step2[👀 STEP 2<br/>Analyze Code]:::step
        Step3[▶️ STEP 3<br/>Run Code]:::step
        Step4[🔧 STEP 4<br/>Experiment]:::step
        Step5[💻 STEP 5<br/>Solve Alone]:::step
        Step6[📝 STEP 6<br/>Review]:::step
        
        Step1 --> Step2 --> Step3 --> Step4 --> Step5 --> Step6
    end
    
    classDef step fill:#00acc1,color:#fff,rx:10,ry:10
    
    style Steps fill:#263238,color:#fff
```

### Time Distribution

```mermaid
pie title ⏱️ Time Distribution (450 min total)
    "📚 Theory Reading (135 min)" : 135
    "💻 Practice Coding (255 min)" : 255
    "📝 Review & Debug (60 min)" : 60
```

---

## 🧠 OOP Theory

### The 4 Pillars of OOP

```mermaid
flowchart TB
    OOP[🤖 OBJECT-ORIENTED<br/>PROGRAMMING]:::title
    
    P1[🔒 ENCAPSULATION]:::pillar
    P2[👨‍👩‍👧 INHERITANCE]:::pillar
    P3[🔄 POLYMORPHISM]:::pillar
    P4[🎭 ABSTRACTION]:::pillar
    
    OOP --> P1
    OOP --> P2
    OOP --> P3
    OOP --> P4
    
    P1 --> D1[✓ Data Protection<br/>✓ Bundle Data+Methods<br/>✓ Access Control]
    P2 --> D2[✓ Code Reuse<br/>✓ Parent-Child<br/>✓ is-a Relationship]
    P3 --> D3[✓ Same Interface<br/>✓ Different Behavior<br/>✓ Flexibility]
    P4 --> D4[✓ Hide Complexity<br/>✓ Simple Interface<br/>✓ Clean Design]
    
    classDef title fill:#673ab7,color:#fff,font-size:24px
    classDef pillar fill:#009688,color:#fff,font-size:18px,rx:10,ry:10
```

---

## 📝 Exercises

### Exercise 1: Bank Account 🏦

**Level**: ⭐ Beginner | **Focus**: Encapsulation

```mermaid
classDiagram
    class BankAccount {
        +holder: str
        -_bank: str
        --balance: float
        +__init__(holder, balance)
        +deposit(amount)
        +withdraw(amount): bool
        +get_balance(): float
    }
```

---

### Exercise 2: Vector2D ➗

**Level**: ⭐⭐ Intermediate | **Focus**: Operator Overloading

```mermaid
classDiagram
    class Vector2D {
        +x: float
        +y: float
        +__init__(x, y)
        +__add__(other)
        +__sub__(other)
        +__mul__(scalar)
        +__eq__(other)
        +norm()
    }
```

### Operators Reference

```mermaid
graph LR
    Op1["__add__"] --> Plus["+"] --> Ex1["v1 + v2"]
    Op2["__sub__"] --> Minus["-"] --> Ex2["v1 - v2"]
    Op3["__mul__"] --> Star["*"] --> Ex3["v1 * 3"]
    Op4["__eq__"] --> Equal["=="] --> Ex4["v1 == v2"]
    
    style Op1 fill:#e3f2fd
    style Op2 fill:#e3f2fd
    style Op3 fill:#e3f2fd
    style Op4 fill:#e3f2fd
```

---

### Exercise 3: School System 🎓

**Level**: ⭐⭐ Intermediate | **Focus**: Inheritance

```mermaid
classDiagram
    class Person {
        +last_name: str
        +first_name: str
        +age: int
        +identity()
    }
    
    class Student {
        +major: str
        +study()
    }
    
    class Teacher {
        +subject: str
        +teach()
    }
    
    Person <|-- Student
    Person <|-- Teacher
```

---

### Exercise 4: Vehicles 🚗

**Level**: ⭐⭐⭐ Advanced | **Focus**: Multiple Inheritance

```mermaid
classDiagram
    class Vehicle {
        +brand: str
        +max_speed: int
    }
    
    class ElectricVehicle {
        +range_km: int
    }
    
    class ConnectedVehicle {
        +os_system: str
    }
    
    class ConnectedElectricCar {
    }
    
    Vehicle <|-- ElectricVehicle
    Vehicle <|-- ConnectedVehicle
    ElectricVehicle <|-- ConnectedElectricCar
    ConnectedVehicle <|-- ConnectedElectricCar
```

### MRO Visualization

```mermaid
flowchart LR
    A[ConnectedElectricCar] --> B[ElectricVehicle]
    B --> C[ConnectedVehicle]
    C --> D[Vehicle]
    D --> E[object]
    
    style A fill:#ffcdd2
    style B fill:#ffcdd2
    style C fill:#ffcdd2
    style D fill:#ffcdd2
    style E fill:#ffcdd2
```

---

### Final Project: Library 📚

**Level**: ⭐⭐⭐⭐ Expert | **Focus**: Complete System

```mermaid
classDiagram
    class Document {
        +title: str
        +author: str
        +year: int
    }
    
    class Book {
        +isbn: str
        +pages: int
    }
    
    class ScientificArticle {
        +journal: str
        +doi: str
    }
    
    class Library {
        +name: str
        +documents: list
        +add()
        +search()
    }
    
    Document <|-- Book
    Document <|-- ScientificArticle
    Library --> "*" Document
```

---

## ▶️ Run Code

### Quick Commands

```mermaid
flowchart TD
    subgraph Commands[💻 How to Run]
        C1[cd Python-Practical-Works] --> C2[python Exercise1.py]
    end
    
    style Commands fill:#263238,color:#fff
```

```bash
# 🪟 Windows / 🍎 macOS / 🐧 Linux
cd Python-Practical-Works
python Exercise1.py
python Exercise2.py
python Exercise3.py
python Exercise4.py
python "Exercise .py"
```

---

## 📊 Results

### Expected Outputs

#### 🏦 Exercise 1 Output

```mermaid
flowchart TB
    subgraph Output[💰 BANK ACCOUNT OUTPUT]
        O1[Account created: Account of Yasmine]:::output
        O2[Balance: 5000 MAD]:::output
        O3[Deposit: +2000 MAD]:::output
        O4[Balance: 7000 MAD]:::output
        O5[Withdrawal: -1000 MAD]:::output
        O6[Final Balance: 6000 MAD]:::output
    end
    
    style Output fill:#1b5e20,color:#fff
    style O1 fill:#4caf50,color:#fff
    style O2 fill:#4caf50,color:#fff
    style O3 fill:#4caf50,color:#fff
    style O4 fill:#4caf50,color:#fff
    style O5 fill:#4caf50,color:#fff
    style O6 fill:#4caf50,color:#fff
```

---

## 💡 Reference

### Quick Reference Mind Map

```mermaid
mindmap
  root((💡 KEY CONCEPTS))
    Naming Conventions
      public name
      protected _name
      private __name
    Dunder Methods
      __init__
      __str__
      __add__
    Inheritance
      super()
      isinstance()
      __mro__
```

---

## 🎬 Videos

### Tutorial Videos

```mermaid
graph TD
    V[🎬 Video Tutorials] --> V1[Corey Schafer]
    V --> V2[Mosh Hamidai]
    V --> V3[Tech With Tim]
    V --> V4[ArjanCodes]
    
    V1 --> D1["Python OOP (45 min)"]
    V2 --> D2["Classes (20 min)"]
    V3 --> D3["Inheritance (25 min)"]
    V4 --> D4["MRO (30 min)"]
    
    style V fill:#e53935,color:#fff
    style V1 fill:#1e88e5,color:#fff
    style V2 fill:#43a047,color:#fff
    style V3 fill:#fb8c00,color:#fff
    style V4 fill:#8e24aa,color:#fff
```

| 📺 Topic | 🔗 Link |
|----------|---------|
| OOP Basics | [Watch](https://www.youtube.com/watch?v=apACNr7DC_s) |
| Classes | [Watch](https://www.youtube.com/watch?v=8ok8hJ7D2sE) |
| Inheritance | [Watch](https://www.youtube.com/watch?v=RSl87lqOXDE) |
| MRO | [Watch](https://www.youtube.com/watch?v=0sD3M7EuzE4) |

---

## ❓ Help

### FAQ Flowchart

```mermaid
flowchart TD
    Q[❓ FAQ] --> Q1{"_ vs __ ?"}
    Q --> Q2{"When inherit?"}
    Q --> Q3{"What is MRO?"}
    Q --> Q4{"Overload ops?"}
    
    Q1 --> A1["__ triggers<br/>name mangling"]
    Q2 --> A2["Use for 'is-a'<br/>relationships"]
    Q3 --> A3["Method lookup<br/>order"]
    Q4 --> A4["Yes! Use<br/>dunder methods"]
    
    style Q fill:#ff9800,color:#fff
    style Q1 fill:#ffc107
    style Q2 fill:#ffc107
    style Q3 fill:#ffc107
    style Q4 fill:#ffc107
```

---

## 📚 Resources

### Further Learning Resources

```mermaid
mindmap
  root((📚 MORE RESOURCES))
    Books
      Fluent Python
      Python Crash Course
      Clean Code
    Websites
      Real Python
      Official Docs
      W3Schools
    Practice
      LeetCode
      HackerRank
      Codewars
```

---

<p align="center">
  
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  
  🎉 THANK YOU FOR USING THIS COURSE! 🎉
  
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  
  <img src="https://komarev.com/ghpvc/?username=Lagmouchyoussef&repo=Python-Practical-Works&style=flat-square&color=green" alt="views"/>
  
</p>

---

<p align="center">
  <strong>🚀 Happy Coding! Build Something Amazing! 🚀</strong><br>
  <em>⭐ Star this repo if you found it helpful!</em>
</p>

---
