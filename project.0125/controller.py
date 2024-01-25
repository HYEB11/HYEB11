import flask as f
import dao

app = f.Flask(__name__)

@app.route("/")
def 목록():
  board_list = dao.findall()
  return f.render_template("list.html", list=board_list)

@app.route("/write")
def 쓰기화면():
  return f.render_template("write.html")

@app.route("/write", methods=['post'])
def 쓰기():
  nickname = f.request.form.get("nickname", type=str)
  title = f.request.form.get("title", type=str)
  content = f.request.form.get("content", type=str)
  dao.save(nickname=nickname, title=title, content=content)
  return f.redirect("/")

@app.route("/read")
def 읽기():
  bno = f.request.args.get('bno', type=int)
  board = dao.findone(bno)
  return f.render_template("read.html", board=board)

@app.route("/update", methods=['post'])
def 변경():
  bno = f.request.form.get("bno", type=int)
  title = f.request.form.get("title", type=str)
  content = f.request.form.get("content", type=str)
  dao.update(bno=bno, title=title, content=content)
  return f.redirect("/")

@app.route("/delete", methods=['post'])
def 삭제():
  bno = f.request.form.get("bno", type=int)
  dao.delete(bno=bno)
  return f.redirect("/")

app.run(debug=True)