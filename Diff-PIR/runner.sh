#!/bin/bash

python resizer.py --dir $1
python main_ddpir_deblur.py $2
python result_collector.py
python visualizer.py --dir testsets/processed_images
python visualizer.py --dir deblurred_results