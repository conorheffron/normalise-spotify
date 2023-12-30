import pandas as pd

def playlist_genre(df, decimals):
    # Note: Genre is class label (5X) but plan to verify as categorical (nominal) feature
    playlist_genre_dict = {'edm' : 1, 'latin' : 2, 'pop' : 3, 'rap' : 4, 'rock' : 5, None: 0}

    # Create dictionary mapping fetal health classification string to integer
    dict_len = len(playlist_genre_dict)

    # Assign int value for genre to new column 'playlist_genre_int'
    df["playlist_genre_int"] = df["playlist_genre"].apply(lambda x: playlist_genre_dict.get(x))

    # absolute difference (after normalisation)
    df["z_i_playlist_genre"] = df["playlist_genre_int"].apply(lambda x: round(abs((x - dict_len) / dict_len), decimals))


def numerical_features(c, df, decimals):
    # Column labels (max, min, difference, z value etc)
    max_c = "max_" + c
    min_c = "min_" + c
    diff_curr_min_c = "diff_curr_min_" + c
    diff_max_min_c = "diff_max_min_" + c
    z_i = "z_i_" + c
    mean_c = "mean_" + c
    sd_c = "sd_" + c
    var_c = "var_" + c

    # Data manipulation (create max, min, difference and z value columns)
    df[max_c] = pd.to_numeric(max(df[c]))
    df[min_c] = pd.to_numeric(min(df[c]))
    df[diff_curr_min_c] = pd.to_numeric(df[c]) - pd.to_numeric(min(df[c]))
    df[diff_max_min_c] = pd.to_numeric(max(df[c])) - pd.to_numeric(min(df[c]))
    df[mean_c] = pd.to_numeric(df[c]).median()
    df[sd_c] = pd.to_numeric(df[c]).std()
    df[var_c] = pd.to_numeric(df[c]).var()
    # if c == "acousticness" or c == "energy":
    #     # already normalised to range[0,1]
    #     df[z_i] = df[c]
    # else:
    df[z_i] = round(df[diff_curr_min_c] / df[diff_max_min_c], decimals)  # Rounding to 3 decimals

    # For numeric or continuous variables
    # The absolute difference after normalisation to range [0, 1] is preferred
    print("------------------------------------------------")
    print("Min of " + c + " is: " + str(pd.to_numeric(df[c]).min()))
    print("Max of " + c + " is: " + str(pd.to_numeric(df[c]).max()))
    print("Mean of " + c + " is: " + str(pd.to_numeric(df[c]).mean()))
    print("Median of " + c + " is: " + str(pd.to_numeric(df[c]).median()))
    print("Standard Deviation of " + c + " is: " + str(pd.to_numeric(df[c]).std()))
    print("Variance of " + c + " is: " + str(pd.to_numeric(df[c]).var()))
    print("Zi sum value " + c + " is: " + str(pd.to_numeric(df[z_i].sum())))
