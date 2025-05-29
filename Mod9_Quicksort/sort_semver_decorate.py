from functools import cmp_to_key
from operator import itemgetter

'3.1.2-jun26'
'2.1.0'
'2.1.0-alpha'
'2.0.4'
'1.2.4'
'1.2.4-charlie'
'1.0.0-alpha'
'0.0.1-testing'

input = ['1.0.0-alpha',
'0.0.1-testing',
         '11.11.0',
         '1.2.4-alpha',
'2.0.4',
'1.2.4',
'1.2.4-charlie',
'3.1.2-jun26',
'2.1.0',
'2.1.0-alpha']


def compare_semver(semver_tuple_1, semver_tuple_2):
    if semver_tuple_1[0] != semver_tuple_2[0]:
        return semver_tuple_1[0] - semver_tuple_2[0]
    if semver_tuple_1[1] != semver_tuple_2[1]:
        return semver_tuple_1[1] - semver_tuple_2[1]
    if semver_tuple_1[2] != semver_tuple_2[2]:
        return semver_tuple_1[2] - semver_tuple_2[2]
    if semver_tuple_1[3] == '':
        return 1
    if semver_tuple_2[3] == '':
        return -1
    if semver_tuple_1[3] < semver_tuple_2[3]:
        return -1
    if semver_tuple_1[3] > semver_tuple_2[3]:
        return 1
    return 0

## Step 1: Decorate

def make_tuple(semver):
    if '-' in semver:
        main, prerelease = semver.split('-')
    else:
        main, prerelease = semver, ''
    major, minor, patch = main.split('.')
    return (int(major), int(minor), int(patch), prerelease, semver)

decorated = [make_tuple(x) for x in input]
print(decorated)

## Step 2: Sort

# decorated.sort(key=cmp_to_key(compare_semver), reverse = True)
decorated.sort(key= itemgetter(3))
print(decorated)
decorated.sort(key=itemgetter(0, 1, 2), reverse = True)

print(decorated)

## Step 3: Undecorate

sorted = [x[4] for x in decorated]
print(sorted)




