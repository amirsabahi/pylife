def reverse_integer(x):
    """Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go
    outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0."""
    # Check if the number is negative
    is_negative = False
    if x < 0:
        is_negative = True
        x = abs(x)

    # Reverse the digits
    reversed_num = int(str(x)[::-1])  # is it optimal?

    # Handle the range constraint
    if reversed_num > 2**31 - 1:
        return 0

    # Restore the negative sign if applicable
    if is_negative:
        reversed_num *= -1

    return reversed_num


# Test the function
num = 98465
reversed_number = reverse_integer(num)
print(f"Reversed integer: {reversed_number}")
