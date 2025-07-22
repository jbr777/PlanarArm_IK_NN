# Inverse Kinematics with Neural Networks & Mixture Density Networks

This repository explores the use of neural networks (NN) and mixture density networks (MDN) to solve the inverse kinematics (IK) problem for a 2-link planar manipulator. The goal is to predict joint angles (`q1`, `q2`) from Cartesian end-effector coordinates (`x`, `y`).

## Project Structure

`train_ik_nn.ipynb`                     Trains a standard neural network for IK prediction           
`train_ik_mdn.ipynb`                    Trains a mixture density network (MDN) for multimodal IK     
`trajectory_planning.ipynb`             Plans and interpolates a path and evaluates model predictions
`workspace_plot_2link_robot.ipynb`      Visualizes the reachable workspace of the robot             
`planar_manipulator.py`                 `PlanarManipulator` class for FK, joint limits, and plotting 

---

## Problem Statement

Inverse kinematics is a **many-to-one** problem: for a given (x, y), multiple valid (q1, q2) pairs may exist (e.g., elbow-up vs. elbow-down). This makes it ideal for probabilistic models like MDNs, which can output multiple modes.

---

## Known Limitation 

**The neural network was trained on data generated within specific joint limits**  
> (`q1 ∈ [-π/2, π/2]`, `q2 ∈ [-π/3, π/3]`),  
> but the model itself was trained **without enforcing those joint constraints** in the loss function or output layer.  
> As a result, the network is free to extrapolate beyond the valid joint range.
> This results in predicted joint angles that are **out of bounds**

### How to detect this issue:
Use:
```python
robot.count_out_of_bounds(predicted_angles)
```
...to report how many predictions violate joint limits.

---

## What Works

- Forward kinematics verified  
- Elbow-up vs. elbow-down classification  
- MDN learns bimodal solutions in many cases 
- Animated comparison with analytical IK   
- Workspace-aware path planning using splines  

---

## To Improve

- Add loss penalty or post-processing for joint limits
- Explore constraint-aware learning or RL-based IK

---

