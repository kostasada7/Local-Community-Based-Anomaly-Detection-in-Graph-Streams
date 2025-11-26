# Local-Community-Based-Anomaly-Detection-in-Graph-Streams
Identifying anomalous behavior by tracking the changes in local communities as networks evolve over time
This repository contains Python files for detecting anomalies by tracking how local communities evolve over time in dynamic graphs. The uploaded scripts are ready to run directly in Python. To ensure correct execution, the contents of the provided communities.zip file must be extracted into the same directory as the Python files. Once set up, the code runs without further adjustments.

The main driver of this program is **seed_set.py**, which loads the graph, selects the anchor node, and then calls **Dynamic_anchor_community**. This function incrementally updates the anchor-based community as new edges stream in, adjusting the structure whenever positive or negative interactions alter stability in the anchor’s neighborhood. It tracks edge changes, prunes the community when necessary, and periodically recomputes the anchor community to preserve coherence as the graph evolves.

After that, **weights_with_anchors.py** is used, containing two subfunctions that handle positive and negative edge events. These functions update internal and external connection counts for all affected nodes, and if the updated scores break the required ordering of the community, they remove the violating node (and potentially others) to maintain a stable, anchor-consistent community.

The remaining `.py` files serve as **supporting modules**, providing auxiliary functions, data handling, and structural operations needed by the main components to perform dynamic community detection effectively.
