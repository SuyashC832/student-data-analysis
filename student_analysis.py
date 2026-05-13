"""
===========================================
   Student Data Analysis System
===========================================
"""

import pandas as pd

# ─────────────────────────────────────────
# 1. CREATE STUDENT DATAFRAME
# ─────────────────────────────────────────

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": [
        "Aarav Sharma", "Priya Verma", "Rohan Mehta", "Sneha Patel",
        "Karan Singh", "Divya Rao", "Arjun Nair", "Meera Joshi",
        "Vivek Gupta", "Pooja Iyer"
    ],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F"],
    "Class": ["10A", "10B", "10A", "10B", "10A", "10B", "10A", "10B", "10A", "10B"],
    "Math":    [88, 72, 95, 60, 78, 85, 91, 55, 70, 82],
    "Science": [76, 80, 90, 65, 70, 88, 85, 60, 74, 79],
    "English": [82, 68, 78, 72, 65, 92, 88, 58, 80, 76],
    "History": [70, 75, 85, 80, 60, 78, 72, 65, 68, 83],
    "Computer":[92, 78, 96, 70, 85, 80, 94, 62, 88, 75],
}

df = pd.DataFrame(data)

# Calculate Total and Percentage
subjects = ["Math", "Science", "English", "History", "Computer"]
df["Total"]      = df[subjects].sum(axis=1)
df["Percentage"] = (df["Total"] / 500 * 100).round(2)

# Grade assignment
def assign_grade(pct):
    if pct >= 90: return "A+"
    elif pct >= 80: return "A"
    elif pct >= 70: return "B"
    elif pct >= 60: return "C"
    else: return "D"

df["Grade"] = df["Percentage"].apply(assign_grade)

# ─────────────────────────────────────────
# 2. DISPLAY FULL DATAFRAME
# ─────────────────────────────────────────

print("=" * 75)
print("              STUDENT MARKS DATAFRAME")
print("=" * 75)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)
print(df.to_string(index=False))

# ─────────────────────────────────────────
# 3. OVERALL STATISTICS
# ─────────────────────────────────────────

print("\n" + "=" * 75)
print("              OVERALL SUBJECT-WISE STATISTICS")
print("=" * 75)

overall_stats = df[subjects].agg(["mean", "max", "min", "std"]).round(2)
overall_stats.index = ["Average", "Maximum", "Minimum", "Std Dev"]
print(overall_stats.to_string())

# ─────────────────────────────────────────
# 4. GROUP BY CLASS → AVG & MAX
# ─────────────────────────────────────────

print("\n" + "=" * 75)
print("              GROUPING BY CLASS — Average & Max Marks")
print("=" * 75)

class_group = df.groupby("Class")[subjects + ["Total", "Percentage"]]

print("\n📊 Average Marks per Class:")
print(class_group.mean().round(2).to_string())

print("\n🏆 Maximum Marks per Class:")
print(class_group.max().to_string())

# ─────────────────────────────────────────
# 5. GROUP BY GENDER → AVG & MAX
# ─────────────────────────────────────────

print("\n" + "=" * 75)
print("              GROUPING BY GENDER — Average & Max Marks")
print("=" * 75)

gender_group = df.groupby("Gender")[subjects + ["Total", "Percentage"]]

print("\n📊 Average Marks by Gender:")
print(gender_group.mean().round(2).to_string())

print("\n🏆 Maximum Marks by Gender:")
print(gender_group.max().to_string())

# ─────────────────────────────────────────
# 6. GROUP BY GRADE → COUNT, AVG PERCENTAGE
# ─────────────────────────────────────────

print("\n" + "=" * 75)
print("              GROUPING BY GRADE — Student Count & Avg %")
print("=" * 75)

grade_summary = df.groupby("Grade").agg(
    Student_Count=("Name", "count"),
    Avg_Percentage=("Percentage", "mean"),
    Max_Percentage=("Percentage", "max"),
    Min_Percentage=("Percentage", "min"),
).round(2).sort_values("Avg_Percentage", ascending=False)

print(grade_summary.to_string())

# ─────────────────────────────────────────
# 7. COMBINED AGGREGATION (CLASS + GENDER)
# ─────────────────────────────────────────

print("\n" + "=" * 75)
print("              MULTI-LEVEL GROUPING: Class + Gender — Avg & Max %")
print("=" * 75)

multi_group = df.groupby(["Class", "Gender"])["Percentage"].agg(
    Average="mean",
    Maximum="max"
).round(2)

print(multi_group.to_string())

# ─────────────────────────────────────────
# 8. TOP PERFORMER PER CLASS
# ─────────────────────────────────────────

print("\n" + "=" * 75)
print("              TOP PERFORMER PER CLASS")
print("=" * 75)

top_per_class = df.loc[df.groupby("Class")["Percentage"].idxmax(),
                       ["Class", "Name", "Total", "Percentage", "Grade"]]
print(top_per_class.to_string(index=False))

# ─────────────────────────────────────────
# 9. SUBJECT-WISE TOPPER
# ─────────────────────────────────────────

print("\n" + "=" * 75)
print("              SUBJECT-WISE TOPPER")
print("=" * 75)

for subject in subjects:
    idx = df[subject].idxmax()
    topper = df.loc[idx]
    print(f"  {subject:<10}: {topper['Name']:<20} — {topper[subject]} marks")

# ─────────────────────────────────────────
# 10. PASS / FAIL SUMMARY
# ─────────────────────────────────────────

print("\n" + "=" * 75)
print("              PASS / FAIL SUMMARY  (Pass ≥ 40 in every subject)")
print("=" * 75)

df["Result"] = df[subjects].apply(lambda row: "Pass" if (row >= 40).all() else "Fail", axis=1)
result_counts = df["Result"].value_counts()
print(result_counts.to_string())

print("\n" + "=" * 75)
print("  Analysis Complete ✓")
print("=" * 75)
