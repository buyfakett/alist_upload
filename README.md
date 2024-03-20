# qiniu_upload

需要在config目录下创建config.yaml

```yaml
alist_url: xxx
username: xxx
password: xxx
```

然后运行脚本，第一个参数是文件所在路径，第二个参数是上传后的路径+名字

```shell
docker run -it --rm \
--name alist_upload \
-v ./config/:/app/config/ \
-v /data/:/data/ \
registry.cn-hangzhou.aliyuncs.com/buyfakett/alist_upload \
python3 main.py /data/xxx.zip xxx.zip
```