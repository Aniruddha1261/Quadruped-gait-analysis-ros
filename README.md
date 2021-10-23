# Quadraped-gait-analysis-ros
---

### Table of content
- [project]()
- [About the project](#about-the-project)
    - [Theory](#theory)
    - [Tech stack](#tech-stack)
    - [File structure](#file-structure) 
- [Getting Started](#getting-started)
   - [Prerequisites and installations](#prerequisites)
   - [Installations](#1-installations)
   - [Execution](#2-execution)
- [Results](#results)
- [Future Works](#future-works)
- [Contributors](#contributors)
- [Acknowledgement](#acknowledgements)
- [resources](#resources)
- [Licence](#licence)
---
## About the project
As its name suggests, Quadruped Robots have four legs or limbs and follow the gait patterns of quadruped animals. They are faster and more stable than biped robots. Depending on their leg structure, they can be broadly classified into two categories, Mammal-type and Sprawling-type.
The aim of this project is to perform teleoperation(keyboard), forward simulation, obstacle avoidance, turning and reverse motion of a quadruped in ROS/ROS2 using Gazebo simulator.
### Theory
   A Quadruped robot is a 4 legged robot which basically consists of a plane torso and 4 legs which have a revolute joint between them. In our case, the degree of freedom of the robot is 8. Quadruped robot simulation includes the detailed study of gaits and gait patterns. To make a quadruped robot move, we have to study about the gaits and plan the gaits for our tobot. It also includes the study of forward and inverse kinematics. Equations of forward and inverse kinematics are to be found for determination of position and configuration of legs. After the gait planning and implementation of forward and inverse kinematics, the robot is made to simulate in Gazebo simulator with the help of Ros.  
- #### Gaits:  
A quadruped robot can walk with statically and dynamically stable gaits. In the statically stable gait, each leg of the robot is lifted up and down sequentially, and there are three stance legs at the least at any moment. This type of gait is named creeping gaits. One gait cycle can be divided into eight different periods of movement. At the beginning of walking, the initial equivalent where four legs are in the stance phase. When one of the legs is lifted, it is transferred to the swing phase; we call this period the step forward stage. In this stage, the equivalent mechanism is. From this, the leg falls and is in contact with the ground until the next leg lifts off; this period is called the switching stage. The equivalent mechanism at this moment exhibits the same configuration as that of the initial period; however, the legs contain different position parameters with the initial period. Four legs of the quadruped robot repeat the motion individually in a certain order from the stance phase to the swing phase, to achieve walking using creeping gait. The step forward stage and switching stage occur alternately while the robot walks. The locomotion of the quadruped robot can be regarded as the movement of these series equivalent mechanisms. The figure below shows the sequence of equivalent mechanisms in one gait cycle. The efficiency of this gait is low because its minimum duty factor is 3/4.
#### Tech stack
 - We are using Gazebo simulator for the simulation and motion of robot.
 - For further refrence [gazebo](http://gazebosim.org/)
#### File structure 
 ![](https://github.com/Aniruddha1261/Quadruped-gait-analysis-ros/blob/9f77b1ad9f48fbf106736620f9b0c5b711b95bee/img%20and%20video%20after%20teleop/Tree1.PNG)  
 ![](https://github.com/Aniruddha1261/Quadruped-gait-analysis-ros/blob/9f77b1ad9f48fbf106736620f9b0c5b711b95bee/img%20and%20video%20after%20teleop/Tree2.PNG)

    
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

   ### 1.1 Cloning this git repo and installing all dependencies:
     
    sudo apt install -y python-rosdep
    cd <your_ws>/src
    git clone https://github.com/Aniruddha1261/Quadruped-gait-analysis-ros.git
    cd ..
    rosdep install --from-paths src --ignore-src -r -y
  
 ###  2. Build your workspace: 
    cd <your_ws>
    catkin_make
    source <your_ws>/devel/setup.bash


### 2. Execution
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

https://user-images.githubusercontent.com/84729149/138568596-dabf1efe-6adf-4f33-8cfd-7c2b6ae51507.mp4


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
#### Licence
[MIT licence](https://opensource.org/licenses/MIT)
