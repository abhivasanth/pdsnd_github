    #Importing time, pandas and numpy libraries
import time
import pandas as pd
import numpy as np

    #City data dictionary for user input
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    #month and days data set
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']

    #function for parsing filters
def get_filters():
    """
    Requests user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city :choices are {}\n".format(list(CITY_DATA.keys()))).lower()
    while city not in CITY_DATA:
        print("Invalid input")
        city = input("Enter the city :choices are {}\n".format(list(CITY_DATA.keys()))).lower()
        continue

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter month :choices are {}\n".format(months)).lower()
    while month not in months:
        print("Invalid input")
        month = input("Enter the month :choices are {}\n".format(months)).lower()
        continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day :choices are {}\n".format(days)).lower()
    while day not in days:
        print("Invalid input")
        day = input("Enter the day :choices are {}\n".format(days)).lower()
        continue

    print('-'*40)
    return city, month, day

     #Function definition for loading the data based on city, month and day
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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day'] == day.title()]

    return df

        #define function for time stats
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel..........\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]


    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]

    print("\nThe common month, day and start hour respectively is ",common_month,common_day,common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #define function for station statistics
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    df['combined_station'] = df['Start Station'] + df['End Station']
    common_combined_station = df['combined_station'].mode()[0]

    print("\nThe common start station is", common_start_station)
    print("\nThe common end station is", common_end_station)
    print("\nThe common combined station is", common_combined_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #define function for statistics based on trip duration
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('\nThe total travel time is',total_travel_time)
    print('\nThe mean travel time is',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #define function for user based statistics
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats....\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_type = df['User Type'].value_counts()
    except KeyError:
        user_type = 'none (due to no data)'

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
    except KeyError:
        gender_count = 'none (due to no data)'


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()

        recent_birth_year = df['Birth Year'].max()

        common_birth_year = df['Birth Year'].mode()
    except KeyError:
        earliest_birth_year = 'none (due to no data)'
        recent_birth_year = 'none (due to no data)'
        common_birth_year = 'none (due to no data)'

    print('\nThe user type is',user_type)
    print('\nThe gender_count is',gender_count)
    print('\nThe earliest birth year is',earliest_birth_year)
    print('\nThe recent birth year is',recent_birth_year)
    print('\nThe common birth year is',common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #define main function
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        print('Hello! Let\'s explore some US bikeshare raw data!')
        #To get inputs (yes/no) from the user to view 5 lines of raw data per every confirmation.
        #Initial value of 0 for printing raw data - per requirement

        a = 0;
        #User to enter a number for viewing raw data
        try:
            b = int(input('if you are given an option, how many lines of raw data do you prefer to view per request? Enter a number\n'))
        except ValueError:
            b=5
            #to improve speed of the process - defaulting value to 5 per requirement
            print("Invalid input. Default value set to 5")

        while True:
            sample_data = input("Do you want to view sample raw data for analysis? Enter yes or no.\n")
            if sample_data.lower() =='yes':
                print(df.iloc[a:b])
                a+=5
                b+=5
            else:
                break

         #Option to restart the program
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
