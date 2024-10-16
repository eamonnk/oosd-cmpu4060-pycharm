nonMotorised = [ "rollerblades", "bicycle", "scooter", "sail wagon", "legs" ]
maxWordLen = max(map(len, nonMotorised))
for mode in sorted(nonMotorised):
   print("--< " + mode.center(maxWordLen, ' ') + " >--")















