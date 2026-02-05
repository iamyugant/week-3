import pandas as pd
import ssl

# Bypass SSL issues common on macOS
ssl._create_default_https_context = ssl._create_unverified_context


def fibonacci(n):
    """Return the nth number in the Fibonacci sequence using recursion."""
    if n <= 1:
        return n

    x = fibonacci(n - 1) + fibonacci(n - 2)
    return x


print(fibonacci(9))


def to_binary(n):
    """Convert a decimal integer to its binary representation using recursion."""
    if n <= 1:
        return n

    x = n % 2 + 10 * to_binary(n // 2)
    return x


print(to_binary(18))

# Define URL
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)


def task_1():
    """Return a list of column names sorted by count of missing values."""
    print("Issue: The 'gender' column uses 0/1 encoding; 0 is not missing.")
    missing_counts = df_bellevue.isnull().sum()
    sorted_cols = missing_counts.sort_values().index.tolist()

    print("\n--- Task 1 Output ---")
    print(sorted_cols)
    return sorted_cols


def task_2():
    """Return a DataFrame showing total admissions per year."""
    print("Issue: Dates are strings; using 'date_in' to extract year.")
    df_temp = df_bellevue.copy()
    df_temp['year'] = pd.to_datetime(df_temp['date_in']).dt.year
    admissions = df_temp.groupby('year').size().reset_index(name='total_admissions')

    print("\n--- Task 2 Output ---")
    print(admissions)
    return admissions

def task_3():
    """Return a Series of average ages grouped by gender."""
    print("Issue: Missing values in age are handled by pandas mean().")
    avg_ages = df_bellevue.groupby('gender')['age'].mean()

    print("\n--- Task 3 Output ---")
    print(avg_ages)
    return avg_ages


def task_4():
    """Return a list of the 5 most common professions."""
    print("Issue: Professions may have case/spelling inconsistencies.")
    top_5 = df_bellevue['profession'].value_counts().head(5).index.tolist()

    print("\n--- Task 4 Output ---")
    print(top_5)
    return top_5


# Calling the functions to trigger the prints
if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
