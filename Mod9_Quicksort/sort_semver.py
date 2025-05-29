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
         '13.11.0',
         '11.11.0-foo',
'2.0.4',
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
    print(f'Comparing {semver1} vs {semver2}')
    if '-' in semver1:
        main1, pre1 = semver1.split('-')
    else:
        main1, pre1 = semver1, ''

    if '-' in semver2:
        main2, pre2 = semver2.split('-')
    else:
        main2, pre2 = semver2, ''

    main1 = main1.split('.')
    main2 = main2.split('.')

    ## Check Major
    if main1[0] != main2[0]:
        return int(main1[0]) - int(main2[0])

    if main1[1] != main2[1]:
        return int(main1[1]) - int(main2[1])

    if main1[2] != main2[2]:
        return int(main1[2]) - int(main2[2])

    if pre1 == '':
        return 1
    if pre2 == '':
        return -1
    return pre1 - pre2


    ## Check Minor

    ## ... so on


# out = compare_semver('3.1.2-jun26', '2.1.0')
# print(out)

v1 = sorted(input, reverse= True)

print(v1)


sorted_list = sorted(input, key=cmp_to_key(compare_semver), reverse = True)

print(sorted_list)