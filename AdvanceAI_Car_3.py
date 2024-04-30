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

def predict_obstacle_trajectory(obstacle, relative_speed, relative_acceleration):
  distance, angle = obstacle
  predicted_trajectory = []
  time_step = 0.1  # Time interval for prediction
  for _ in range(5):  # Predict for 0.5 seconds
    predicted_distance = distance + relative_speed * time_step + 0.5 * relative_acceleration * time_step**2
    predicted_angle = angle  # Assuming constant heading for simplicity
    predicted_trajectory.append((predicted_distance, predicted_angle))
    distance = predicted_distance
    relative_speed += relative_acceleration * time_step
  return predicted_trajectory

def cost_function(trajectory, obstacles, lane_position):
  collision_risk = sum(assess_risk(pos) for obstacle in obstacles for pos in obstacle)
  lane_deviation_penalty = abs(lane_position) * 0.2  # Penalize deviations from lane center
  return collision_risk + lane_deviation_penalty

def plan_trajectory(obstacles, lane_position):
  best_trajectory = None
  min_cost = float('inf')
  for steer_angle in [-0.2, -0.1, 0, 0.1, 0.2]:  # Sample multiple steering angles
    predicted_lane_position = lane_position + steer_angle * 0.5
    predicted_obstacles = [predict_obstacle_trajectory(obs, 0, 0) for obs in obstacles]
    trajectory_cost = cost_function(predicted_obstacles, predicted_lane_position)
    if trajectory_cost < min_cost and -1 <= predicted_lane_position <= 1:
      best_trajectory = steer_angle
      min_cost = trajectory_cost
  if best_trajectory is None:
    return "BRAKE"  # No safe trajectory found, brake
  elif best_trajectory < 0:
    return "STEER_RIGHT"
  elif best_trajectory > 0:
    return "STEER_LEFT"
  else:
    return "NONE"

def control_car(action, lane_position):
  if action == "BRAKE":
    print("Applying brakes...")
  elif action == "STEER":
    if lane_position < 0:
      print("Steering right...")
    else:
      print("Steering left...")
  elif action == "ACCELERATE":
    print("Accelerating...")
  else:
    print("Invalid action.")

while True:
  obstacles, lane_position = sense_environment()
  action = plan_trajectory(obstacles, lane_position)
  control_car(action, lane_position)
  
  # Add delay or condition to exit loop
