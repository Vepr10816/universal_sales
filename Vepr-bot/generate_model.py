"""
Автосоздание моделей из БД.
"""

import os

import psycopg2
conn = psycopg2.connect(dbname='db_vepr', user='postgres',
                        password='1', host='localhost')
cursor = conn.cursor()

cursor.execute("""select
    t.table_name,
    array_agg(c.column_name::text) as columns,
	array_agg(c.data_type::text) as types
from
    information_schema.tables t
inner join information_schema.columns c on
    t.table_name = c.table_name
where
    t.table_schema = 'public'
    and t.table_type= 'BASE TABLE'
    and c.table_schema = 'public'
group by t.table_name""")


THIS_PATH = os.getcwd()

for table in cursor.fetchall():
    foreignKeys = []
    tableName = table[0].replace("_", "")
    columns = table[1]
    my_file = open(f'{THIS_PATH}/models/{tableName}.py', "w+")
    my_file.write(f'class {tableName[0].upper() + tableName[1:]}:\n\n')
    my_file.write('\tdef __init__(self):\n')
    for i in range(len(columns)):
        defaultValue = ""
        columnType = table[2][i]
        columnName = columns[i]
        if '_id' in columnName:
            foreignKeys.append(columnName.replace("_id", ""))
            columnName = columnName.replace("_id", "")
        if columnType == 'bigint' or columnType == 'interger' or 'double' in columnType:
            defaultValue = '0'
        if columnType == 'text':
            defaultValue = "\" \""
        my_file.write(f'\t\tself.{columnName} = {defaultValue}\n')
    for columnName in columns:
        if '_id' in columnName:
            columnName = columnName.replace("_id","")
        my_file.write('\n\t@property\n'+
                        f'\tdef _{columnName}(self):\n'+
                            f'\t\treturn self.{columnName}\n\n'+

                       f'\t@_{columnName}.setter\n'+
                        f'\tdef _{columnName}(self, value):\n'+
                            f'\t\tself.{columnName} = value\n\n\n')

    my_file.write('\tdef get(self):\n'+
                    f'\t\t{tableName}Dict = self.__dict__\n'
                    f'\t\tdel {tableName}Dict[\'id\']\n')

    for key in foreignKeys:
        my_file.write(f'\t\t{tableName}Dict[\'id{key[0].upper() + key[1:]}\'] = {tableName}Dict.pop(\'{key}\')\n')

    my_file.write(f'\t\treturn {tableName}Dict\n\n')

    my_file.write(f'\tdef set(self')

    for columnName in columns:
        my_file.write(f', {columnName.replace("_id","")}')

    my_file.write('):\n')

    for columnName in columns:
        my_file.write(f'\t\tself.{columnName.replace("_id","")} = {columnName.replace("_id","")}\n')

    my_file.write('\t\treturn self')

    my_file.close()

cursor.close()