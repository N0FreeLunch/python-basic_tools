Install
=======

install on ubuntu 20.04
-----------------------
```
sudo apt-get update
sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
wget -P /tmp https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
sha256sum /tmp/Anaconda3-2020.02-Linux-x86_64.sh
bash /tmp/Anaconda3-2020.02-Linux-x86_64.sh
```
(enter)(enter)(enter)(enter)(enter)
Do you approve the license terms? [yes|no]
```
yes
```
(enter)(enter)(enter)(enter)(enter)
by running conda init? [yes|no]
```
yes
```

after Install
-------------
```
source ~/.bashrc
```


UPDATE
------
```
conda update --all
```
Proceed ([y]/n)?
```
y
```

[Caution!!]:warning::warning::warning: Dont run this. anaconda3 remove process
------------------------------------------------------------------------------
```
rm -rf ~/anaconda3 ~/.condarc ~/.conda ~/.continuum
```

conda env setting
-----------------
```
  conda config --set auto_activate_base false
```

run conda env
-------------
```
  conda activate
```

run activate env
----------------
```
  conda deactivate
```

##Run python shell in this project folder
```
python
```
