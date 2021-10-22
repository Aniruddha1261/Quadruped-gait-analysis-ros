# Quadraped-gait-analysis-ros
---

## Domains:

### Table of content

- [About the project](#about-the-project)
    - [Tech stack](#1tech-stack)
    - [File structure](#file-structure)
- [Getting Started](#getting-started)
   - [Installations](#1-installations)
   - [Quick start](#2-quick-start)
- [Results](#results)
- [resources](#acknowledgements-and-resources)
---
## About the project
As its name suggests, Quadruped Robots have four legs or limbs and follow the gait patterns of quadruped animals. They are faster and more stable than biped robots. Depending on their leg structure, they can be broadly classified into two categories, Mammal-type and Sprawling-type.
The aim of this project is to perform teleoperation(keyboard), forward simulation, obstacle avoidance, turning and reverse motion of a quadruped in ROS/ROS2 using Gazebo simulator.
#### 1.Tech stack
 - We are using Gazebo simulator for the simulation and motion of robot.
 - For further refrence [gazebo](http://gazebosim.org/)
#### 2.File structure 

    
## Domains:
- Forward and inverse kinematics 
- Gait Analysis and Generations
- Mapping in Ros
- Configurations of planners and controllers.
- Ros.
- Simulation (Gazebo)

### File Structure
## Getting Started
### Prerequisites
1. **Ros noetic**
2. **Gazebo**
3. **Rviz**
### 1. Installations

   ### 1.1 Cloning the git repo of champ and installing all dependencies:
     
    sudo apt install -y python-rosdep
    cd <your_ws>/src
    git clone --recursive https://github.com/chvmp/champ
    git clone https://github.com/chvmp/champ_teleop
    cd ..
    rosdep install --from-paths src --ignore-src -r -y
  
 ###  2. Build your workspace: 
    cd <your_ws>
    catkin_make
    source <your_ws>/devel/setup.bash


### 2. Quick Start
   ### 2.1 Walking demo in RVIZ:

#### 2.1.1 Run the base driver:

    roslaunch champ_config bringup.launch rviz:=true

#### 2.1.2 Run the teleop node:

    roslaunch champ_teleop teleop.launch

### 2.2 Using gazebo
#### 2.2.1 Run the Gazebo environment:

    roslaunch champ_config gazebo.launch 
![gazebo_simulation](idhar bhi photo)

#### 2.2.2 Command for teleoperation
press the ```Tab``` after this command  

    rostopic pub /cmd_vel geometry msgs/Twist "linear:
image after publishing
![gazebo](idhar link dalna hai video ka)

## Results 
Quadruped robots can be made to walk on planes as well as rough surfaces. They have the most stable configuration among the multi legged robots.
They can be used for transportation on a small scale like for household purposes as well as in factories.
## Future works
## Contributors
[Chaitanya Deshpande](https://github.com/ChaitanyaSRA)
## Acknowledgements and resources
