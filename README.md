<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

<h1>🎓 Student's Real-Time Performance Insights Dashboard</h1>

<p>
  <span>⚛️ Streamlit</span> |
  <span>📊 Plotly</span> |
  <span>🤖 Scikit-learn</span> |
  <span>📂 Pandas</span>
</p>

<p>
  An interactive <b>Machine Learning Dashboard</b> built with <strong>Streamlit</strong> 
  for analyzing <b>student academic performance</b> and predicting <b>dropout risks</b>.  
  The system provides real-time predictions, visual insights, and personalized recommendations.
</p>

<hr>

<h2>📑 Table of Contents</h2>
<ul>
  <li><a href="#overview">📝 Project Overview</a></li>
  <li><a href="#features">✨ Features</a></li>
  <li><a href="#tech-stack">🛠 Tech Stack</a></li>
  <li><a href="#getting-started">🚀 Getting Started</a></li>
  <li><a href="#usage">🎮 Usage</a></li>
  <li><a href="#dashboard">📊 Dashboard Highlights</a></li>
  <li><a href="#contribute">🤝 Contributing</a></li>
</ul>

<hr>

<h2 id="overview">📝 1. Project Overview</h2>
<p>
The dashboard uses <b>Gradient Boosting Classifier</b> to predict whether a student is 
<b>at risk of dropping out</b> based on academic scores, absences, and demographic features.
It leverages <b>machine learning pipelines</b> with preprocessing (OneHotEncoding for categorical variables) 
and outputs both predictions and visualization-driven insights.
</p>

<h2 id="features">✨ 2. Features</h2>
<ul>
  <li>📈 Predicts student dropout risk in real time</li>
  <li>🧠 Uses Gradient Boosting Classifier for ML modeling</li>
  <li>🎨 Interactive visualizations powered by Plotly</li>
  <li>📊 Pie, Line, and Bar charts for insights</li>
  <li>🛠 Sidebar controls for exploring student data</li>
  <li>🚨 Personalized alerts & recommendations for at-risk students</li>
  <li>📚 Academic insights summary (accuracy, correlations, early indicators)</li>
</ul>

<h2 id="tech-stack">🛠 3. Tech Stack</h2>
<table>
  <tr><th>⚙️ Layer</th><th>🔧 Technology</th></tr>
  <tr><td>Frontend</td><td>🎨 Streamlit</td></tr>
  <tr><td>Data Handling</td><td>📂 Pandas</td></tr>
  <tr><td>Visualization</td><td>📊 Plotly Express</td></tr>
  <tr><td>Machine Learning</td><td>🤖 Scikit-learn (GradientBoostingClassifier)</td></tr>
</table>

<h2 id="getting-started">🚀 4. Getting Started</h2>

<h3>✅ Prerequisites</h3>
<ul>
  <li>Python 3.8+</li>
  <li>pip package manager</li>
</ul>

<h3>⚡ Installation</h3>
<pre><code>git clone https://github.com/your-username/student-risk-dashboard.git
cd student-risk-dashboard
pip install -r requirements.txt
</code></pre>

<h3>▶️ Run the App</h3>
<pre><code>streamlit run hi.py
</code></pre>
<p>
The app will start locally at <a href="http://localhost:8501" target="_blank">http://localhost:8501</a>.
</p>

<h2 id="usage">🎮 5. Usage</h2>
<ul>
  <li>📌 Select a student index from the sidebar</li>
  <li>📊 View dropout risk predictions & probabilities</li>
  <li>🚨 See alerts & recommendations tailored to the student</li>
  <li>📈 Explore performance trends across exams</li>
  <li>📉 Analyze absences vs dropout correlation</li>
</ul>

<h2 id="dashboard">📊 6. Dashboard Highlights</h2>
<ul>
  <li>🥧 <b>Dropout Risk Distribution:</b> Pie chart of at-risk vs not-at-risk students</li>
  <li>📈 <b>Performance Trends:</b> Line chart of G1, G2, G3 average scores</li>
  <li>📉 <b>Absences Impact:</b> Bar chart comparing average absences by risk group</li>
  <li>📚 <b>Insights:</b> Model accuracy, correlations, early-warning signals</li>
</ul>

<h2 id="contribute">🤝 7. Contributing</h2>
<ol>
  <li>🍴 Fork the repository</li>
  <li>🌿 Create a new branch (<code>feature/xyz</code>)</li>
  <li>💾 Commit changes</li>
  <li>📤 Push to your branch</li>
  <li>🔁 Open a Pull Request</li>
</ol>

<footer>
  <p>© 2025 🎓 Student Risk Dashboard | Built with ❤️ using Streamlit & Scikit-learn</p>
</footer>

</body>
</html>
