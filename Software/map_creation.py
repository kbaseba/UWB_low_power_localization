import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
from shapely.geometry import box, Point, Polygon as ShapelyPolygon


class MapCreation:
    def __init__(self, width=100, height=100, num_obstacles=10):
        self.width = width
        self.height = height
        self.num_obstacles = num_obstacles
        self.obstacles = []
        self.shadows = []
        self.generate_obstacles()

    def generate_obstacles(self):
        """Generate random obstacles."""
        max_attempts = 100
        for _ in range(self.num_obstacles):
            for attempt in range(max_attempts):
                shape_type = np.random.choice(["rectangle", "circle", "polygon"])
                if shape_type == "rectangle":
                    x, y = np.random.randint(5, self.width - 15), np.random.randint(5, self.height - 15)
                    w, h = np.random.randint(5, 15), np.random.randint(5, 15)
                    if not self._check_overlap("rectangle", x, y, w, h):
                        self.obstacles.append(("rectangle", x, y, w, h))
                        self._generate_shadow("rectangle", x, y, w, h)
                        break
                elif shape_type == "circle":
                    cx, cy = np.random.randint(10, self.width - 10), np.random.randint(10, self.height - 10)
                    r = np.random.randint(3, 8)
                    if not self._check_overlap("circle", cx, cy, r):
                        self.obstacles.append(("circle", cx, cy, r))
                        self._generate_shadow("circle", cx, cy, r)
                        break
                elif shape_type == "polygon":
                    num_points = np.random.randint(3, 6)
                    points = np.random.randint(0, min(self.width, self.height), size=(num_points, 2))
                    if not self._check_overlap("polygon", points=points):
                        self.obstacles.append(("polygon", points))
                        self._generate_shadow("polygon", points)
                        break

    def _check_overlap(self, shape_type, *args, **kwargs):
        """Check if the new obstacle overlaps with existing obstacles."""
        new_geom = None
        if shape_type == "rectangle":
            x, y, w, h = args
            new_geom = box(x, y, x + w, y + h)
        elif shape_type == "circle":
            cx, cy, r = args
            new_geom = Point(cx, cy).buffer(r)
        elif shape_type == "polygon":
            points = kwargs["points"]
            new_geom = ShapelyPolygon(points)

        for obs in self.obstacles:
            if obs[0] == "rectangle":
                x, y, w, h = obs[1:]
                existing_geom = box(x, y, x + w, y + h)
            elif obs[0] == "circle":
                cx, cy, r = obs[1:]
                existing_geom = Point(cx, cy).buffer(r)
            elif obs[0] == "polygon":
                existing_geom = ShapelyPolygon(obs[1])

            if new_geom.intersects(existing_geom):
                return True
        return False

    def _generate_shadow(self, shape_type, *args):
        """Generate a shadow as a duplicate shape offset by the light source direction."""
        shadow_offset = (-5, 5)  # Example light source direction
        if shape_type == "rectangle":
            x, y, w, h = args
            shadow_x = x + shadow_offset[0]
            shadow_y = y + shadow_offset[1]
            self.shadows.append(("rectangle", shadow_x, shadow_y, w, h))
        elif shape_type == "circle":
            cx, cy, r = args
            shadow_cx = cx + shadow_offset[0]
            shadow_cy = cy + shadow_offset[1]
            self.shadows.append(("circle", shadow_cx, shadow_cy, r))
        elif shape_type == "polygon":
            points = args[0]
            shadow_points = [(x + shadow_offset[0], y + shadow_offset[1]) for x, y in points]
            self.shadows.append(("polygon", shadow_points))

    def plot_map(self):
        """Visualize the map with obstacles and shadows."""
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')

        # Plot shadows
        for shadow in self.shadows:
            if shadow[0] == "rectangle":
                _, x, y, w, h = shadow
                ax.add_patch(Rectangle((x, y), w, h, color='gray', alpha=0.5))
            elif shadow[0] == "circle":
                _, cx, cy, r = shadow
                ax.add_patch(Circle((cx, cy), r, color='gray', alpha=0.5))
            elif shadow[0] == "polygon":
                _, points = shadow
                ax.add_patch(Polygon(points, closed=True, color='gray', alpha=0.5))

        # Plot obstacles
        for obs in self.obstacles:
            if obs[0] == "rectangle":
                _, x, y, w, h = obs
                ax.add_patch(Rectangle((x, y), w, h, color='blue', alpha=0.9))
            elif obs[0] == "circle":
                _, cx, cy, r = obs
                ax.add_patch(Circle((cx, cy), r, color='blue', alpha=0.9))
            elif obs[0] == "polygon":
                _, points = obs
                ax.add_patch(Polygon(points, closed=True, color='blue', alpha=0.9))

        ax.set_title("Map with Obstacles and Shadows")
        plt.show()


if __name__ == "__main__":
    map_creation = MapCreation(width=200, height=200, num_obstacles=30)
    map_creation.plot_map()
