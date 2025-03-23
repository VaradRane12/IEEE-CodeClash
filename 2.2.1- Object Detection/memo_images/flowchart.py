from graphviz import Digraph

# Create a directed graph
dot = Digraph("Experimental_Pipeline", format="png")

# Define nodes
dot.node("A", "Input Images\n(No Fog, Medium Fog, Dense Fog)", shape="rect", style="filled", fillcolor="lightblue")
dot.node("B", "Contrast Enhancement\n(CLAHE Applied)", shape="rect", style="filled", fillcolor="lightgray")
dot.node("C", "Object Detection\n(YOLO Model)", shape="rect", style="filled", fillcolor="lightgreen")
dot.node("D", "IoU Evaluation\n(Compare Bounding Boxes)", shape="rect", style="filled", fillcolor="lightcoral")

# Define edges
dot.edge("A", "B", label="Enhance contrast")
dot.edge("B", "C", label="Detect objects")
dot.edge("C", "D", label="Calculate IoU")

# Save and render
dot.render("experimental_pipeline", view=True)
