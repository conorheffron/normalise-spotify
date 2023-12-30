
def evaluation_output(df):
    # Write data frame to CSV
    df.to_csv("out.csv")

    # Use columns that start with 'z_i_'
    filter_col = [col for col in df if col.startswith("z_i_") or col == "playlist_genre"]
    # Write fetal health and z values to CSV
    df[filter_col].to_csv("z_values.csv")

    # Exclude categorical columns and only select z values or numeric data
    filter_col_sums = [col for col in df if col.startswith("z_i_")]
    # Sort by aggregation of z values (summation)
    ordered_z_sums = df[filter_col_sums].sum().sort_values(ascending=False)

    # Print ordered z sums
    ordered_z_sums.to_csv("z_sums.csv")

    # Print features from max-min normalisation process in ascending order
    print("------------------------------------------------")
    print(ordered_z_sums)  # [0:7])
