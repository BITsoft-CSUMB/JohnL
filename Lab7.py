# CST205 Lab 7 - Programmer: John Lester
# Welcome to the BITsoft Thanksgiving card generator v1.0
# Use pic = makeCard() to pick your background, then insert picture, then CSUMB logo
# Use writePictureTo(pic, 'C:\\Path\\To\\Save\\image.jpg') to save result

def chromakey(newPic, bckPic, targetX = 0, targetY = 0, overRide = False, tolerance = 60):
  for x in range(0, getWidth(newPic)):
    if x + targetX < getWidth(bckPic):
      for y in range(0, getHeight(newPic)):
        if y + targetY < getHeight(bckPic):
          pix = getPixel(newPic, x, y)
          bPix = getPixel(bckPic, x + targetX, y + targetY)
          color = getColor(pix)
          bColor = getColor(bPix)
          if (distance(color, Color(0, 215, 0)) > tolerance) and ((distance(bColor, Color(0, 215, 0)) < 60) or (distance(bColor, Color(0, 131, 0)) < 60) or (distance(bColor, Color(45, 221, 45)) < 60) or overRide):
            newPix = getPixel(bckPic, x + targetX, y + targetY)
            setColor(bPix, color)
  return bckPic

def shrink(origPic, factor):
  if factor <= 1:
    return origPic
  width = getWidth(origPic)
  height = getHeight(origPic)
  newPic = makeEmptyPicture(int(width / factor), int(height / factor))
  oldX = 0
  for newX in range(0, getWidth(newPic)):
    oldY = 0
    for newY in range(0, getHeight(newPic)):
      oldPix = getPixel(origPic, oldX, oldY)
      newPix = getPixel(newPic, newX, newY)
      setColor(newPix, getColor(oldPix))
      oldY += factor
    oldX += factor
  return newPic

def addThxMessage(pic, text):
  size = 48  #centering only kinda works with 48pt text
  xPos = int((getWidth(pic)/2) - (len(text) * 12.6))
  yPos = size
  style = makeStyle('Palatino Linotype', italic + bold, size)
  addTextWithStyle(pic, xPos+2, yPos+2, text, style, gray)
  addTextWithStyle(pic, xPos, yPos, text, style, orange)
  return pic

def makeCard():
  filenameB = pickAFile()
  bckgrnd = makePicture(filenameB)
  filenameP = pickAFile()
  pic = makePicture(filenameP)
  show(pic)
  if (getWidth(pic) > getWidth(bckgrnd)):
    pic = shrink(pic, int(getWidth(pic)/getWidth(bckgrnd)))
  else:
    bckgrnd = shrink(bckgrnd, int(getWidth(bckgrnd)/getWidth(pic)))
  repaint(pic)
  pic = chromakey(pic, bckgrnd, 0, 0)
  repaint(pic)
  pic = addThxMessage(pic, "Happy Thanksgiving")
  repaint(pic)
  filenameL = pickAFile()
  csumbLogo = makePicture(filenameL)
  pic = chromakey(csumbLogo, pic, getWidth(pic)-getHeight(csumbLogo), getHeight(pic)-getHeight(csumbLogo), True, 120)
  repaint(pic)
  return pic
