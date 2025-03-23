import numpy as np
import matplotlib.pyplot as plt

# Sample IoU scores (Replace with actual computed values)
iou_scores = {
    "No Fog": 1.0,             # Perfect match (baseline)
    "Medium Fog": 0.8323,        # Replace with actual Medium Fog IoU
    "Dense Fog": 0.7625          # Replace with actual Dense Fog IoU
}

# Extract labels and values
labels = list(iou_scores.keys())
values = list(iou_scores.values())

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.bar(labels, values, color=['blue', 'orange', 'red'])

# Add titles and labels
plt.xlabel("Fog Conditions")
plt.ylabel("Average IoU Score")
plt.title("Comparison of IoU Across Fog Conditions")
plt.ylim(0, 1.1)  # IoU is always between 0 and 1

# Display values on bars
for i, v in enumerate(values):
    plt.text(i, v + 0.03, f"{v:.2f}", ha='center', fontsize=12)

# Show the plot
plt.show()
