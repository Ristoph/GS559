import sys
import fibber

user_num = int(sys.argv[1])
if len(sys.argv) == 2:
    print fibber.fibber(user_num)
elif len(sys.argv) == 3:
    user_first = int(sys.argv[2])
    print fibber.fibber(user_num, user_first)
elif len(sys.argv) == 4:
    user_first = int(sys.argv[2])
    user_second = int(sys.argv[3])
    print fibber.fibber(user_num, user_first, user_second)