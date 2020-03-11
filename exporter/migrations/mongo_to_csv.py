import pymongo
import csv


#   Creates the header for the csv with translation, for example translation={'_id': 'ID'},
#   so that field name '_id' becomes 'ID' in the header
def create_header(field_names, translation=None) -> str:
    if translation is None:
        translation = dict()
    header = ''

    for i in range(len(field_names)):
        if field_names[i] in translation.keys():
            header = header + translation[field_names[i]]
        elif field_names[i].split('/')[-1] in translation.keys():
            header = header + translation[field_names[i].split('/')[-1]]
        else:
            header = header + field_names[i].split('/')[-1]
        if i + 1 < len(field_names):
            header = header + ', '
    return header + '\n'


#   Extracts the wanted fields (names/values) from a source dictionary that can have a tree like structure,
#   Like a document with Array fields
def extract_fields(source, fields, parent='') -> dict:
    extracted = {}
    for field in fields:
        if type(field) is not dict:
            if field in source:
                extracted[parent+str(field)] = source[field]
            else:
                print("Couldn't find (value) {}".format(field))
                extracted[parent+str(field)] = None
        else:
            sub_source_key = tuple(field.keys())[0]
            sub_fields = tuple(field.values())[0]
            if sub_source_key in source:
                sub = extract_fields(source[sub_source_key], sub_fields, parent=parent+str(sub_source_key)+'/')
                extracted.update(sub)
            else:
                print("Couldn't find (Array/Object) {}".format(sub_source_key))
                for sub_name in extract_fieldnames(sub_fields):
                    extracted[parent+str(sub_source_key)+'/'+sub_name] = None
    return extracted


#   Extract just the fieldnames from a tree structure
def extract_fieldnames(fields, parent='') -> list:
    fieldnames = []
    for field in fields:
        if type(field) is not dict:
            fieldnames.append(parent + str(field))
        else:
            fieldnames.extend(extract_fieldnames(tuple(field.values())[0], parent+str(tuple(field.keys())[0])+'/'))
    return fieldnames


#   Runs the export script and creates a csv file.
#   Give the field names in <fields> like a list/tuple like: ['price', 'color']
#   A field within a field can be done like this: ['price', {'prop': ['brand', 'unit']}, 'color']
#   Translating multiple fields with the same name should be given like this:
#   {'prop/unit': 'ProdID', 'cstm/unit': 'deviceID', 'color': 'Color'}
def execute_export(collection_name, fields, sample_size=None, translation=None,
                   export_name=None, db_name='huwebshop', mongo_ip='mongodb://localhost:27017/'):
    if translation is None:
        translation = dict()

    #   Setup connection to MongoDB
    myclient = pymongo.MongoClient(mongo_ip)
    db = myclient[db_name]
    col = db[collection_name]
    print("Connected to MongoDB...")

    #   Get the data from MongoDB
    finds = col.find()
    if sample_size is not None:
        finds = finds[:sample_size]
    print("Data received...")

    #   Write as csv file
    field_names = extract_fieldnames(fields)
    if export_name is None:
        export_name = collection_name
    filename = 'csvs/{}.csv'.format(export_name)
    print("Writing to {}...".format(filename))
    with open(filename, 'w') as file:
        file.write(create_header(field_names, translation))

        writer = csv.DictWriter(file, field_names)
        i = 0
        for document in finds:
            row_dict = extract_fields(document, fields)
            writer.writerow(row_dict)

            i += 1
            if i % 10000 == 0:
                print("Written {} documents.".format(i))
        print("Written {} documents.".format(i))

    print("Done exporting.")


if __name__ == '__main__':
    m_collection_name = 'sessions'
    m_fields = ('_id', {'user_agent': [{'os': ['familiy', 'version_string']}]}, 'session_start', 'session_end')
    m_sample_size = 100
    execute_export(m_collection_name, m_fields, m_sample_size, export_name='Sessions')
