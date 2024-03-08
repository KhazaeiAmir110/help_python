from math import radians, cos, sin, asin, sqrt

class CaculatDistanc:

	def __init__(self,lat1,lon1,lat2,lon2):
		self.lat1=lat1
		self.lat2=lat2
		self.lon1=lon1
		self.lon2=lon2

	def distance(self):
		
		# طول و عرض جغرافیایی را به رادیان تبدیل میکنیم.
		lon1 = radians(self.lon1)
		lon2 = radians(self.lon2)
		lat1 = radians(self.lat1)
		lat2 = radians(self.lat2)
		
		# Haversine
		dlon = lon2 - lon1 
		dlat = lat2 - lat1
		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

		c = 2 * asin(sqrt(a)) 
		
		# Radius of earth in kilometers. Use 3956 for miles
		r = 6371
		
		# calculate the result
		return (c * r) 


	 
	

#p1=CaculatDistanc(40.7128,-74.0060,51.5072,-0.1276)	
#print(p1.distance(),"K.M")
#####(40.7128,-74.0060,51.5072,-0.1276) new york to london
