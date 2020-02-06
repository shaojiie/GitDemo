import os
import pandas as pd


HERE = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.abspath(os.path.join(HERE, '..', 'data'))


def make_df_from_excel(file_name, nrows):
    """Read from an Excel file in chunks and make a single DataFrame.

    Parameters
    ----------
    file_name : str
    nrows : int
        Number of rows to read at a time. These Excel files are too big,
        so we can't read all rows in one go.
    """
    file_path = os.path.abspath(os.path.join(DATA_DIR, file_name))
    
    # 源代码注释掉以下这一段
    #xl = pd.ExcelFile(file_path)
    ## In this case, there was only a single Worksheet in the Workbook.
    #sheetname = xl.sheet_names[0]
    
    # 主动给予sheet名字
    sheetname = "sheet1"
    # Read the header outside of the loop, so all chunk reads are
    # consistent across all loop iterations.
    df_header = pd.read_excel(file_path, sheetname=sheetname, nrows=1)
    print(f"Excel file: {file_name} (worksheet: {sheetname})")

    chunks = []
    i_chunk = 0
    # The first row is the header. We have already read it, so we skip it.
    skiprows = 1
    while True:
        df_chunk = pd.read_excel(
            file_path, sheetname=sheetname,
            nrows=nrows, skiprows=skiprows, header=None)
        skiprows += nrows
        # When there is no data, we know we can break out of the loop.
        if not df_chunk.shape[0]:
            break
        else:
            print(f"  - chunk {i_chunk} ({df_chunk.shape[0]} rows)")
            chunks.append(df_chunk)
        i_chunk += 1

    df_chunks = pd.concat(chunks)
    # Rename the columns to concatenate the chunks with the header.
    columns = {i: col for i, col in enumerate(df_header.columns.tolist())}
    df_chunks.rename(columns=columns, inplace=True)
    df = pd.concat([df_header, df_chunks])
    return df

if __name__ == '__main__':
    df = make_df_from_excel('claims-2002-2006_0.xls', nrows=10000