from terminaltables import AsciiTable

table_data = [
    ['Connector', 'Adaptor', 'Start_Date', 'Action'],
    ['row1 column1', 'row1 column2', '2019-08-28 10:10:00', '1'],
    ['row2 column1', 'row2 column2', '2019-08-28 10:10:00', '1'],
    ['row3 column1', 'row3 column2', '2019-08-28 10:10:00', '1']
]
table = AsciiTable(table_data)
print(table.table)
