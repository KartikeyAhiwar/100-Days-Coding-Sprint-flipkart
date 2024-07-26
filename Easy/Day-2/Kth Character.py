def kth_character_from_reversed_string(s, k):
  """
  Finds the kth character from the reversed string.

  Args:
    s: The input string.
    k: The desired index in the reversed string.

  Returns:
    The kth character from the reversed string.
  """

  n = len(s)
  return s[n - k]

# Read input
n, k = map(int, input().split())
s = input()

# Calculate and print the result
print(kth_character_from_reversed_string(s, k))