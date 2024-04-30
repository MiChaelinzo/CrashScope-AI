import random

def sense_environment():
  # Simulate sensor readings
  obstacle_distance = random.randint(0, 10) 
  lane_position = random.uniform(-1, 1)   
  relative_speed = random.uniform(-2, 2)  # Relative speed of obstacle (-: approaching, +: receding)
  return obstacle_distance, lane_position, relative_speed

def assess_risk(obstacle_distance, lane_position, relative_speed):
  risk = 0
  if obstacle_distance > 0:
    # Risk increases as distance decreases and relative speed increases
    risk = (1 / obstacle_distance) * (1 + abs(relative_speed))
  risk += abs(lane_position) * 0.5  # Penalize lane deviations
  return risk

def predict_future_risk(current_risk, relative_speed):
  # Simple prediction based on current risk and relative speed
  predicted_risk = current_risk
  if relative_speed < 0:
    predicted_risk *= (1 + abs(relative_speed))  # Risk increases if approaching
  return predicted_risk

def make_decision(current_risk, predicted_risk):
  if predicted_risk > 0.8:
    return "BRAKE"
  elif current_risk > 0.5 or predicted_risk > 0.5:
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
  obstacle_distance, lane_position, relative_speed = sense_environment()
  current_risk = assess_risk(obstacle_distance, lane_position, relative_speed)
  predicted_risk = predict_future_risk(current_risk, relative_speed)
  action = make_decision(current_risk, predicted_risk)
  control_car(action, lane_position)
  
  # Add delay or condition to exit loop
