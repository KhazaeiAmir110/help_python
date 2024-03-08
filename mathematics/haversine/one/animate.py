import cartopy.crs as ccrs
import matplotlib.animation as animation
import matplotlib.pyplot as plt

class Animate:
    def __init__(self,lat1,lon1,lat2,lon2):
        self.lat1=lat1
        self.lon1=lon1
        self.lat2=lat2
        self.lon2=lon2

    def start(self):    
        ax = plt.axes(projection=ccrs.Robinson())
        ax.stock_img()
        #####get_one(40.7128,-74.0060,51.5072,-0.1276)

        [line] = plt.plot([self.lon1, self.lon2], [self.lat1, self.lat2],
                color='red', linewidth=7, marker='s',
                transform=ccrs.Geodetic(),
                )

        t_path = line._get_transformed_path()
        path_in_data_coords, _ = t_path.get_transformed_path_and_affine()


        # Draw the point that we want to animate.
        [point] = plt.plot(self.lon1, self.lat1, marker='s', transform=ax.projection)

        def animate_point(i):
            verts = path_in_data_coords.vertices
            i = i % verts.shape[0]
            # Set the coordinates of the line to the coordinate of the path.
            point.set_data(verts[i, 0], verts[i, 1])

        ani = animation.FuncAnimation(
            ax.figure, animate_point,
            frames= path_in_data_coords.vertices.shape[0],
            interval=125, repeat=True)

        ani.save('point_ani.gif', writer='blue')
        plt.show()

#p1=Animate(40.7128,-74.0060,51.5072,-0.1276)
#p1.start()
#####(40.7128,-74.0060,51.5072,-0.1276) new york to london
