import pymongo
import csv


#   Give a list of fieldnames that you want and those you don't, returns a "filter" for MongoDB's find function
def create_return_filter(allow, block) -> dict:
    if '_id' not in allow:
        block = list(block) + ['_id']
    return_filter = {}
    for field_name in allow:
        return_filter[field_name] = True
    for field_name in block:
        return_filter[field_name] = False
    return return_filter


#   Creates the header for the csv with translation, for example translation={'_id': 'ID'},
#   so that field name '_id' becomes 'ID' in the header
def create_header(field_names, translation={}):
    header = ''
    for i in range(len(field_names)):
        if field_names[i] in translation.keys():
            header = header + translation[field_names[i]]
        else:
            header = header + field_names[i]
        if i + 1 < len(field_names):
            header = header + ', '
    return header + '\n'


#   Runs the export script and creates a csv file
def execute_export(collection_name, field_names,
                   sample_size=None, translation={}, db_name='huwebshop', mongo_ip='mongodb://localhost:27017/'):
    #   Setup connection to MongoDB
    myclient = pymongo.MongoClient(mongo_ip)
    db = myclient[db_name]
    col = db[collection_name]
    print("Connected to MongoDB...")

    #   Get the data from MongoDB
    finds = col.find({}, create_return_filter(field_names, ()))
    if sample_size is not None:
        finds = finds[:sample_size]
    print("Data received...")

    #   Write as csv file
    filename = 'csvs/{}.csv'.format(collection_name)
    print("Writing to {}...".format(filename))
    with open(filename, 'w') as file:
        #   Write header
        file.write(create_header(field_names, translation))
        #   Write values
        writer = csv.DictWriter(file, field_names)
        i = 0
        for document in finds:
            document: dict
            couldnt_find = set(field_names).difference(set(document.keys()))
            if len(couldnt_find) > 0:
                print("Couldn't find {} in {} id: {}".format(couldnt_find, collection_name, document['_id']))

            writer.writerow(document)
            
            i += 1
            if i % 10000 == 0:
                print("Written {} documents.".format(i))

    print("Done exporting.")


if __name__ == '__main__':
    m_collection_name = 'sessions'
    m_field_names = ('_id', 'session_start', 'session_end')
    m_sample_size = 100
    execute_export(m_collection_name, m_field_names, m_sample_size)
