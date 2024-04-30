import random
import math

def sense_environment():
  # Simulate multiple obstacle detections
  num_obstacles = random.randint(0, 3)
  obstacles = []
  for _ in range(num_obstacles):
    obstacle_distance = random.randint(1, 10)
    obstacle_angle = random.uniform(-math.pi/2, math.pi/2)  # Angle relative to car's heading
    obstacles.append((obstacle_distance, obstacle_angle))
  lane_position = random.uniform(-1, 1)
  return obstacles, lane_position

def assess_risk(obstacle):
  distance, angle = obstacle
  # Risk increases with proximity and as obstacle is closer to the car's path
  risk = (1 / distance) * (1 + abs(math.sin(angle))) 
  return risk

def predict_future_obstacle(obstacle, relative_speed):
  # Simplified prediction assuming constant speed and heading
  distance, angle = obstacle
  predicted_distance = distance + relative_speed  # Adjust based on relative speed
  return predicted_distance, angle

def plan_path(obstacles, lane_position):
  # Basic path planning: prioritize avoiding closest obstacle
  if not obstacles:
    return "NONE"  # No obstacles, no action needed
  closest_obstacle = min(obstacles, key=assess_risk)
  _, angle = closest_obstacle
  if abs(angle) < math.pi/6:  # Obstacle directly ahead
    return "BRAKE"
  elif angle > 0:
    return "STEER_LEFT"  # Obstacle on the right, steer left
  else:
    return "STEER_RIGHT"

def control_car(action, lane_position):
  # ... (similar to previous versions, with added steering actions)

while True:
  obstacles, lane_position = sense_environment()
  predicted_obstacles = [predict_future_obstacle(obs, 0) for obs in obstacles]  # Assume relative speed 0 for now
  action = plan_path(predicted_obstacles, lane_position)
  control_car(action, lane_position)
  
  # Add delay or condition to exit loop
