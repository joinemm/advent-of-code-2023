import           Data.Char

part1 input = do
  sum [read [head nums, last nums] :: Int | nums <- [filter isDigit c | c <- lines input]]


main = do
  example <- readFile "../../inputs/1/example"
  input <- readFile "../../inputs/1/full"
  print (part1 example)
  print (part1 input)
