def find_max_difference(queries):
  """
  Finds the maximum absolute difference between the numbers with the highest and lowest frequencies.

  Args:
    queries: A list of tuples representing the queries (count, number).

  Returns:
    The maximum absolute difference, or 0 if there are only two numbers with the same occurrence.
  """

  frequencies = {}
  for count, number in queries:
    if number in frequencies:
      frequencies[number] += count
    else:
      frequencies[number] = count

  max_frequency = max(frequencies.values())
  min_frequency = min(frequencies.values())

  # Check if there are only two numbers with the same occurrence.
  if len(frequencies) == 2 and max_frequency == min_frequency:
    return 0

  # Find the numbers with the highest and lowest frequencies.
  max_number = max(frequencies, key=frequencies.get)
  min_number = min(frequencies, key=frequencies.get)

  return abs(max_number - min_number)

# Get input
q = int(input())
queries = []
for _ in range(q):
  count, number = map(int, input().split())
  queries.append((count, number))

# Find and print the maximum difference
result = find_max_difference(queries)
print(result)