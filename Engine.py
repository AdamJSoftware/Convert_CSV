import pandas

pandas.set_option('display.max_columns', 20)

def main(input, output_path, configuration):
    df = pandas.read_csv(input)
    with open(configuration) as f:
        f = f.read()
        columnsToRemove, f = f.split("\n|||NEW&TABLE2|||")
        f = "|||NEW&TABLE2|||" + f
        df = columns_to_remove(columnsToRemove, df)
        df = df.reset_index(drop=True)
        columnsToRename, f = f.split("\n|||NEW&TABLE3|||")
        f = "|||NEW&TABLE3|||" + f
        df = columns_to_rename(columnsToRename, df)
        df = df.reset_index(drop=True)
        columnsToAdd, f = f.split("\n|||NEW&TABLE4|||")
        f = "|||NEW&TABLE4|||" + f
        df = columns_to_add(columnsToAdd, df)
        try:
            df = df.reset_index(drop=True)
        except:
            pass
        columnsToReorganize, f = f.split("\n|||NEW&TABLE5|||")
        f = "|||NEW&TABLE5|||" + f
        df = columns_to_reorganize(columnsToReorganize, df)
        try:
            df = df.reset_index()
        except:
            pass
        rowsToRemove, f = f.split("\n|||NEW&TABLE6|||")
        f = "|||NEW&TABLE6|||" + f
        df = rows_to_remove(rowsToRemove, df)
        try:
            df = df.reset_index()
        except:
            pass
        rowsToSwitch, f = f.split("\n|||NEW&TABLE7|||")
        f = "|||NEW&TABLE7|||" + f
        try:
            df = df.drop(['index'], axis=1)
            df = df.drop(['level_0'], axis=1)
        except:
            pass
        try:
            df = df.reset_index(drop=True)
        except:
            pass
        df = rows_to_switch(rowsToSwitch, df)
        try:
            df = df.reset_index(drop=True)
        except:
            pass
        print(df)
        output(df, output_path)


def columns_to_remove(input, df):
    input = input.split("|||NEW&TABLE1|||\n")[1]
    input = input.split("\n")
    j = 0
    for position, item in enumerate(input):
        if item == "|NEWCOLUMN|":
            column = input[position+1]
            j = 1
        else:
            if j == 0:
                if column != "":
                    if item == "":
                        df = df.drop([column], axis=1)
                    else:
                        dfToList = df[column].tolist()
                        if dfToList.__contains__(item):
                            df = df.drop(columns=[column])

            else:
                j = 0
    return df


def columns_to_rename(input, df):
    input = input.split("|||NEW&TABLE2|||\n")[1]
    input = input.split("\n")
    j = 0
    for position, item in enumerate(input):
        if item == "|NEWCOLUMN|":
            column = input[position + 1]
            j = 1
        else:
            if j == 0:
                if column != "":
                    if item == "":
                        pass
                    else:
                        df = df.rename({column: item}, axis=1)
            else:
                j = 0
    return df

def columns_to_add(input, df):
    input = input.split("|||NEW&TABLE3|||\n")[1]
    input = input.split("\n")
    j = 0
    for position, item in enumerate(input):
        if item == "|NEWCOLUMN|":
            column = input[position + 1]
            j = 1
        else:
            if j == 0:
                if column != "":
                    df.insert(0, column,item)
            else:
                j = 0
    return df

def columns_to_reorganize(input, df):
    input = input.split("|||NEW&TABLE4|||\n")[1]
    input = input.split("\n")
    j = 0
    for position, item in enumerate(input):
        if item == "|NEWCOLUMN|":
            column = input[position + 1]
            j = 1
        else:
            if j == 0:
                if column != "":
                    df.insert(0, column, item)
            else:
                j = 0
    return df

def rows_to_remove(input, df):
    input = input.split("|||NEW&TABLE5|||\n")[1]
    input = input.split("\n")
    j = 0
    for position, item in enumerate(input):
        if item == "|NEWCOLUMN|":
            column = input[position + 1]
            j = 1
        else:
            if j == 0:
                if column != "":
                    dfToList = df[column].tolist()
                    for index, obj in enumerate(dfToList):
                        if obj == item:
                            df = df.drop([index])
            else:
                j = 0
    return df

def rows_to_switch(input, df):
    input = input.split("|||NEW&TABLE6|||\n")[1]
    input = input.split("\n")
    j = 0
    for position, item in enumerate(input):
        if item == "|NEWCOLUMN|":
            column = input[position + 1]
            j = 1
        else:
            if j == 0:
                item1,item2 = item.split('==')
                print(item1)
                print(item2)
                if column != "":
                    dfToList = df[column].tolist()
                    print(dfToList)
                    for index, obj in enumerate(dfToList):
                        if obj == item1:
                            df.at[index, column] = item2
                            print(index)

            else:
                j = 0
    return df


def crop():
    pass


def output(df, output_path):
    try:
        # df = df.drop(['index'], axis=1)
        df = df.drop(['level_0'], axis=1)
    except:
        pass

    df.to_csv(output_path, index=False)

