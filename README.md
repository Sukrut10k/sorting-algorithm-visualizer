# Sorting Algorithm Visualizer

## Demo
![Demo Video](./assets/demo.mp4)

## Project Overview

The Sorting Algorithm Visualizer is an interactive web application that demonstrates how various sorting algorithms work with real-time visualizations and performance metrics. This tool helps computer science students and developers understand sorting algorithms through dynamic animations and comprehensive statistical analysis.

## Project Structure

```
Sorting-Algorithm-Visualizer/
│
├── static/                  # Static files
│   ├── css/
│   │   └── styles.css       # Professional styling with CSS variables
│   └── js/
│       └── visualizer.js    # Core visualization logic
│
├── templates/               # Frontend templates
│   └── index.html           # Main application interface
│
├── app.py                   # Flask backend server
│
├── requirements.txt         # Python dependencies
│
└── README.md                # Project documentation
```

## Key Features

- **8 Sorting Algorithms**: Visualize Bubble, Selection, Insertion, Merge, Quick, Heap, Radix, and Counting sorts
- **Interactive Controls**: Adjust array size, initial order, and animation speed
- **Performance Metrics**: Real-time tracking of comparisons, swaps, and time complexity
- **Educational Resources**: Algorithm complexity reference table
- **Comparison Mode**: Benchmark multiple algorithms simultaneously
- **Responsive Design**: Works on desktop and mobile devices
- **Professional UI**: Clean, modern interface with smooth animations

## Implemented Algorithms

| Algorithm       | Best Case  | Average Case | Worst Case | Space  | Stable |
|----------------|-----------|--------------|------------|--------|--------|
| Bubble Sort    | O(n)      | O(n²)        | O(n²)      | O(1)   | Yes    |
| Selection Sort | O(n²)     | O(n²)        | O(n²)      | O(1)   | No     |
| Insertion Sort | O(n)      | O(n²)        | O(n²)      | O(1)   | Yes    |
| Merge Sort     | O(n log n)| O(n log n)   | O(n log n) | O(n)   | Yes    |
| Quick Sort     | O(n log n)| O(n log n)   | O(n²)      | O(log n)| No   |
| Heap Sort      | O(n log n)| O(n log n)   | O(n log n) | O(1)   | No     |
| Radix Sort     | O(nk)     | O(nk)        | O(nk)      | O(n+k) | Yes    |
| Counting Sort  | O(n+k)    | O(n+k)       | O(n+k)     | O(k)   | Yes    |

## Technologies Used

### Backend
- **Flask** (Python): Lightweight web server
- **NumPy**: Array processing (for benchmarking)

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with variables and transitions
- **JavaScript (ES6+)**: Core application logic
- **Chart.js**: Data visualization

### Performance Analysis
- Custom metrics tracking (comparisons, swaps, array accesses)
- Theoretical vs actual complexity comparison
- Accuracy percentage calculations

## Installation & Setup

### Prerequisites
- Python 3.8+
- Modern web browser (Chrome, Firefox, Edge)

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/Sukrut10k/Sorting-Algorithm-Visualizer.git
   cd Sorting-Algorithm-Visualizer
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install flask numpy
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser to:
   ```
   http://localhost:5000
   ```
## Usage Guide

1. **Generate Array**:
   - Select array size (10-200 elements)
   - Choose initial order (Random, Sorted, Reverse Sorted, Nearly Sorted)

2. **Select Algorithm**:
   - Choose from 8 sorting algorithms
   - View complexity information in the reference table

3. **Adjust Speed**:
   - Control animation speed (Slow to Very Fast)

4. **Start Visualization**:
   - Click "Start Sorting" to begin the animation
   - Use "Stop" to pause or "Reset" to start over

5. **Compare Algorithms**:
   - Click "Compare All" to benchmark all algorithms
   - View performance charts and statistics

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add some NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## Acknowledgments

- Inspired by Tech With Tim's YouTube tutorials
```
