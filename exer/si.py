from web3 import Web3

def cprint(text, color):
  """
  Prints text in color.

  Args:
    text: The text to print.
    color: The color to print the text in.
  """
  color_codes = {
      "black": 30,
      "red": 31,
      "green": 32,
      "yellow": 33,
      "blue": 34,
      "magenta": 35,
      "cyan": 36,
      "white": 37,
  }

  if color not in color_codes:
    color = "white"

  print(f"\033[{color_codes[color]}m{text}\033[0m")


# Example usage
web3 = Web3(Web3.HTTPProvider("https://www.example.com = web3.toHex(web3.eth.send_transaction({"from": web3.eth.accounts[0], "to": web3.eth.accounts[1], "value": 1000000000000000000}))
cprint(f'\n>>> loop radiant | https://www.example.com ', 'green')
