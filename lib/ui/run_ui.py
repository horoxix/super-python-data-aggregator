import tkinter
from tkinter import filedialog
from lib.insert import import_from_csv_file


class Application(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.geometry("400x200")
        self.console_label = tkinter.StringVar()
        self.console_label2 = tkinter.StringVar()
        self.tableLabel = tkinter.StringVar()
        self.table_selection = tkinter.StringVar()
        self.db_type_label = tkinter.StringVar()
        self.db_type = tkinter.StringVar()
        self.grid()

        # Add button
        button = tkinter.Button(self, text=u"Add", command=self.add)
        button.grid(column=0, row=0, sticky='E')

        # View button
        button = tkinter.Button(self, text=u"View", command=self.view)
        button.grid(column=1, row=0, sticky='E')

        # Label for Console field
        self.tableLabel.set("Console:")
        label = tkinter.Label(self, textvariable=self.tableLabel, anchor="w")
        label.grid(column=0, row=5, sticky='W')

        # Output label
        label = tkinter.Label(self, textvariable=self.console_label, anchor="w", fg="white", bg="black")
        label.grid(column=0, row=6, columnspan=3, sticky='EW')

        # Label for FILE field
        self.tableLabel.set("File:")
        label = tkinter.Label(self, textvariable=self.tableLabel, anchor="w")
        label.grid(column=0, row=7, sticky='W')

        # Output label 2

        label2 = tkinter.Label(self, textvariable=self.console_label2, anchor="w", fg="white", bg="black")
        label2.grid(column=0, row=8, columnspan=3, sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        self.resizable(False, False)
        self.update()
        self.geometry(self.geometry())

        # Table Selection Field
        self.tableLabel.set("Table")
        label = tkinter.Label(self, textvariable=self.tableLabel, anchor="w")
        label.grid(column=0, row=4, sticky='W')
        option_list = ('call_statistics', 'NULL')
        self.table_selection.set(option_list[0])
        self.drop_down = tkinter.OptionMenu(self, self.table_selection, *option_list)
        self.drop_down.grid(column=0, row=4)

        # Database Type Selection Field
        self.db_type_label.set("Database Type")
        label = tkinter.Label(self, textvariable=self.db_type_label, anchor="w")
        label.grid(column=0, row=5, sticky='W')
        # db_type_label Drop Down
        db_option_list = ('MySQL', 'PostgreSQL')
        self.db_type.set(db_option_list[0])
        self.drop_down = tkinter.OptionMenu(self, self.db_type, *db_option_list)
        self.drop_down.grid(column=0, row=5)

        # Browse button to select csv file
        browse_button = tkinter.Button(self, text="Browse", command=self.browse_function)
        browse_button.grid(column=1, row=9, sticky='E')

    def initialize(self):
        pass

    def add(self):
        # Deletes single clump based on clumpID input
        self.console_label.set("Adding data")
        import_from_csv_file.insert_data_from_csv(self.browse_function(),
                                                  self.db_type.get(),
                                                  self.table_selection.get()
                                                  )

    def view(self):
        # Deletes single clump based on clumpID input
        self.console_label.set("viewing data from " + self.entryVariable.get())
        # Add functionality here.

    def browse_function(self):
        # Asks to select a file when the browse button is clicked.
        filename = filedialog.askopenfilename()
        if filename.endswith('.csv'):
            self.console_label2.set(filename)
            return filename
        else:
            self.console_label2.set("Please select a CSV file")


if __name__ == "__main__":
    app = Application(None)
    app.title('Result Aggregator')
    app.mainloop()






