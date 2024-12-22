import pandas as pd
import numpy as np

def clean_data(path):
    data=pd.read_csv(path)
    data.drop(["author.bot","author.avatar","author.discriminator","author.global_name","author.id","author.username","call","channel_id","components","content","edited_timestamp","embeds.0.author.icon_url","embeds.0.author.proxy_icon_url","embeds.0.color","embeds.0.content_scan_version","embeds.0.type","flags","interaction","mention_everyone","mentions","message_reference","nonce","pinned","position","reactions","referenced_message","resolved","role_subscription_data","sticker_items","stickers","thread","tts","type","userName","webhook_id","mention_channels"],axis=1,inplace=True)
    cols_to_drop = data.columns[8:57]  # Select columns from index 10 to 56 (inclusive)
    data.drop(cols_to_drop, axis=1, inplace=True)
    return data

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
    return None
def developerActivity(data):
    return None

def main():
    # data=clean_data("data.csv")
    # data.to_csv("clean_data.csv",index=False)
    data=pd.read_csv("clean_data.csv")
    longestStreak(data)
    monthWiseActivity(data)
    developerActivity(data)


if __name__ == "__main__":  
    main()