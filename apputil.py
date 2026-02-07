import seaborn as sns
import pandas as pd


# update/add code below ...

"""
Exercise 1
"""
def fibonacci(n):
    
    """
    Hard coding the output if n=0 or 1
    """

    if n<=1:
        return n

    """
    recursively computing the nth fibonacci number
    """

    while n>1:
        x= fibonacci(n-1) + fibonacci(n-2)
        return x

print(fibonacci(9))


"""
Exercise 2
"""
def to_binary(n):
    """
    Recursively convert a non-negative integer to its binary representation.
    """
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


print(to_binary(2))
print(to_binary(12)) 


"""
Exercise 3
"""

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)


def task_1():
    """
    Return a list of column names sorted by number of missing values
    (least missing to most missing).
    """
    df = df_bellevue.copy()

    """
    Fix known issue: inconsistent gender values treated as missing
    """
    print("Cleaning gender column: standardizing missing/invalid entries.")
    df["gender"] = df["gender"].replace(["", " ", "unknown", "Unknown"], pd.NA)

    missing_counts = df.isna().sum()
    sorted_columns = missing_counts.sort_values().index.tolist()

    return sorted_columns


def task_2():
    """
    Return a DataFrame with total admissions per year.
    """
    df = df_bellevue.copy()

    print("Extracting year from date_in column.")
    df["year"] = pd.to_datetime(df["date_in"], errors="coerce").dt.year

    print("Dropping rows with missing year values.")
    df = df.dropna(subset=["year"])

    admissions_per_year = (
        df.groupby("year")
        .size()
        .reset_index(name="total_admissions")
    )

    return admissions_per_year


def task_3():
    """
    Return a Series with average age by gender.
    """
    df = df_bellevue.copy()

    print("Removing rows with missing gender or age values.")
    df = df.dropna(subset=["gender", "age"])

    avg_age_by_gender = df.groupby("gender")["age"].mean()

    return avg_age_by_gender


def task_4():
    """
    Return a list of the five most common professions.
    """
    df = df_bellevue.copy()

    print("Dropping rows with missing profession values.")
    df = df.dropna(subset=["profession"])

    top_professions = (
        df["profession"]
        .value_counts()
        .head(5)
        .index
        .tolist()
    )

    return top_professions

print("\nExercise 3 Outputs")

print("\nTask 1:")
print(task_1())

print("\nTask 2:")
print(task_2())

print("\nTask 3:")
print(task_3())

print("\nTask 4:")
print(task_4())