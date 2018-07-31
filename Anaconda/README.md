
# Anaconda3 for linux 
[64-Bit (x86) Installer (622 MB) ](https://www.anaconda.com/download/#linux)
Downloads Anaconda3-5.2.0-Linux-x86_64.sh

1. Downlaod Anacodna
2. install JupyterLab
3. install tensorflow


```shell=
wget ttps://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
bash Anaconda3-5.2.0-Linux-x86_64.sh
# yes
# PREFIX=/opt/Anaconda
# for all user
export PATH="/opt/Anaconda/bin:$PATH"
conda update conda
# conda: 4.5.4-py36_0 --> 4.5.8-py36_0
 
conda install -c conda-forge jupyterlab 
# certifi:    2018.4.16-py36_0 --> 2018.4.16-py36_0 conda-forge
# conda:      4.5.8-py36_0     --> 4.5.9-py36_0     conda-forge
# jupyterlab: 0.32.1-py36_0    --> 0.32.1-py36_0    conda-forge 
 
conda install -c conda-forge jupyterhub
#    alembic:                 0.9.9-py_0            conda-forge
#    appdirs:                 1.4.3-py_1            conda-forge
#    async_generator:         1.9-0                 conda-forge
#    automat:                 0.7.0-py36_0          conda-forge
#    configurable-http-proxy: 3.1.0-node8_1         conda-forge
#    constantly:              15.1.0-py_0           conda-forge
#    hyperlink:               17.3.1-py_0           conda-forge
#    incremental:             17.5.0-py_0           conda-forge
#    jupyterhub:              0.9.1-py36_0          conda-forge
#    libgcc:                  7.2.0-h69d50b8_2
#    mako:                    1.0.7-py_1            conda-forge
#    nodejs:                  8.10.0-0              conda-forge
#    pamela:                  0.3.0-py36_0          conda-forge
#    prometheus_client:       0.3.0-py_0            conda-forge
#    pyasn1:                  0.4.4-py_0            conda-forge
#    pyasn1-modules:          0.2.1-py_0            conda-forge
#    pyhamcrest:              1.9.0-py_2            conda-forge
#    python-editor:           1.0.3-py36_0          conda-forge
#    python-oauth2:           1.0.1-py36_0          conda-forge
#    service_identity:        17.0.0-py_0           conda-forge
#    twisted:                 18.7.0-py36h470a237_0 conda-forge
#    zope.interface:          4.5.0-py36h470a237_0  conda-forge
 
conda install tensorflow
# The following packages will be downloaded:
# 
#     package                    |            build
#     ---------------------------|-----------------
#     protobuf-3.5.2             |   py36hf484d3e_1         610 KB
#     tensorflow-base-1.9.0      |mkl_py36h2ca6a6a_0        75.7 MB
#     libprotobuf-3.5.2          |       h6f1eeef_0         4.2 MB
#     astor-0.7.1                |           py36_0          43 KB
#     certifi-2018.4.16          |           py36_0         142 KB
#     markdown-2.6.11            |           py36_0         104 KB
#     absl-py-0.3.0              |           py36_0         137 KB
#     grpcio-1.12.1              |   py36hdbcaa40_0         1.7 MB
#     gast-0.2.0                 |           py36_0          15 KB
#     twisted-17.5.0             |           py36_0         4.3 MB
#     tensorboard-1.9.0          |   py36hf484d3e_0         3.3 MB
#     tensorflow-1.9.0           |mkl_py36h6d6ce78_1           3 KB
#     _tflow_190_select-0.0.3    |              mkl           2 KB
#     termcolor-1.1.0            |           py36_1           7 KB
#     ------------------------------------------------------------
#                                            Total:        90.2 MB
# 
# The following NEW packages will be INSTALLED:
# 
#     _tflow_190_select: 0.0.3-mkl
#     absl-py:           0.3.0-py36_0
#     astor:             0.7.1-py36_0
#     gast:              0.2.0-py36_0
#     grpcio:            1.12.1-py36hdbcaa40_0
#     libprotobuf:       3.5.2-h6f1eeef_0
#     markdown:          2.6.11-py36_0
#     protobuf:          3.5.2-py36hf484d3e_1
#     tensorboard:       1.9.0-py36hf484d3e_0
#     tensorflow:        1.9.0-mkl_py36h6d6ce78_1
#     tensorflow-base:   1.9.0-mkl_py36h2ca6a6a_0
#     termcolor:         1.1.0-py36_1
# 
# The following packages will be UPDATED:
# 
#     certifi:           2018.4.16-py36_0         conda-forge --> 2018.4.16-py36_0
# 
# The following packages will be DOWNGRADED:
# 
#     twisted:           18.7.0-py36h470a237_0    conda-forge --> 17.5.0-py36_0
```

# jupyterhub

need small case useraccount

openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout jupyterhub.key -out jupyterhub.crt





