# Title: Battery-free Real-time Localization of [Autonomous](https://millimobile.cs.washington.edu) Robot Swarms Using UWB

### Summary:

There is no current approach for completely battery-free real-time localization of autonomous mobile robots. We aim to use the MilliMobile as the power harvesting sensory nodes for robotic swarm localization through the utilization of ultra wideband (UWB) technology for centimeter level precision and exploration of dynamic environments.

### Splash images

### 

### 

### 

### 

### Project git repo(s):

Example: [https://github.com/shushuai3/multi-robot-localization?tab=readme-ov-file](https://github.com/shushuai3/multi-robot-localization?tab=readme-ov-file)

Our Repository: https://github.com/kbaseba/UWB_low_power_localization

## Big picture

### What is the overall problem that this and related research is trying to solve?

Battery-free autonomous robots such as the MilliMobile and Origami Microfliers, capable of operating on harvested solar and RF power, challenge the conventional notion that motion and actuation are beyond the capabilities of battery-free devices \[1,2\]. Through miniaturizing robots to the gram scale and enabling intermittent capacitor discharge to control locomotion, these robots can operate fully autonomously on as little as 50 μW of power or less \[1\]. While capable of aerial and land locomotion, these robots currently lack navigation and feedback control \[1\]. There are significant opportunities to enhance networking capabilities, establishing connectivity between these robots to enable large-scale swarms of battery-free robotic sensor nodes \[1\].

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

## System capabilities, validation deliverables, engineering tasks

### Concrete external deadlines (paper submissions):

Include dates as well as target proposed title / abstract for expected submission

### Detailed schedule (weekly capabilities / deliverables / tasks):

**Roles and Responsibilities:**

- All team members will work cohesively on the different aspects of the project, this is just for accountability and giving ownership to the different parts of the deliverables.

**Hardware:** Tilboon, Renish  
**Software:** Colin, Peter

**TASKS: 6-7? Weeks of ACTUAL work, 1-2 for presentation & submission**

1. Research of problem statement and related areas  
   1. UWB  
   2. Localization techniques/algorithms in general  
   3. Hardware components and constraints (power, current, solar power generation)  
   4. Hardware cost  
2. High-level block diagram of the system design. (General)  
   1. Literature review  
   2. Algorithm creation  
   3. Understanding component selection and constraints  
   4. Localization techniques  
3. Begin code implementation directly based on block diagram  
4. Test simulation  
5. If testing is validated to our satisfaction, begin implementing algorithms on hardware  
6. Test hardware application (real-world test)  
7. Presentation and submission preparation (also whatever tasks bleed over from previous weeks can be completed here)

| Start Date | Goals | Tasks | Deliverables |
| :---: | ----- | ----- | ----- |
| Week 4 (10/21) | **Software**:  **Hardware**:  **General**: Literature review, code base setup, hardware component selection  | **Software**:  **Hardware**:  **General**:  | **Software**:  **Hardware**:  **General**:   |
| Week 5 (10/28) | **Software**:  **Hardware**:  **General**:  | **Software**:  **Hardware**:  **General:**  | **Software**:  **Hardware**:  **General:**  |
| Week 6 (11/04) | **Software**:  **Hardware**:  **General**:  | **Software**:  **Hardware**:  **General:**  | **Software**:  **Hardware**:  **General:**  |
| Week 7 (11/11) | **Software**:  **Hardware**:  **General**:  | **Software**:  **Hardware**:  **General:**  | **Software**:  **Hardware**:  **General:**  |
| Week 8 (11/18) | **Software**:  **Hardware**:  **General**:  | **Software**:  **Hardware**:  **General:**  | **Software**:  **Hardware**:  **General:**  |
| Week 9 (11/25) | **Software**:  **Hardware**:  **General**:  | **Software**:  **Hardware**:  **General:**  | **Software**:  **Hardware**:  **General:** Teaser video submission before 4 PM on **11/29** |
| Week 10 (12/02) | **Software**:  **Hardware**:  **General**:  | **Software**:  **Hardware**:  **General**:  | **Software**:  **Hardware**:  **General:** 16 minute project presentation before 4 PM on **12/06** |
| Week 11 (12/09) | Final paper writing | Complete the write-up by Thursday | \-Project demo in class on **12/10** \-Submit final write up by **(12/13)** |

