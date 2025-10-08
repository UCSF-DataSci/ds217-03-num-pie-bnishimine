#!/usr/bin/env python3
"""
Health Sensor Data Analysis Script

Complete the TODO sections to analyze health sensor data using NumPy.
This script demonstrates basic NumPy operations for data loading, statistics,
filtering, and report generation.
"""

import numpy as np


def load_data(filename):
    """Load CSV data using NumPy.
    
    Args:
        filename: Path to CSV file
        
    Returns:
        NumPy structured array with all columns
    """
    # This code is provided because np.genfromtxt() is not covered in the lecture
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'), 
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]
    
    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data


def calculate_statistics(data):
    """Calculate basic statistics for numeric columns.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with statistics
    """
    # Average heart rate (use .mean())
    hr_mean = data['heart_rate'].mean()

    # Average systolic BP (use .mean())
    sbp_mean = data['blood_pressure_systolic'].mean()

    # Average glucose level (use .mean())
    glucose_mean = data['glucose_level'].mean()
    # Return as dictionary
    # Format values with f-strings using .1f    
    stats = {
        'avg_heart_rate': f"{hr_mean:.1f}",
        'avg_systolic_bp': f"{sbp_mean:.1f}",
        'avg_glucose': f"{glucose_mean:.1f}"
    }
    return stats



def find_abnormal_readings(data):
    """Find readings with abnormal values.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with counts
    """
     # Heart rate > 90 (use boolean indexing)
    hr_90 = data[data['heart_rate'] > 90]

    # Systolic BP > 130 (use boolean indexing)
    sbp_130 = data[data['blood_pressure_systolic'] > 130]

    # Glucose > 110 (use boolean indexing)
    glucose_110 = data[data['glucose_level'] > 110]

    # Return dictionary with counts
    abnormal = {
        'high_heart_rate': len(hr_90),
        'high_blood_pressure': len(sbp_130),
        'high_glucose': len(glucose_110)
    }
    return abnormal



def generate_report(stats, abnormal, total_readings):
    """Generate formatted analysis report.
    
    Args:
        stats: Dictionary of statistics
        abnormal: Dictionary of abnormal counts
        total_readings: Total number of readings
        
    Returns:
        Formatted string report
    """
    report = f"Health Data Analysis\n"
    report += f"\nStats:\n"
    report += f"Average Heart Rate: {stats['avg_heart_rate']} bpm\n"
    report += f"Average Systolic BP: {stats['avg_systolic_bp']} mmHg\n"
    report += f"Average Glucose Level: {stats['avg_glucose']} mg/dL\n"
    report += f"\nAbnormal Readings:\n"
    report += f"High Heart Rate (>90 bpm): {abnormal['high_heart_rate']}\n"
    report += f"High Systolic BP (>130 mmHg): {abnormal['high_blood_pressure']}\n"
    report += f"High Glucose Level (>110 mg/dL): {abnormal['high_glucose']}\n"
    report += f"Total Readings: {total_readings}\n"
    return report
    pass


def save_report(report, filename):
    """Save report to file.
    
    Args:
        report: Report string
        filename: Output filename
    """
    with open (filename, 'w') as f:
        f.write(report)


def main():
    """Main execution function."""
    data = load_data('health_data.csv')
    stats = calculate_statistics(data)
    abnormal = find_abnormal_readings(data)
    report = generate_report(stats, abnormal, len(data))
                             
    save_report(report, 'output/analysis_report.txt')
    print("Analysis complete. Report saved to 'output/analysis_report.txt'.")


if __name__ == "__main__":
    main()