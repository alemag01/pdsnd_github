Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
import datetime
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA:
        print("Please select your city: Chicago, New York City, Washington")
        city = input().lower()

        if city not in CITY_DATA:
            print("Invalid selection")

    # TO DO: get user input for month (all, january, february, ... , june)
    # Creating a dictionary for months and use the key to validate user input with a while loop
    MONTHS = {'all': 0, 'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    month = ''
    while month not in MONTHS.keys():
        print("Please enter the month, between January to June, for which you're seeking the data")
        print("If you want to see results for all months, type \'all\'")
        month = input().lower()

        if month not in MONTHS:
            print("Invalid input")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Creating a list for days of the week and use a while loop to validate user input
    DAYS = {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
    day = ''
    while day not in DAYS:
        print("Please enter the day of the week for which you're seeking the data")
        print("If you want to see results for the entire month, type \'all\'")
        day = input().lower()

        if day not in DAYS:
            print("Invalid input")

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

    # open csv
    df = pd.read_csv(CITY_DATA[city])
    
    # Split 'Start Time' timestamp and create dataframes for month, day and hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filtering by month using if statement and using the index of the months list to to create a new dataframe containing filtered data
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month] 

    # filter by day using if statement to create the new dataframe containing filtered data. Title method is used to capitalise the first       letter of the day
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df
   
    
def time_stats(df, month):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # Using mode and datetime.date().strftime()function to return most popular month in letters
   
    if month == 'all':

        popular_month = df['month'].mode()[0]
        full_month_name = datetime.date(1900, popular_month, 1).strftime('%B')
        print(f"\nMost Popular Month: {full_month_name}")
        
    else:
        
        popular_month = df['month'].mode()[0]
        full_month_name = datetime.date(1900, popular_month, 1).strftime('%B')
        print(f"\nYour Month Selection is: {full_month_name}")
    

    # TO DO: display the most common day of week
    if month == 'all':
    
        popular_day = df['day'].mode()[0]
        print(f"Most Popular Day: {popular_day}")
        
    else:
        
        popular_day = df['day'].mode()[0]
        print(f"Your Day Selection is: {popular_day}")

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print(f"Most Popular Start Hour: {popular_hour}:00")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_start_station = df['Start Station'].mode()[0]
    print(f"Most Popular Start Station is: {popular_start_station}")


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"Most Popular End Station is: {popular_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    # use .map(str) function to concatenate rows across columns
    df["Station Combination"] = df["Start Station"].map(str) + " to " + df["End Station"]
    popular_station_combo = df['Station Combination'].mode()[0]
    print(f"Most Popular Trip is between {popular_station_combo}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # using .sum() function to sum all seconds and divmod method to extract days, hours, minutes and seconds
    total_travel_time_s = df['Trip Duration'].sum()
    MinutesGet, SecondsGet = divmod(total_travel_time_s, 60)
    HoursGet, MinutesGet = divmod(MinutesGet,60) 
    DaysGet, HoursGet = divmod(HoursGet,24)
    
    print(f"Total Travel Time was:\n")
    print(DaysGet, "Days")
    print(HoursGet, "Hours")
    print(MinutesGet, "Minutes")
    print(SecondsGet, "Seconds\n")
    
    # TO DO: display mean travel time
    # using .mean() function to caluclate mean tracel time in seconds and divmod method to convert to minutes, seconds
    mean_travel_time_s = df['Trip Duration'].mean()
    MinutesGet_mean, SecondsGet_mean = divmod(mean_travel_time_s, 60)
    
    print(f"Mean Travel Time was:\n")
    print(MinutesGet, "Minutes")
    print(SecondsGet, "Seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # using value count function to count user types and aggregate results
    user_type_count = df['User Type'].value_counts()
    print(f"User types were\n{user_type_count}\n")

    # TO DO: Display counts of gender
    
    try:
        gender_count = df['Gender'].value_counts()
    except:
        print("Gender data not available\n")
    else:
        print(f"Users were\n{gender_count}\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    # .min(), .max() and .mode() functions used here to return earliest, most recent, and most common year of birth
    #using try, except, else statements to handle NaN in the Washington dataset
    
    try:
        Earliest_birthdate = df['Birth Year'].min()
    except:
        print("Birth data not available\n")
    
    try:
        Most_recent_birthdate = df['Birth Year'].max()
    except:
        print(" ") 
    
    try:
        Most_common_birthdate = df['Birth Year'].mode()[0]
    except:
        print(" ")
        
    else:
        print(f"Youngest user was born in {int(Most_recent_birthdate)}")
        print(f"Oldest user was born in {int(Earliest_birthdate)}")
        print(f"Most common year of birth of users is {int(Most_common_birthdate)}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays 5 rows of data for the city selected by the users.
    Args:
        param1 (df): The dataframe used for filtering the data.
    Returns:
        None.
    """
    USER_RESPONSE = ['yes', 'no']
    user_response = ''
    row_count = 0
    while user_response not in USER_RESPONSE:
        print("\nDo you want to view the raw data?")
        print("Yes or No")
        user_response = input().lower()
        if user_response == "yes":
            print(df.head())
        elif user_response not in USER_RESPONSE:
            print("\nInvalid input.")


    #Extra while loop to ask user if they want to continue viewing data
    while user_response == 'yes':
        print("Do you want to view more raw data?")
        row_count += 5
        user_response = input().lower()
        if user_response == "yes":
             print(df[row_count:row_count+5])
        elif user_response != "yes":
             break

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()