def clear_data_func_dict(data:dict)->dict:
    return {
        "id": data["id"],
        "track_name": data["track_name"],
        "size_bytes": data["size_bytes"],
        "price": data["price"],
        "prime_genre": data["prime_genre"],
    }

def clear_data_func_list(data:list)->list:
    result = []
    for dict in data:
        result.append(clear_data_func_dict(dict))
    
    return result

def clear_list_of_list_data(data:list):
    return [
        data[1],
        data[2],
        data[3],
        data[5],
        data[6],
        data[12],
    ]

"""
{
id,
track_name, 
n_citacoes, 
size_bytes, 
price,
prime_genre
}
"""
