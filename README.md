# Local-Community-Based-Anomaly-Detection-in-Graph-Streams
Identifying anomalous behavior by tracking the changes in local communities as networks evolve over time
This repository contains Python files for detecting anomalies by tracking how local communities evolve over time in dynamic graphs. The uploaded .py scripts are ready to run directly in Python. To ensure correct execution, the contents of the provided communities.zip file must be extracted into the same directory as the Python files. Once set up, the code runs without further adjustments.

The output of the scripts is the detected local community at each time step. We can then compare these results against the ground truth communities (from the communities file) to evaluate whether the detected community diverges from the expected structure over time.
