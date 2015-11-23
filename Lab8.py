# CST205 Lab 8 - Programmer: John Lester & Matthew Crenshaw
# writeSoundTo(sound, filepath)

sound = makeSound(pickAFile())

def increaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * 2)
   return sound

def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value / 2)
  return sound

def changeVolume(sound, factor):
  for sample in getSamples(sound):
    value = int(getSampleValue(sample) * factor)
    if value > 32767:
      value = 32767
    elif value < -32768:
      value = -32768
    setSampleValue(sample, value)
  return sound

def maxSample(sound):
  highest = 0
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    highest = max(highest, value)
  return highest

def maxVolume(sound):
  factor = 32767 / maxSample(sound)
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, int(value * factor))
  return sound

def goToEleven(sound):
  for sample in getSamples(sound):
     value = getSampleValue(sample)
     if value > 0:
       setSampleValue(sample, 32767)
     elif value < 0:
       setSampleValue(sample, -32768)
  return sound
