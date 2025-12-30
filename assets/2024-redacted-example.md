---
title: "如何使用文字遮挡功能"
date: 2024-05-10
draft: false
tags: ["教程"]
---

## FBI风格黑条遮挡

有时候你想写一些内容，但不想让所有人看到具体细节。

例如：我在 {{< redacted >}}某大公司{{< /redacted >}} 工作，年薪 {{< redacted >}}很高{{< /redacted >}}。

我的密码是 {{< redacted >}}admin123{{< /redacted >}} （开玩笑的）。

## 使用方法

在你的 markdown 文件中：

```markdown
这是普通文字，{{</* redacted */>}}这部分会被遮挡{{</* /redacted */>}}，这里又是普通文字。
```

显示效果：这部分会被遮挡 → ███████

完美保护隐私！ 🔒

