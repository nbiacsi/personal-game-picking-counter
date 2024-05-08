"""
    Author: Sloth
    Date: 3/5/2024
    Description: Script to append to a log file of who picked the game to play for the night. Get the total number of times you've picked in a row.
"""

# Imports.
from csv import reader
from datetime import date


# Gets user input and prints the result of how many times I picked in a row.
def main() -> None:
    FILE_PATH: str = r"C:\Users\nickb\OneDrive\Misc\Scripts\Picking Counter\Log.csv"
    name: str = input("Enter the person who picked today: ")
    game: str = input("Enter the game that was picked today: ")
    write_log(FILE_PATH, name, game)
    print(get_count(FILE_PATH, name))


# Writes data to log file.
def write_log(file_path: str, name: str, game: str) -> None:
    """
    Writes the name of the person who picked, the game, and today's date to a CSV sheet.

    Args:
        file_path (str): File path of CSV sheet.
        name (str): Name of the person who picked today.
        game (str): Name of the game that was picked today.

    Returns:
        None.
    """
    date_output: date = date.today().strftime("%m-%d")
    output = f"{name},{date_output},{game}"
    if name == "Nick":
        with open(file_path, "w") as file:
            file.write("Name,Date,Game\n")
            file.write(output)
            return

    with open(file_path, "a") as file:
        file.write(f"\n{output}")


# Function to format and output the log file. Also gets the number of times I picked in a row.
def get_count(file_path: str, name: str) -> str:
    """
    Gets the number of times you've picked in a row from the CSV sheet.

    Args:
        file_path (str): File path of the CSV sheet.
        name (str): Name of the person who just picked.

    Returns:
        A string stating the number of times the user has picked in a row.
    """
    return_string: str = "Number of times you've picked in a row: "
    with open(file_path, "r") as readFile:
        log: reader = reader(readFile)
        arr: list[str] = [row for row in log]
        arr.reverse()
        if not name == "Me":
            return return_string + str(0)

        for i in range(len(arr)):
            if arr[i][0] == "Me":
                continue

            return return_string + str(i)


if __name__ == "__main__":
    main()
