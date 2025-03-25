# Power Profile Dataset for AES-GF Hardware Design

This repository contains the structured dataset of power profiles generated from the AES-GF hardware-optimized encryption design. The dataset includes layout-specific power consumption traces to support analysis, evaluation, and research in side-channel vulnerability and secure physical design.
 
## 📌 Overview

We used **AES-GF** as the baseline design, which integrates AES in Galois/Counter Mode (GCM) with Galois Field arithmetic for efficient authenticated encryption. The power profile data was generated following two key steps:

1. **Layout Database Generation**  
   A set of 100 unique hardware layouts of the AES-GF design were generated using custom physical design scripts and place-and-route tools.

2. **Power Trace Collection**  
   For each layout, 200,000 power traces were simulated and recorded. Each trace consists of **300 time-sampled current measurements**, capturing the dynamic power behavior under various operating conditions.

## 📁 Dataset Structure

The dataset is organized into folders for each layout (`Layout0` to `Layout100`), with power profiles collected from two key configurations (`key0` and `key1`).

```text
total_power_profile/
├── Layout0/
│   ├── key0/ Layout0.csv
│   └── key1/ Layout0.csv
├── Layout1/
│   ├── key0/ Layout1.csv
│   └── key1/ Layout1.csv
...
├── Layout100/
│   ├── key0/ Layout100.csv
│   └── key1/ Layout100.csv
```

Each `.csv` file contains the following columns:
- `sample_no` – Index of the sample point
- `time` – Time in seconds (s)
- `current` – Current consumption in Amperes (A)

## 🔍 Use Cases

This dataset is valuable for researchers and practitioners working on:

- Side-channel attack (SCA) resistance analysis
- Layout-level power modeling 
- Machine learning models for side-channel leakage analysis

## 🧠 Contributors

This dataset was prepared by researchers at Silda Lab, University of Florida. For questions, reach out via GitHub Issues or contact dsaha@ufl.edu

### Major Contributors
Dipayan Saha
Farimah Farahmandi
---

**Feel free to fork, use, and adapt this dataset with proper attribution.**
