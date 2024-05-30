#!/bin/bash

cd code
python test.py -opt options/test/test_spsr.json
cd ..
python process_imgs.py
