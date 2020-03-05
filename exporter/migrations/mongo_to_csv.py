import pymongo
import csv


#   Give a list of fieldnames that you want and those you don't, returns a "filter" for MongoDB's find function
def create_return_filter(allow, block) -> dict:
    if '_id' not in allow:
        block = list(block) + ['_id']
    return_filter = {}
    for x in allow:
        return_filter[x] = True
    for x in block:
        return_filter[x] = False
    return return_filter


#   Runs the export script and creates a csv file
def run_export(collection_name, field_names,
               sample_size=None, db_name='huwebshop', mongo_ip='mongodb://localhost:27017/'):
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
    filename = collection_name + '.csv'
    print("Writing to {}...".format(filename))
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, field_names)
        writer.writerows(finds)

    print("Done exporting.")


if __name__ == '__main__':
    m_collection_name = 'sessions'
    m_field_names = ('_id', 'session_start', 'session_end')
    m_sample_size = 10
    run_export(m_collection_name, m_field_names, m_sample_size)
