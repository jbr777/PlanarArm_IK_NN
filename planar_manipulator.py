import numpy as np
import matplotlib.pyplot as plt

class PlanarManipulator:
    def __init__(self, L1, L2, q1_lim, q2_lim):
        self.L1 = L1
        self.L2 = L2
        self.q1_min, self.q1_max = q1_lim
        self.q2_min, self.q2_max = q2_lim

    def within_joint_limits(self, q):
        q = np.atleast_2d(q)  # Ensures shape (N, 2)
        q1, q2 = q[:, 0], q[:, 1]
        valid_q1 = (self.q1_min <= q1) & (q1 <= self.q1_max)
        valid_q2 = (self.q2_min <= q2) & (q2 <= self.q2_max)
        return valid_q1 & valid_q2  # Returns boolean mask

    def forward_kinematics(self, q):
        q = np.atleast_2d(q)  # Ensure (N, 2)
        """
        is_valid = self.within_joint_limits(q)

        if not np.all(is_valid):
            raise ValueError("One or more joint configurations are outside the limits.")
        """
        q1, q2 = q[:, 0], q[:, 1]
        x1 = self.L1 * np.cos(q1)
        y1 = self.L1 * np.sin(q1)
        x2 = x1 + self.L2 * np.cos(q1 + q2)
        y2 = y1 + self.L2 * np.sin(q1 + q2)

        joint1_pos = np.stack([x1, y1], axis=1)  # Shape (N, 2)
        end_effector_pos = np.stack([x2, y2], axis=1)  # Shape (N, 2)

        return joint1_pos, end_effector_pos
    
    def plot(self, q1, q2, color='red', label='Robot'):
        q = np.array([[q1, q2]])
        joint1, ee = self.forward_kinematics(q)
        x1, y1 = joint1[0]
        x2, y2 = ee[0]
        plt.plot([0, x1, x2], [0, y1, y2], color=color, marker='o', label=label)
        plt.axis('equal')

    def count_out_of_bounds(self, q):
        q = np.atleast_2d(q)
        mask = self.within_joint_limits(q)
        total = len(mask)
        invalid = np.sum(~mask)
        print(f"Total samples: {total}")
        print(f"Out of bounds: {invalid} ({100 * invalid / total:.2f}%)")
        return invalid


