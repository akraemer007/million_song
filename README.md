# What Exactly Are We Turning Down for Again?

## Summary

Music is part of our daily lives. We listen to it when we work out. We listen to it when we're sad. This project attempts to predict what type of popular music is listened to based on external factors. If the stock market is up, are people attracted to happy music? Conversely, if the stock market is down, do people stay indoors and listen to The Cure and Morrissey on repeat?

## Impact:

While there are many examples of machine learning in the music industry, most examples center around recommender systems based on user preferences and associating similar artists. This project instead focuses on using music as an indicator of public sentiment.

## Process:



## Data:

| Source                                                                                    | Description                                                | Format                               | Data Acquired |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------|--------------------------------------|--------------|
| [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/pages/getting-dataset) | Large, detailed dataset of one million songs.              | SQLite DB (summary), HDF5 (detailed) | Yes          |
| [MusixMatch Lyrics](https://labrosa.ee.columbia.edu/millionsong/musixmatch)               | Lyrics of 237,622 songs which map to MSD dataset           | SQLite DB (bag of words)             | Yes          |
| [Billboard](http://www.umdmusic.com/default.asp?Lang=English&Chart=D)                     | Billboard Top 20 List going back to 1949                   | CSV                                  | Yes          |
| [S&P 500](https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC)                      | Weekly market highs and lows of S&P 500 going back to 1950 | CSV                                  | Yes          |

## Potential Roadblocks
- Failing to create reliable music sentiment score
- Failing to find correlation between the stock market and music sentiment score
- Matching billboard top tracks to Million Song Dataset











-
