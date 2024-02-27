def calculate_rectangle_area(length, width):
  """Calculates the area of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The area of the rectangle.
  """
  return length * width

def calculate_rectangle_perimeter(length, width):
  """Calculates the perimeter of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The perimeter of the rectangle.
  """
  return 2 * (length + width)

def calculate_circle_area(radius):
  """Calculates the area of a circle.

  Args:
    radius: The radius of the circle.

  Returns:
    The area of the circle.
  """
  import math
  return math.pi * radius**2

def calculate_circle_perimeter(radius):
  """Calculates the perimeter of a circle.

  Args:
    radius: The radius of the circle.

  Returns:
    The perimeter of the circle.
  """
  import math
  return 2 * math.pi * radius

while True:
  # Get user choice
  print("\nArea and Perimeter Calculator")
  print("1. Rectangle")
  print("2. Circle")
  print("3. Exit")
  choice = input("Enter your choice (1-3): ")

  # Handle user choice
  if choice == '1':
    try:
      length = float(input("Enter rectangle length: "))
      width = float(input("Enter rectangle width: "))
      area = calculate_rectangle_area(length, width)
      perimeter = calculate_rectangle_perimeter(length, width)
      print(f"Rectangle area: {area:.2f}")
      print(f"Rectangle perimeter: {perimeter:.2f}")
    except ValueError:
      print("Invalid input. Please enter numbers only.")
  elif choice == '2':
    try:
      radius = float(input("Enter circle radius: "))
      area = calculate_circle_area(radius)
      perimeter = calculate_circle_perimeter(radius)
      print(f"Circle area: {area:.2f}")
      print(f"Circle perimeter: {perimeter:.2f}")
    except ValueError:
      print("Invalid input. Please enter a number only.")
  elif choice == '3':
    print("Exiting calculator.")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 3.")
