def rank_utility(df, row_indices, column, value):
    agg = 0
    for i, index in enumerate(row_indices):
        hit = 1 if df.iloc[index][column] == value else 0
        hit = hit * (1 / (i + 1))
        agg += hit

    return agg