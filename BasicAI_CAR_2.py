import random

def sense_environment():
  # Simulate sensor readings with some randomness
  obstacle_distance = random.randint(1, 10)  # Distance to obstacle (0: no obstacle)
  lane_position = random.uniform(-1, 1)    # Position within lane (-1: left edge, 1: right edge)
  return obstacle_distance, lane_position

def assess_risk(obstacle_distance, lane_position):
  # Calculate risk factor based on distance and lane position
  if obstacle_distance == 0:
    risk = 0
  else:
    risk = 1 / obstacle_distance + abs(lane_position) * 0.5
  return risk

def make_decision(risk):
  if risk > 0.8:
    return "BRAKE"
  elif risk > 0.3:
    return "STEER"
  else:
    return "ACCELERATE"

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
  obstacle_distance, lane_position = sense_environment()
  risk = assess_risk(obstacle_distance, lane_position)
  action = make_decision(risk)
  control_car(action, lane_position)
  
  # Add delay or condition to exit loop
