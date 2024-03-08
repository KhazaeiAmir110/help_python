from caculat_distanc import CaculatDistanc
from animate import Animate

"""
طول و عرض جغرافیایی برحسب درجه
"""
# # new york
# x1 = 40.7128
# y1 = -74.0060

# # lyon
# x1=45.7597
# y1=4.8422

# # london
# x2 = 51.5072
# y2 = -0.1276

"""
شهر سینسیناتی، ایالت اوهایو در ایالات متحده آمریکا
"""
# Cincinnati
# x1 =-84.412977
# y1 = 39.152501
#
# x2 = -84.412946
# y2 = 39.152505

x1, y1 = 35.6895, 139.6917  # مختصات توکیو، ژاپن
x2, y2 = 40.7128, -74.0060  # مختصات نیویورک، ایالات متحده

one=CaculatDistanc(x1, y1, x2, y2)
two=Animate(x1, y1, x2, y2)

print("We have the distance of ",one.distance(),"K.M from the two point :)")

two.start()


#####(40.7128,-74.0060,51.5072,-0.1276) new york to london => 5570.242313172575 K.M
