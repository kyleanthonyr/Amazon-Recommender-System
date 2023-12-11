import re
from collections import defaultdict
from random import choice
import pandas as pd


def get_random_user(trainset):
    '''Gets a random user found in the trainset'''
    return choice(list(trainset.userID))


def get_top_n(predictions, n=10):
    """Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    """

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


def get_recs_and_ratings(all_user_recs, trainset) -> dict:
    '''Get top-n predicted recommendations for a random user and returns a dictionary of book IDs and predicted ratings.'''

    # Get Random User and their Recommendations and Ratings
    rand_user = get_random_user(trainset)
    recs = all_user_recs[rand_user]

    # Wrangle their recommendations and ratings into a dict
    bookID = [id[0] for id in recs]
    rating = [rec[1] for rec in recs]

    pairs = {
        'books': bookID,
        'predicted_ratings': rating
    }

    return pairs


def clean_text_list(text_list):
    '''Helper function to cleanup string output of description column'''
    # Filter out empty strings and HTML tags, then join the remaining text
    cleaned_sentence = ' '.join(filter(lambda x: x.strip() != '', [
                                re.sub(r'<.*?>', '', text).strip() for text in text_list]))
    return cleaned_sentence


# Define a function to check if a value resembles the specified pattern
def replace_unavailable(value):
    if isinstance(value, str) and any(pattern in value for pattern in [
        r'a-section\.a-spacing-mini',
        r'#actionPanel #availability',
        r'#actionPanel #merchant-info',
        r'#actionPanel #pa_avaliability_message',
        r'#actionPanel #availability-brief',
        r'#actionPanel #bbop-sbbop-container',
        r'#actionPanel .buybox-main',
        r'#actionPanel #priceblock_ourprice_row span.feature img',
        r'#actionPanel #pa_feedbackForm_rootmain',
        r'#buybox_feature_div #deal #regularBuybox',
        r'#hero-quick-promo hr',
        r'#actionPanel #hqp',
        r'#actionPanel #amsDetailRight',
        r'#actionPanel #amsDetailRightWide',
        r'#actionPanel #hqp #hqp-left',
        r'div#hqp-bottom.a-section.burj',
        r'#instantOrderUpdate_feature_div'
    ]):
        return 'Price not available'
    else:
        return value


def cleanup_cols(df: pd.DataFrame) -> pd.DataFrame:
    # Cleanup output of Description column
    df['description'] = df['description'].apply(clean_text_list)
    df['description'] = df.description.replace(
        [''], ['No Description Available.'])

    # If price is missing, replace with 'No Price Available'
    df['price'] = df.price.replace([''], ['Price Not Available.'])
    df['price'] = df.price.apply(replace_unavailable)

    # Convert asin col to int dtype for merge late
    df['asin'] = df['asin'].astype('int')

    return df


def get_metadata(user_recs, spark_session, metadata_file='../data/books_meta.gz') -> pd.DataFrame:
    '''Get the metadata for provided recommended book IDS and return a cleanly formatted DF'''

    # Load the file containing the metadata
    spark_df = spark_session.read.json(metadata_file)

    # Find the metadata for user recommendations
    columns = ['asin', 'title', 'price', 'description']
    recommendations = spark_df[spark_df.asin.isin(
        user_recs['books'])][*columns].toPandas()

    # Cleanup output of Column
    cleaned_recommendations = cleanup_cols(recommendations)

    return cleaned_recommendations
