from utils.clear_data import clear_data_func_list, clear_data_func_dict
from utils.read_csv_file import read_csv_file
from utils.create_files import create_csv_file, create_json_file, create_sqlite3_file
from operator import itemgetter

def main():
    (
        dict_with_max_rating_count_news_genre,
        list_dict_lines_books,
        list_dict_lines_music,
        list_with_max_rating_count_news_genre,
        list_list_lines_books,
        list_list_lines_music
    ) = read_csv_file()
    
    list_dict_lines_books.sort(key=lambda l:int(l["rating_count_tot"]), reverse=True)
    list_dict_lines_music.sort(key=lambda l:int(l["rating_count_tot"]), reverse=True)

    list_list_lines_books = sorted(list_list_lines_books, key=itemgetter(6), reverse=True )[0:10]
    list_list_lines_music = sorted(list_list_lines_music, key=itemgetter(6), reverse=True )[0:10]

    clear_list_dict_lines_music = clear_data_func_list(list_dict_lines_music[0:10])
    clear_list_dict_lines_books = clear_data_func_list(list_dict_lines_books[0:10])
    clear_dict_with_max_rating_count_news_genre = clear_data_func_dict(dict_with_max_rating_count_news_genre)

    result = { 
        "News":clear_dict_with_max_rating_count_news_genre, 
        "Music":[*clear_list_dict_lines_music], 
        "Books":[*clear_list_dict_lines_books]
    }

    create_csv_file([
        list_with_max_rating_count_news_genre,
        *list_list_lines_books,
        *list_list_lines_music
    ])
    create_json_file(result)
    create_sqlite3_file()
    
if __name__ == "__main__":
    main()
