# Quadraped-gait-analysis-ros
---

### Table of content

- [About the project](#about-the-project)
    - [Tech stack](#tech-stack)
    <!-- - [File structure](#file-structure) -->
- [Getting Started](#getting-started)
   - [Installations](#1-installations)
   - [Quick start](#2-quick-start)
- [Results](#results)
- [resources](#resources)
---
## About the project
As its name suggests, Quadruped Robots have four legs or limbs and follow the gait patterns of quadruped animals. They are faster and more stable than biped robots. Depending on their leg structure, they can be broadly classified into two categories, Mammal-type and Sprawling-type.
The aim of this project is to perform teleoperation(keyboard), forward simulation, obstacle avoidance, turning and reverse motion of a quadruped in ROS/ROS2 using Gazebo simulator.
#### Tech stack
 - We are using Gazebo simulator for the simulation and motion of robot.
 - For further refrence [gazebo](http://gazebosim.org/)
<!-- #### 2.File structure 
- [Resources]()
- [images and video]() -->

    
## Domains:
- Forward and inverse kinematics 
- Gait Analysis and Generations
- Mapping in Ros
- Configurations of planners and controllers.
- Ros.
- Simulation (Gazebo)

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
![gazebo_simulation](https://github.com/Aniruddha1261/Quadruped-gait-analysis-ros/blob/f9d751f21d9cd5b621717ff34094627b9a2b8f81/img%20and%20video%20after%20teleop/Screenshot%20from%202021-10-22%2013-53-54.png)

#### 2.2.2 Command for teleoperation
press the ```Tab``` after this command  

    rostopic pub /cmd_vel geometry msgs/Twist "linear:
after publishing teleop operations
[![gazebo](https://github.com/Aniruddha1261/Quadruped-gait-analysis-ros/blob/c4bb1e4bbac1265e0eeed3668f1c279e53175240/img%20and%20video%20after%20teleop/pic%202.jpeg)](https://drive.google.com/file/d/1-4tTh6GlYbAnATi6XE0_TzINrJ437D7K/view?usp=sharing)
## Results 
Quadruped robots can be made to walk on planes as well as rough surfaces. They have the most stable configuration among the multi legged robots.
They can be used for transportation on a small scale like for household purposes as well as in factories.
## Future works
- Forward Simulation
- Obstracle Avoidance
## Contributors
- [Chaitanya Deshpande](https://github.com/ChaitanyaSRA)
- [Aniruddha Thakre](https://github.com/Aniruddha1261)
## Acknowledgements 
- #### [SRA VJTI](https://sravjti.in/) Eklavya 2021
## Resources

- #### [URDF exporting](https://youtu.be/T7X_p_KMwus)
- #### [Champ setup](https://github.com/chvmp/champ_teleop)
- #### [Ros](https://www.ros.org/)
- #### [Gazebo](http://gazebosim.org/)
- #### Teleoperations in Gazebo
   - [Youtube](https://www.youtube.com/watch?v=ufYxkNnEFYw)
   - [Robotics.com](https://www.generationrobots.com/blog/en/robotic-simulation-scenarios-with-gazebo-and-ros/)
   - [gazebosim.org](http://gazebosim.org/tutorials?tut=set_velocity)
   - [Velocity of joints](https://youtube.com/playlist?list=PLK0b4e05Lnzah3QAIsdb0JxAY21YypdZl)
- #### Gait Analysis
   - [website](https://cjme.springeropen.com/articles/10.1186/s10033-019-0321-2)
   - [Git repo](https://github.com/chaitravi-ce/Eklavya-QuadrupedMotionSimulation)
- #### Researh papers
   - [Kinematics](https://github.com/Aniruddha1261/Quadruped-gait-analysis-ros/blob/c4bb1e4bbac1265e0eeed3668f1c279e53175240/Resources/4c1fa16c13baef9e3102007eb48ca039-1.pdf)
   - [Inverse-Kinematic](https://github.com/Aniruddha1261/Quadruped-gait-analysis-ros/blob/c4bb1e4bbac1265e0eeed3668f1c279e53175240/Resources/Inverse-Kinematic-Analysis-Of-A-Quadruped-Robot.pdf)
   - [Swidwa Quadruped Gait Thesis](https://github.com/Aniruddha1261/Quadruped-gait-analysis-ros/blob/c4bb1e4bbac1265e0eeed3668f1c279e53175240/Resources/Swidwa_Quadruped_Gait_Thesis-2.pdf)
   - [Trotting Gait](https://github.com/Aniruddha1261/Quadruped-gait-analysis-ros/blob/c4bb1e4bbac1265e0eeed3668f1c279e53175240/Resources/TrottingGaitPlanningandImplementationforaLittleQuadrupedRobot.pdf)
