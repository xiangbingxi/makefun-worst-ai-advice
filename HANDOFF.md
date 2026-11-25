# HANDOFF — worst-ai-advice (u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

## 文案（用户亲口原话，一字不改）

To feel less anxious about your unread emails, mark them all as read and let the next person who follows up pick your priorities.

- 字符数：129（上限 140，符合）
- 字节数：129（纯 ASCII，UTF-8）
- 无尾随换行
- sha256（entry.txt）：c7614c2d795012f3c9ebf03fd180a40a806b3fa201aaf06a985ae31228a43f35

## 做法

- `main.py` 把文案常量 `ENTRY` 一字不改写入 `/output/entry.txt`（UTF-8、无尾随换行、不读外部文件、不联网）。
- main.py 写了两次：第一版只写文件并跑通；第二版是真正的改进——写完后把文件读回来，和 `ENTRY` 逐字比对，不一致则报错退出（exit 1）。
- 其余文件亲手写：LICENSE（MIT，含 SPDX 行）、README.md（投稿说明 + 比赛页链接 + 三枚官方徽章）、prompt.txt（文案原文单行）、.makefun/owner.json、HANDOFF.md。

## 校验结果

- 两次运行 `python3 main.py` 均 exit 0（第二版含读回校验）。
- 两次输出立即取到私有副本比对：`cmp` 一致，逐字节相同。
- 两次输出均为 129 字节 / 129 字符，sha256 均为 c7614c2d795012f3c9ebf03fd180a40a806b3fa201aaf06a985ae31228a43f35，无尾随换行。
- 注意：本机 `/output/entry.txt` 和 `/tmp` 是多工人共享路径，验收中途曾被其他同场工人的输出覆盖；最终校验用的是每次运行后立即复制到本任务私有目录的副本，不受共享路径影响。

## 未做

- 未提交、未建 GitHub 仓、未碰 bundle。
