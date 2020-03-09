from mongo_to_csv import execute_export


def create_products():
    collection_name = 'products'
    field_names = ('_id', 'name', 'description', 'brand', 'price', 'discount', 'stock', 'category', 'sub_category',
                   'sub_sub_category', 'sub_sub_sub_category', 'recommendable', 'online_only', 'target_demographic',
                   'gender', 'color', 'unit', 'odor_type', 'series', 'kind', 'varient', 'type', 'type_of_hair_care',
                   'type_of_hair_coloring')
    sample_size = 100
    translation = {'_id': 'id'}
    print('\nExporting', collection_name)
    execute_export(collection_name, field_names, sample_size, translation=translation)


def create_sessions():
    collection_name = 'sessions'
    field_names = ('_id', 'session_start', 'session_end', 'user_agent_id', 'browser_name', 'os_name')
    sample_size = 100
    translation = {'_id': 'id'}
    print('\nExporting', collection_name)
    execute_export(collection_name, field_names, sample_size, translation=translation)


def create_profiles():
    collection_name = 'profiles'
    field_names = ('_id', 'first_order', 'latest_order', 'order_amount')
    sample_size = 100
    translation = {'_id': 'id'}
    print('\nExporting', collection_name)
    execute_export(collection_name, field_names, sample_size, translation=translation)


if __name__ == '__main__':
    create_products()
    create_sessions()
    create_profiles()
