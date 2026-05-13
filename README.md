[README.md](https://github.com/user-attachments/files/27696796/README.md)
# 📊 Student Data Analysis System

A Python-based data analysis project that performs grouping and aggregation on student marks using **Pandas**.

---

## 📁 Project Structure

```
student-data-analysis/
│
├── student_analysis.py   # Main analysis script
└── README.md             # Project documentation
```

---

## 📌 Features

- ✅ Creates a structured student marks DataFrame
- ✅ Calculates Total, Percentage, and Grade for each student
- ✅ Subject-wise statistics — Average, Max, Min, Std Dev
- ✅ Grouping by **Class** → Average & Max marks
- ✅ Grouping by **Gender** → Average & Max marks
- ✅ Grouping by **Grade** → Student count & Avg percentage
- ✅ Multi-level grouping — Class + Gender combined
- ✅ Top performer per class
- ✅ Subject-wise topper
- ✅ Pass / Fail summary

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3.x | Programming language |
| Pandas | Data analysis & manipulation |

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/student-data-analysis.git
cd student-data-analysis
```

### 2. Install dependencies
```bash
pip install pandas
```

### 3. Run the script
```bash
python student_analysis.py
```

---

## 📊 Sample Output

```
STUDENT MARKS DATAFRAME
─────────────────────────────────────────────────────────────
 Student_ID   Name           Class  Math  Science  ...  Grade
       101    Aarav Sharma   10A     88     76     ...    A
       102    Priya Verma    10B     72     80     ...    B
       ...

GROUPING BY CLASS — Average & Max Marks
─────────────────────────────────────────────────────────────
Average:
  10A → 80.80%
  10B → 73.52%

TOP PERFORMER PER CLASS
─────────────────────────────────────────────────────────────
  10A → Rohan Mehta   — 444/500 (88.8%) — Grade A
  10B → Divya Rao     — 423/500 (84.6%) — Grade A
```

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
