import csv
import re


with open('unilist.csv', 'r') as g:
    the_reader = csv.reader(g)
    scanned = []

    for row in the_reader:
        if row:
            query = row[0].lower()
            if re.search(r'uniten', query):
                scanned.append("UNITEN")
            elif re.search(r'tenaga', query):
                scanned.append('UNITEN')
            elif re.search(r'msu', query):
                scanned.append('MSU')
            elif re.search(r'management science', query):
                scanned.append('MSU')
            elif re.search(r'putra', query):
                scanned.append('UPM')
            elif re.search(r'upm', query):
                scanned.append('UPM')
            elif re.search(r'unisel', query):
                scanned.append('UNISEL')
            elif re.search(r'selangor', query):
                scanned.append('UNISEL')
            elif re.search(r'uum', query):
                scanned.append('UUM')
            elif re.search(r'utara', query):
                scanned.append('UUM')
            elif re.search(r'kelantan', query):
                scanned.append('UMK')
            elif re.search(r'umk', query):
                scanned.append('UMK')
            elif re.search(r'usm', query):
                scanned.append('USM')
            elif re.search(r'science', query):
                scanned.append('USM')
            elif re.search(r'sains malaysia', query):
                scanned.append('USM')
            elif re.search(r'utm', query):
                scanned.append('UTM')
            elif re.search(r'universiti teknologi malaysia', query):
                scanned.append('UTM')
            elif re.search(r'umt', query):
                scanned.append('UMT')
            elif re.search(r'terengganu', query):
                scanned.append('UMT')
            elif re.search(r'ump', query):
                scanned.append('UMP')
            elif re.search(r'pahang', query):
                scanned.append('UMP')
            elif re.search(r'universiti malaya', query):
                scanned.append('UM')
            elif re.search(r'malaya', query):
                scanned.append('UM')
            elif re.search(r'uitm', query):
                scanned.append('UITM')
            elif re.search(r'utem', query):
                scanned.append('UTEM')
            elif re.search(r'unimas', query):
                scanned.append('UNIMAS')
            elif re.search(r'malaysia sarawak', query):
                scanned.append('UNIMAS')
            elif re.search(r'unitar', query):
                scanned.append('UNITAR')
            elif re.search(r'southampton', query):
                scanned.append('Southamton')
            elif re.search(r'perdana', query):
                scanned.append('PERDANA')
            elif re.search(r'inti', query):
                scanned.append('INTI')
            elif re.search(r'city university', query):
                scanned.append('CITY')
            elif re.search(r'northern university', query):
                scanned.append('UUM')
            elif re.search(r'small', query):
                scanned.append('Small Changes')
            elif re.search(r'persatuan mahasiswa hindu', query):
                scanned.append('UTM')
            elif re.search(r'upsi', query):
                scanned.append('UPSI')
            elif re.search(r'imu', query):
                scanned.append('IMU')
            elif re.search(r'unikl', query):
                scanned.append('UniKL')
            elif re.search(r'ukm', query):
                scanned.append('UKM')
            elif re.search(r'national university of malaysia', query):
                scanned.append('UKM')
            elif re.search(r'kebangsaan malaysia', query):
                scanned.append('UKM')
            elif re.search(r'ums', query):
                scanned.append('UMS')
            elif re.search(r'kdu', query):
                scanned.append('KDU')

            else:
                print(query)


    print("There are " + str(len(scanned)) + " items in uni")

    uni_checked = []
    for item in scanned:
        if item not in uni_checked:
            uni = item
            i = 0
            for check in scanned:
                if uni == check:
                    i += 1
            print(uni + " = " + str(i))
            uni_checked.append(item)
