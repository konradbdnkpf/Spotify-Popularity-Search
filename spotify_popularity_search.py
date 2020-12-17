# -*- coding: utf-8 -*-
"""
This is a Python project by: Konrad Biedenkopf, Fabian Heeb, Fabio Petrig and Chloé Vergnière.
The code was written in the course of: Programming - Introduction Level, at the University of St.Gallen

Using a Dataset (original can be found here: https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks/discussion/191122),
that uses data from the Spotify API, this program allows a user to find out different things in regards to the popularity on spotify of the over 170'000 songs in the dataset.
Dataset by: Yamaç Eren Ay (https://www.kaggle.com/yamaerenay)

The program has four functions:

1. Look up most popular songs of a year range (from date of creation).
2. Look up the most popular songs of a month in a year (from date of creation).
3. Look up most popular songs by an artist.
4. Search for the popularity of a song.

For every funtion you can choose up to which rank you would like to have the songs displayed.
You can see up to the top 100 songs for each one.

You will need the Pandas, Numpy and datetime packages to run this program.
"""

#Program starts here

import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
import datetime as dt

# import and read data
url = 'https://raw.githubusercontent.com/konradbdnkpf/Spotify-Popularity-Search/main/data.csv'
data = pd.read_csv(url, encoding = "utf-8")

# make sure that popularity values are of integer type
data.popularity = data.popularity.astype('Int64')

# helper function for formatting artists
def format_artists(lst):
  artists = lst[1]
  arts_nobrackets = artists[1:-1]
  arts_nocomma = arts_nobrackets.replace(',', ' &')
  arts_noquote = arts_nocomma.replace("'", '')
  del lst[1]
  lst.insert(1, arts_noquote)
  return lst

# helper function for creating ranking

def add_ranking(tuple_in_list):
  full_list = list(tuple_in_list)
  rank_ele = full_list.pop()
  flat_lst = [item for elem in full_list for item in elem]
  flat_lst.insert(5,rank_ele)
  return flat_lst

# year_range function for menu option 1
def year_range(starting, ending, rank):
  # format of the print statement
  f = '{5}. {0}: {2}, by {1} ({3}) with a pop. score of {4}.'

  # organizing data
  data_ordered = data.reindex(columns=['year','artists','name','release_date','popularity'])
  data_sorted = data_ordered.sort_values('popularity', ascending=False)
  data_sorted.year = data_sorted.year.astype('str')
  data_list = data_sorted.values.tolist()

  # append all songs from given year range to a new list
  rng_list = [str(v) for v in range(starting,ending+1)]
  song_list = []
  for lst in data_list:
    format_artists(lst)
    for y in rng_list:
      if y in lst[0]:
        song_list.append(lst)

  # prepare ranking of the songs and slice list up to given rank
  rank_list = [str(v) for v in range(1, rank+1)]
  song_list_upto = song_list[:rank]
  tuple_list = list(zip(song_list_upto,rank_list))

  # output conditional on user input
  if rank == 1 and starting != ending:
    print("\nIn the dataset, the most popular song released between %i & %i is:\n" % (starting, ending))
  elif rank == 1 and starting == ending:
    print("\nIn the dataset, the most popular song released in %i is:\n" % starting)
  elif rank > 1 and starting != ending:
    print("\nIn the dataset, the %i most popular songs released between %i & %i are:\n" % (rank, starting, ending))
  elif rank > 1 and starting == ending:
    print("\nIn the dataset, the %i most popular songs released in %i are:\n" % (rank, starting))
  for tpl in tuple_list:
    flat_list = add_ranking(tpl)
    print(f.format(*flat_list))
  return user_input()

# month_year function for menu option 2
def month_year(year, month, rank):
  # format of the print statement
  f = "{5}. {0}, by {1} ({4}) with a pop. score of {3}."
    
  # organizing dataset
  data_ordered = data.reindex(columns=['name','artists','release_date','year','popularity'])
  data_ordered["release_date"] = pd.to_datetime(data_ordered["release_date"])
  data_indexed = data_ordered.set_index("release_date")
    
  # slice the dataframe depending on number of days in the given month (avoid errors)
  if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    songs_month = data_indexed.loc['%i-%i-01'%(year, month):'%i-%i-31'%(year, month)]
  elif month==4 or month==6 or month==9 or month==11:
    songs_month = data_indexed.loc['%i-%i-01'%(year, month):'%i-%i-30'%(year, month)]
  elif month==2 and year%4!=0:
    songs_month = data_indexed.loc['%i-%i-01'%(year, month):'%i-%i-28'%(year, month)]
  elif month==2 and year%4==0:
    songs_month = data_indexed.loc['%i-%i-01'%(year, month):'%i-%i-29'%(year, month)]
    
  # sort the sclice of the df and create a list with most popular songs of given month
  pop_songs_month = songs_month.sort_values('popularity', ascending=False)
  idx_copy = pop_songs_month.index.copy()
  pop_songs_month["date_of_release"] = idx_copy
  pop_songs_month["date_of_release"] = pop_songs_month.date_of_release.dt.strftime("%Y-%m-%d")
  most_pop_songs = pop_songs_month.head(rank)
  song_list = most_pop_songs.values.tolist()

  # formatting artists
  for lst in song_list:
    format_artists(lst)

  # output if data unavailable for given month
  if len(song_list) == 0:
    print("\nData for songs released in month %i of %i is not available."%(month,year))
    print("(N.b.: older songs often do not have a release date, but only release year. Songs of %i with incomplete data are stored at 01-01-%i)"%(year,year))
    return user_input()
  # output if not enough data available for given month
  if len(song_list) < rank:
    rank_list = [str(v) for v in range(1, len(song_list)+1)]
    tuple_list = list(zip(song_list, rank_list))
    if len(song_list) == 1:
      print("\nThere is only %i song in the dataset for month %i of %i:"%(len(song_list),month,year))
    else:
      print("\nThere are only %i songs available for month %i of %i:"%(len(song_list),month,year))
    for tpl in tuple_list:
      flat_list = add_ranking(tpl)
      print(f.format(*flat_list))
    return user_input()  
  # Output if data available for given month
  else:
    rank_list = [str(v) for v in range(1, rank+1)]
    tuple_list = list(zip(song_list, rank_list))
    if rank == 1:
      print("\In the dataset, the most popular song released in month %i of %i are:\n"%(month, year))
    else:
      print("\In the dataset, the %i most popular songs released in month %i of %i are:\n"%(rank,month, year))
    for tpl in tuple_list:
      flat_list = add_ranking(tpl)
      print(f.format(*flat_list))
    return user_input()

# artist_songs function for menu option 3
def artist_songs(artist, rank):
  artist_name = artist.lower()
  # format of the print statement
  f = "{5}. {0}, by {1} ({2}) with a pop. score of {4}."

  # organizing dataset
  data_ordered = data.reindex(columns=['name','artists','release_date','year','popularity'])
  data_ordered.year = data_ordered.year.astype('str')
  data_ordered.release_date = data_ordered.release_date.astype('str')
  data_sorted = data_ordered.sort_values('popularity', ascending=False)    
  data_sorted.popularity = data_sorted.popularity.astype('str')
  data_list = data_sorted.values.tolist()

  # split, lower values in artist column and add the artist's songs to a new list    
  artist_list = []
  for lst in data_list:
    format_artists(lst)
    lst_low = [v.lower() for v in lst]
    if artist_name in lst_low[1]:
      artist_list.append(lst)

  # output if data unavailable for given month
  if len(artist_list) == 0:
    print("\nUnfortunately, there are no results for your search '%s'."%artist)
    return user_input()
  # output if not enough data available for given month 
  elif 0 < len(artist_list) < rank:
    artists_best = artist_list[0:len(artist_list)]
    rank_lst = [str(v) for v in range(1, len(artists_best)+1)]
    tuple_list = list(zip(artists_best, rank_lst))
    if len(artist_list) == 1:
      print("\nThere is only 1 song found in the dataset for your artist search '%s':\n" % artist)
    else:
      print("\nThere are only %i songs found in the dataset for your artist search '%s':\n"%(len(artist_list), artist))
    for tpl in tuple_list:
      flat_list = add_ranking(tpl)      
      print(f.format(*flat_list))
    return user_input()
  # Output if data available for given month
  else:
    artists_best = artist_list[0:rank]
    rank_lst = [str(v) for v in range(1, len(artists_best)+1)]
    tuple_list = list(zip(artists_best, rank_lst))
    if rank == 1:
      print("\nThe most popular song in the dataset for your artist search '%s' is:\n" % artist)
    else:
      print("\nThe %i most popular songs in teh dataset for your artist search '%s' are:\n"%(rank,artist))
    for tpl in tuple_list:
      flat_list = add_ranking(tpl)
      print(f.format(*flat_list))
    return user_input()

# song_title function for menu option 4
def song_title(song, rank):
  song_name = song.lower()
  # format of the print statement
  f = "{5}. {0}, by {1} ({2}) with a popularity score of {4}."
    
  # organizing dataset and converting column types for easier use
  data_ordered = data.reindex(columns=['name','artists','release_date','year','popularity'])
  data_ordered.year = data_ordered.year.astype('str')
  data_ordered.release_date = data_ordered.release_date.astype('str')
  data_sorted = data_ordered.sort_values('popularity', ascending=False)    
  data_sorted.popularity = data_sorted.popularity.astype('str')
  data_list = data_sorted.values.tolist()

  # split, lower values in artist column and add the artist's songs to a new list    
  song_list = []
  for lst in data_list:
    format_artists(lst)
    lst_low = [v.lower() for v in lst]
    if song_name in lst_low[0]:
      song_list.append(lst)

  # output if data unavailable for given month
  if len(song_list) == 0:
    print("\nUnfortunately, there are no results for your search '%s'."%song)
    return user_input()
  # output if not enough data available for given month
  elif 0 < len(song_list) < rank:
    songs_found = song_list[0:len(song_list)]
    rank_lst = [str(v) for v in range(1, len(songs_found)+1)]
    tuple_list = list(zip(songs_found, rank_lst))
    if len(song_list) == 1:
      print("\nThere is only 1 song in the dataset for your title search '%s':\n" % song)
    else:
      print("\nThere are only %i songs in the dataset for your title search '%s':\n" % (len(song_list), song))
    for tpl in tuple_list:
      flat_list = add_ranking(tpl)
      print(f.format(*flat_list))
    return user_input()
  # Output if data available for given month
  else:
    songs_found = song_list[0:rank]
    rank_lst = [str(v) for v in range(1, rank+1)]
    tuple_list = list(zip(songs_found, rank_lst))
    if rank == 1:
      print("\nThe most popular song in the dataset for your title search '%s' is:\n" % song)
    else:
      print("\nThe %i most popular songs found for your title search '%s' are:\n" % (rank,song))
    for tpl in tuple_list:
      flat_list = add_ranking(tpl)
      print(f.format(*flat_list))
    return user_input()

# main function
def user_input():

  # overview menu options and user input
  print("\nWhat would you like to do:\n"
  "1: Look up most popular songs realeased in a year range.\n"
  "2: Look up most popular songs released in a month/year.\n"
  "3: Search for most popular songs of an artist.\n"
  "4: Search for popularity of a title.\n"
  "Q: Quit")
  first_choice = input()

  # menu option 1 conditions with try/except for Value Errors
  if first_choice == "1":
    try:
      _begyear = int(input("   Enter beginning year (1921-2020): "))
      _endyear = int(input("   Enter end year (1921-2020): "))
      _ranking = int(input("      Up to which rank per year (1-100): "))
      if _begyear < 1921 or _begyear > 2020:
        print("\nValue entered out of bounds.")
        return user_input()
      elif _endyear < 1921 or _endyear > 2020:
        print("\nValue entered out of bounds.")
        return user_input()
      elif _ranking < 1 or _ranking > 100:
        print("\nValue entered out of bounds.")
        return user_input()
      # in case user inputs years in the wrong order
      elif _begyear > _endyear:
        _beginyear = _endyear
        _endinyear = _begyear
        year_range(_beginyear, _endinyear, _ranking)
      else:
        year_range(_begyear, _endyear, _ranking)
    except ValueError:
      print("\nYear and rank inputs must be integers.")
      return user_input()

  # menu option 2 condition and try/excpept for Value Errors
  elif first_choice == "2":
    try:
      inp_month = int(input("   Enter a month as a number (1-12): "))
      inp_year = int(input("   Enter a year (1921-2020): "))
      ranking = int(input("      Up to which rank (1-100): "))
      if inp_month < 1 or inp_month > 12:
        print("\nValue entered out of bounds.")
        return user_input()
      elif inp_year < 1921 or inp_year > 2020:
        print("\nValue entered out of bounds.")
        return user_input()
      elif ranking < 1 or ranking > 100:
        print("\nValue entered out of bounds.")
        return user_input()
      else:
        return month_year(inp_year, inp_month, ranking)
    except ValueError:
      print("\nYear, month and rank inputs must be integers.")
      return user_input()

  # menu option 3 conditions with try/except for Value Errors
  elif first_choice == "3":
    try:
      name_raw = input("   Enter a name of an artist (or part of a name): ")
      _ranking = int(input("      Up to which rank (1-100): "))
      if _ranking < 1 or _ranking > 100:
        print("\nValue entered out of bounds.")
        return user_input()
      else:
        name = name_raw.strip() 
        return artist_songs(name, _ranking)
    except ValueError:
      print("\nRank input must be an integer.")
      return user_input()

  # menu option 4 conditions with try/except for Value Errors
  elif first_choice == "4":
    try:
      title_raw = input("   Enter a song title (or part of a title): ")
      _ranking = int(input("      Up to which rank (1-100): "))
      if _ranking < 1 or _ranking > 100:
        print("\nValue entered out of bounds.")
        return user_input()
      else:
        title = title_raw.strip()
        return song_title(title, _ranking)
    except ValueError:
      print("\nRank input must be an integer.")
      return user_input()
  
  # menu option quit and condition if random input from user
  elif first_choice == "Q" or first_choice == "q":
    print("\nYou have exited the program successfully.")
  else:
    print("\nYou entered a non-applicable value.")
    return user_input()

user_input()