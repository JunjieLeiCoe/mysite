# Junjie Lei's Personal Website

A personal website built with Hugo and the hugo-paged theme, featuring a modern sidebar design with dark/light theme toggle.

## 🚀 Features

- **Left Sidebar Navigation** - Clean, modern sidebar with avatar and menu
- **Dark/Light Theme Toggle** - User preference saved in browser
- **Fully Responsive** - Mobile-friendly design
- **Multilingual** - Chinese (CN) and English (EN) support
- **Fast & Modern** - Built with Hugo static site generator

## 🛠️ Local Development

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) v0.153.3 or higher

### Running Locally

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# Start the Hugo development server
hugo server -D

# Visit http://localhost:1313/cn/ in your browser
```

## 📦 Project Structure

```
.
├── content/          # Content files (posts, pages)
│   ├── cn/          # Chinese content
│   └── en/          # English content
├── layouts/         # Custom layout overrides
├── static/          # Static files (images, CSS)
│   ├── css/
│   └── images/
├── themes/          # Hugo themes
│   └── hugo-paged/
└── hugo.yaml        # Site configuration
```

## 🎨 Customization

### Change Avatar

Replace `/static/images/avatar.svg` with your own image (supports .svg, .png, .jpg).

### Change Tagline

Edit `hugo.yaml`:

```yaml
params:
  tagline: "Your custom tagline here"
```

### Change Menu Items

Edit the `menu` section in `hugo.yaml`:

```yaml
menu:
  main:
    - name: "首页"
      url: "/cn/"
      weight: 1
    # Add more menu items...
```

### Customize Theme Colors

Edit `/static/css/custom.css` to modify colors for light and dark themes.

## 📝 Adding Content

### Create a new blog post (Chinese)

```bash
hugo new cn/blog/my-post.md
```

### Create a new blog post (English)

```bash
hugo new en/blog/my-post.md
```

## 🌐 Deployment

This site is automatically deployed to GitHub Pages using GitHub Actions.

Every push to the `main` branch triggers a new deployment.

### GitHub Pages URL

Your site will be available at:
- `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

Or if using a custom domain:
- `https://your-domain.com/`

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Theme based on [hugo-paged](https://github.com/yihui/hugo-paged) by Yihui Xie
- Inspired by [yihui.org](https://yihui.org) and [jinjipang.com](https://jinjipang.com)

---

© Junjie Lei 2025

