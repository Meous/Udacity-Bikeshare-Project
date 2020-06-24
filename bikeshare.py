""" 
Code submitted by Kwame Adu Manu

This is in fulfillment of Explore US Bikeshare Data towards the Programming for Science Certificate Nanodegree

"""

import time
import pandas as pd
import numpy as np

#loading bikeshare data files

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hey there! Welcome and enjoy exploring US bikeshare data!\n')
  
    # Accepting user input for city (chicago, new york city, washington). 
    cities = "\n1. chicago \n2. new york city \n3. washington \n"
    print('List of cities:', cities.title())

    city = input("Kindly enter city name here:\n").lower()

    #Leveraging on while loop to handle errors
    while city not in ['chicago', 'new york city', 'washington']:
        city = input(
        "Wrong input! Kindly try again:\n").lower()

    print('-'*70)
    
    #Printing list of months
    months_data = "january, february, march, april, may, june, all"
    print('List of months:', months_data.title())

    #Accepting user input for month (all, january, february, ... , june)
    month = input("Kindly enter month here: \n").lower()

    #Leveraging on while loops to handle errors
    while month not in ['january','february','march','april','may','june','all']:
        month = input(
        "Wrong input. Please try again: ").lower()

    print('-'*70)
        
    #Accepting user input for day (all, monday, tuesday, ... sunday)
    print ('Select any day of the week or enter All for summary\n')
    day = input("Kindly enter any day here:\n").lower()

    #Leveraging on while loops to handle errors
    while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']:
        day = input(
        "Wrong input. Please try again: ").lower()

    print('-'*70)
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

    #reading data
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df ['Start Time'].dt.weekday_name
    
    #filter by month where applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
      
        df = df[df['month'] == month]
        
    #filter by day where applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("January: 1, February: 2, March: 3, April: 4, May: 5, June: 6\n")
    print("The most common month is: {}".format(
        str(df['month'].mode().values[0]))
    )

    # TO DO: display the most common day of week
    print("The most common day of the week: {}".format(
        str(df['day_of_week'].mode().values[0]))
    )

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(
        str(df['start_hour'].mode().values[0]))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*70)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station is: {} ".format(df['Start Station'].mode().values[0])
         )

    # TO DO: display most commonly used end station
    print("Most commonly used end station is: {}".format(df['End Station'].mode().values[0])
         )

    # TO DO: display most frequent combination of start station and end station trip
    frq_cmb = df['Start Station'] + ' to ' + df['End Station']
    print('The most frequnt combination of start station and end station trip was{}'.format(frq_cmb.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*70)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print("The total travel time is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("The average travel time is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*70)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print('User types:', df['User Type'].value_counts())
    except:
        print('User type data is not available for this filter')
    # TO DO: Display counts of gender
    
    try:
        print('Count of genders:',df['Gender'].value_counts())
    except:
        print('Gender data is not available for your chosen filter')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode().values[0]
        print("Earlierst Year:{}\nRecent Year:{}\nCommon Year:{}".format(earliest_year,recent_year,common_year)) 
    except:
        print('Birth Year data is not available for your chosen filter')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)

#Allowing the user to view rows of raw data, five rows at a time
def display_data (df):
    #Seeking user consent/input for first five rows of data
    view_raw_data = input('Do you want to view the first five rows of the raw data for this statistics?\nKindly type Yes or No\n').lower()
    #Conditional statement to return values only if user responds yes
    if view_raw_data == 'yes':
        print(df.head())
    else:
        return  
    
    #this block allows users to continually view next 5 rows of data until they decide otherwise
    row_data = 0
    while True:
        view_raw_data = input('\nWould you like to view next five rows of the raw data?\nKindly type Yes or No.\n').lower()
        if view_raw_data.lower() != 'yes':
            return
        row_data += 5
        print(df.iloc[row_data:row_data+5])
      
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
