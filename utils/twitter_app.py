from pytwitter import Api

def twitter_reports(query):
    api = Api(
        bearer_token="AAAAAAAAAAAAAAAAAAAAACqefQEAAAAA9UA77HH4oId7122yloSgffO4A0Y%3D8ceaVvsLohtrPIZxk89oimi5XN6TEiJ6S1xJAuTgSkBhuu8SJj" 
    )
    results = api.get_tweets_counts(query=query)
    total_quotations = results.meta.total_tweet_count
    return total_quotations

def set_number_of_quotation_dict(app_dict:dict)->dict:
    for app in app_dict:
        if "&" in app["track_name"]:
            app['n_citacoes'] = twitter_reports(query=app['track_name'].replace('&','').replace('–',''))
        elif "–" in app["track_name"]:
            app['n_citacoes'] = twitter_reports(query=app['track_name'].replace('–',''))
        else:
            app['n_citacoes'] = twitter_reports(query=app['track_name'].replace('–',''))

    return app_dict

def set_number_of_quotation_list(app_list:list)->list:
    for app in app_list:
        if "&" in app[2]:
            n_citacao = twitter_reports(query=app[2].replace('&','').replace('–',''))
        elif "–" in app[2]:
            n_citacao = twitter_reports(query=app[2].replace('–',''))
        else:
            n_citacao = twitter_reports(query=app[2].replace('–',''))
        
        app.append(n_citacao)
    return app_list
