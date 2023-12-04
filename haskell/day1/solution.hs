import           Data.Char (isDigit)
import           Data.List (isPrefixOf)

summer' :: String -> Int
summer' line = do
  let nums = filter (>0) [reader' xs | xs <- tailor' line]
  sum [read (show (head nums) ++ show( last nums)) :: Int ]

digiter' :: Char -> Int
digiter' c | isDigit c = read [c] :: Int
           | otherwise = 0

reader' :: String -> Int
reader' s | "one" `isPrefixOf` s = 1
          | "two" `isPrefixOf` s = 2
          | "three" `isPrefixOf` s = 3
          | "four" `isPrefixOf` s = 4
          | "five" `isPrefixOf` s = 5
          | "six" `isPrefixOf` s = 6
          | "seven" `isPrefixOf` s = 7
          | "eight" `isPrefixOf` s = 8
          | "nine" `isPrefixOf` s = 9
          | otherwise = digiter' (head s)

tailor' :: String -> [String]
tailor' []     = []
tailor' (x:xs) = (x:xs) : tailor' xs


part1' :: String -> Int
part1' input = do
  sum [read [head nums, last nums] :: Int | nums <- [filter isDigit c | c <- lines input ] ]

part2' :: String -> Int
part2' input = do
  sum [ summer' line | line <- lines input ]


main = do
  input <- readFile "../../inputs/1/full"
  print (part1' input)
  print (part2' input)
