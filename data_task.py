browsing_data=int(input("Enter the browsing data:"))
video_data=int(input("Enter the video streaming data:"))
online_class_data=int(input("Enter the online class data:"))
total_data=browsing_data+video_data+online_class_data
remaining_data=2000-total_data
print(f"Total data used:{total_data} MB")
print(f"Remaining data:{remaining_data} MB")

'''
# output

Enter the browsing data:500
Enter the video streaming data:800
Enter the online class data:300
Total data used:1600 MB
Remaining data:400 MB
'''
