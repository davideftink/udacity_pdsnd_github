"""
Name: BikeShare Systems Data Explore Application
Date: 2025.09.18
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYSOFWEEK = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 
              'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city (chicago, new york city, washington)
    is_city = 'n'
    while is_city == 'n':
        city_list = list(CITY_DATA.keys())
        print("\nThe following cities can be used to filter the data.")
        print(city_list)
        city = input("Enter the city name: ").lower()
        
        if city in CITY_DATA:
            is_city = 'y'
            print("\nThe city '{}' has been selected.".format(city))
        else:
            print("\nCity not found!")

    # Get user input for month (all, january, february, ... , june)
    is_month = 'n'
    while is_month == 'n':
        month_list = list(MONTHS)
        month_list.insert(0, "all")
        print("\nThe following months can be used to filter the data.")
        print(month_list)
        month = input("Enter the month: ").lower()
        
        if month in month_list:
            is_month = 'y'
            print("\nThe month '{}' has been selected.".format(month))
        else:
            print("\nMonth not found!")

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    is_day = 'n'
    while is_day == 'n':
        day_list = list(DAYSOFWEEK)
        day_list.insert(0, "all")
        print("\nThe following days can be used to filter the data.")
        print(day_list)
        day = input("Enter the day: ").lower()
        
        if day in day_list:
            is_day = 'y'
            print("\nThe day '{}' has been selected.".format(day))
        else:
            print("\nDay not found!")

    print('-'*40)
    
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week, & hour from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1
    
        # Filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['Day of Week'] == day.title()]
        
    return df


def get_raw_data(df):
    """Displays the raw data 5 rows at a time."""
    
    # Prompt to display raw data
    show_data = input("Would you like see the raw data? Enter yes or no.\n")
    if show_data.lower() in ['yes', 'y']:
        row_index = 0
        get_next = 'y'
        row_count = len(df)
        print("\nTotal row count: {}".format(row_count))
        # Display raw data 5 rows at a time
        while get_next.lower() in ['yes', 'y']:
            print(df.iloc[row_index:row_index+5])
            row_index += 5
            # Prompt to continue with raw data
            if row_index < row_count:
                get_next = input('\nDisplay next 5 rows? Enter yes or no.\n')
            else:
                get_next = 'n'
    
    print('-'*40)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        get_raw_data(df)
        
        stats = input('\nWould you like to see data statistics? Enter yes or no.\n')
        if stats.lower() in ['yes', 'y']:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ['yes', 'y']:
            break


if __name__ == "__main__":
	main()
