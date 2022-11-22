# POPC_frames_archive
This archive provides a python script required to perform detector analysis in the paper:
"The Ultralong Chain of Cer[EOS] Shows an Intriguing Molecular Dynamics in Rigid Stratum Corneum Lipid Models"

by F. Fandrei, T. Havrisak, L. Opalka, O. Engberg, A. A. Smith, P. Pullmannova, N. Kucera, V. Ondrejcekova, B. Deme, L. Novalkova, M. Steinhart, K. Vavrova, D. Huster 

For this archive, the contact person is A. A. Smith 
albert.smith-penzel@medizin.uni-leipzig.de

The main script is linoleic_det_ana.py

There is NO INSTALLATION required for the code. Just place everything in a folder, navigate there, and run. However, python3 and the following modules must be installed from other sources (these are the tested versions, although other versions may work).

Python v. 3.7.3
numpy v. 1.17.2,
scipy v. 1.3.0,
MDAnalysis v. 0.19.2,
matplotlib v. 3.0.3

We recommend installing Anaconda: https://docs.continuum.io/anaconda/install/
The Anaconda installation includes numpy, scipy, pandas, and matplotlib. 

MDAnalysis is installed by running:
conda config --add channels conda-forge
conda install mdanalysis
(https://www.mdanalysis.org/pages/installation_quick_start/)

All files are copyrighted under the GNU General Public License. A copy of the license has been provided in the file LICENSE

Copyright 2022 Albert Smith-Penzel

This work was supported by DFG grant SM 576/1-1
(This applies to the detector analysis and code found here. The full paper was supported by additional funding and is the work of the authors listed above)