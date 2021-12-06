# Advent of Code 2021 - Day 3, part 1 in Python 3.
# https://adventofcode.com/2021/day/3

from utils import getFreq


def getGammaRate(data):
    gammaRate = []
    for i in range(0, len(data[0])):
        binNumber = [x[i] for x in data]
        avg = getFreq(binNumber)
        mostCommon = max(avg, key=avg.get)

        gammaRate.append(mostCommon)

    return gammaRate


def getEpsilon(data):
    epsilonRate = []
    for i in range(0, len(data[0])):
        binNumber = [x[i] for x in data]
        avg = getFreq(binNumber)
        leastCommon = min(avg, key=avg.get)

        epsilonRate.append(leastCommon)

    return epsilonRate


with open('input.txt', 'r') as f:
    data = f.read().split("\n")


gammaRate = getGammaRate(data)
gammaInt = int(''.join(map(str, gammaRate)), 2)

print(f"\nGamma Rate: {''.join(gammaRate)}")
print(f"Gamma Rate (DECIMAL/INT): {gammaInt}")

epsilonRate = getEpsilon(data)
epsilonInt = int(''.join(map(str, epsilonRate)), 2)

print(f"\nEpsilon Rate: {''.join(epsilonRate)}")
print(f"Epsilon Rate (DECIMAL/INT): {epsilonInt}")

print("\nPower Consumption (in INT/Decimal):", gammaInt * epsilonInt, "\n")
