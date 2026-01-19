import random
from datetime import datetime

class PhysiologicalMonitor:
    """Mock physiological monitoring that simulates heart rate data"""
    
    def __init__(self):
        self.base_heart_rate = 70
        self.current_heart_rate = self.base_heart_rate
        
    def get_current_heart_rate(self):
        """
        Simulates real-time heart rate measurement
        Returns a heart rate value that varies slightly from baseline
        """
        # Add some variation to make it realistic
        variation = random.randint(-15, 20)
        self.current_heart_rate = max(50, min(150, self.base_heart_rate + variation))
        return self.current_heart_rate
    
    def get_heart_rate_trend(self, minutes=30):
        """
        Get simulated heart rate trend over the past N minutes
        Returns a list of heart rate readings
        """
        readings = []
        for i in range(minutes):
            variation = random.randint(-20, 25)
            hr = max(50, min(150, self.base_heart_rate + variation))
            readings.append({
                'timestamp': datetime.now().isoformat(),
                'heart_rate': hr,
                'minute': i
            })
        return readings
    
    def set_stress_level(self, level):
        """
        Adjust baseline heart rate based on stress level (0-100)
        """
        # Maps stress level to heart rate increase
        stress_increase = (level / 100) * 40  # Up to 40 BPM increase
        self.base_heart_rate = 70 + int(stress_increase)
    
    def get_heart_rate_stats(self, readings=None):
        """Calculate stats from heart rate readings"""
        if not readings or len(readings) == 0:
            return {
                'avg': 0,
                'min': 0,
                'max': 0,
                'current': self.current_heart_rate
            }
        
        heart_rates = [r['heart_rate'] for r in readings]
        return {
            'avg': round(sum(heart_rates) / len(heart_rates)),
            'min': min(heart_rates),
            'max': max(heart_rates),
            'current': self.current_heart_rate
        }

# Global instance
physiological_monitor = PhysiologicalMonitor()