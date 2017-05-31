

## Install Python 2.7
```shell=
wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz
tar xvfz Python-2.7.12.tgz
cd Python-2.7.12
./configure --prefix=/opt/python2.7 --enable-shared
make
make altinstall
```

## Offline Packages Installation

+ 下載套件  
`pip install --download=/path/to/packages/downloaded <packageName>`

+ 下載 requirement 套件列表  
`pip install --download=/path/to/packages/downloaded -r requirements.txt`

+ 安裝套件  
`pip install --download /path/to/download/to_packagename`

