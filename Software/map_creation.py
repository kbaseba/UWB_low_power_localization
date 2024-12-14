import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
from shapely.geometry import Polygon as ShapelyPolygon, box

from testbench_tools import simulation_configuration_setup
from Central_Hub.Sector_Assignment.sector_assignment import SectorAssignment
from Central_Hub.Leader_Selection.leader_selection import LeaderSelection

from Central_Hub.Swarm_Coordination.frontier_identification import FrontierIdentification

class Map:
    def __init__(self, plot_metrics, width=100, height=100, num_obstacles=10, light_variation=True):
        self.width = width
        self.height = height
        self.map_grid = np.zeros((height, width))  # 0 = free space
        self.obstacles = []
        self.num_obstacles = num_obstacles
        self.generate_obstacles()
        self.light_map = np.ones((height, width))  # Default light intensity = 1
        
        if light_variation:
            self.generate_light_intensity()

        if plot_metrics == False:
            self.fig, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = plt.subplots(2, 2, figsize=(10, 10))

        # Initialize a matrix to represent the map
        self.map_matrix = np.zeros((100, 100))

        # Metrics for plotting
        self.low_power_percentages = []
        self.map_accuracy_history = []
        self.map_coverage_history = []


    def generate_obstacles(self):
        """Generate non-overlapping obstacles."""
        max_attempts = 100
        for _ in range(self.num_obstacles):
            for attempt in range(max_attempts):
                shape_type = np.random.choice(["rectangle", "circle", "polygon"])
                if shape_type == "rectangle":
                    x, y = np.random.randint(5, self.width - 15), np.random.randint(5, self.height - 15)
                    w, h = np.random.randint(5, 15), np.random.randint(5, 15)
                    if not self._check_overlap("rectangle", x, y, w, h):
                        self.obstacles.append(("rectangle", x, y, w, h))
                        break
                elif shape_type == "circle":
                    cx, cy = np.random.randint(10, self.width - 10), np.random.randint(10, self.height - 10)
                    r = np.random.randint(3, 8)
                    if not self._check_overlap("circle", cx, cy, r):
                        self.obstacles.append(("circle", cx, cy, r))
                        break
                elif shape_type == "polygon":
                    num_points = np.random.randint(3, 6)
                    points = np.random.randint(0, min(self.width, self.height), size=(num_points, 2))
                    if not self._check_overlap("polygon", points=points):
                        self.obstacles.append(("polygon", points))
                        break

    def _check_overlap(self, shape_type, *args, **kwargs):
        """Check if the new obstacle overlaps with existing obstacles."""
        new_geom = None
        if shape_type == "rectangle":
            x, y, w, h = args
            new_geom = box(x, y, x + w, y + h)
        elif shape_type == "circle":
            cx, cy, r = args
            new_geom = ShapelyPolygon([(cx + r * np.cos(theta), cy + r * np.sin(theta)) for theta in np.linspace(0, 2 * np.pi, 100)])
        elif shape_type == "polygon":
            points = kwargs["points"]
            new_geom = ShapelyPolygon(points)

        for obs in self.obstacles:
            if obs[0] == "rectangle":
                x, y, w, h = obs[1:]
                existing_geom = box(x, y, x + w, y + h)
            elif obs[0] == "circle":
                cx, cy, r = obs[1:]
                existing_geom = ShapelyPolygon([(cx + r * np.cos(theta), cy + r * np.sin(theta)) for theta in np.linspace(0, 2 * np.pi, 100)])
            elif obs[0] == "polygon":
                existing_geom = ShapelyPolygon(obs[1])

            if new_geom.intersects(existing_geom):
                return True
        return False

    def generate_light_intensity(self):
        """Create varying light intensities with realistic attached shadows."""
        # Simulate a light source at the top center of the map
        light_source = (self.width / 2, 0)  # Top center of the map

        # Start with a uniform gradient background
        gradient = np.linspace(1.0, 0.5, self.height).reshape(-1, 1)
        self.light_map *= gradient

        # Add shadows for each obstacle
        for obstacle in self.obstacles:
            if obstacle[0] == "rectangle":
                x, y, w, h = obstacle[1:]
                self._generate_rectangle_shadow(x, y, w, h, light_source)

            elif obstacle[0] == "circle":
                cx, cy, r = obstacle[1:]
                self._generate_circle_shadow(cx, cy, r, light_source)

            elif obstacle[0] == "polygon":
                points = obstacle[1]
                self._generate_polygon_shadow(points, light_source)

    def _generate_rectangle_shadow(self, x, y, w, h, light_source):
        """Generate shadow for a rectangle."""
        rect_corners = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        shadow_polygon = self._extend_shadow(rect_corners, light_source)
        self._apply_shadow_to_polygon(shadow_polygon, shadow_value=0.5)

    def _generate_circle_shadow(self, cx, cy, r, light_source):
        """Generate shadow for a circle."""
        circle_points = [
            (cx + r * np.cos(theta), cy + r * np.sin(theta))
            for theta in np.linspace(0, 2 * np.pi, 100)
        ]
        shadow_polygon = self._extend_shadow(circle_points, light_source)
        self._apply_shadow_to_polygon(shadow_polygon, shadow_value=0.5)

    def _generate_polygon_shadow(self, points, light_source):
        """Generate shadow for a polygon."""
        shadow_polygon = self._extend_shadow(points, light_source)
        self._apply_shadow_to_polygon(shadow_polygon, shadow_value=0.5)

    def _extend_shadow(self, points, light_source, length=20):
        """Extend the shadow from object points away from the light source."""
        shadow_points = []
        for x, y in points:
            dx, dy = x - light_source[0], y - light_source[1]
            magnitude = np.sqrt(dx**2 + dy**2) + 1e-6  # Avoid division by zero
            shadow_x = x + length * (dx / magnitude)
            shadow_y = y + length * (dy / magnitude)
            shadow_points.append((shadow_x, shadow_y))
        return points + shadow_points[::-1]  # Combine original and shadow points

    def _apply_shadow_to_polygon(self, points, shadow_value):
        """Apply shadow to a given polygon area with high resolution."""
        from matplotlib.path import Path

        # Create a high-resolution grid for accurate shadow calculation
        x, y = np.meshgrid(
            np.linspace(0, self.width, self.width * 10),
            np.linspace(0, self.height, self.height * 10),
        )
        grid_points = np.stack((x.flatten(), y.flatten()), axis=-1)

        # Define the polygon path for the shadow
        poly_path = Path(points)

        # Check which points in the high-res grid fall within the polygon
        mask = poly_path.contains_points(grid_points).reshape(x.shape)

        # Downsample the high-res mask back to the original resolution
        downsampled_mask = mask[::10, ::10]

        # Apply the shadow value to the light map
        self.light_map[downsampled_mask] *= shadow_value
    
    def update(self, sectors, robots, hub, sensor_node_positions, anchor_positions, hub_position, map_accuracy):
        # Clear the axis and redraw
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        """Visualize the map with optional overlays for sectors and nodes."""
        self.ax1.imshow(self.light_map, cmap='gray', origin='lower')

        # Draw each obstacle
        for obs in self.obstacles:
            if obs[0] == "rectangle":
                _, x, y, w, h = obs
                self.ax1.add_patch(Rectangle((x, y), w, h, color='blue', alpha=0.9))
            elif obs[0] == "circle":
                _, cx, cy, r = obs
                self.ax1.add_patch(Circle((cx, cy), r, color='blue', alpha=0.9))
            elif obs[0] == "polygon":
                _, points = obs
                poly = Polygon(points, closed=True, color='blue', alpha=0.9)
                self.ax1.add_patch(poly)

        # Overlay sectors with black dotted lines
        if sectors:
            for sector in sectors:
                x_start, x_end, y_start, y_end = sector
                rect = Rectangle((x_start, y_start), x_end - x_start, y_end - y_start, 
                                edgecolor='black', facecolor='none', linestyle='--', linewidth=1)
                self.ax1.add_patch(rect)

        # Overlay nodes as x's or o's
        if sensor_node_positions:
            for x, y in sensor_node_positions:
                self.ax1.plot(x, y, 'rx', markersize=6)  # Red 'x' for nodes

        if anchor_positions:
            for x, y in anchor_positions:
                self.ax1.plot(x, y, 'o', markersize=14, color='yellow')

        if hub_position:
            self.ax1.plot(hub_position[0], hub_position[1], 'go', markersize=18)

        # if len(robot.esimate_history) > 20:
        for robot in robots:
            # Extract x and y coordinates for the trajectory, ignoring the first 10 estimates
            x_history = [state[0, 0] for state in robot.estimate_history[10:]]  # x-coordinates from 21st onwards
            y_history = [state[1, 0] for state in robot.estimate_history[10:]]  # y-coordinates from 21st onwards

            # Plot the path
            self.ax2.plot(x_history, y_history, color='black', label=f'Robot {robot.id}')  # Add a label if robots have IDs

        for robot in robots:
            # Determine the marker color based on battery level
            if 0 <= robot.power_level <= 32:
                marker_color = 'red'
            elif 32 < robot.power_level <= 65:
                marker_color = 'yellow'
            elif 65 < robot.power_level <= 100:
                marker_color = 'green'
            else:
                marker_color = 'gray'  # Fallback for invalid battery levels

            # Get the most recent position
            if len(robot.estimate_history) > 0:  # Ensure there are enough estimates
                last_state = robot.position_history[-1]  # Only the most recent state
                x_last, y_last = last_state[0, 0], last_state[1, 0]

                # Plot only the most recent point
                # self.ax3.scatter(x_last, y_last, color=marker_color, s=100, label=f'Robot {robot.id} ({robot.power_level}%)')
                
                # Annotate the power level next to the dot
                self.ax3.text(x_last, y_last, f'{int(robot.power_level)}%', fontsize=10, color=marker_color)
        
        # Calculate the average percentage of time spent in low power
        if robots:
            low_power_percentages = [
                robot.time_spent_low_power / (robot.time_spent_active + robot.time_spent_low_power) * 100
                for robot in robots if robot.time_spent_active + robot.time_spent_low_power > 0
            ]
            average_low_power_percentage = sum(low_power_percentages) / len(low_power_percentages) if low_power_percentages else 0
        else:
            average_low_power_percentage = 0

        for x,y in hub.collisions:
            self.ax1.plot(x, y, 'o', markersize=2, color='red')
            self.ax2.plot(x, y, 'o', markersize=2, color='red')

        for position in hub.curr_localizations:
            self.ax1.plot(position[0], position[1], 'o', markersize=2, color='green')

        # Set self.axis limits and title
        self.ax1.set_xlim(0, self.width)
        self.ax1.set_ylim(0, self.height)
        self.ax1.set_title("Actual Map")
        
        self.ax2.set_xlim(0, self.width)
        self.ax2.set_ylim(0, self.height)
        
        self.ax2.set_title(f"Map Accuracy: {map_accuracy.update():.2f}%")

        self.ax3.set_xlim(0, self.width)
        self.ax3.set_ylim(0, self.height)
        self.ax3.set_title(f"Avg. Low Power: {average_low_power_percentage:.2f}%")

        # Set a fixed resolution for the grid (similar to FrontierIdentification)
        matrix_height = 100  # Fixed grid height
        matrix_width = 100  # Fixed grid width


        # Update the map matrix based on robot estimate history
        for robot in robots:
            for point in robot.position_history:
                x, y = point[0, 0], point[1, 0]
                # Convert continuous coordinates to the fixed resolution grid
                grid_x = min(max(round((x / self.width) * (matrix_width - 1)), 0), matrix_width - 1)
                grid_y = min(max(round((y / self.height) * (matrix_height - 1)), 0), matrix_height - 1)
                self.map_matrix[grid_y, grid_x] = 1  # Mark the cell as visited

        # Optionally include collision points for additional coverage
        for point in hub.collisions:
            x, y = point[0], point[1]
            grid_x = min(max(round((x / self.width) * (matrix_width - 1)), 0), matrix_width - 1)
            grid_y = min(max(round((y / self.height) * (matrix_height - 1)), 0), matrix_height - 1)
            self.map_matrix[grid_y, grid_x] = 2  # Mark the cell as a collision

        # Visualize the updated map matrix
        self.ax4.imshow(self.map_matrix, cmap='magma', interpolation='nearest')

        # Calculate map coverage percentage
        map_discovery = np.count_nonzero(self.map_matrix > 0) / (matrix_height * matrix_width) * 100

        # Set the title with the formatted percentage
        self.ax4.set_title(f"Map Coverage Percentage: {map_discovery:.2f}%")


    def calculate_metrics(self, robots, hub, map_accuracy):
        matrix_height = 100  # Fixed grid height
        matrix_width = 100  # Fixed grid width

        # Calculate average low power percentage
        if robots:
            low_power_percentages_timestep = [
                robot.time_spent_low_power / (robot.time_spent_active + robot.time_spent_low_power) * 100
                for robot in robots if robot.time_spent_active + robot.time_spent_low_power > 0
            ]
            average_low_power_percentage = sum(low_power_percentages_timestep) / len(low_power_percentages_timestep) if low_power_percentages_timestep else 0
        else:
            average_low_power_percentage = 0

        # Append to the history list
        self.low_power_percentages.append(average_low_power_percentage)

        # Update map accuracy
        current_map_accuracy = map_accuracy.update()
        self.map_accuracy_history.append(current_map_accuracy)

        # Update the map matrix based on robot estimate history
        for robot in robots:
            for point in robot.position_history:
                x, y = point[0, 0], point[1, 0]
                # Convert continuous coordinates to the fixed resolution grid
                grid_x = min(max(round((x / self.width) * (matrix_width - 1)), 0), matrix_width - 1)
                grid_y = min(max(round((y / self.height) * (matrix_height - 1)), 0), matrix_height - 1)
                self.map_matrix[grid_y, grid_x] = 1  # Mark the cell as visited

        # Optionally include collision points for additional coverage
        for point in hub.collisions:
            x, y = point[0], point[1]
            grid_x = min(max(round((x / self.width) * (matrix_width - 1)), 0), matrix_width - 1)
            grid_y = min(max(round((y / self.height) * (matrix_height - 1)), 0), matrix_height - 1)
            self.map_matrix[grid_y, grid_x] = 2  # Mark the cell as a collision

        # Update map coverage percentage
        map_discovery = np.count_nonzero(self.map_matrix > 0) / (matrix_height * matrix_width) * 100
        self.map_coverage_history.append(map_discovery)

    
    def plot_metrics(self):
        """
        Plots percent low power, map accuracy, and map coverage as three separate scatter plots.

        Parameters:
        - low_power_percentages: List of average low power percentages at different time steps.
        - map_accuracy_history: List of map accuracy values at different time steps.
        - map_coverage_history: List of map coverage values at different time steps.
        """
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # Create 3 subplots side by side

        # Plot Low Power Percentages
        axes[0].scatter(range(len(self.low_power_percentages)), self.low_power_percentages, color='red')
        axes[0].set_title("Low Power Percentage Over Time")
        axes[0].set_xlabel("Time Step")
        axes[0].set_ylabel("Low Power Percentage (%)")

        # Plot Map Accuracy
        axes[1].scatter(range(len(self.map_accuracy_history)), self.map_accuracy_history, color='blue')
        axes[1].set_title("Map Accuracy Over Time")
        axes[1].set_xlabel("Time Step")
        axes[1].set_ylabel("Map Accuracy (%)")

        # Plot Map Coverage
        axes[2].scatter(range(len(self.map_coverage_history)), self.map_coverage_history, color='green')
        axes[2].set_title("Map Coverage Over Time")
        axes[2].set_xlabel("Time Step")
        axes[2].set_ylabel("Map Coverage (%)")

        # Adjust layout for clarity
        plt.tight_layout()
        plt.show()