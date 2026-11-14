import random


def get_valid_rolls():
  
  while True:
    user_input = input("Number of rolls: ").strip()
    try:
      num_rolls = int(user_input)
      if 1 <= num_rolls <= 1000:
        return num_rolls
      else:
        print("Invalid input. Enter a whole number from 1 to 1000.")
    except ValueError:
      print("Invalid input. Enter a whole number from 1 to 1000.")


def roll_dice(num_rolls):
 
  return [random.randint(1, 6) for _ in range(num_rolls)]


def calculate_statistics(rolls):
  

  frequency = {face: 0 for face in range(1, 7)}
  for roll in rolls:
    frequency[roll] += 1

  total = sum(rolls)
  average = total / len(rolls)

  max_freq = max(frequency.values())
  most_frequent = [
      face for face, count in frequency.items() if count == max_freq
  ]

  return frequency, total, average, most_frequent, max_freq


def display_results(frequency, total, average, most_frequent, max_freq):
  
  freq_str = " | ".join(
      f"{face}:{frequency[face]}" for face in range(1, 7)
  )
  print(f"Frequency: {freq_str}")
  print(f"Total: {total} | Average: {average:.2f}")

  # Format singular/plural output for most frequent face(s)
  time_word = "time" if max_freq == 1 else "times"
  if len(most_frequent) == 1:
    print(f"Most frequent: {most_frequent[0]} ({max_freq} {time_word})")
  else:
    faces_str = " and ".join(map(str, most_frequent))
    print(f"Most frequent: {faces_str} ({max_freq} {time_word} each)")


def main():
  while True:
    num_rolls = get_valid_rolls()
    rolls = roll_dice(num_rolls)
    print(f"Rolls: {', '.join(map(str, rolls))}")

    frequency, total, average, most_frequent, max_freq = calculate_statistics(
        rolls
    )
    display_results(frequency, total, average, most_frequent, max_freq)

    while True:
      play_again = input("Play again? (y/n): ").strip().lower()
      if play_again in ("y", "n"):
        break
      print("Invalid input. Please enter 'y' or 'n'.")

    if play_again == "n":
      print("Thanks for playing!")
      break


if __name__ == "__main__":
  main()