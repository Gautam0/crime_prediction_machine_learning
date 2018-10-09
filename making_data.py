# from ezodf import opendoc, Sheet
# import csv

# def normalize(lst):
#     s = sum(lst)
#     return map(lambda x: float(x)/s, lst)

# doc = opendoc('yearly_crime_all_data.ods')
# for sheet in doc.sheets:
#    new_list = [15]
#    for code in range(ord('B'), ord('P') + 1):
#    		char = chr(code) + '17'   		
# 	   	cell_value = int( sheet[char].value )
# 	   	new_list.append(cell_value);
#    with open('data_1.csv', mode='a') as crime_file:
#     	crime_writer = csv.writer(crime_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     	crime_writer.writerow(new_list)


from ezodf import opendoc, Sheet
import csv

def normalize(lst):
    s = sum(lst)
    value = map(lambda x: float(x)/s, lst)
    value = [ '%.2f' % elem for elem in value ]
    return value


n_list =[17966,
5062,
1763,
2857,
1186,
1123,
28630,
9549,
20440,
6367,
14698,
8174,
17893,
15954,
640]
n_list = normalize(n_list)
print n_list

# doc = opendoc('yearly_crime_all_data.ods')
# for sheet in doc.sheets:
#    ano_list = []
#    for code in range(ord('B'), ord('P') + 1):
#    	   new_list = []
# 	   for cell_ind in range(3,18):
# 		   char = chr(code) + str(cell_ind)   		
# 	   	   cell_value = int( sheet[char].value )
# 		   new_list.append(cell_value)
# 	   new_list = normalize(new_list)
# 	   ano_list.append( new_list[14] )
#    with open('data_2.csv', mode='a') as crime_file:
#        crime_writer = csv.writer(crime_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#        crime_writer.writerow(ano_list)