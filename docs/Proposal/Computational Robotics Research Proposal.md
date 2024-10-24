# Title: Battery-free Real-time Localization of [Autonomous](https://millimobile.cs.washington.edu) Robot Swarms Using UWB

### Summary:

There is no current approach for completely battery-free real-time localization of autonomous mobile robots. We aim to use the MilliMobile as the power harvesting sensory nodes for robotic swarm localization through the utilization of ultra wideband (UWB) technology for centimeter level precision and exploration of dynamic environments.

### Splash images



### Project git repo(s):

Example: [https://github.com/shushuai3/multi-robot-localization?tab=readme-ov-file](https://github.com/shushuai3/multi-robot-localization?tab=readme-ov-file)

Our Repository: https://github.com/kbaseba/UWB_low_power_localization/tree/main

## Big picture

### What is the overall problem that this and related research is trying to solve?

Battery-free autonomous robots such as the MilliMobile and Origami Microfliers, capable of operating on harvested solar and RF power, challenge the conventional notion that motion and actuation are beyond the capabilities of battery-free devices [1,2]. Through miniaturizing robots to the gram scale and enabling intermittent capacitor discharge to control locomotion, these robots can operate fully autonomously on as little as 50 μW of power or less [1]. While capable of aerial and land locomotion, these robots currently lack navigation and feedback control [1]. There are significant opportunities to enhance networking capabilities, establishing connectivity between these robots to enable large-scale swarms of battery-free robotic sensor nodes [1].

### Why should people (everyone) care about the problem?

Battery-free localization of autonomous, insect-scale robots using UWB will allow for long-term environmental sensing in hard to reach areas. The centimeter scale precision that UWB enables will allow users to deeply understand the dynamics of new environments as the robots autonomously path plan and explore maximizing power harvesting, as well as local discovery. This will open new areas for research in the areas of battery-free sensing and locomotion.

### What has been done so far to address this problem?

Extensive research has been done to create autonomous battery-free robots. Localization has previously been successful within the robotics community in many areas. The individual topics this research topic explores are by no means “novel”. The combination of all of these topics is what makes this research new. Combining localization techniques in a low-power manner and enabling this technology on insect-scale locomotive robotic is the unexplored path we aim to find new research outcomes.

## Specific project scope

### What subset of the overall big picture problem are you addressing in particular?

Overall, we aim to address both the hardware and software challenges this problem poses to us. Specifically, we will need to make hardware component changes to the current Millimobile implementation. We will need to select components for UWB communication that are optimized for low power environments. Additionally, we may need to update the onboard circuit itself, imploring a higher capacitance to store more voltage necessary for UWB communication. On the software side, we are posed with an entirely new subset of challenges. We need to prioritize the duty cycle of UWB communication as well as use swarms of these robots as effectively as possible so they do not die. We will use BLE communication between leader and follower nodes and potentially, leaders and followers may be dynamic. The communication rate and determination of where to explore is completely novel and we will need to create algorithms that maximize path planning in dynamic environments, as well as power harvesting within the swarm.

### How does solving this subproblem lead towards solving the big picture problem?

If successful, we will have enabled autonomous, insect-scale robots capable of locomotion to effectively explore dynamic environments in swarms and localize at the centimeter scale without the use of any battery or previously stored power.

### What is your specific approach to solving this subproblem?

We will attack the problem from both the hardware and software sides. We will create a simulated environment with constraint inputs which will help us to develop algorithms that optimize the power harvesting and path exploration of the robotic swarms. We will also be implementing this on hardware components and getting real power, current, and voltage measurements; informing us on the capabilities of the system and changes we need to make in the software implementation.

### How can you be reasonably sure this approach will result in a solution?

We aim to generate strict hardware requirements which we can feed as inputs into our software simulation. From this point we will find areas to optimize our system. This will generate results which we will aim to replicate (based on our measurements) in real-life. The use of the simulator in parallel with the hardware development will show us what constraints we need to abide by and the feasibility of our design overall.

### How will we know that this subproblem has been satisfactorily solved, using quantitative metrics?

We can map out the exploration of the robotic swarms and quantitatively see how much of the dynamic environment has been mapped, as well as the efficiency of the swarm overall in power harvesting and map exploration.

## Broader impact

(even if someone doesn't care about the big picture problem that you started with, why should they still care about the specific work that you've produced?  Who else can use your processes and results, and how?)

### What is the value of your approach beyond this specific solution?

### What is the value of this solution beyond solely solving this subproblem and getting us closer to solving the big picture problem?

## Background / related work / references

Located in ./doc/References

## System capabilities, validation deliverables, engineering tasks

### Concrete external deadlines (paper submissions):

\<TODO: discuss potential venues\>

### Detailed schedule (weekly capabilities / deliverables / tasks):

**Roles and Responsibilities:**

- All team members will work cohesively on the different aspects of the project, this is just for accountability and giving ownership to the different parts of the deliverables.

**Hardware:** Tilboon, Renish  
**Software:** Colin, Peter

**TASKS: 6-7? Weeks of ACTUAL work, 1-2 for presentation & submission**

1. Research of problem statement and related areas  
2. High-level block diagram of the system design. (General)  
3. Initial code implementation directly based on block diagram  
   1. Software-begin coding directly reflecting block diagram  
   2. Hardware-begin testing components power and current draw/generation for real-world constraints to input into the system  
4. Testing simulation/begin hardware implementation  
   1. Software-generate results for simulation  
      1. Generate multiple (monte-carlo) gridworld plot (video) that shows (given the real-world constraints) the motion of the robotic nodes as they explore a simulated environment. Shows when a robot dies, communication patterns, potential power levels, communication platform (UWB, vs BLE) etc  
   2. Hardware-begin implementing firmware  
5. Further software simulation to validate hypothesis, finish firmware algorithm implementation  
6. Test hardware application (real-world test)  
7. Presentation and submission preparation (also whatever tasks bleed over from previous weeks can be completed here)  
8. Paper writing

| Start Date | Capabilities | Tasks | Deliverables |
| :---: | ----- | ----- | ----- |
| Week 4 (10/21) | **Software**: Personal understanding of background material, ideas for system implementation **Hardware**: Personal understanding of background material, ideas for system implementation **General**: Create and update code base. Establish branches for development. | **Software**: Understand reference material and current state of the art algorithms in relation to localization techniques **Hardware**: Understand reference material and current state of the art localization technology **General**: Establish Github repository | **Software**: Google Doc literature review of current localization algorithms as it relates to this project and generate summary of implementation idea **Hardware**:  **General**: Google Doc literature review of current localization technology-generate summary of implementation idea  |
| Week 5 (10/28) | **General**: System block diagram | **General:** Based upon individual literature review individually generate system design ideas, meet to generate a system plan based on individual research and cited work, Justify validity of potential solution | **General:** In-depth block diagram of the entire system, with all inputs/outputs needed for each block. Each block represents a class, each class has an initialization and update function. |
| Week 6 (11/04) | **Software**: Initial code implementation **Hardware**: Component test results | **Software**: Based upon block diagram, implement codes/classes for system **Hardware**: Test the hardware components purchased in the previous week, and maintain a record of results. Setup the code environment and understand the microcontroller. | **Software**: Updated code base with initial implementation of block diagram **Hardware**: Based upon measurement, constrain the simulation capabilities. Firmware environment setup |
| Week 7 (11/11) | **Software**:  **Hardware**:  **General**: Re-evaluate status and update calendar accordingly | **Software**: Generate results for simulation **Hardware**: Begin firmware implementation **General**: Re-evaluate status and update calendar accordingly | **Software**: Generate multiple (monte-carlo) gridworld plot (video) that shows (given the real-world constraints) the motion of the robotic nodes as they explore a simulated environment. Shows when a robot dies, communication patterns, potential power levels, communication platform (UWB, vs BLE) etc. **Hardware**: Establish communication between nodes and generate measurements for power and current draw. **General:** Re-evaluate status and update calendar accordingly |
| Week 8 (11/18) | **Software**: Further testing of simulation and assisting with firmware development **Hardware**: Completed firmware for hardware application **General**: Plans for teaser video | **Software**: Based upon previous results, further test system. Generate more plots/videos for tentative results. Aso assist with firmware code implementation **Hardware**: Complete code implementation **General:** Start making the teaser video | **Software**: More test results (plots-videos) that show node motion in the environment given the constraints. Firmware implementation **Hardware**: Validate firmware implementation through real-world test using a few microcontrollers and measure constraints (power, current drawn, voltage, etc) **General:** Initial teaser video |
| Week 9 (11/25) | **General**: Real-world test of hardware/firmware, demonstrating validity of hypothesis (video for this) | **General:** Real-world testing on microcontrollers. Complete making the teaser video | **General:** Teaser video submission before 4 PM on **11/29** |
| Week 10 (12/02) | **General**: A thorough and concise presentation on our work done in the last 6 weeks. | **General**: Complete the entire presentation, including relevant figures, video clips, plots, code snippets | **General:** 16 minute project presentation before 4 PM on **12/06** |
| Week 11 (12/09) | **General:** Final paper that is professional enough for conferences | **General:** Complete the write-up by Thursday **(12/12)** | **General:** Project demo in class on **12/10** \-Submit final write up by **(12/13)** |

**Important dates:**

Renish \- 11/06 (2 Midterms) ; 12/09 (1 Final)  
Tilboon \- 10/30 (1 Midterm) ; 12/04 (1 Final)

