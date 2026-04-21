# Python Code Structure Demo

# -------------------------------
# 1. Setup / Initial Data
# -------------------------------

prices = [100, 200, 300]
discount_rate = 0.1


# -------------------------------
# 2. Helper Functions
# -------------------------------

def calculate_total(price_list):
    """Calculate total price from list"""
    return sum(price_list)


def apply_discount(total, rate):
    """Apply discount to total amount"""
    return total - (total * rate)


def display_result(total, final_amount):
    """Display results"""
    print("Total Price:", total)
    print("Final Price after discount:", final_amount)


# -------------------------------
# 3. Main Execution
# -------------------------------

def main():
    total_price = calculate_total(prices)
    final_price = apply_discount(total_price, discount_rate)
    display_result(total_price, final_price)


# -------------------------------
# 4. Entry Point
# -------------------------------

if __name__ == "__main__":
    main()