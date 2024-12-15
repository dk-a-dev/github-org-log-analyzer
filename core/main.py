import pandas as pd
import numpy as np

def clean_data(path):
    data=pd.read_csv(path)
    data.drop(["author.bot","author.avatar","author.discriminator","author.global_name","author.id","author.username","call","channel_id","components","content","edited_timestamp","embeds.0.author.icon_url","embeds.0.author.proxy_icon_url","embeds.0.color","embeds.0.content_scan_version","embeds.0.type","flags","interaction","mention_everyone","mentions","message_reference","nonce","pinned","position","reactions","referenced_message","resolved","role_subscription_data","sticker_items","stickers","thread","tts","type","userName","webhook_id","mention_channels"],axis=1,inplace=True)
    cols_to_drop = data.columns[8:57]  # Select columns from index 10 to 56 (inclusive)
    data.drop(cols_to_drop, axis=1, inplace=True)
    return data

def main():
    # data=clean_data("data.csv")
    # data.to_csv("clean_data.csv",index=False)
    data=pd.read_csv("clean_data.csv")
    print(data.iloc[0])

if __name__ == "__main__":  
    main()