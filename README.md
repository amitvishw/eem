## Setup Instructions

### 1. Clone the repository

```bash
git https://github.com/amitvishw/eem.git
cd eem
```

### 2. Project Structure

```css
.
├── src
│ ├── Robot.py
│ ├── Mission.py
│ ├── Plateau.py
│ └── constants
│ └── constants.py
├── tests
│ └── test_ *.py
├── main.py
├── requirements.txt
└── README.md

```

### 3. Create and activate a Python 3.10 virtual environment

```bash
python3.10 -m venv venv
source venv/bin/activate
```

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 5. Run Main

```bash
python main.py
```

### 6. (Optional) Run Tests

```
python -m pytest tests/
```
