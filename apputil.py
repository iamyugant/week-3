import pandas as pd


url = (
    "https://github.com/melaniewalsh/Intro-Cultural-Analytics/"
    "raw/master/book/data/bellevue_almshouse_modified.csv"
)

df_bellevue = pd.read_csv(url)
# df_bellevue = pd.read_csv("./data/.../mydata.csv")


def fibonacci(n):
    """Return the nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def to_binary(n):
    """Convert an integer to its binary representation as a string."""
    if n == 0:
        return "0"

    bits = []
    while n:
        bits.append(str(n % 2))
        n //= 2

    return "".join(reversed(bits))



def task_1():
    df = df_bellevue.copy()

    print(
        "Cleaning gender column: normalizing values and "
        "treating blanks as missing."
    )

     # Clean gender without changing the overall missing-count ordering
    df["gender"] = (
    df["gender"]
    .astype("string")
    .str.strip()
    .str.lower()
    .replace({"": pd.NA, "m": "male", "w": "female"})
)

    df.loc[~df["gender"].isin(["male", "female"]), "gender"] = pd.NA

    missing_counts = df.isna().sum()
    sorted_columns = missing_counts.sort_values().index.tolist()

    # print("first_name counts (including missing):")
    # print(df["first_name"].astype("string").value_counts(dropna=False))

    # print("\ngender counts (including missing):")
    # print(df["gender"].astype("string").value_counts(dropna=False))
    return sorted_columns

def task_2():
    df = df_bellevue.copy()

    print(
        "Extracting year from date_in and dropping rows "
        "with invalid or missing dates."
    )

    df["date_in"] = pd.to_datetime(df["date_in"], errors="coerce")
    df = df.dropna(subset=["date_in"])
    df["year"] = df["date_in"].dt.year

    admissions_by_year = (
        df.groupby("year")
        .size()
        .reset_index(name="total_admissions")
    )

    return admissions_by_year


def task_3():
    df = df_bellevue.copy()

    print(
        "Cleaning gender column by standardizing historical labels "
        "(m, h → male; w, g → female) and removing invalid ages."
    )

    df["gender"] = (
        df["gender"]
        .astype(str)
        .str.strip()
        .str.lower()
        .replace(
            {
                "m": "male",
                "h": "male",
                "w": "female",
                "g": "female",
                "nan": pd.NA,
            }
        )
    )

    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    avg_age_by_gender = (
        df.dropna(subset=["gender", "age"])
        .groupby("gender")["age"]
        .mean()
    )

    return avg_age_by_gender


def task_4():
    df = df_bellevue.copy()

    print("Cleaning profession column: lowercasing and trimming whitespace.")

    df["profession"] = (
        df["profession"]
        .astype(str)
        .str.strip()
        .str.lower()
        .replace("nan", pd.NA)
    )

    top_professions = (
        df["profession"]
        .dropna()
        .value_counts()
        .head(5)
        .index
        .tolist()
    )

    return top_professions

print(fibonacci(9))
print(to_binary(2))
print(to_binary(12))
print(task_1())
print(task_2())
print(task_3())
print(task_4())