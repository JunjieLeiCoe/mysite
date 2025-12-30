# 📊 CV Timeline Guide

## How to Update Your CV Timeline

The timeline is powered by JavaScript data in `/layouts/_default/cv.html`.

### Edit Timeline Data

Find this section in `cv.html` and modify:

```javascript
const timelineData = [
  // Education
  { 
    title: "博士 - 数据科学",      // Degree title
    institution: "XX大学",         // School name
    start: "2020-09",              // Start date (YYYY-MM)
    end: "2024-06",                // End date (YYYY-MM or "present")
    type: "education",             // Type: "education" or "work"
    color: "#3b82f6"               // Blue for education
  },
  
  // Work Experience
  { 
    title: "数据科学家",           // Job title
    institution: "Google",         // Company name
    start: "2024-07",
    end: "present",                // Use "present" for current job
    type: "work",
    color: "#22c55e"               // Green for work
  },
];
```

### Date Format

- **Format**: `"YYYY-MM"` (e.g., `"2024-01"` for January 2024)
- **Current job/study**: Use `"present"` for end date

### Colors

- **Education**: Blue `#3b82f6`
- **Work**: Green `#22c55e`
- **Custom**: Use any hex color code

### Example: Adding New Experience

```javascript
{ 
  title: "软件工程师",
  institution: "Microsoft",
  start: "2022-06",
  end: "2024-06",
  type: "work",
  color: "#22c55e"
},
```

## Features

✅ **Interactive Gantt Chart** - Visual timeline of your career  
✅ **Hover for Details** - Shows full information on hover  
✅ **Auto-scaling** - Adjusts to your date range  
✅ **Color-coded** - Blue for education, green for work  
✅ **Responsive** - Scrollable on mobile  
✅ **Print-friendly** - Download as PDF button  

## Tips

1. **Order doesn't matter** - Timeline auto-sorts by date
2. **Overlapping is OK** - Shows concurrent education/work
3. **Update both files** - `/content/cn/cv/_index.md` AND `/content/en/cv/_index.md`
4. **Keep data in sync** - Timeline data should match your CV text content

---

Your CV is now a living, interactive document! 📈✨

