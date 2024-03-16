"""Name : Ved Lakkad
Enrollment No. : 2302031700019
ID : 8118
Phone number : 9974876307
Question : 3

IN THIS QUESTION I AM ASSUMING SQL SERVER KAAM KR RHE HEI"""

import pandas as pd
import json


# df generate krne ke liye
def generate_dataframe(n_students):

    columns = ["enrollment_number", "name", "gender", "email", "contact", "sem1"]
    for i in range(1, 9):
        columns.append(f"sem1_sub{i}_marks1")
    columns.extend(["spi", "cpi"])

    df = pd.DataFrame(columns=columns)

    return df


# data input lene ke liye
def input_data(df, n_students):

    for i in range(n_students):
        print(f"\nStudent {i + 1}:")
        for col in df.columns[:5]:
            while True:
                try:
                    df.loc[i, col] = input(f"Enter {col}: ")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid value.")

        for col in df.columns[5:14]:  # sem1_sub1_marks1 se sem1_sub8_marks1
            while True:
                try:
                    value = input(f"Enter {col}: ")
                    if col in ["spi", "cpi"]:
                        df.loc[i, col] = float(value)
                    else:
                        df.loc[i, col] = int(value)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid numeric value.")


# json mei save krne ke liye
def save_to_json(df, filename):

    df_copy = df.copy()
    df_copy.set_index("sem1", inplace=True)  # set multi-index for 'sem1' column
    df_copy.to_json(filename, orient="index")


# json se extract krne ke liye
def fetch_from_json_to_csv(filename):

    with open(filename, "r") as f:
        data = json.load(f)

    df = pd.DataFrame.from_dict(data, orient="index")  # df restore krne ke liye
    df.to_csv(filename.replace(".json", ".csv"), index=False)


def fetch_from_csv_to_database(csv_filename, database_name, table_name):

    # df ko replace krna hei connection details ke saath
    engine = None

    # dynamically tables create krne hei
    if not engine.execute(f"SHOW TABLES LIKE '{table_name}'").fetchone():
        engine.execute(f"CREATE TABLE {table_name} ({ ', '.join(df.columns) })")

    # data import krna hei
    df = pd.read_csv(csv_filename)
    df.to_sql(table_name, engine, index=False, if_exists="append")


def main():

    n_students = int(input("Enter the number of students: "))

    # df generate
    df = generate_dataframe(n_students)

    # data input
    input_data(df, n_students)

    # save to JSON
    save_to_json(df, "file.json")

    # fetch from JSON
    fetch_from_json_to_csv("file.json")


if __name__ == "__main__":
    main()
