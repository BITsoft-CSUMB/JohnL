# CST205 Mid-Term - Programmer: John Lester
# on load you will need to select a media path for it to download images to
# then call CSUMBerize() or framed() to modify your image

localPath = setMediaPath()

def CSUMBerize():
  csumbPic = makePicture(pickAFile())
  csumbPic = sharpen(csumbPic)
  csumbPic = addLogo(csumbPic)
  show(csumbPic)
  writePictureTo(csumbPic, localPath+'\\CSUMBerize.png')
  return

def framed():
  framedPic = makePicture(pickAFile())
  framedPic = soften(framedPic)
  framedPic = soften(framedPic)
  framedPic = addFrame(framedPic)
  framedPic = addLogo(framedPic)
  show(framedPic)
  writePictureTo(framedPic, localPath+'\\framed.png')
  return

def BnW(bwPic):
  bwPixels = getPixels(bwPic)
  for bwPix in bwPixels:
    bwRed = getRed(bwPix)
    bwGreen = getGreen(bwPix)
    bwBlue = getBlue(bwPix)
    intensity = int((bwRed + bwGreen + bwBlue) / 3)
    setColor(bwPix, Color(intensity, intensity, intensity))
  return bwPic

def lineDrawing(lnPic):
  lnPic = BnW(lnPic)
  threshold = 64
  for x in range(0, getWidth(lnPic)):
    for y in range(0, getHeight(lnPic)):
      pix = getPixel(lnPic, x, y)
      lum = getColor(pix)
      if y < getHeight(lnPic)-1:
        bPix = getPixel(lnPic, x, y+1)
      bLum = getColor(bPix)
      if x < getWidth(lnPic)-1:
        rPix = getPixel(lnPic, x+1, y)
      rLum = getColor(rPix)
      if distance(lum, bLum) > threshold and distance(lum, rLum) > threshold:
        setColor(pix, black)
      else:
        setColor(pix, white)
  return lnPic

def simpleCopy(oldPic):
  newPic = makeEmptyPicture(getWidth(oldPic), getHeight(oldPic))
  for x in range(0, getWidth(oldPic)):
    for y in range(0, getHeight(oldPic)):
      pix = getPixel(oldPic, x, y)
      newPix = getPixel(newPic, x, y)
      setColor(newPix, getColor(pix))
  return newPic

def sharpen(shPic):
  mkPic = simpleCopy(shPic)
  mkPic = lineDrawing(mkPic)
  for x in range(0, getWidth(shPic)):
    for y in range(0, getHeight(shPic)):
      shPix = getPixel(shPic, x, y)
      mkPix = getPixel(mkPic, x, y)
      shColor = getColor(shPix)
      mkColor = getColor(mkPix)
      if distance(mkColor, white) < 5:
        pixRed = int(getRed(shPix) * 1.1)
        if pixRed > 255:
          pixRed = 255
        pixGreen = int(getGreen(shPix) * 1.1)
        if pixGreen > 255:
          pixGreen = 255
        pixBlue = int(getBlue(shPix) * 1.1)
        if pixBlue > 255:
          pixBlue = 255
        setColor(shPix, Color(pixRed, pixGreen, pixBlue))
      else:
        setColor(shPix, black)
  return shPic

def addLogo(lgPic):
  import os.path
  if not os.path.exists(localPath+'\\logo.png'):
    import urllib
    urllib.urlretrieve('http://wsiab.net/BITsoft/Lab7/csumb-logo-white.png', localPath+'\\logo.png')
  logo = makePicture(localPath+'\\logo.png')
  targetX = getWidth(lgPic) - getWidth(logo)
  targetY = getHeight(lgPic) - getHeight(logo)
  for x in range(0, getWidth(logo)):
    for y in range(0, getHeight(logo)):
      pix = getPixel(logo, x, y)
      bPix = getPixel(lgPic, x + targetX, y + targetY)
      color = getColor(pix)
      if distance(color, Color(0, 215, 0)) > 250:
        setColor(bPix, gray)
  for x in range(0, getWidth(logo)):
    for y in range(0, getHeight(logo)):
      pix = getPixel(logo, x, y)
      bPix = getPixel(lgPic, x + targetX - 2, y + targetY - 2)
      color = getColor(pix)
      if distance(color, Color(0, 215, 0)) > 250:
        setColor(bPix, white)
  return lgPic

def soften(inPic):
  sfPic = simpleCopy(inPic)
  for x in range(0, getWidth(inPic)):
    for y in range(0, getHeight(inPic)):
      pix = getPixel(inPic, x, y)
      newPix = getPixel(sfPic, x, y)
      if y > 0:
        uPix = getPixel(inPic, x, y-1)
      else:
        uPix = getPixel(inPic, x, y)
      if y > 0 and x < getWidth(inPic)-1:
        urPix = getPixel(inPic, x+1, y-1)
      else:
        urPix = getPixel(inPic, x, y)
      if x < getWidth(inPic)-1:
        rPix = getPixel(inPic, x+1, y)
      else:
        rPix = getPixel(inPic, x, y)
      if y < getHeight(inPic)-1 and x < getWidth(inPic)-1:
        drPix = getPixel(inPic, x+1, y+1)
      else:
        drPix = getPixel(inPic, x, y)
      if y < getHeight(inPic)-1:
        dPix = getPixel(inPic, x, y+1)
      else:
        dPix = getPixel(inPic, x, y)
      if y < getHeight(inPic)-1 and x > 0:
        dlPix = getPixel(inPic, x-1, y+1)
      else:
        dlPix = getPixel(inPic, x, y)
      if x > 0:
        lPix = getPixel(inPic, x-1, y)
      else:
        lPix = getPixel(inPic, x, y)
      if x > 0 and y > 0:
        ulPix = getPixel(inPic, x-1, y-1)
      else:
        ulPix = getPixel(inPic, x, y)
      newRed = int(getRed(uPix)*0.1 + getRed(urPix)*0.1 + getRed(rPix)*0.1 + getRed(drPix)*0.1 + getRed(dPix)*0.1 + getRed(dlPix)*0.1 + getRed(lPix)*0.1 + getRed(ulPix)*0.1 + getRed(pix)*0.2)
      newGreen = int(getGreen(uPix)*0.1 + getGreen(urPix)*0.1 + getGreen(rPix)*0.1 + getGreen(drPix)*0.1 + getGreen(dPix)*0.1 + getGreen(dlPix)*0.1 + getGreen(lPix)*0.1 + getGreen(ulPix)*0.1 + getGreen(pix)*0.2)
      newBlue = int(getBlue(uPix)*0.1 + getBlue(urPix)*0.1 + getBlue(rPix)*0.1 + getBlue(drPix)*0.1 + getBlue(dPix)*0.1 + getBlue(dlPix)*0.1 + getBlue(lPix)*0.1 + getBlue(ulPix)*0.1 + getBlue(pix)*0.2)
      setColor(newPix, Color(newRed, newGreen, newBlue))
  return sfPic

def addFrame(frPic):
  for x in range(0, getWidth(frPic)):
    for y in range(0, int(getHeight(frPic)*0.05)):
      newPix = getPixel(frPic, x, y)
      if x%8 > 6 and y%4 > 2:
        setColor(newPix, Color(41, 36, 33))
      else:
        setColor(newPix, Color(139, 69, 14))
    for y in range(int(getHeight(frPic)-getHeight(frPic)*0.05), getHeight(frPic)):
      newPix = getPixel(frPic, x, y)
      if x%8 > 6 and y%4 > 2:
        setColor(newPix, Color(41, 36, 33))
      else:
        setColor(newPix, Color(139, 69, 14))
  for y in range(0, getHeight(frPic)):
    for x in range(0, int(getWidth(frPic)*0.05)):
      newPix = getPixel(frPic, x, y)
      if x%8 > 6 and y%4 > 2:
        setColor(newPix, Color(41, 36, 33))
      else:
        setColor(newPix, Color(139, 69, 14))
    for x in range(int(getWidth(frPic)-getWidth(frPic)*0.05), getWidth(frPic)):
      newPix = getPixel(frPic, x, y)
      if x%8 > 6 and y%4 > 2:
        setColor(newPix, Color(41, 36, 33))
      else:
        setColor(newPix, Color(139, 69, 14))
  for x in range(int(getWidth(frPic)*0.05), int(getWidth(frPic)-getWidth(frPic)*0.05)):
    for y in range(int(getHeight(frPic)*0.05), int(getHeight(frPic)*0.05)+2):
      newPix = getPixel(frPic, x, y)
      setColor(newPix, black)
    for y in range(int(getHeight(frPic)-getHeight(frPic)*0.05-2), int(getHeight(frPic)-getHeight(frPic)*0.05)):
      newPix = getPixel(frPic, x, y)
      setColor(newPix, black)
  for y in range(int(getHeight(frPic)*0.05), int(getHeight(frPic)-getHeight(frPic)*0.05)):
    for x in range(int(getWidth(frPic)*0.05), int(getWidth(frPic)*0.05)+2):
      newPix = getPixel(frPic, x, y)
      setColor(newPix, black)
    for x in range(int(getWidth(frPic)-getWidth(frPic)*0.05-2), int(getWidth(frPic)-getWidth(frPic)*0.05)):
      newPix = getPixel(frPic, x, y)
      setColor(newPix, black)
  return frPic
