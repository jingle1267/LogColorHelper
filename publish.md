# 打包上传步骤

### 1. 修改版本等信息

### 2. 打包


```
python3 setup.py sdist bdist_wheel
```

### 3. 发布上传

```
python3 -m twine upload dist/*
```

参考 https://github.com/pypa/twine
