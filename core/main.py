import pandas as pd
import numpy as np

def clean_data(path):
    data=pd.read_csv(path)
    data.drop(["author.bot","author.avatar","author.discriminator","author.global_name","author.id","author.username","call","channel_id","components","content","edited_timestamp","embeds.0.author.icon_url","embeds.0.author.proxy_icon_url","embeds.0.color","embeds.0.content_scan_version","embeds.0.type","flags","interaction","mention_everyone","mentions","message_reference","nonce","pinned","position","reactions","referenced_message","resolved","role_subscription_data","sticker_items","stickers","thread","tts","type","userName","webhook_id","mention_channels"],axis=1,inplace=True)
    cols_to_drop = data.columns[8:57]  # Select columns from index 10 to 56 (inclusive)
    data.drop(cols_to_drop, axis=1, inplace=True)
    return data

def totalActiveDays(data):
    data['timestamp'] = pd.to_datetime(data['timestamp'], format='ISO8601', errors='coerce')
    data['date'] = pd.to_datetime(data['timestamp']).dt.date

    data = data.dropna(subset=['date'])
    unique_dates = data['date'].unique()
    print(f"Total Active Days: {len(unique_dates)}")

def longestGap(data):
    longestGap = 0
    gap = 0
    start_date = None
    end_date = None

    data['timestamp'] = pd.to_datetime(data['timestamp'], format='ISO8601', errors='coerce')
    data['date'] = pd.to_datetime(data['timestamp']).dt.date

    data = data.dropna(subset=['date'])
    unique_dates = sorted(data['date'].unique())

    for i in range(1, len(unique_dates)):
        current_gap = (unique_dates[i] - unique_dates[i - 1]).days - 1
        if current_gap > 0:
            gap = current_gap
            if gap > longestGap:
                longestGap = gap
                start_date = unique_dates[i - 1]
                end_date = unique_dates[i]
        else:
            gap = 0

    print(f"Longest Gap: {longestGap}")
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")


def busiestDay(data):
    data['timestamp'] = pd.to_datetime(data['timestamp'], format='ISO8601', errors='coerce')
    data['date'] = pd.to_datetime(data['timestamp']).dt.date
    busiest_day = data['date'].value_counts().idxmax()
    busiest_day_count = data['date'].value_counts().max()
    print(f"Busiest Day: {busiest_day}")
    print(f"Total Messages: {busiest_day_count}")

def longestStreak(data):
    longestStreak = 0
    streak = 0

    data['timestamp'] = pd.to_datetime(data['timestamp'], format='ISO8601', errors='coerce')
    data['date'] = pd.to_datetime(data['timestamp']).dt.date

    data = data.dropna(subset=['date'])
    unique_dates = sorted(data['date'].unique())
    
    for i in range(1, len(unique_dates)):
        if (unique_dates[i] - unique_dates[i - 1]).days == 1:
            if streak == 0:
                temp_start_date = unique_dates[i - 1]
            streak += 1
        else:
            if streak > longestStreak:
                longestStreak = streak
                start_date = temp_start_date
                end_date = unique_dates[i - 1]
            streak = 0
            temp_start_date = None
    
    if streak > longestStreak:
        longestStreak = streak
        start_date = temp_start_date
        end_date = unique_dates[-1]
    
    print(f"Longest Streak: {longestStreak}")
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")

def monthWiseActivity(data):
    data['timestamp'] = pd.to_datetime(data['timestamp'], format='ISO8601', errors='coerce')
    data['month'] = pd.to_datetime(data['timestamp']).dt.to_period('M')
    month_wise_activity = data.groupby('month').size()
    print(month_wise_activity)

def timeWiseActivity(data):
    data['timestamp'] = pd.to_datetime(data['timestamp'], format='ISO8601', errors='coerce')
    data['hour'] = pd.to_datetime(data['timestamp']).dt.hour
    time_wise_activity = data.groupby('hour').size()
    time_wise_activity = time_wise_activity.groupby(pd.cut(time_wise_activity.index, np.arange(0, 25, 4))).sum()
    print(time_wise_activity)

def allDeveloperActivity(data):
    developer_activity = {}

    data['embeds.0.author.url'] = data['embeds.0.author.url'].fillna('')
    
    for url in data['embeds.0.author.url']:
        if url != '':
            dev_name = url.split('/')[-1]
            if dev_name in developer_activity:
                developer_activity[dev_name] += 1
            else:
                developer_activity[dev_name] = 1

    developer_activity = dict(sorted(developer_activity.items(), key=lambda item: item[1], reverse=True))
    for key, value in developer_activity.items():
        print(f"{key}: {value}")
    print("Most Active Developer: ", list(developer_activity.keys())[0])

            
def main():
    # data=clean_data("data.csv")
    # data.to_csv("clean_data.csv",index=False)
    data=pd.read_csv("clean_data.csv")
    # longestStreak(data)
    # monthWiseActivity(data)
    # totalActiveDays(data)
    # longestGap(data)
    # busiestDay(data)
    # timeWiseActivity(data)
    # allDeveloperActivity(data)
    

if __name__ == "__main__":  
    main()