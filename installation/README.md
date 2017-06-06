
## Install Python 2.7.10

+ SUSE SLEX 11-SP3 & Centos 6.7 適用
```shell=
wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz
tar xvfz Python-2.7.10.tgz
cd Python-2.7.10
./configure --prefix=/opt/python2.7 --enable-shared --with-zlib --with-threads
make
make altinstall
echo "/opt/python2.7/lib" >> /etc/ld.so.conf.d/opt-python2.7.conf
ldconfig
```

## Linux install pip

```shell=
curl -O https://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz
tar xvfz pip-1.2.1.tar.gz
cd pip-1.2.1
zypper install python-setuptools
python setup.py install
ln -sfn /usr/local/bin/pip /usr/bin/pip
```
### pip usage

```shell=
pip show <packageName>
```



## Offline Packages Installation

+ [方法一] goto and download: https://pypi.python.org/pypi/pip?

```shell=
xvfz pip-9.0.1.tar.gz
cd pip-9.0.1
python setup.py install
```

+ [方法二] pip下載套件  
`pip install --download=/path/to/packages/downloaded <packageName>`

+ 下載 requirement 套件列表  
`pip install --download=/path/to/packages/downloaded -r requirements.txt`

+ 安裝套件  
`pip install --download /path/to/download/to_packagename`




## [小進階] Virtualenv
### Install virtualenv

+ goto and download: https://pypi.python.org/pypi/virtualenv?

```shell=
xvfz virtualenv-15.1.0.tar.gz
cd virtualenv-15.1.0
python setup.py install
```

### virtualenv usage

+ 建立專案
`virtualenv <projectName>`
+ 開啟環境所使用Python版本
`virtualenv -p <opt/Python2.7/bin/Python2.7> <projectName>`
 - 或是直接將預設虛擬環境指定好 `vi ~/.bashrc`
 `export VIRTUALENVWRAPPER_PYTHON=/opt/Python2.7/bin/Python2.7`
+ 必須啟動才生效
  `source <projectPath>/bin/activate`

> Ref
+ http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/#virtualenvironments-ref

## Other Issue for SuSe

> pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.

```shell=
zypper install openssl
zypper install openssl-devel
# 然後重新compile python2.7就行惹
```



