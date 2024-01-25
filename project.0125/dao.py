import datetime

board_list=[]
bno = 1

def save(title:str, content:str, nickname:str)->bool:
  global bno
  writeday = datetime.datetime.now().date()
  board = dict(bno=bno, title=title, content=content, nickname=nickname, writeday=writeday, readcnt=0)
  board_list.append(board)
  bno+=1
  return True

def findall():
  return board_list

def findone(bno:int)->dict:
  for board in board_list:
    if board['bno']==bno:
      board['readcnt']+=1
      return board
  return None

def update(bno:int, title:str, content:str)->bool:
  for board in board_list:
    if board['bno']==bno:
      board['title'] = title
      board['content'] = content
      return True
  return False

def delete(bno:int)->bool:
  for board in board_list:
    if board['bno']==bno:
      board_list.remove(board)
      return True
  return False