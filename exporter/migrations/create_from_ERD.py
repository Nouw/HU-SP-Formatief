from mongo_to_csv import execute_export

"""
TODO:
familiy (os & browser collision)
"""


def create_products():
    collection_name = 'products'
    fields = ('_id', 'name', 'description', 'brand', {'price': ['selling_price', 'discount']}, 'category',
              'sub_category', 'sub_sub_category', 'sub_sub_sub_category', 'recommendable',
              {'properties': ['online_only', 'doelgroep', 'eenheid', 'geursoort', 'serie', 'soort', 'variant', 'type',
                              'soorthaarverzorging', 'typehaarkleuring', 'availability']},
              'gender', 'color', 'type_of_hair_care', 'type_of_hair_coloring')
    sample_size = 100
    translation = {'_id': 'id', 'selling_price': 'price', 'doelgroep': 'target_demographic', 'eenheid': 'unit',
                   'geursoort': 'odor_type', 'serie': 'series', 'soort': 'kind', 'availability': 'stock',
                   'typehaarkleuring': 'type_of_hair_care', 'soorthaarverzorging': 'type_of_hair_coloring'}
    print('\nExporting', collection_name)
    execute_export(collection_name, fields, sample_size, translation=translation, export_name='Products')


def create_sessions():
    collection_name = 'sessions'
    flags = {'flags': ['is_mobile', 'is_pc', 'is_tablet', 'is_email_client']}
    device = {'device': ['family', 'brand', 'model']}
    user_agent = {'user_agent': [{'os': ['familiy']}, {'browser': ['familiy']}, flags, device]}
    fields = ('_id', 'session_start', 'session_end', user_agent)
    sample_size = 100
    translation = {'_id': 'id', 'user_agent/browser/familiy': 'browser_name', 'user_agent/os/familiy': 'os_name',
                   'is_mobile': 'is_mobile_flag', 'is_pc': 'is_pc_flag','is_tablet': 'is_tablet_flag',
                   'is_email_client': 'is_email_flag',
                   'family': 'device_family', 'brand': 'device_brand', 'model': 'device_model'}
    print('\nExporting', collection_name)
    execute_export(collection_name, fields, sample_size, translation=translation, export_name='Sessions')


def create_profiles():
    collection_name = 'visitors'
    fields = ('_id', {'order': ['first', 'latest', 'count']})
    sample_size = 100
    translation = {'_id': 'id', 'first': 'first_order', 'latest': 'latest_order', 'count': 'order_amount'}
    print('\nExporting', collection_name)
    execute_export(collection_name, fields, sample_size, translation=translation, export_name='Profiles')


if __name__ == '__main__':
    create_products()
    create_sessions()
    create_profiles()
