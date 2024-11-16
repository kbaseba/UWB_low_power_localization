# Engineering plan

## Contribution 1

### Motivation

*What is a specific problem that we'd currently like to solve, but can't with the existing science?*

Centimeter-level localization and environment exploration for battery-free autonomous robot swarms.

### Contribution

*What is the additional knowledge that would enable that problem to be solved?*

- How can insect-scale robots achieve localization with sub-milliwatt power using only onboard components?
- Does inter-swarm communication methods improve exploration efficiency given individual power constraints?
  - Inter robot communication vs centralized communication hub
- How can UWB localization be duty-cycled and integrated with BLE to maximize power efficiency?
  - Dynamic leader nodes
- How do we effectively estimate the state of nodes given the low frequency of localization
  - Onboard vs. Hub
    - Kalman Filtering, etc.
- What path planning algorithm best balances power harvesting with optimal landscape coverage?

### Results

*What data will be necessary to capture and communicate that new knowledge?  That is, what data will demonstrate:*

To validate our solution, we will produce these specific metrics and data:

- **Localization Accuracy**: Measure average error in centimeters and success rate across different environments and swarm densities.

- **Power Consumption**: Record per-robot power usage (µW or mW) during localization cycles to confirm operation under 1mW.

- **Localization Range**: Determine the maximum range that maintains centimeter-level accuracy as swarm density changes.

- **Anchor Optimization**: Measure localization accuracy relative to anchor node density, identifying the minimum nodes required for optimal precision.

- **Path Planning Efficiency**: Track area coverage (%) and energy usage per robot, balancing navigation accuracy with power savings.

- **Control Comparison**: Collect accuracy, range, and power data from standard vs. optimized setups to demonstrate performance gains from our approach.

### Experiment

*What experiment(s) will generate that specific data?*

#### Experiment Setup

The experiment will use a **2D gridworld simulation**, dividing the landscape into sectors with adjustable parameters:

- **Node Density**: Robots per sector, varied from sparse to dense.
- **Light Intensity**: Simulates power harvesting capability.
- **Anchor Node Placement**: Different anchor patterns and densities.
- **Communication Frequency**: Duty cycling for UWB/BLE.
- **Environment Complexity**: Number and shape of objects, including shadows.

##### General Experiment Setup

- **Node Density**: Test various robot densities to assess localization accuracy and range impact.
- **Anchor Placement**: Experiment with anchor patterns and densities to optimize localization precision.
- **Energy Availability**: Adjust light intensity to simulate varying power availability per sector.
- **Duty Cycling**: Test different UWB/BLE duty cycles to balance power efficiency and localization needs.
- **Environment Complexity**: Adjust the number and shape of obstacles, and vary the light intensity profiles (shadows).

##### Baseline Test Setup

The baseline test will use **fixed settings**:

- **Non-duty-cycled UWB/BLE** for continuous localization.
- **Random anchor placement** with sparse coverage.
- **Uniform node density** and **consistent light intensity** to simulate standard, low-power conditions.

##### Specific Experiments to Generate Data

1. **Localization Accuracy**: Measure average localization error (cm) across configurations by varying **node density** and **anchor placements**.

2. **Power Consumption**: Record per-cycle power usage (<1mW).

3. **Localization Range**: Determine maximum range with centimeter accuracy under different node densities and anchor configurations.

4. **Anchor Optimization**: Test different anchor node densities to identify the minimum number needed for optimal localization accuracy.

5. **Path Planning Efficiency**: Use light intensity and duty cycles to track area coverage (%) and energy consumption, assessing path planning efficiency.

6. **Control Comparisons**: Run baseline tests to benchmark localization accuracy, range, and power usage, validating improvements from optimized configurations.
