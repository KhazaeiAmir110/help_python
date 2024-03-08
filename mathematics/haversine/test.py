import matplotlib.pyplot as plt

# مشخصات مکان‌ها
lat1, lon1 = 35.6895, 139.6917  # مختصات توکیو، ژاپن
lat2, lon2 = 40.7128, -74.0060  # مختصات نیویورک، ایالات متحده

plt.plot([lon1, lon2], [lat1, lat2], 'ro-')

plt.xlim(min(lon1, lon2) - 10, max(lon1, lon2) + 10)
plt.ylim(min(lat1, lat2) - 10, max(lat1, lat2) + 10)

plt.xlabel('طول جغرافیایی')
plt.ylabel('عرضجغرافیایی')

plt.title('خط بین دو نقطه')

plt.show()