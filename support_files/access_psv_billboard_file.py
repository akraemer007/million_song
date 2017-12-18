# how to move a file from local machine to ec2
# scp -i ~/.ssh/capstone.pem ~/projects/umdmusic-downloader/us_billboard.psv ec2-user@ec2-18-217-5-71.us-east-2.compute.amazonaws.com:~/million_song/data

billboard_df = pd.read_csv('us_billboard.psv', sep='|', index_col=False, names=['this_week_position', 'last_week_position', 'peak_position_this_week', 'total_weeks_this_week','title','artist','entry_date','entry_position', 'peak_position_overall','total_weeks_overall', 'lookup_date'])

