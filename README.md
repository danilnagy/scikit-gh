# scikit-gh

Demo of connection between Rhino/Grasshopper and scikit-learn Machine Learning library for Python. 

- Uses Grasshopper Python node only for data handling inside model
- Launches remote Python process for analysis using scikit-learn
- Handles all dependencies for python numerical analyses outside Grasshopper (solves issue of getting numpy/scipy to work inside Grasshopper Python)