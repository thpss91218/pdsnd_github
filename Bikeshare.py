import time
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


    while True:
        city = input("Please enter the city you want to know about:\n").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Sorry! We can only provide data for Chicago, New York City and Washington.\n")
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("Please enter a specific month or 'all' to access information for the first six months:\n").lower()
        if month not in ('january','february','march','april','may','june','all'):
            print("Sorry! You can only access data for the first six months.\n")
            continue
        else:
            break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Would you like to find out information for a specific day? \n If  not, enter 'all' to access data for the whole week:\n").lower()
        if day not in ('monday','tuesday','wednesday','thursday','friday','all'):
            print("Incorrect input! Please try again.\n")
            continue
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january','february', 'march', 'april', 'may',
                       'june']
        month = month.index(month)+1
        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]







    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    month_name = ['Jan','Feb','Mar','Apr','May','Jun']
    popular_month = df['month'].mode()[0]
    popular_month_name = month_name[popular_month - 1]

    # TO DO: display the most common day of week
    df['Day of Week'] = df['Start Time'].dt.weekday
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    popular_weekday = df['Day of Week'].mode()[0]
    popular_weekday_name = week[popular_weekday]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("The most frequent time to travel is:\n In {} \n On {} \n at {}:00".format(popular_month_name,popular_weekday_name,popular_hour))






def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    df['combination_count'] = df['Start Station'].map(str) + '&' + df['End Station']
    popular_combination = df['combination_count'].value_counts().idxmax()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("The largest number of users travel from {} station, and the most of people return bike at {}               station.".format(popular_start_station, popular_end_station))
    print("{} is the most popular combination of start station and end station.".format(popular_combination))

def display_data(df):
    while True:
        word = input("Please enter 'Y' if you'd like to see 2 more popular start and end station combination: ")
        if word == "Y":
           i = 1
           df['combination_count'] = df['Start Station'].map(str) + '&' + df['End Station']
           popular_combination_1 = df['combination_count'].sort_values().iloc[i]
           popular_combination_2 = df['combination_count'].sort_values().iloc[i+1]

           print("{}\n{}\n".format(popular_combination_1,popular_combination_2))
           i += 3
        else:
           print("Finished.")
           break


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_time = df['Trip Duration'].sum()
    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("The total trip duration is {} seconds, and the average trip duration is {} seconds.".format(sum_time,avg_time))



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()

    # TO DO: Display counts of gender

    if df.get("Gender") is None:
        print("Gender data is not available for Washington!")
    else:
        gender_count = df['Gender'].value_counts()

        print("Here's the user information for the specified period:\n{}\n\n{}".format(user_type,gender_count))

    # TO DO: Display earliest, most recent, and most common year of birth

    if df.get("Gender") is not None:

        birth_year = df['Birth Year'].dropna(axis=0)
        earliest_year = birth_year.sort_values().iloc[0]
        recent_year = birth_year.sort_values().iloc[-1]
        common_year = birth_year.mode().iloc[0]
        print(" The eldest user was born in {}.".format(earliest_year))
        print(" The youngest user was born in {}.".format(recent_year))
        print("The greatest number of users were born in {}.".format(common_year))
    else:
        print("Birth year data is not available for Washington!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





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
