# archive search · 资料馆检索结果和人工判断审阅台

使用 Python 3.11 标准库，不需要联网、第三方包或数据库。输入示例使用本地合成记录。

```sh
python3 -m archive_search review data/sample.json
python3 -m unittest discover -s tests -v
```

输出为 UTF-8 JSON。输入文件不可读、业务引用无效或记录不符合口径时退出码为 2，同时报告原因。

## 记录口径

`queries` 包含 `group`、`weight` 和截断 `cutoff`。`runs` 按排序版本保存每个查询的片段编号顺序，同一榜单的片段不能重复。`judgments` 以 `collection/query/segment` 为键，`relevant` 为 0 或 1；编号相同但馆藏修订不同不能共用判断。
`pending` 是馆员已接到的补看单；`policy` 记录候选、当前排序、单组允许的变化量和每日审阅量。现有审阅表显示已核覆盖和各补看单的业务优先级。
