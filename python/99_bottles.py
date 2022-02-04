def bottle_song(n):
  for i in range(n, 0, -1):
    print(current_beer_count(i))
    print(take_one_down(i))
  print(current_beer_count(0))
  print(buy_more_beer(n))


def current_beer_count(n):
  return(f'{"No more" if n == 0 else n} bottle{"" if n == 1 else "s"} of beer on the wall, {"no more" if n == 0 else n} bottle{"" if n == 1 else "s"} of beer.')


def take_one_down(n):
  return(f'Take one down and pass it around, {"no more" if n == 1 else n - 1} bottle{"" if n - 1 == 1 else "s" } of beer on the wall.')


def buy_more_beer(n):
  return(f'Go to the store and buy some more, {n} bottles of beer on the wall.')


bottle_song(5)
