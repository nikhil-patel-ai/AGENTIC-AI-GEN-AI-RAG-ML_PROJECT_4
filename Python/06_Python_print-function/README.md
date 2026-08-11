<<<<<<< HEAD
# Python `print()` Function Examples

This notebook demonstrates how to use Python's built-in `print()` function for output and formatting. It covers basic printing, printing variables, string formatting, and special `print()` parameters like `end` and `sep`.

## Contents

1. Basic expressions and results
2. Printing variables
3. Printing multiple values in one call
4. Printing strings, numbers, and mixed values
5. Using `print()` with formatted messages
6. Using `.format()` and f-strings
7. Combining multiple print styles
8. Using `end` to control line endings
9. Using `sep` to control separators between items

## Notebook overview

### 1. Basic `print()` usage
The notebook first shows expressions like `4 + 8`, `8 - 6`, and `20 * 5` alone. In Python, expressions alone do not display output outside a notebook cell unless the result is the last expression.

Then it shows how `print()` displays the results:
```python
print(4 + 8)
print(8 - 6)
print(20 * 5)
```

### 2. Printing variables
The notebook defines variables and prints their values:
```python
a = 5
b = 8
print(a)
print(b)
```

It also shows printing multiple variables in a single call:
```python
print(a, b)
print(a, b, c)
```

### 3. Printing values and strings
`print()` can output several values separated by spaces by default:
```python
print(10)
print(10, 20)
print('python')
print(10, 20, 'python')
```

An empty `print()` adds a blank line:
```python
print()
```

### 4. Printing calculated results
The notebook shows how to print the result of arithmetic operations stored in variables:
```python
num1 = 50
num2 = 60
add = num1 + num2
print(add)
```

### 5. Print with descriptive string output
Using string literals with comma-separated values shows a readable sentence:
```python
print('The addition of', num1, 'and', num2, 'is=', add)
```

### 6. Using `.format()` for formatted output
The notebook introduces the `.format()` method for string formatting:
```python
print('The addition of {} and {} is= {}'.format(num1, num2, add))
```

It also demonstrates handling more values:
```python
print('The addition of {} and {} and {} and {} is= {}'.format(num1, num2, num3, num4, add))
```

Plus average formatting:
```python
avg1 = round((num1 + num2 + num3) / 3, 2)
print('The average of {}, {}, and {} is= {} or {}'.format(num1, num2, num3, avg, avg1))
```

### 7. Using f-strings
The notebook shows f-strings as a concise, modern formatting option:
```python
print(f'The addition of {num1} and {num2} is= {add}')
print(f'Hello my name is {name} and i am {age} year old from {city}')
```

### 8. Combining print styles
Example of printing the same result using plain `print()`, `.format()`, and f-strings:
```python
print('The addition of', num1, 'and', num2, 'is=', add)
print('The addition of {} and {} is= {}'.format(num1, num2, add))
print(f'The addition of {num1} and {num2} is= {add}')
```

### 9. Controlling line endings with `end`
The `end` parameter changes how `print()` ends the line. By default it is a newline `\n`.
```python
print('hello', end=' ')
print('world good day')
```

You can also use custom endings:
```python
print('hello', end=' ++++ ')
print('world good day')
```

### 10. Custom separators with `sep`
The `sep` parameter changes how items are separated within a single `print()` call:
```python
print('hello', 'hi', 'how are you', sep=' ---> ')
print('hello', 'hi', 'how are you', sep=' ***** ')
print('hello', 'hi', 'how are you', sep=' & ')
print('hello', 'hi', 'how are you', sep=' @ ')
```

Example of creating tighter output without spaces:
```python
print(1, 2, end=' ')
print(3, '.', sep='')
```

## Notes
- `print()` automatically separates arguments with a space unless `sep` is changed.
- `end` controls what is printed after the final item, so output can continue on the same line.
- f-strings are recommended for readability and simplicity in modern Python.
- `.format()` is a flexible alternative when you need placeholder-based formatting.

## Getting started
Open `print-function.ipynb` in Jupyter or VS Code notebook view to run each cell interactively and see the output examples.
=======
# Full Stack Data Science with Gen AI & Agentic AI

This repository contains my learning, notes, practice, and projects from my
**Full Stack Data Science with Gen AI & Agentic AI** course.

I am using this repository to learn concepts, practice them with code, and
keep my learning journey organized topic-wise.

---

## What Will I Learn?

This course covers different areas of Data Science, Machine Learning,
Artificial Intelligence, Generative AI, Agentic AI, and MLOps.

### Python
- Python Basics
- Variables and Data Types
- Operators
- Conditional Statements
- Loops
- Functions
- Lists, Tuples, Sets and Dictionaries
- List and Dictionary Comprehension
- Functions and Lambda
- Object-Oriented Programming
- Decorators
- Iterators and Generators
- Exception Handling
- File Handling
- Modules and Packages
- Regular Expressions
- Pickling and Unpickling

### Data Analysis
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy
- Statsmodels
- Exploratory Data Analysis (EDA)
- Data Cleaning and Data Visualization

### Mathematics & Statistics
- Probability
- Distributions
- Linear Algebra
- Calculus
- Descriptive Statistics
- Inferential Statistics
- Correlation and Regression
- Hypothesis Testing
- ANOVA
- Chi-Square Test
- Bias and Variance
- Other statistical concepts used in Machine Learning

### SQL & Databases
- DBMS and RDBMS
- SQL
- MySQL
- SQL Commands
- CRUD Operations
- Constraints
- Joins
- SQL Clauses
- Aggregate Functions
- SQL vs NoSQL

### Machine Learning
- Introduction to Machine Learning
- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning
- Data Preprocessing
- Feature Engineering
- Feature Selection
- Feature Scaling
- Dimensionality Reduction
- Regression
- Classification
- Clustering
- Ensemble Learning
- Recommendation Systems
- Time Series and Forecasting
- Model Evaluation
- Cross Validation
- Hyperparameter Tuning
- Scikit-learn

### Power BI
- Power BI Basics
- Reports and Visualizations
- Data Sources
- Power Query
- Data Transformation
- DAX
- Filters
- Slicers
- Hierarchies
- Dashboard and Report Creation

### Deep Learning
- Neural Networks
- Perceptron
- ANN
- Backpropagation
- Gradient Descent
- PyTorch
- TensorFlow
- Keras
- CNN
- RNN
- LSTM
- GRU
- Transformers
- Transfer Learning

The course also includes image processing and image classification.

### Natural Language Processing (NLP)
- Text Cleaning
- Tokenization
- Bag of Words
- TF-IDF
- N-Grams
- Word2Vec
- GloVe
- Text Classification
- Sentiment Analysis
- Topic Modelling
- Part-of-Speech Tagging
- Dependency Parsing
- Named Entity Recognition (NER)
- NLTK
- spaCy

### Computer Vision
- Image Processing
- CNN
- OpenCV
- Face Detection
- Object Detection
- Video Processing
- YOLO
- Image Classification

### Generative AI
- Introduction to Generative AI
- Generative AI Models
- Text Generation
- Image Generation
- Multimodal AI
- GANs
- VQGAN
- CLIP
- Autoencoders
- VAEs
- Stable Diffusion

The course includes hands-on work with text, image and multimodal models.

### LLMs
- Large Language Models
- Foundation Models
- Pre-trained vs Fine-tuned Models
- OpenAI
- Gemini
- LLaMA
- Claude
- Mistral / Mixtral
- DeepSeek
- Grok
- Hugging Face
- LangChain
- Whisper
- LLM Fine-tuning
- LoRA
- QLoRA

The course also covers deploying LLM-based applications and fine-tuning
models.

### Prompt Engineering
- Introduction to Prompt Engineering
- Prompt Structure
- Zero-Shot Prompting
- One-Shot Prompting
- Few-Shot Prompting
- Chain of Thought (CoT)
- Self-Consistency
- Role-Based Prompting
- RAG
- ReAct
- Dynamic Structured Prompting (DSP)
- LLM Settings and Configuration

The course also includes hands-on prompt experiments and AI application
building.

### Vector Databases & RAG
- Vector Databases
- Embeddings
- Similarity Search
- FAISS
- Pinecone
- ChromaDB
- Weaviate
- Milvus
- Qdrant
- Retrieval-Augmented Generation (RAG)
- AI Search Applications

The syllabus includes building RAG and search applications using vector
databases and LLMs.

### Agentic AI
- Introduction to Agentic AI
- Autonomous AI
- Single-Agent Systems
- Multi-Agent Systems
- AI Agent Memory
- Planning and Decision Making
- Tool Use
- Agent Communication
- CrewAI
- SmolAgent
- PhiData
- Agentic AI with LLMs
- AI Agent Deployment

The course includes hands-on work such as building single agents,
multi-agent research assistants and CrewAI workflows.

### MCP (Model Context Protocol)
- Introduction to MCP
- Need and Importance of MCP
- MCP Architecture
- MCP Host
- MCP Client
- MCP Server
- Data Flow and Communication
- Resources
- Tools
- Prompts
- MCP SDKs and Frameworks
- MCP with LLMs and AI Agents

### MLOps & Deployment
- MLOps
- DevOps vs MLOps
- ML Lifecycle
- Docker
- Model Packaging
- CI/CD
- GitHub Actions
- Jenkins
- MLflow
- Kubeflow
- Model Deployment
- Cloud Deployment

The course includes hands-on CI/CD and Docker-based ML deployment.

---

## Repository Structure

I am organizing this repository **topic-wise**.

Each topic has its own folder.

Inside each folder:

- `README.md` → My notes for that topic
- `.py` / `.ipynb` / other files → My practice and examples
- Project files → Projects related to that topic

For example:

```text
FSDS-with-Gen-AI-and-Agentic-AI/
│
├── Python/
│   ├── README.md
│   ├── variables.py
│   ├── data_types.py
│   ├── list.py
│   ├── tuple.py
│   └── set.py
│
├── NumPy/
│   ├── README.md
│   └── practice.py
│
├── Pandas/
│   ├── README.md
│   └── practice.py
│
├── Statistics/
│   ├── README.md
│   └── practice.py
│
├── SQL/
│   ├── README.md
│   └── queries.sql
│
├── Machine-Learning/
│   ├── README.md
│   └── practice.py
│
├── Deep-Learning/
│   ├── README.md
│   └── practice.py
│
├── NLP/
│   ├── README.md
│   └── practice.py
│
├── Computer-Vision/
│   ├── README.md
│   └── practice.py
│
├── Generative-AI/
│   ├── README.md
│   └── practice.py
│
├── LLM/
│   ├── README.md
│   └── practice.py
│
├── Prompt-Engineering/
│   ├── README.md
│   └── practice.py
│
├── Vector-Database/
│   ├── README.md
│   └── practice.py
│
├── Agentic-AI/
│   ├── README.md
│   └── practice.py
│
├── MCP/
│   ├── README.md
│   └── practice.py
│
└── MLOps/
    ├── README.md
    └── ...

```

## How I Use This Repository

For every topic I learn:

1. I understand the concept.
2. I write my notes in that topic's `README.md`.
3. I practice the concept using code.
4. I upload my practice to GitHub.
5. I update the notes whenever I learn something new.
6. I add projects as I build them.

### Example

If I am learning **Lists in Python**:

```text
Python/
└── Lists/
    ├── README.md
    └── list.py
```

`README.md` contains my **notes and explanation**.

`list.py` contains my **practice code**.

---

## Goal

The goal of this repository is to learn by **understanding, practicing, and building**, rather than only collecting notes.

This repository will also act as a record of my learning journey in:

**Data Science → Machine Learning → Deep Learning → Generative AI → LLMs → Agentic AI → MLOps**
>>>>>>> origin/main
