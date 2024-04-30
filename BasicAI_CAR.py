def sense_environment():
  # Replace with actual sensor readings
  obstacle_ahead = False
  lane_departure = False
  return obstacle_ahead, lane_departure

def make_decision(obstacle_ahead, lane_departure):
  if obstacle_ahead:
    return "BRAKE"
  elif lane_departure:
    return "STEER"
  else:
    return "ACCELERATE"

def control_car(action):
  if action == "BRAKE":
    print("Applying brakes...")
  elif action == "STEER":
    print("Steering back into lane...")
  elif action == "ACCELERATE":
    print("Accelerating...")
  else:
    print("Invalid action.")

while True:
  obstacle_ahead, lane_departure = sense_environment()
  action = make_decision(obstacle_ahead, lane_departure)
  control_car(action)
  
  # Add delay or condition to exit loop
