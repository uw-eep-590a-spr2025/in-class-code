from functools import cmp_to_key


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
'2.0.4',
         '11.11.0',
'1.2.4',
'1.2.4-charlie',
'3.1.2-jun26',
'2.1.0',
'2.1.0-alpha']

def compare_by_prerelease(semver1, semver2):
    out1 = semver1.split('-')
    if len(out1) == 1:
        pass
    out2 = semver2.split('-')
    if len(out2) == 1:
        pass

    ## TODO: come back if we want and compare by pre-release string

## Return
def compare_semver(semver1, semver2):

    if '-' in semver1:
        main1, pre1 = semver1.split('-')
    else:
        main1, pre1 = semver1, ''

    if '-' in semver2:
        main2, pre2 = semver2.split('-')
    else:
        main2, pre2 = semver2, ''

    mmp1 = main1.split('.')
    mmp2 = main2.split('.')

    print(f'mmp1: {mmp1}; mmp2: {mmp2}')

    ## Check Major
    print(f'Comparing major: {mmp1[0]} vs {mmp2[0]}')
    if mmp1[0] != mmp2[0]:
        return int(mmp1[0]) - int(mmp2[0])

    print(f'Comparing minor: {mmp1[1]} vs {mmp2[1]}')
    if mmp1[1] != mmp2[1]:
        return int(mmp1[1]) - int(mmp2[1])

    print(f'Comparing patch: {mmp1[2]} vs {mmp2[2]}')
    if mmp1[2] != mmp2[2]:
        return int(mmp1[2]) - int(mmp2[2])

    print(f'Comparing prerelease: {pre1} vs {pre2}')
    if pre1 == '':
        return 1
    if pre2 == '':
        return -1
    if pre1 > pre2:
        return 1
    if pre2 < pre1:
        return -1
    return 0


    ## Check Minor

    ## ... so on


# out = compare_semver('3.1.2-jun26', '2.1.0')
# print(out)


sorted_list = sorted(input, key=cmp_to_key(compare_semver), reverse = True)

print(sorted_list)