
[![Python](https://img.shields.io/pypi/pyversions/pandas)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey)](https://www.python.org/downloads/)

# Spotify Popularity Search

Using a [Dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks/discussion/191122), that uses data from the Spotify API, this **Python** program allows a user to find out different things in regards to the popularity on spotify of the over 170'000 songs in the dataset.

- [Functions](#Functions)
- [What does Popularity mean?](#What-does-Popularity-mean?)
- [Limitations](#Limitations)
- [Using the Program](#Using-the-Program)
  - [Necessary Packages and Dataset](#Necessary-Packages-and-Dataset)
  - [Navigating the Menu](#Navigating-the-Menu)
- [Project Information](#Project-Information)
  

# Functions:

The program has four functions:

1. Look up most popular songs of a year range (from date of creation).
2. Look up the most popular songs of a month in a year (from date of creation).
3. Look up most popular songs by an artist.
4. Search for the popularity of a song.

For every funtion you can choose up to which rank you would like to have the songs displayed. 
You can see up to the top 100 songs for each one.

The [Dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks/discussion/191122) leaves many more options, mostly about musical properties of the songs, but these are of no use to us for this application.


# What does Popularity mean?

The [Spotify API](https://developer.spotify.com/documentation/web-api/reference/tracks/get-track/) describes the popularity rating as follows:
> The popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays are. Generally speaking, songs that are being played a lot now will have a higher popularity than songs that were played a lot in the past. Duplicate tracks (e.g. the same track from a single and an album) are rated independently. Artist and album popularity is derived mathematically from track popularity. Note that the popularity value may lag actual popularity by a few days: the value is not updated in real time.

# Limitations

- The [Dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks/discussion/191122) only contains roughly 170'000 songs, out of over 50 Million that are currently on Spotify.\
Thus, there will be many artists and songs for which you will not find any data.

- Because the Spotify API only gives out popularity scores as integers, an exact differentiation between songs popularity is often not possible.

# Using the Program

## Necessary Packages and Dataset

To use the program you will need **[Pandas](https://pandas.pydata.org)**, **[Numpy](https://numpy.org/install/)** and datetime packages.

The Dataset (version from 13.Dec.2020) can be found in the documents of this repository or here: [Dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks/discussion/191122).\
The program uses the raw of the copy of the [Dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks/discussion/191122) (version from 13.Dec.2020), that was uploaded to this repository.

If you want to use and updated version of the [Dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks/discussion/191122), you will need to download the Data.csv file in the Kaggle and change the location in the code from:

```
# import and read data
url = 'https://raw.githubusercontent.com/konradbdnkpf/Spotify-Popularity-Search/main/data.csv'
data = pd.read_csv(url, encoding = "utf-8")
```
to the local path of the Data file on your computer:
```
# import and read data
data = pd.read_csv("PATH", encoding = "utf-8") 
```
Exchange "PATH" for the local file path on your computer.

## Navigating the Menu

The Program will ask you which of the functions you want to use:

> What would you like to do:\
1: Look up most popular songs realeased in a year range.\
2: Look up most popular songs released in a month/year.\
3: Search for most popular songs of an artist.\
4: Search for popularity of a title.\
Q: Quit

Use a function by entering the number associated with it, or Q to quit.

**Function 1:**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Will ask you to enter a beginning year and an end year between 1921 and 2020.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Will then ask you until which rank you would like to know the most popular songs.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 will only give you the most popular. 100 the 100 most popular songs.

> Enter beginning year (1921-2020):\
  Enter end year (1921-2020):
  Up to which rank (1-100):

**Funtion 2:**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Will first ask you for a month in numeric form. 1 beeing January.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Will then ask you for a year between 1921 and 2020.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Will then ask you until which rank you would like to know the most popular songs.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 will only give you the most popular. 100 the 100 most popular songs.

> Enter a month as a number (1-12):\
  Enter a year (1921-2020):\
  Up to which rank (1-100):

**Function 3:**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Will ask you for the name (or part of the name) of an artist.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Will then ask you until which rank you would like to know the most popular songs.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 will only give you the most popular. 100 the 100 most popular songs.

> Enter a name of an artist (or part of a name):\
  Up to which rank (1-100):

**Function 4:**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Will ask you for a song title (or part of the title).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Will then ask you until which rank you would like to know the most popular songs.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 will only give you the most popular. 100 the 100 most popular songs.

> Enter a song title (or part of a title):\
  Up to which rank (1-100):

Should you enter values that are not meant to be entered, the program will let you know and restart from the menu. 

# Project Information

This is a project by: Konrad Biedenkopf, Fabian Heeb, Fabio Petrig and Chloé Vergnière.\
The code was written using Google Colab in the course of: *Programming - Introduction Level*, at the University of St.Gallen

The Dataset was created by [Yamaç Eren Ay](https://www.kaggle.com/yamaerenay).
