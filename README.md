# LunarCrush Social Analytics Dashboard

A comprehensive social analytics dashboard leveraging LunarCrush API v4 to analyze creator profiles, community interactions, and content performance for grant evaluation purposes.

## 🚀 Overview

This project provides an exhaustive analysis framework for evaluating social media creators using LunarCrush's powerful social analytics API. Originally designed for the Stacks DeGrants Phase III Grant Program, it enables treasury committees to make data-driven funding decisions based on social presence, engagement quality, and ecosystem alignment.

## 🎯 Key Features

### 📊 Interactive Dashboard (`index.html`)
- **Creator Profile Analysis**: Comprehensive creator metrics including followers, rank, and 24h interactions
- **Grant Evaluation System**: Automated scoring with recommendation engine (CONDITIONAL APPROVE/APPROVE/REJECT)
- **Top Community Visualization**: Interactive cards showing top interactors with profile images and engagement metrics
- **Topic Influence Analysis**: Chart.js visualizations showing topic distribution and Stacks ecosystem alignment
- **Content Intelligence**: Sentiment analysis, keyword frequency, and engagement metrics
- **Viral Posts Display**: Interactive tweet cards with engagement bars and sentiment indicators

### 🔍 Analytics Capabilities
- **Social Score Calculation**: Multi-factor scoring system (followers, engagement, ecosystem alignment, network quality)
- **Network Intelligence**: Community analysis with influence metrics and quality scoring
- **Temporal Patterns**: Growth tracking and activity pattern analysis
- **Stacks Ecosystem Alignment**: Keyword-based relevance scoring for blockchain ecosystem fit

## 🛠️ Technical Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Tailwind CSS (CDN)
- **Charts**: Chart.js for data visualization
- **API**: LunarCrush API v4
- **Data Format**: JSON for structured analytics output

## 📁 Project Structure

```
lunarcrush-setup/
├── index.html              # Main dashboard application
├── requirements.txt        # Python dependencies (if using analysis scripts)
├── LICENSE                 # MIT License
├── lunar.md               # LunarCrush API documentation
├── lunarcrushapi.md       # Additional API reference
└── README.md              # This file
```

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Clone the repository
git clone <repository-url>
cd lunarcrush-setup

# Install dependencies (if using Python scripts)
pip install -r requirements.txt
```

### 2. Configure API Access
Create a `.env` file with your LunarCrush API key:
```env
LUNARCRUSH_API_KEY=your_api_key_here
```

### 3. Launch Dashboard
Simply open `index.html` in your web browser. The dashboard includes hardcoded sample data for demonstration purposes.

## 📊 Dashboard Sections

### Creator Profile
- Avatar and basic information
- Follower count and social rank
- 24-hour interaction metrics
- Topic influence breakdown

### Grant Evaluation
- **Recommendation Engine**: Automated grant decision (CONDITIONAL APPROVE/APPROVE/REJECT)
- **Overall Score**: Composite score out of 100
- **Strategic Score**: Ecosystem alignment assessment
- **Visual Indicators**: Color-coded cards with progress bars

### Top Community
- **Interactive Cards**: Profile images with ranking badges
- **Engagement Metrics**: Interaction counts and progress bars
- **Community Stats**: Total members, interactions, and averages
- **Hover Effects**: Smooth animations and scaling

### Topic Influence Analysis
- **Bar Chart**: Topic frequency and distribution
- **Stacks Alignment**: Ecosystem relevance scoring
- **Keyword Analysis**: Content theme identification

### Content Intelligence
- **Sentiment Distribution**: Pie chart showing emotional tone
- **Keyword Frequency**: Bar chart of most-used terms
- **Content Summary**: Post counts and engagement averages
- **Sentiment Overview**: Positive/neutral/negative breakdown

### Viral Posts
- **Interactive Tweet Cards**: Custom-designed cards replacing unreliable Twitter embeds
- **Engagement Visualization**: Relative performance bars
- **Sentiment Indicators**: Emoji-based emotional scoring
- **Clickable Links**: Direct access to original tweets

## 🎨 Design Features

- **Dark Theme**: Professional dark color scheme optimized for data visualization
- **Mobile Responsive**: Adaptive layout for all screen sizes
- **Smooth Animations**: Hover effects, scaling, and transition animations
- **Gradient Backgrounds**: Modern visual appeal with color-coded sections
- **Interactive Elements**: Clickable cards, progress bars, and dynamic charts

## 📈 Analytics Methodology

### Social Score Calculation
The system uses a weighted scoring algorithm:

- **Followers (25%)**: Audience size and reach
- **Engagement (30%)**: Interaction quality and frequency
- **Ecosystem Alignment (35%)**: Stacks blockchain relevance
- **Network Quality (10%)**: Community influence and diversity

### Grant Recommendation Logic
- **CONDITIONAL APPROVE**: Score 50-70, good potential with monitoring
- **APPROVE**: Score 70-85, strong candidate
- **STRONG APPROVE**: Score 85+, exceptional fit
- **REJECT**: Score <50, insufficient metrics

## 🔧 API Integration

### LunarCrush API v4 Endpoints Used
- `/public/creator/:network/:id/v1` - Creator profile data
- `/public/creator/:network/:id/topics/v1` - Topic influence analysis
- `/public/creator/:network/:id/community/v1` - Community interactions
- `/public/creator/:network/:id/posts/v1` - Post content and metrics
- `/public/searches/search` - General search functionality

### Data Processing
- **Real-time Analysis**: Live API data processing
- **Caching Strategy**: Optimized for performance
- **Error Handling**: Graceful degradation for API failures
- **Data Validation**: Robust input sanitization

## 🎯 Use Cases

### Grant Evaluation
- **Stacks DeGrants**: Automated social presence assessment
- **Treasury Committees**: Data-driven funding decisions
- **Due Diligence**: Comprehensive creator analysis

### Social Media Analytics
- **Influence Measurement**: Community reach and engagement
- **Content Performance**: Viral post identification and analysis
- **Network Analysis**: Community structure and quality assessment

### Research Applications
- **Academic Studies**: Social media behavior analysis
- **Market Research**: Creator ecosystem mapping
- **Trend Analysis**: Topic influence and sentiment tracking

## 🚀 Future Enhancements

- **Multi-Platform Support**: Expand beyond Twitter/X
- **Real-time Updates**: Live data streaming
- **Advanced ML**: Predictive analytics and trend forecasting
- **Export Features**: PDF reports and data downloads
- **API Integration**: Additional social platforms and data sources

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📞 Support

For questions or support, please open an issue in the repository or contact the development team.

---

**Built with ❤️ for the Stacks ecosystem and social analytics community**
