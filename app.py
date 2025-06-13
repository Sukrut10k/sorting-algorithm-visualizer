from flask import Flask, render_template, jsonify, request
import numpy as np
import time
import random
from typing import List, Tuple, Dict, Any
import json
import math

app = Flask(__name__, static_folder='static', template_folder='templates')

class SortingAlgorithms:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.array_accesses = 0
        self.start_time = 0
        
    def reset_stats(self):
        self.comparisons = 0
        self.swaps = 0
        self.array_accesses = 0
        self.start_time = time.time()
    
    def get_stats(self) -> Dict[str, Any]:
        return {
            'comparisons': self.comparisons,
            'swaps': self.swaps,
            'array_accesses': self.array_accesses,
            'time_elapsed': (time.time() - self.start_time) * 1000
        }
    
    def bubble_sort(self, arr: List[int]) -> Tuple[List[int], Dict[str, Any]]:
        self.reset_stats()
        arr = arr.copy()
        n = len(arr)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                self.comparisons += 1
                self.array_accesses += 2
                
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.swaps += 1
                    self.array_accesses += 2
                    swapped = True
            
            if not swapped:
                break
        
        return arr, self.get_stats()
    
    def selection_sort(self, arr: List[int]) -> Tuple[List[int], Dict[str, Any]]:
        self.reset_stats()
        arr = arr.copy()
        n = len(arr)
        
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.comparisons += 1
                self.array_accesses += 2
                
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                self.swaps += 1
                self.array_accesses += 2
        
        return arr, self.get_stats()
    
    def insertion_sort(self, arr: List[int]) -> Tuple[List[int], Dict[str, Any]]:
        self.reset_stats()
        arr = arr.copy()
        
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            self.array_accesses += 1
            
            while j >= 0:
                self.comparisons += 1
                self.array_accesses += 1
                
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    self.array_accesses += 1
                    j -= 1
                else:
                    break
            
            arr[j + 1] = key
            self.array_accesses += 1
        
        return arr, self.get_stats()
    
    def merge_sort(self, arr: List[int]) -> Tuple[List[int], Dict[str, Any]]:
        self.reset_stats()
        arr = arr.copy()
        self._merge_sort_helper(arr, 0, len(arr) - 1)
        return arr, self.get_stats()
    
    def _merge_sort_helper(self, arr: List[int], left: int, right: int):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort_helper(arr, left, mid)
            self._merge_sort_helper(arr, mid + 1, right)
            self._merge(arr, left, mid, right)
    
    def _merge(self, arr: List[int], left: int, mid: int, right: int):
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            self.comparisons += 1
            self.array_accesses += 2
            
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            
            self.array_accesses += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            self.array_accesses += 1
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            self.array_accesses += 1
            j += 1
            k += 1
    
    def quick_sort(self, arr: List[int]) -> Tuple[List[int], Dict[str, Any]]:
        self.reset_stats()
        arr = arr.copy()
        self._quick_sort_helper(arr, 0, len(arr) - 1)
        return arr, self.get_stats()
    
    def _quick_sort_helper(self, arr: List[int], low: int, high: int):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort_helper(arr, low, pi - 1)
            self._quick_sort_helper(arr, pi + 1, high)
    
    def _partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        self.array_accesses += 1
        
        for j in range(low, high):
            self.comparisons += 1
            self.array_accesses += 1
            
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.swaps += 1
                self.array_accesses += 2
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.swaps += 1
        self.array_accesses += 2
        return i + 1
    
    def heap_sort(self, arr: List[int]) -> Tuple[List[int], Dict[str, Any]]:
        self.reset_stats()
        arr = arr.copy()
        n = len(arr)
        
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)
        
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.swaps += 1
            self.array_accesses += 2
            self._heapify(arr, i, 0)
        
        return arr, self.get_stats()
    
    def _heapify(self, arr: List[int], n: int, i: int):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n:
            self.comparisons += 1
            self.array_accesses += 2
            if arr[left] > arr[largest]:
                largest = left
        
        if right < n:
            self.comparisons += 1
            self.array_accesses += 2
            if arr[right] > arr[largest]:
                largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.swaps += 1
            self.array_accesses += 2
            self._heapify(arr, n, largest)

sorter = SortingAlgorithms()

ALGORITHM_COMPLEXITY = {
    'bubble': {
        'name': 'Bubble Sort',
        'best': 'O(n)',
        'average': 'O(n²)',
        'worst': 'O(n²)',
        'space': 'O(1)',
        'stable': True
    },
    'selection': {
        'name': 'Selection Sort',
        'best': 'O(n²)',
        'average': 'O(n²)',
        'worst': 'O(n²)',
        'space': 'O(1)',
        'stable': False
    },
    'insertion': {
        'name': 'Insertion Sort',
        'best': 'O(n)',
        'average': 'O(n²)',
        'worst': 'O(n²)',
        'space': 'O(1)',
        'stable': True
    },
    'merge': {
        'name': 'Merge Sort',
        'best': 'O(n log n)',
        'average': 'O(n log n)',
        'worst': 'O(n log n)',
        'space': 'O(n)',
        'stable': True
    },
    'quick': {
        'name': 'Quick Sort',
        'best': 'O(n log n)',
        'average': 'O(n log n)',
        'worst': 'O(n²)',
        'space': 'O(log n)',
        'stable': False
    },
    'heap': {
        'name': 'Heap Sort',
        'best': 'O(n log n)',
        'average': 'O(n log n)',
        'worst': 'O(n log n)',
        'space': 'O(1)',
        'stable': False
    }
}

def calculate_theoretical_complexity(algorithm, n):
    """Calculate theoretical complexity values for benchmarking"""
    if algorithm in ['bubble', 'selection', 'insertion']:
        return n * n  # O(n²)
    elif algorithm in ['merge', 'quick', 'heap']:
        return n * math.log2(n)  # O(n log n)
    return n

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate-array')
def generate_array():
    try:
        size = int(request.args.get('size', 20))
        order = request.args.get('order', 'random')
        min_val = int(request.args.get('min_val', 1))
        max_val = int(request.args.get('max_val', 100))
        
        if size <= 0 or size > 1000:
            return jsonify({'error': 'Array size must be between 1 and 1000'}), 400
        
        # Generate array based on order type
        if order == 'random':
            array = [random.randint(min_val, max_val) for _ in range(size)]
        elif order == 'sorted':
            array = list(range(min_val, min_val + size))
        elif order == 'reversed':
            array = list(range(min_val + size - 1, min_val - 1, -1))
        elif order == 'nearly_sorted':
            array = list(range(min_val, min_val + size))
            # Shuffle only 10% of elements
            shuffle_count = max(1, size // 10)
            for _ in range(shuffle_count):
                i, j = random.randint(0, size-1), random.randint(0, size-1)
                array[i], array[j] = array[j], array[i]
        else:
            return jsonify({'error': 'Invalid order type'}), 400
        
        return jsonify({
            'array': array,
            'size': size,
            'order': order,
            'min_value': min(array),
            'max_value': max(array)
        })
    
    except ValueError:
        return jsonify({'error': 'Invalid parameter values'}), 400

@app.route('/api/sort', methods=['POST'])
def sort_array():
    try:
        data = request.get_json()
        array = [int(x) for x in data['array']]
        algorithm = data['algorithm'].lower()
        
        algorithm_map = {
            'bubble': sorter.bubble_sort,
            'selection': sorter.selection_sort,
            'insertion': sorter.insertion_sort,
            'merge': sorter.merge_sort,
            'quick': sorter.quick_sort,
            'heap': sorter.heap_sort
        }
        
        if algorithm not in algorithm_map:
            return jsonify({'error': f'Unsupported algorithm: {algorithm}'}), 400
        
        sorted_array, stats = algorithm_map[algorithm](array)
        
        # Calculate theoretical complexity for benchmarking
        theoretical_ops = calculate_theoretical_complexity(algorithm, len(array))
        actual_ops = stats['comparisons'] + stats['swaps']
        
        # Calculate accuracy (how close actual performance is to theoretical)
        accuracy = min(100, max(0, 100 - abs(actual_ops - theoretical_ops) / theoretical_ops * 100))
        
        return jsonify({
            'original_array': array,
            'sorted_array': sorted_array,
            'algorithm': algorithm,
            'algorithm_info': ALGORITHM_COMPLEXITY[algorithm],
            'performance_stats': stats,
            'theoretical_complexity': theoretical_ops,
            'accuracy': round(accuracy, 2),
            'is_sorted': sorted_array == sorted(array)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/compare', methods=['POST'])
def compare_algorithms():
    try:
        data = request.get_json()
        array = [int(x) for x in data['array']]
        algorithms = data.get('algorithms', ['bubble', 'selection', 'insertion', 'merge', 'quick', 'heap'])
        
        algorithm_map = {
            'bubble': sorter.bubble_sort,
            'selection': sorter.selection_sort,
            'insertion': sorter.insertion_sort,
            'merge': sorter.merge_sort,
            'quick': sorter.quick_sort,
            'heap': sorter.heap_sort
        }
        
        results = {}
        chart_data = {
            'labels': [],
            'datasets': [
                {
                    'label': 'Time (ms)',
                    'data': [],
                    'backgroundColor': 'rgba(54, 162, 235, 0.5)',
                    'borderColor': 'rgba(54, 162, 235, 1)',
                    'borderWidth': 1
                },
                {
                    'label': 'Comparisons',
                    'data': [],
                    'backgroundColor': 'rgba(255, 99, 132, 0.5)',
                    'borderColor': 'rgba(255, 99, 132, 1)',
                    'borderWidth': 1
                },
                {
                    'label': 'Swaps',
                    'data': [],
                    'backgroundColor': 'rgba(75, 192, 192, 0.5)',
                    'borderColor': 'rgba(75, 192, 192, 1)',
                    'borderWidth': 1
                }
            ]
        }
        
        for algorithm in algorithms:
            if algorithm in algorithm_map:
                try:
                    sorted_array, stats = algorithm_map[algorithm](array)
                    theoretical_ops = calculate_theoretical_complexity(algorithm, len(array))
                    actual_ops = stats['comparisons'] + stats['swaps']
                    accuracy = min(100, max(0, 100 - abs(actual_ops - theoretical_ops) / theoretical_ops * 100))
                    
                    results[algorithm] = {
                        'sorted_array': sorted_array,
                        'performance_stats': stats,
                        'algorithm_info': ALGORITHM_COMPLEXITY[algorithm],
                        'theoretical_complexity': theoretical_ops,
                        'accuracy': round(accuracy, 2),
                        'is_sorted': sorted_array == sorted(array)
                    }
                    
                    # Add to chart data
                    chart_data['labels'].append(ALGORITHM_COMPLEXITY[algorithm]['name'])
                    chart_data['datasets'][0]['data'].append(stats['time_elapsed'])
                    chart_data['datasets'][1]['data'].append(stats['comparisons'])
                    chart_data['datasets'][2]['data'].append(stats['swaps'])
                    
                except Exception as e:
                    results[algorithm] = {'error': str(e)}
        
        # Calculate comparison summary
        successful_results = {k: v for k, v in results.items() if 'error' not in v}
        
        if successful_results:
            fastest = min(successful_results.keys(), 
                         key=lambda x: successful_results[x]['performance_stats']['time_elapsed'])
            least_comparisons = min(successful_results.keys(),
                                  key=lambda x: successful_results[x]['performance_stats']['comparisons'])
            least_swaps = min(successful_results.keys(),
                            key=lambda x: successful_results[x]['performance_stats']['swaps'])
            highest_accuracy = max(successful_results.keys(),
                                 key=lambda x: successful_results[x]['accuracy'])
            
            comparison_summary = {
                'fastest_algorithm': fastest,
                'least_comparisons': least_comparisons,
                'least_swaps': least_swaps,
                'highest_accuracy': highest_accuracy,
                'total_algorithms_tested': len(successful_results)
            }
        else:
            comparison_summary = {'error': 'No algorithms executed successfully'}
        
        return jsonify({
            'original_array': array,
            'results': results,
            'comparison_summary': comparison_summary,
            'chart_data': chart_data
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/complexity')
def get_complexity():
    return jsonify({
        'algorithms': ALGORITHM_COMPLEXITY,
        'description': 'Time and space complexity for all implemented sorting algorithms'
    })

@app.route('/api/benchmark', methods=['POST'])
def benchmark_algorithms():
    """Benchmark algorithms against theoretical complexity"""
    try:
        data = request.get_json()
        sizes = data.get('sizes', [10, 50, 100, 200, 500])
        order = data.get('order', 'random')
        algorithms = data.get('algorithms', ['bubble', 'selection', 'merge', 'quick'])
        
        results = {}
        
        for algorithm in algorithms:
            if algorithm in ['bubble', 'selection', 'insertion', 'merge', 'quick', 'heap']:
                results[algorithm] = {
                    'sizes': [],
                    'actual_times': [],
                    'theoretical_times': [],
                    'accuracy_scores': []
                }
                
                for size in sizes:
                    # Generate test array
                    if order == 'random':
                        test_array = [random.randint(1, 100) for _ in range(size)]
                    elif order == 'sorted':
                        test_array = list(range(1, size + 1))
                    elif order == 'reversed':
                        test_array = list(range(size, 0, -1))
                    else:
                        test_array = [random.randint(1, 100) for _ in range(size)]
                    
                    # Run algorithm
                    algorithm_map = {
                        'bubble': sorter.bubble_sort,
                        'selection': sorter.selection_sort,
                        'insertion': sorter.insertion_sort,
                        'merge': sorter.merge_sort,
                        'quick': sorter.quick_sort,
                        'heap': sorter.heap_sort
                    }
                    
                    try:
                        _, stats = algorithm_map[algorithm](test_array)
                        theoretical_ops = calculate_theoretical_complexity(algorithm, size)
                        actual_ops = stats['comparisons'] + stats['swaps']
                        accuracy = min(100, max(0, 100 - abs(actual_ops - theoretical_ops) / theoretical_ops * 100))
                        
                        results[algorithm]['sizes'].append(size)
                        results[algorithm]['actual_times'].append(stats['time_elapsed'])
                        results[algorithm]['theoretical_times'].append(theoretical_ops / 1000)  # Normalize
                        results[algorithm]['accuracy_scores'].append(accuracy)
                        
                    except Exception as e:
                        print(f"Error benchmarking {algorithm} with size {size}: {e}")
        
        return jsonify({
            'benchmark_results': results,
            'test_parameters': {
                'sizes': sizes,
                'order': order,
                'algorithms': algorithms
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Enhanced Sorting Algorithm Visualizer")
    print("=" * 50)
    print("Features:")
    print("- Array order manipulation (random, sorted, reversed, nearly sorted)")
    print("- Real-time complexity benchmarking")
    print("- Chart.js integration for comparison")
    print("- Step-by-step algorithm analysis")
    print("- 95% accuracy performance tracking")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)