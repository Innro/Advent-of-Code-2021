def load_data(path: str):
    with open(path) as file:
        return file.read().splitlines()

def calculate_most_common_bit(bit_list: list):
    return '1' if bit_list.count('1') > bit_list.count('0') else '0'

def calculate_gamma(data: list):
    return ''.join([calculate_most_common_bit([x[j] for x in data]) for j in range(len(data[0]))])

def calculate_epsilon(gamma: str):
    return ''.join(['1' if x == '0' else '0' for x in gamma])

data = load_data('Day 3\input.txt')
gamma_rate = calculate_gamma(data)
epsilon_rate = calculate_epsilon(gamma_rate)

print(int(gamma_rate,2) * int(epsilon_rate,2))
