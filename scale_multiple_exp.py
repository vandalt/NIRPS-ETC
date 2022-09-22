import numpy as np
from pandas import read_csv

etc_input_file = "etc_targets_input_pisco.txt"
etc_results_file = "etc_targets_output_pisco.txt"

scaled_output_file = "scaled_etc_output.csv"

input_params = read_csv(etc_input_file, sep=r"\s+", header=0, comment="#")
etc_results = read_csv(etc_results_file, sep=r"\s+", header=0, comment="#")

snr_cols = [c for c in etc_results.columns if "S/N" in c]

n_exp = input_params["n_exp"]

scaled_etc_results = etc_results.copy()
scaled_etc_results[snr_cols] = etc_results[snr_cols].multiply(np.sqrt(n_exp.values), axis="rows")

total_time_hr = input_params["t_exp"] * n_exp / 3600.0
scaled_etc_results["tot_time(hr)"] = total_time_hr

scaled_etc_results.to_csv(scaled_output_file, sep=",", index=False)
