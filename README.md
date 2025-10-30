# normalise-spotify

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Python package](https://github.com/conorheffron/normalise-spotify/actions/workflows/python-package.yml/badge.svg)](https://github.com/conorheffron/normalise-spotify/actions/workflows/python-package.yml)

![Proof HTML](https://github.com/conorheffron/normalise-spotify/actions/workflows/proof-html.yml/badge.svg)

## Min-Max Normalisation of Spotify Data

#### See full report at [Report](https://conorheffron.github.io/normalise-spotify/report.pdf) & R code/analysis at [Rmd](https://conorheffron.github.io/normalise-spotify/assignment-2.pdf)

### Sample CLI usage: python main.py `number_of_decimals_for_rounding`

```shell
 python main.py 3
```

```shell
 > python main.py 2
The number of decimals set is 2
Spotify data dimensions: (21812, 13)
------------------------------------------------
Min of danceability is: 0.0
Max of danceability is: 0.983
Mean of danceability is: 0.6514165734458096
Median of danceability is: 0.667
Standard Deviation of danceability is: 0.1463938018880771
Variance of danceability is: 0.021431145231245567
Z score value danceability is: 14454.170000000002
------------------------------------------------
Min of energy is: 0.000175
Max of energy is: 1.0
Mean of energy is: 0.7201891396937466
Median of energy is: 0.745
Standard Deviation of energy is: 0.1734950267410095
Variance of energy is: 0.030100524303863604
Z score value energy is: 15698.15
------------------------------------------------
Min of key is: 0
Max of key is: 11
Mean of key is: 5.359205941683477
Median of key is: 6.0
Standard Deviation of key is: 3.604633195031203
Variance of key is: 12.99338047072086
Z score value key is: 10631.75
------------------------------------------------
Min of loudness is: -46.448
Max of loudness is: 1.275
Mean of loudness is: -6.488673665871998
Median of loudness is: -5.895
Standard Deviation of loudness is: 2.969534676572623
Variance of loudness is: 8.818136195367273
Z score value loudness is: 18263.84
------------------------------------------------
Min of mode is: 0
Max of mode is: 1
Mean of mode is: 0.578809829451678
Median of mode is: 1.0
Standard Deviation of mode is: 0.49376126632609246
Variance of mode is: 0.24380018812394644
Z score value mode is: 12625.0
------------------------------------------------
Min of speechiness is: 0.0
Max of speechiness is: 0.877
Mean of speechiness is: 0.10477729231615623
Median of speechiness is: 0.0614
Standard Deviation of speechiness is: 0.0995377389466803
Variance of speechiness is: 0.009907761474617477
Z score value speechiness is: 2606.0000000000005
------------------------------------------------
Min of acousticness is: 0.0
Max of acousticness is: 0.994
Mean of acousticness is: 0.15819448752980012
Median of acousticness is: 0.067
Standard Deviation of acousticness is: 0.2074554900373028
Variance of acousticness is: 0.04303778034661744
Z score value acousticness is: 3467.55
------------------------------------------------
Min of instrumentalness is: 0.0
Max of instrumentalness is: 0.994
Mean of instrumentalness is: 0.0964625660187053
Median of instrumentalness is: 2.2e-05
Standard Deviation of instrumentalness is: 0.23831234781115662
Variance of instrumentalness is: 0.056792775119265684
Z score value instrumentalness is: 2113.51
------------------------------------------------
Min of liveness is: 0.0
Max of liveness is: 0.996
Mean of liveness is: 0.19425706583532001
Median of liveness is: 0.13
Standard Deviation of liveness is: 0.15813235139325513
Variance of liveness is: 0.025005840557159913
Z score value liveness is: 4253.33
------------------------------------------------
Min of valence is: 0.0
Max of valence is: 0.991
Mean of valence is: 0.5054820983862094
Median of valence is: 0.506
Standard Deviation of valence is: 0.23474981893651678
Variance of valence is: 0.05510747749072741
Z score value valence is: 11125.94
------------------------------------------------
Min of tempo is: 0.0
Max of tempo is: 220.252
Mean of tempo is: 122.23560191637631
Median of tempo is: 123.966
Standard Deviation of tempo is: 26.325958217264375
Variance of tempo is: 693.0560760571498
Z score value tempo is: 12101.340000000002
------------------------------------------------
Min of duration_ms is: 4000
Max of duration_ms is: 517810
Mean of duration_ms is: 223585.04231615624
Median of duration_ms is: 213507.0
Standard Deviation of duration_ms is: 59883.42208965201
Variance of duration_ms is: 3586024241.167423
Z score value duration_ms is: 9321.51

------------------------------------------------
z_i_loudness            18263.84
z_i_energy              15698.15
z_i_danceability        14454.17
z_i_mode                12625.00
z_i_tempo               12101.34
z_i_playlist_genre      11156.35
z_i_valence             11125.94
z_i_key                 10631.75
z_i_duration_ms          9321.51
z_i_liveness             4253.33
z_i_acousticness         3467.55
z_i_speechiness          2606.00
z_i_instrumentalness     2113.51
dtype: float64
```


