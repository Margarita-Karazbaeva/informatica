import sys
letter = sys.argv[1].upper()
nucls = { "A":"purine", "C":"pyrimidine", "G":"purine","T":"pyrimidine"}
print(nucls[letter])