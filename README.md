# 介绍

使用 [讯飞星火embeddings接口](https://www.xfyun.cn/doc/spark/embedding_api.html) 实现的简易知识库API。

# 用法

将你已开通讯飞星火embedding权限的appid、api_key、api_secret写入`search.py`。

将问题对以及已经查到的问题标识符、问题以及问题的embedding向量分别写入`subfeatures_dataset.csv`内的`Name`, `Description`, `Description Embeddings`。

启动 app.py

```python
python app.py
```

访问 `http://localhost:5000/search?description=<query>`。将query替换为你的要匹配的问题。例如`http://localhost:5000/search?description=话费怎么查`

接口将返回相似度由高到低的前五个问题的标识符以及得分。
```json
[
  {
    "score": 0.9682152555160143, 
    "subfeature": 5
  }, 
  {
    "score": 0.9043227799045512, 
    "subfeature": 3
  }, 
  {
    "score": 0.8832442272195338, 
    "subfeature": 1
  }, 
  {
    "score": 0.8672601961443654, 
    "subfeature": 4
  }, 
  {
    "score": 0.8264842492121457, 
    "subfeature": 2
  }
]
```