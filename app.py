from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Recursive Tower of Hanoi solver
def hanoi(n, source, auxiliary, destination, moves=None):
    if moves is None:
        moves = []
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {destination}")
    else:
        hanoi(n - 1, source, destination, auxiliary, moves)
        moves.append(f"Move disk {n} from {source} to {destination}")
        hanoi(n - 1, auxiliary, source, destination, moves)
    return moves

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json()
    n = int(data.get("disks", 3))
    moves = hanoi(n, "Source", "Auxiliary", "Destination")
    return jsonify({
        "moves": moves,
        "total_moves": len(moves),
        "min_moves": 2**n - 1
    })

if __name__ == "__main__":
    app.run(debug=True)