def get_ordered_list(lst=None):
  if lst is None:
    user_input = input("Enter a list of integers (comma-separated): ")
    lst = [int(x.strip()) for x in user_input.split(",")]

  return sorted(lst)