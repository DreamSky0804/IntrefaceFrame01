import xlrd
def getdata():
    wk = xlrd.open_workbook("testcases/case.xlsx")
    st = wk.sheet_by_name("Sheet1")
    rows = st.nrows
    cols = st.ncols
    datas = []
    for i in range(1,rows):
        switch = st.cell(i,0).value
        if switch == "on" :
            datas.append([st.cell(i,j).value for j in range(1,cols)])
    return datas
if __name__ == '__main__':
    g = getdata()
    print(g)


