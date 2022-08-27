import csv

def read_csv_file(path='input/AppleStore.csv'):
    arquivo = open(path)
    linhas = csv.reader(arquivo)
    list_rating_count_total_max_value = 0
    first_line = True
    line_with_max_rating_count_list = []
    lines_books_dict = []
    lines_music_dict = []
    lines_books_list = []
    lines_music_list = []

    for linha in linhas:
        
        if first_line:
            header = linha        
        
        if linha[12]=="Music" or linha[12]=="Book":
            new_line = {}
            for i in range(len(header)):
                new_line[f"{header[i]}"] = linha[i]

            linha[6] = int(linha[6])
            if linha[12]=="Book":
                lines_books_dict.append(new_line)
                lines_books_list.append(linha)
            else:
                lines_music_dict.append(new_line)
                lines_music_list.append(linha)

        if linha[12]=="News":
            if list_rating_count_total_max_value < int(linha[6]):
                list_rating_count_total_max_value = int(linha[6])
                line_with_max_rating_count_list = linha
        first_line = False

    dict_news_with_max_rating_count={}
    for i in range(len(header)):
        dict_news_with_max_rating_count[f"{header[i]}"] = line_with_max_rating_count_list[i]

    return (
        dict_news_with_max_rating_count,
        lines_books_dict,
        lines_music_dict,
        line_with_max_rating_count_list,
        lines_books_list,
        lines_music_list
    )

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
