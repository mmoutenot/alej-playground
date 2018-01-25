
csv_contents = ''
with open('test.csv') as csv_file:
  csv_contents = csv_file.read()

# split csv contents into rows strings
rows = csv_contents.split('\n')

# isolate the elements, remove them from rows and split into list of strings
elements = rows.pop(0).split(', ')

# initialize a list for all our row dictionaries 
row_dictionaries = []

for row in rows:
  # split row string into a list of strings
  row_columns = row.split(', ')

  # initialize a new dictionary that we will fill with element: value
  dictionary = {}

  current_position = 0
  for row_column in row_columns:
    element = elements[current_position]

    # add the key-value pair where key = element (name, address, etc) and value = row's content (Marshall Moutenot) 
    dictionary[element] = row_column

    # increment position for next element (i.e. 0 = name, 1 = address)
    current_position = current_position + 1

  # add row's dictionary to list of all rows' dictionaries
  row_dictionaries.append(dictionary)

print('row_dictionaries: ', row_dictionaries)