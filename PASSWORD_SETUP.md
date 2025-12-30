# 🔒 Privacy Features Guide

## Feature 1: Redacted Text (FBI-style Black Bars)

### Usage:
Use the `redacted` shortcode to hide sensitive text:

```markdown
我的密码是 {{</* redacted */>}}secret123{{</* /redacted */>}}
```

**Result:** 我的密码是 ███████

### Examples:
- Hide names: 我在 {{</* redacted */>}}Google{{</* /redacted */>}} 工作
- Hide numbers: 年薪 {{</* redacted */>}}$150k{{</* /redacted */>}}
- Hide locations: 住在 {{</* redacted */>}}北京{{</* /redacted */>}}

---

## Feature 2: Password-Protected Posts

### Step 1: Generate Password Hash

Run this in your browser console or use an online tool:

```javascript
async function hashPassword(password) {
  const encoder = new TextEncoder();
  const data = encoder.encode(password);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

// Example:
hashPassword("mypassword").then(hash => console.log(hash));
```

**Or use this Python script:**

```python
import hashlib

password = "mypassword"
hash_value = hashlib.sha256(password.encode()).hexdigest()
print(hash_value)
```

### Step 2: Create Protected Post

In your blog post front matter:

```markdown
---
title: "私密文章"
date: 2024-01-01
layout: "protected"
password_hash: "your_hash_here"
tags: ["私密"]
---

This content will be password protected!
```

### Step 3: How It Works

- Post appears in blog listing (title visible)
- When clicked, shows password prompt 🔒
- Enter correct password to unlock
- Content stays unlocked during browser session
- No password stored in plain text (only SHA-256 hash)

---

## Examples

### Common Password Hashes:

| Password    | SHA-256 Hash |
|-------------|--------------|
| `password`  | `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8` |
| `secret`    | `2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b` |
| `admin123`  | `240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9` |

### Example Posts:

**1. Partially Redacted (public post with hidden text):**
```markdown
---
title: "工作日志"
date: 2024-01-15
tags: ["工作"]
---

今天面试了 {{</* redacted */>}}5个候选人{{</* /redacted */>}}，
选择了 {{</* redacted */>}}张三{{</* /redacted */>}} 加入团队。
```

**2. Fully Protected (requires password):**
```markdown
---
title: "私密日记"
date: 2024-01-20
layout: "protected"
password_hash: "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
tags: ["日记", "私密"]
---

这里是只有我能看到的内容...
```

---

## Security Notes

⚠️ **Important:**
- Password protection is **client-side** (JavaScript-based)
- Not 100% secure (someone could inspect page source)
- Good for: Personal diaries, draft posts, semi-private content
- NOT for: Truly confidential information

For real security, use a private repository or don't publish sensitive content!

---

## Styling

Both features work in light and dark modes automatically! 🌓


