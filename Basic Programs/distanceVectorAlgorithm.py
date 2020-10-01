import xlrd

x=[8,7,4,13,17,9,3,12,10,14,6,17]
list=[]
wb = xlrd.open_workbook(r'input.xlsx')
data = wb.sheet_by_index(0)
graph = wb.sheet_by_index(1)
router=input("Enter router:")
for i in range(1,13):
    if data.cell_value(i,0)==router:
        index=i

for i in range(1,data.nrows):
    min=999
    for j in range(1,data.ncols):
        if data.cell_value(i,j)+x[j-1]<min and graph.cell_value(index,j)==1:

            min=data.cell_value(i,j)+x[j-1]
            insert=[data.cell_value(i,0),min,data.cell_value(0,j)]
            if data.cell_value(i,0)==router:
                insert =[data.cell_value(i, 0), '-', '-']
    list.append(insert)
#print(*list, sep="\n")
for i in list:
    print(*i)
