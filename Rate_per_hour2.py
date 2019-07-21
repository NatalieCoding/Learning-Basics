hours = input("Enter Hours:")
rate = input("Enter Rate:")

if int(hours) <= 40:
  def computepay(hours, rate):
    wages = int(hours) * int(rate)
    return wages
  x = computepay(hours, rate)
  print("Pay: ") + str(x)
else:
  overhours = int(hours) - 40
  def computepay(overhours, rate):
    wages = (int(overhours) * int(rate) * 1.5) + (40 * int(rate))
    return wages
  x = computepay(overhours, rate)
  print("Pay: ") + str(x)
