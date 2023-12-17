# import time
#
#
# # gmtime()
# print(time.gmtime())
#
# # time() => epoch : 1-1-1970 00:00:00
# print(time.time())
#
# # ctime
# print(time.ctime())
#
#
# # sleep
# """
# print(time.sleep(5))
# print("Hello word")
# """
#
# # srtftime()
# """
#     %Y  Year with century as a decimal number.
#     %m  Month as a decimal number [01,12].
#     %d  Day of the month as a decimal number [01,31].
#     %H  Hour (24-hour clock) as a decimal number [00,23].
#     %M  Minute as a decimal number [00,59].
#     %S  Second as a decimal number [00,61].
#     %z  Time zone offset from UTC.
#     %a  Locale's abbreviated weekday name.
#     %A  Locale's full weekday name.
#     %b  Locale's abbreviated month name.
#     %B  Locale's full month name.
#     %c  Locale's appropriate date and time representation.
#     %I  Hour (12-hour clock) as a decimal number [01,12].
#     %p  Locale's equivalent of either AM or PM.
# """
# print(time.strftime("%a"))
#
# # Calculation time
#
# # perf_counter => user
# print(time.perf_counter())
#
# # process_time => cpu
# print(time.process_time())


import  datetime

time_1 = datetime.time(5,4,3)
print(time_1)
"""
Arguments:

        hour, minute (required)
        second, microsecond (default to zero)
        tzinfo (default to None)
        fold (keyword only, default to zero)
        """

print(datetime.date(2024, 5,3))
"""
Arguments:

        year, month, day (required, base 1)
"""

