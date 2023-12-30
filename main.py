import pandas as pd

import evaluation
import normalise as normy


def assignment_2(decimals):
    # Read spotify data
    df = pd.read_csv('./spotify_23211267.csv')

    # Print (# observations, # variables)
    print("Spotify data dimensions: " + str(df.shape))

    normalise(df, decimals)

    evaluation.evaluation_output(df)


def normalise(df, decimals):
    # Loop through columns in data frame & normalise numeric features where relevant
    for c in df.columns:
        if c != 'playlist_genre':
            # Normalise all other numeric features (continuous...)
            normy.numerical_features(c, df, decimals)
        else:
            normy.playlist_genre(df, decimals)


if __name__ == '__main__':
    # Main run configurations
    decimals = 3

    # Run assignment 2 code
    assignment_2(decimals)