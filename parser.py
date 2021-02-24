import json
import pdb
import os
import matplotlib.pyplot as plt

def get_all_dates():
    """
    Looks in the data directory and gets all the dates present.
    """
    dates = []

    current_directory = os.getcwd()

    for _, years, _ in os.walk(os.path.join(current_directory, 'data')):
        for year in years:
            for _, months, _ in os.walk(os.path.join(current_directory, 'data', year)):
                for month in months:
                    dates.append(f'{month}/{year}')

    return dates

def open_json(month, year):
    """
    Opens the json file and returns a dictionary.
    """
    directory = f'data/{year}/{month}/'
    file_name = f'{year}-{month}-summary.json'

    with open(directory + file_name) as json_file:
        data = json.load(json_file)

    return data

def get_daily_heat_duration(data):
    """
    Returns the fotal heat time for the given day.
    """
    heating = 0
    cooling = 0

    for cycle in data['cycles']:
        if cycle['heat1']:
            heating = (heating + int(cycle['duration'][:-1]) / 60 / 60)
        elif cycle['cool1']:
            cooling = (cooling + int(cycle['duration'][:-1]) / 60 / 60)

    return (heating, cooling)

if __name__ == '__main__':
    label = []
    heat_average_7_day = []
    date_row = []
    heat_time = []
    cool_time = []

    # go through all dates
    for date in get_all_dates():
        month = open_json(date.split('/')[0], date.split('/')[1])

        # parse every single day in each month
        for day in month:
            # get daily information
            temp_heat_time, temp_cool_time = get_daily_heat_duration(month[day])

            # remove extra string parts from date
            date_row.append(day[:-10])

            # add heat/cool data
            heat_time.append(temp_heat_time)
            cool_time.append(temp_cool_time)

            # calculate heat average
            try:
                count = 0
                heat_average = 0
                for index in range(-1, -10, -1):
                    count = count + 1
                    heat_average = heat_average + heat_time[index]
            except:
                pass
            finally:
                heat_average_7_day.append(heat_average/count)

    # setup line graph
    plt.style.use('dark_background')
    plt.plot(date_row, heat_time, label='Heat Time', c='r')
    plt.plot(date_row, heat_average_7_day, label='Average Heat Time', c='b')
    plt.title('Date Vs Heat Time')
    plt.xlabel('Date')
    plt.ylabel('Time Heat On (H)')
    plt.legend()
    axis = plt.gca()
    axis.set_ylim([0, 24])
    plt.yticks([0, 6, 12, 18, 24])

    # clean up x axis labels (30 days)
    for day in date_row[::30]:
        label.append(day)
    plt.xticks(label)

    # show the plot
    plt.show()
