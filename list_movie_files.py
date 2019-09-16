'''
Last edited on: 10-Sept-2019, Thursday

Steps to run:

First navigate to network folder on MAC. Connect to each of the file systems accross the network. Credentials:
Username:
Password:

Paths to consider:

A. Ds418Play_TT:

1. /Volumes/Documentary
2. /Volumes/Movies_4K/HD MOVIES
3. /Volumes/Movies_2018/English/1080P
4. /Volumes/Movies_2018/English/1080P HD
5. /Volumes/Movies_2018/English/4K Movies
6. /Volumes/Movies_2018/French
7. /Volumes/Movies_2018/Malayalam
8. /Volumes/Movies_2018/Hindi
9. /Volumes/Movies_2018/Tamil
10. /Volumes/TV Shows
11. /Volumes/TV Shows Part 2
12. /Volumes/video-1/Documentary
13. /Volumes/video-1/Video_Courses
14. /Volumes/video-1/Movies/English/1080P
15. /Volumes/video-1/Movies/English/1080P HD
16. /Volumes/video-1/Movies/English/720P
17. /Volumes/video-1/Movies/English/Divx
18. /Volumes/video-1/Movies/Malayalam

Note: Tebby's Music is in :
/Volumes/music/Tebby_Music/Music

B. NASE65660

1. /Volumes/Download/French
2. /Volumes/Download/Hindi
3. /Volumes/Download/Other
4. /Volumes/Download/Tamil
5. /Volumes/Movies_New/Movies/4K Movies
6. /Volumes/Movies_New/Movies/1080P HD
7. /Volumes/Movies_New/French
8. /Volumes/Movies_New/Hindi
9. /Volumes/Movies_New/Malayalam
10. /Volumes/Movies_New/Tamil
11. /Volumes/Video/Movies/English/720P
12. /Volumes/Video/Movies/English/1080P HD
13. /Volumes/Video/Movies/English/1080P
14. /Volumes/Video/Movies/Malayalam 2017
15. /Volumes/Videos3/Documentaries
16. /Volumes/Videos3/TV Shows

'''

import os
import csv

contents = dict()
list1 = list()
list1.append("/Volumes/Download/French")
list1.append("/Volumes/Download/Hindi")
list1.append("/Volumes/Download/Other")
list1.append("/Volumes/Download/Tamil")
list1.append("/Volumes/Movies_New/Movies/4K Movies")
list1.append("/Volumes/Movies_New/Movies/1080P HD")
list1.append("/Volumes/Movies_New/French")
list1.append("/Volumes/Movies_New/Hindi")
list1.append("/Volumes/Movies_New/Malayalam")
list1.append("/Volumes/Movies_New/Tamil")
list1.append("/Volumes/Movies_New/Others")
list1.append("/Volumes/Video-1/Movies/English/720P")
list1.append("/Volumes/Video-1/Movies/English/1080P HD")
list1.append("/Volumes/Video-1/Movies/English/1080P")
list1.append("/Volumes/Video-1/Movies/Malayalam 2017")
list1.append("/Volumes/Videos3/Documentaries")
list1.append("/Volumes/Videos3/TV Shows")

contents["NASE65660"] = list1

list2 = list()
list2.append("/Volumes/Documentary")
list2.append("/Volumes/Movies_4K/HD MOVIES")
list2.append("/Volumes/Movies_2018/English/1080P")
list2.append("/Volumes/Movies_2018/English/1080P HD")
list2.append("/Volumes/Movies_2018/English/4K Movies")
list2.append("/Volumes/Movies_2018/French")
list2.append("/Volumes/Movies_2018/Malayalam")
list2.append("/Volumes/Movies_2018/Hindi")
list2.append("/Volumes/Movies_2018/Tamil")
list2.append("/Volumes/TV Shows")
list2.append("/Volumes/TV Shows Part 2")
list2.append("/Volumes/video/Documentary")
list2.append("/Volumes/video/Video_Courses")
list2.append("/Volumes/video/Movies/English/1080P")
list2.append("/Volumes/video/Movies/English/1080P HD")
list2.append("/Volumes/video/Movies/English/720P")
list2.append("/Volumes/video/Movies/English/Divx")
list2.append("/Volumes/video/Movies/Malayalam")

contents["Ds418Play_TT"] = list2
f = open('Movie_Inventory.csv', 'w')
f.write("Network Drive,Mounted Path,File Or Folder\n")
for key, value_list in contents.items():
    for dir in value_list:
        data = os.listdir(dir)
        for item in data:
            dir = dir.replace("/Volumes/", "")
            f.write("{},{},{}\n".format(key, dir, item))
f.close()
