# AI Agent Quick Start Guide
*Optimized for LLM understanding and task execution*

## 🎯 Repository Purpose
**Primary Function**: Social analytics dashboard for grant evaluation using LunarCrush API v4
**Target Use Case**: Stacks DeGrants Phase III Grant Program evaluation
**Core Technology**: HTML/CSS/JS dashboard with hardcoded JSON data

## 📁 File Structure & Purpose

```
lunarcrush-setup/
├── index.html                              # MAIN DASHBOARD (Primary file)
├── README.md                               # Human documentation
├── lunarcrush-api-technical-analysis.md    # Deep technical analysis
├── lunar.md                                # API documentation
├── lunarcrushapi.md                        # Additional API reference
├── lunarcrush-api-test.py                  # Python API testing script
├── lunar-crush-analytics-screenshot.png   # Dashboard preview image
└── LICENSE                                 # MIT License
```

## 🚀 Quick Start for AI Agents

### 1. **Primary File to Modify**: `index.html`
- **Location**: Root directory
- **Purpose**: Complete interactive dashboard
- **Technology**: Vanilla HTML/CSS/JS with Tailwind CSS (CDN)
- **Data Source**: Hardcoded JSON object (`jsonData`) starting at line ~81

### 2. **Key Dashboard Sections** (in order):
```html
<!-- Creator Profile -->
<div id="creator-profile"></div>

<!-- Grant Evaluation -->  
<div id="grant-evaluation"></div>

<!-- Top Community -->
<div id="top-community"></div>

<!-- Topic Influence Analysis -->
<canvas id="topic-influence-chart"></canvas>

<!-- Content Intelligence -->
<div id="content-intelligence-details"></div>

<!-- Viral Posts -->
<div id="viral-posts-container"></div>

<!-- Analysis Metadata -->
<div id="analysis-metadata"></div>
```

### 3. **JavaScript Functions** (Critical for modifications):
```javascript
// Core rendering functions
renderAnalysisMetadata(data)
renderCreatorProfile(data) 
renderGrantEvaluation(data)
renderTopCommunity(data)
renderTopicInfluenceAnalysis(data)
renderContentIntelligence(data)
renderViralPosts(posts)

// Data source
const jsonData = { /* hardcoded data object */ }
```

## 🔧 Common AI Agent Tasks

### **Task 1: Update Dashboard Data**
```javascript
// Modify the jsonData object (lines ~81-140)
// Structure: analysis_metadata, creator_profile, grant_evaluation, etc.
// All functions automatically re-render when page loads
```

### **Task 2: Add New Dashboard Section**
```html
<!-- Add HTML structure -->
<div>
    <h2 class="text-2xl font-bold mb-4 border-b border-gray-600 pb-2">New Section</h2>
    <div id="new-section"></div>
</div>

<!-- Add JavaScript function -->
function renderNewSection(data) {
    const container = document.getElementById('new-section');
    container.innerHTML = `<!-- HTML content -->`;
}

<!-- Add to DOMContentLoaded event -->
renderNewSection(jsonData.new_section_data);
```

### **Task 3: Modify Existing Visualizations**
- **Charts**: Use Chart.js (already loaded via CDN)
- **Styling**: Tailwind CSS classes (already loaded via CDN)
- **Data**: Modify `jsonData` object properties

### **Task 4: API Integration**
- **Current State**: Uses hardcoded data
- **API Script**: `lunarcrush-api-test.py` for testing
- **Integration**: Replace `jsonData` with API calls

## 📊 Data Structure Reference

### **Creator Profile Data**:
```javascript
creator_profile: {
    creator_name: "attractfund1ng",
    creator_display_name: "Blockface.btc", 
    creator_followers: 2226,
    creator_rank: 1064039,
    interactions_24h: 1672,
    top_community: [/* array of community members */]
}
```

### **Grant Evaluation Data**:
```javascript
grant_evaluation: {
    recommendation: "CONDITIONAL APPROVE",
    overall_score: 56,
    strategic_value: {
        overall_strategic_score: 80
    }
}
```

### **Viral Posts Data**:
```javascript
viral_posts: [{
    id: "1978914101788102670",
    title: "Q: Who are we building for? #APTOS",
    interactions: 1862,
    sentiment: 3,
    link: "https://x.com/attractfund1ng/status/..."
}]
```

## 🎨 Styling Guidelines

### **Color Scheme**:
- **Background**: `#1a202c` (dark gray)
- **Text**: `#cbd5e0` (light gray)
- **Cards**: `bg-gray-800` with `border-gray-700`
- **Accents**: Blue (`text-blue-400`), Green (`text-green-400`), Purple (`text-purple-400`)

### **Layout Patterns**:
```html
<!-- Standard section -->
<div>
    <h2 class="text-2xl font-bold mb-4 border-b border-gray-600 pb-2">Title</h2>
    <div id="content-container"></div>
</div>

<!-- Metric cards -->
<div class="bg-gradient-to-r from-blue-600 to-blue-800 rounded-lg p-4 text-center">
    <div class="text-2xl font-bold text-white">Value</div>
    <div class="text-blue-200 text-sm">Label</div>
</div>
```

## 🔍 API Integration Notes

### **LunarCrush API v4**:
- **Base URL**: `https://lunarcrush.com/api4`
- **Authentication**: Bearer token in Authorization header
- **Key Endpoints**:
  - `/public/creator/:network/:id/v1` - Creator data
  - `/public/creator/:network/:id/topics/v1` - Topic analysis
  - `/public/creator/:network/:id/community/v1` - Community data
  - `/public/creator/:network/:id/posts/v1` - Post data

### **Python Testing**:
```python
# Use lunarcrush-api-test.py for API validation
# Requires .env file with LUNARCRUSH_API_KEY
```

## ⚡ Performance Considerations

### **Current Optimizations**:
- **CDN Resources**: Tailwind CSS, Chart.js loaded via CDN
- **Hardcoded Data**: No API calls = instant loading
- **Efficient Rendering**: Functions only run on DOMContentLoaded

### **For API Integration**:
- **Caching**: Implement client-side caching for API responses
- **Error Handling**: Add try/catch blocks for API failures
- **Loading States**: Add loading indicators for async operations

## 🚨 Common Issues & Solutions

### **Issue 1: Charts Not Rendering**
```javascript
// Ensure Chart.js is loaded before rendering
document.addEventListener('DOMContentLoaded', () => {
    // Chart rendering functions here
});
```

### **Issue 2: Data Not Updating**
```javascript
// Modify jsonData object, then refresh page
// Or call render functions with new data
```

### **Issue 3: Styling Issues**
```html
<!-- Use Tailwind classes consistently -->
<!-- Check for conflicting CSS -->
<!-- Ensure proper HTML structure -->
```

## 🎯 Agent Task Templates

### **Template 1: Add New Metric**
```javascript
// 1. Add to jsonData
jsonData.new_metric = { value: 100, label: "New Metric" };

// 2. Add HTML
<div class="bg-gray-800 rounded p-4">
    <div class="text-xl font-bold text-white">${data.value}</div>
    <div class="text-gray-400">${data.label}</div>
</div>

// 3. Add render function
function renderNewMetric(data) {
    // Implementation
}
```

### **Template 2: Modify Chart**
```javascript
// 1. Update data structure
jsonData.chart_data = { labels: [...], datasets: [...] };

// 2. Modify Chart.js configuration
new Chart(ctx, {
    type: 'bar',
    data: jsonData.chart_data,
    options: { /* chart options */ }
});
```

## 📝 Development Workflow

### **For AI Agents**:
1. **Read**: `index.html` to understand current structure
2. **Modify**: `jsonData` object for data changes
3. **Add**: New HTML sections and JavaScript functions
4. **Test**: Open `index.html` in browser
5. **Iterate**: Refine based on visual results

### **File Priority Order**:
1. `index.html` (Primary dashboard)
2. `README.md` (Documentation updates)
3. `lunarcrush-api-test.py` (API testing)
4. Other files (Reference only)

## 🔗 External Resources

- **Live Demo**: https://blockface-lunarcrush-stacks-evals.netlify.app/
- **Tailwind CSS**: https://tailwindcss.com/docs
- **Chart.js**: https://www.chartjs.org/docs/
- **LunarCrush API**: https://lunarcrush.com/api4

---

**Note**: This repository is optimized for rapid prototyping and demonstration. The hardcoded data approach allows for immediate visualization without API setup complexity.
