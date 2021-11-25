# Predicting Remaining Useful Life (RUL) of EV Batteries

The purpose of this project is to predict RUL of EV batteries by estimating _Battery Capacity_ using indirect discharge cycle parameters. A thorough EDA is performed after which pertinent features are extracted from the data. Seven different learning models are trained on data from one battery but are tested on other batteries as well.

The dataset used in the project was obtained from the [Prognostics Centre of Excellence](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/). 

### Directory Structure

```
.
├── README.md
├── datasets
│   ├── README.txt
│   ├── data.zip
│   └── save_data_as_pickle.py
├── images
│   ├── mlp_blue.png
│   └── model.png
├── requirements.txt
└── src
    └── Predicting RUL of EV Batteries.ipynb
```

#### Dataset Citation
B. Saha and K. Goebel (2007). "Battery Data Set", NASA Ames Prognostics Data Repository (http://ti.arc.nasa.gov/project/prognostic-data-repository), NASA Ames Research Center, Moffett Field, CA
