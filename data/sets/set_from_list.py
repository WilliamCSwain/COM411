def observed():
  observations = []

  for count in range(7):
    print("Please enter an observation:")
    observation.append(input())

  return observations

def run():
  print("Counting observations...")
  observations = observed()

  observations_set = set()
  for observation in observations:
    data = (observation, observations.count(observation))
    observations_set.add(date)

  for data in observations_set:
    print(f"{data[0]} observed {data[1]} times.")

run()