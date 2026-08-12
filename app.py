from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "interview_question_designer"

# ============================================================
# QUESTION BANK
# ============================================================

QUESTION_BANK = {

    # ========================================================
    # PYTHON DEVELOPER
    # ========================================================

    "Python Developer": [

        {
            "question": "Explain Python Lists.",
            "answer": "Python lists are ordered, mutable collections that can store elements of different data types. They support indexing, slicing, appending, inserting, deleting, and updating elements.",
            "indicator": "Ordered, Mutable, Indexing, Slicing"
        },

        {
            "question": "Difference between List and Tuple?",
            "answer": "Lists are mutable, while tuples are immutable. Lists consume slightly more memory but allow modifications. Tuples are faster and are ideal for fixed collections of data.",
            "indicator": "Mutable, Immutable, Memory, Performance"
        },

        {
            "question": "What is Object-Oriented Programming (OOP)?",
            "answer": "OOP is a programming paradigm based on objects. The four main principles are Encapsulation, Inheritance, Polymorphism, and Abstraction.",
            "indicator": "Encapsulation, Inheritance, Polymorphism, Abstraction"
        },

        {
            "question": "Explain Exception Handling in Python.",
            "answer": "Exception handling prevents program crashes by handling runtime errors using try, except, else, finally, and raise blocks.",
            "indicator": "try, except, finally, raise"
        },

        {
            "question": "What are Python Decorators?",
            "answer": "Decorators are functions that modify the behavior of another function without changing its original source code. They are written using the @ symbol.",
            "indicator": "@decorator, Wrapper Function"
        },

        {
            "question": "What are Generators?",
            "answer": "Generators are functions that use the yield keyword to produce values one at a time instead of returning all values at once, making them memory efficient.",
            "indicator": "yield, Memory Efficient"
        },

        {
            "question": "Difference between Multithreading and Multiprocessing?",
            "answer": "Multithreading runs multiple threads inside one process and is suitable for I/O-bound tasks. Multiprocessing runs separate processes and is better for CPU-intensive tasks.",
            "indicator": "CPU Bound, I/O Bound, GIL"
        },

        {
            "question": "What is a Lambda Function?",
            "answer": "A lambda function is an anonymous one-line function created using the lambda keyword.",
            "indicator": "Anonymous Function"
        },

        {
            "question": "What are Python Modules?",
            "answer": "Modules are Python files containing reusable functions, variables, and classes that can be imported into other programs.",
            "indicator": "Reusable Code, import"
        },

        {
            "question": "What is a Virtual Environment?",
            "answer": "A virtual environment is an isolated Python environment that allows projects to have separate dependencies without conflicts.",
            "indicator": "Dependency Isolation"
        }
    ],
        # ========================================================
    # JAVA DEVELOPER
    # ========================================================

    "Java Developer": [

        {
            "question": "What is JVM?",
            "answer": "The Java Virtual Machine (JVM) is responsible for executing Java bytecode. It provides platform independence by allowing Java programs to run on any operating system that has a JVM.",
            "indicator": "Bytecode, Platform Independent"
        },

        {
            "question": "Difference between JDK and JRE?",
            "answer": "JDK (Java Development Kit) contains tools required to develop Java applications, while JRE (Java Runtime Environment) contains only the libraries and JVM required to run Java applications.",
            "indicator": "Development, Runtime"
        },

        {
            "question": "Explain OOP Concepts.",
            "answer": "The four pillars of OOP are Encapsulation, Inheritance, Polymorphism, and Abstraction. These principles help in writing reusable and maintainable code.",
            "indicator": "Encapsulation, Inheritance, Polymorphism, Abstraction"
        },

        {
            "question": "Difference between Array and ArrayList?",
            "answer": "Arrays have a fixed size, while ArrayLists are dynamic and can grow or shrink automatically. ArrayLists belong to the Java Collections Framework.",
            "indicator": "Fixed Size, Dynamic"
        },

        {
            "question": "Explain Exception Handling.",
            "answer": "Exception handling allows a program to handle runtime errors gracefully using try, catch, finally, throw, and throws.",
            "indicator": "try, catch, finally"
        },

        {
            "question": "What is Multithreading?",
            "answer": "Multithreading allows multiple threads to execute concurrently within a program, improving responsiveness and performance.",
            "indicator": "Concurrent Execution"
        },

        {
            "question": "Difference between HashMap and Hashtable?",
            "answer": "HashMap is not synchronized and allows one null key, whereas Hashtable is synchronized and does not allow null keys or values.",
            "indicator": "Synchronization, Null Keys"
        },

        {
            "question": "What are Interfaces?",
            "answer": "Interfaces define a contract that implementing classes must follow. They support abstraction and multiple inheritance in Java.",
            "indicator": "Abstraction, Multiple Inheritance"
        },

        {
            "question": "What is Garbage Collection?",
            "answer": "Garbage Collection automatically removes unused objects from memory, preventing memory leaks and improving application performance.",
            "indicator": "Automatic Memory Management"
        },

        {
            "question": "Explain the Collections Framework.",
            "answer": "The Collections Framework provides ready-made classes and interfaces like List, Set, Queue, and Map for efficient data storage and manipulation.",
            "indicator": "List, Set, Queue, Map"
        }

    ],

    # ========================================================
    # WEB DEVELOPER
    # ========================================================

    "Web Developer": [

        {
            "question": "Difference between HTML and HTML5?",
            "answer": "HTML5 introduced semantic tags, multimedia support, local storage, canvas, and improved form controls compared to earlier HTML versions.",
            "indicator": "Semantic Tags, Multimedia"
        },

        {
            "question": "Difference between CSS and Bootstrap?",
            "answer": "CSS is used to style web pages, while Bootstrap is a CSS framework that provides pre-built responsive components.",
            "indicator": "Styling, Framework"
        },

        {
            "question": "Explain Flexbox.",
            "answer": "Flexbox is a CSS layout model that helps align and distribute space among elements efficiently in one dimension.",
            "indicator": "Layout, Alignment"
        },

        {
            "question": "Difference between GET and POST?",
            "answer": "GET sends data through the URL and is mainly used to retrieve data. POST sends data in the request body and is used for creating or updating resources.",
            "indicator": "URL, Request Body"
        },

        {
            "question": "What is the JavaScript DOM?",
            "answer": "The Document Object Model (DOM) represents an HTML page as a tree structure that JavaScript can access and manipulate dynamically.",
            "indicator": "Document Object Model"
        },

        {
            "question": "Difference between var, let, and const?",
            "answer": "var is function-scoped, let is block-scoped, and const is block-scoped with values that cannot be reassigned.",
            "indicator": "Scope, Reassignment"
        },

        {
            "question": "Explain Responsive Design.",
            "answer": "Responsive Design ensures websites adapt to different screen sizes using flexible layouts, media queries, and responsive units.",
            "indicator": "Media Queries, Mobile Friendly"
        },

        {
            "question": "What is REST API?",
            "answer": "A REST API is an architectural style that allows communication between client and server using HTTP methods like GET, POST, PUT, and DELETE.",
            "indicator": "HTTP Methods"
        },

        {
            "question": "Difference between SQL and NoSQL?",
            "answer": "SQL databases store structured relational data, whereas NoSQL databases store flexible, non-relational data such as documents and key-value pairs.",
            "indicator": "Relational, Non-Relational"
        },

        {
            "question": "Explain Sessions and Cookies.",
            "answer": "Cookies store small pieces of data in the browser, while sessions store user data securely on the server during a user's interaction.",
            "indicator": "Client Storage, Server Storage"
        }

    ],
        # ========================================================
    # DATA ANALYST
    # ========================================================

    "Data Analyst": [

        {
            "question": "What is Data Cleaning?",
            "answer": "Data cleaning is the process of identifying and correcting inaccurate, incomplete, duplicate, or inconsistent data before analysis.",
            "indicator": "Missing Values, Duplicates, Data Quality"
        },

        {
            "question": "Difference between INNER JOIN and LEFT JOIN?",
            "answer": "INNER JOIN returns only matching records from both tables, whereas LEFT JOIN returns all records from the left table and matching records from the right table.",
            "indicator": "Matching Records, Left Table"
        },

        {
            "question": "Explain GROUP BY in SQL.",
            "answer": "GROUP BY groups rows having the same values so aggregate functions like COUNT(), SUM(), AVG(), MAX(), and MIN() can be applied.",
            "indicator": "Aggregation, COUNT, SUM"
        },

        {
            "question": "Difference between Mean and Median?",
            "answer": "Mean is the average of all values, while Median is the middle value after sorting. Median is less affected by outliers.",
            "indicator": "Average, Outliers"
        },

        {
            "question": "What is Normalization?",
            "answer": "Normalization is the process of organizing database tables to reduce redundancy and improve data integrity.",
            "indicator": "Reduce Redundancy, Database Design"
        },

        {
            "question": "What is a Primary Key?",
            "answer": "A Primary Key uniquely identifies each record in a table. It cannot contain NULL values and must be unique.",
            "indicator": "Unique, Not Null"
        },

        {
            "question": "What is Power BI?",
            "answer": "Power BI is Microsoft's Business Intelligence tool used to visualize data, create dashboards, and generate interactive reports.",
            "indicator": "Dashboards, Visualization"
        },

        {
            "question": "Difference between Structured and Unstructured Data?",
            "answer": "Structured data follows a predefined format such as tables in databases, whereas unstructured data includes images, videos, emails, and documents.",
            "indicator": "Database, Images, Text"
        },

        {
            "question": "Explain Data Visualization.",
            "answer": "Data visualization is the graphical representation of information using charts, graphs, maps, and dashboards to help understand trends and patterns.",
            "indicator": "Charts, Graphs, Dashboards"
        },

        {
            "question": "What is SQL?",
            "answer": "SQL (Structured Query Language) is used to create, retrieve, update, delete, and manage relational databases.",
            "indicator": "Database, CRUD Operations"
        }

    ],

    # ========================================================
    # MACHINE LEARNING ENGINEER
    # ========================================================

    "Machine Learning Engineer": [

        {
            "question": "What is Machine Learning?",
            "answer": "Machine Learning is a branch of Artificial Intelligence that enables computers to learn patterns from data and make predictions without being explicitly programmed.",
            "indicator": "Learning from Data, Prediction"
        },

        {
            "question": "Difference between AI and ML?",
            "answer": "Artificial Intelligence is the broader concept of creating intelligent systems, while Machine Learning is a subset of AI that learns from data.",
            "indicator": "Subset Relationship"
        },

        {
            "question": "Explain Supervised Learning.",
            "answer": "Supervised Learning uses labeled data to train models that can predict outputs for unseen inputs.",
            "indicator": "Labeled Data"
        },

        {
            "question": "Explain Unsupervised Learning.",
            "answer": "Unsupervised Learning finds hidden patterns and relationships in unlabeled data using clustering and dimensionality reduction techniques.",
            "indicator": "Clustering, Unlabeled Data"
        },

        {
            "question": "What is Overfitting?",
            "answer": "Overfitting occurs when a model learns the training data too well, including noise, causing poor performance on new data.",
            "indicator": "Poor Generalization"
        },

        {
            "question": "Difference between Classification and Regression?",
            "answer": "Classification predicts discrete categories, whereas Regression predicts continuous numerical values.",
            "indicator": "Categorical, Numerical"
        },

        {
            "question": "Explain Decision Trees.",
            "answer": "Decision Trees are supervised learning algorithms that split data into branches based on feature values to make predictions.",
            "indicator": "Tree Structure, Splitting"
        },

        {
            "question": "What is Feature Engineering?",
            "answer": "Feature Engineering is the process of selecting, creating, and transforming features to improve machine learning model performance.",
            "indicator": "Feature Selection, Transformation"
        },

        {
            "question": "Explain Train-Test Split.",
            "answer": "The dataset is divided into training and testing sets. The training set builds the model, while the testing set evaluates its performance.",
            "indicator": "Model Evaluation"
        },

        {
            "question": "What is Cross Validation?",
            "answer": "Cross Validation evaluates a model by dividing the dataset into multiple folds and training/testing repeatedly to obtain reliable performance estimates.",
            "indicator": "K-Fold, Reliable Evaluation"
        }

    ]

}
# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# LOGIN PAGE
# ============================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Dummy Login
        if username and password:

            session["user"] = username

            return redirect(url_for("designer"))

    return render_template("login.html")


# ============================================================
# INTERVIEW QUESTION DESIGNER
# ============================================================

@app.route("/designer", methods=["GET", "POST"])
def designer():

    if "user" not in session:
        return redirect(url_for("login"))

    questions = []

    role = ""
    level = ""

    if request.method == "POST":

        role = request.form.get("role")
        level = request.form.get("level")

        if role in QUESTION_BANK:

            for i, item in enumerate(QUESTION_BANK[role], start=1):

                questions.append({

                    "number": i,

                    "question": item["question"],

                    "answer": item["answer"],

                    "indicator": item["indicator"],

                    "level": level

                })

    return render_template(

        "main.html",

        username=session["user"],

        questions=questions,

        role=role,

        level=level

    )


# ============================================================
# LOGOUT
# ============================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )