from tkinter import filedialog
import pandas as pd
import numpy as np
import os
import sys
pd.options.mode.chained_assignment = None
pd.set_option('display.max_rows', 1000)
b = 0
c = 0

AorW = input("If you would like to append to an existing file, please type 'a'. If you would like write a new file, "
             "please type 'w'.")
if AorW == "w":
    c = 1

if AorW == "a":
    c = 1

if c == 0:
    input("Please restart the program and enter a proper option...")
    sys.exit()
file_to_write = filedialog.askopenfilename()
with open(file_to_write) as FileToRemove:
    FileToRemove_Contents = FileToRemove.read()
    FileToRemove_Contents = str(FileToRemove_Contents)
    if FileToRemove_Contents.__contains__("Cloth Total:"):
        FileToRemove_Contents = FileToRemove_Contents.split("SHIPPING", 1)[1]
        FileToRemove_Contents = "SHIPPING" + FileToRemove_Contents
        df = pd.read_csv(file_to_write)

        file_name = os.path.basename(file_to_write)

        Partial_file_name = "Partial " + file_name
        file = open(Partial_file_name, "w")
        file.write(FileToRemove_Contents)
        file.close()

        with open(Partial_file_name) as Test:
            df = pd.read_csv(Partial_file_name)
            df.rename(columns={'SHIPPING ': 'SHIPPING MARKS'}, inplace=True)
            df.rename(columns={'BAR ': 'ITEM CODE'}, inplace=True)
            df.rename(columns={'COUNTRY ': 'Country of Origin'}, inplace=True)
            df.rename(columns={'ORIGIN  ': 'ORIGIN OF FABRIC'}, inplace=True)
            df.rename(columns={'Total Unit ': 'Sum of Total Unit Weight (kg)'}, inplace=True)
            df.rename(columns={'AMOUNT ': ' Sum of AMOUNT (USA $) '}, inplace=True)
            df.rename(columns={'STYLE #': 'STYLE#'}, inplace=True)
            df.rename(columns={'QTY': 'Sum of QTY'}, inplace=True)
            df.rename(columns={'P.O.#': 'P.O#'}, inplace=True)
            df.rename(columns={'COST': ' COST '}, inplace=True)
            df = df.drop(df.index[[0]])
            df = df.reset_index(drop=True)
            LastLine = df.loc[df['Weight '] == 'Cloth Total:']
            LastLine = str(LastLine.index.values)
            LastLine = LastLine.replace("[", "")
            LastLine = LastLine.replace("]", "")
            LastLine = int(LastLine)
            LastLine = LastLine - 1
            df = df.drop(df.index[LastLine:])
            df = df[['P.O#', 'ITEM CODE', 'H/S', 'STYLE#', 'DESCRIPTION', 'FABRIC CONTENT', 'Country of Origin',
                    'ORIGIN OF FABRIC', ' COST ',
                    'Sum of QTY', 'Sum of Total Unit Weight (kg)', ' Sum of AMOUNT (USA $) ']]
            new_file_name = "Partial " + file_name
            file = open(new_file_name, "w")
            df.to_csv(new_file_name, index=False)
            file.close()

    if FileToRemove_Contents.__contains__("Grand Total"):
        FileToRemove_Contents = FileToRemove_Contents.split("P.O#", 1)[1]
        FileToRemove_Contents = "P.O#" + FileToRemove_Contents
        FinalString = FileToRemove_Contents.split("Grand Total", 1)[0]

        file_name = os.path.basename(file_to_write)
        Partial_file_name = "Partial " + file_name
        file = open(Partial_file_name, "w")
        file.write(FinalString)
        file.close()
    if "Cloth Total:" not in FileToRemove_Contents:
        b += 1
    if "Grand Total" not in FileToRemove_Contents:
        b += 1
    if b == 2:
        input("Format Not Detected. Press Enter to continue...")
        sys.exit()

df = pd.read_csv(Partial_file_name)
df = df[['DESCRIPTION']]
different_values = (df.DESCRIPTION.unique())
amount_of_values = np.count_nonzero(different_values)
different_values = (df.DESCRIPTION.unique())
df = pd.DataFrame(different_values)
df = df.reindex(columns=np.append(df.columns.values,
                                  ['Dsc1']))
df = df.reset_index()
df['Part Code'] = df.index
df['Dsc1'] = different_values
df = df[['Part Code', 'Dsc1']]

if AorW == "a":
    Old_df = pd.read_csv("../../Resources/Part Codes.csv")
    sort = True
    df = Old_df.append(df)
    df = df[['Dsc1']]
    different_values = (df.Dsc1.unique())
    df = pd.DataFrame(different_values)
    df = df.reindex(columns=np.append(df.columns.values,
                                      ['Dsc1']))
    df = df.reset_index()
    df['Part Code'] = df.index
    df['Dsc1'] = different_values
    df = df[['Part Code', 'Dsc1']]

print(df)
new_file_name = "../../Resources/Part Codes.csv"
file = new_file_name
file = open(new_file_name, "a")
df.to_csv(new_file_name, index=False)
file.close()
os.remove(Partial_file_name)
input("Process complete. Press Enter to continue...")