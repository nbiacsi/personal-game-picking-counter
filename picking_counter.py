"""
    Author: Sloth
    Date: 6/26/2024
    Description: Python script to log who picks in a given day of playing games. It returns the number of times the user picked in a row.
"""

# TODO: Convert this script to a .exe self.application so that it can be run straight from the desktop instead of having to open VSCode to run this self.app.
# TODO: Push to GH.

from csv import reader
import customtkinter as ctk
from datetime import date


class GUI:
    """
    Creates a GUI that allows for user input for a name and a game picked and returns the number of times that you picked a game in a row.

    Args:
        file_path: str - Path of the log file for both entering data into and getting data from.

    Returns:
        None
    """

    def __init__(self, file_path: str) -> None:
        """
        Default constructor. Takes in a file path and creates the CustomTKinter app.

        Args:
            file_path: str - Path of the log file for both entering data into and getting data from.

        Returns:
            None
        """
        self.app: ctk.CTk = ctk.CTk()
        self.app.geometry("450x300")
        self.app.winfo_toplevel().title("Picking Games Counter")

        self.name_entry: ctk.CTkEntry = ctk.CTkEntry(
            master=self.app, placeholder_text="Person who picked today", width=250
        )
        self.name_entry.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.game_entry: ctk.CTkEntry = ctk.CTkEntry(
            master=self.app, placeholder_text="Game that was picked", width=250
        )
        self.game_entry.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        self.result_label: ctk.CTkLabel = ctk.CTkLabel(master=self.app, text=None)
        self.result_label.grid(row=3, column=1, padx=20, pady=20, sticky="nsew")

        self.file_path: str = file_path

        self.create_log_button: ctk.CTkButton = ctk.CTkButton(
            master=self.app,
            text="Generate Log Event",
            command=self._create_log_event,
            width=250,
        )
        self.create_log_button.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

        self.app.bind("<Return>", lambda e=None: self._create_log_event())

        name_label: ctk.CTkLabel = ctk.CTkLabel(master=self.app, text="Name")
        name_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        game_label: ctk.CTkLabel = ctk.CTkLabel(master=self.app, text="Game")
        game_label.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.app.mainloop()

    def _create_log_event(self) -> None:
        """
        Function that is called when pressing on the create_log_button. Creates a log event in the log sheet.

        Args:
            None.

        Returns:
            None.
        """
        self.name: str = self.name_entry.get().replace("\n", "")
        self.game: str = self.game_entry.get().replace("\n", "")
        self._write_log()
        self._set_count()

        self.app.after(0, self.create_log_button.destroy)

        # Sets a timeout for 5 seconds and then closes the self.app after.
        self.app.after(3000, self.app.destroy)

    def _set_count(self) -> None:
        """
        Function to set the text on the self.result_label of number of times that you picked in a row.

        Args:
            None.

        Returns:
            None.
        """
        pick: str = self._get_pick_times()
        self.result_label.configure(
            text=f"Number of times you've picked in a row: {pick}"
        )

    def _write_log(self) -> None:
        """
        Writes the name of the person who picked, the game, and today's date to a CSV sheet.

        Args:
            None.

        Returns:
            None.
        """
        date_output: date = date.today().strftime("%m-%d")
        output = f"{self.name},{date_output},{self.game}"
        if self.name == "Nick":
            with open(self.file_path, "w") as file:
                file.write("Name,Date,Game\n")
                file.write(output)
                return

        with open(self.file_path, "a") as file:
            file.write(f"\n{output}")

    def _get_pick_times(self) -> int:
        """
        Gets the number of times you've picked in a row from the CSV sheet.

        Args:
            None.

        Returns:
            A string stating the number of times the user has picked in a row.
        """
        with open(self.file_path, "r") as readFile:
            log: reader = reader(readFile)
            arr: list[str] = [row for row in log]
            arr.reverse()

        if not self.name == "Me":
            return 0

        for i in range(len(arr)):
            if arr[i][0] != "Me":
                return i


def main() -> None:
    file_path: str = r"D:\Misc\Scripts\Picking Counter\Log.csv"
    GUI(file_path)


if __name__ == "__main__":
    main()
