using System;
using System.Collections.Generic;

namespace mazegenApp {
    public class Cell {
        public string state = "wall";

        public Cell(string state) {
            this.state = state;
        }

        public char render() {
            if(state == "wall") return '#';
            else if(state == "empty") return '░';
            else if(state == "player") return 'T';
            else return '!';
        }
    }
    public class Player {
        public int x = 1;
        public int y = 1;
        public Player(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public class Board {
        public int width = 15;
        public int height = 15;
        public int spacingAmount = 1;
        public Player player;

        public List<List<Cell>> grid = new List<List<Cell>>();

        public Board(int width, int height, int spacingAmount, Player player) {
            for(int i = 0; i < height; i++) {
                grid.Add(new List<Cell>());
                for(int j = 0; j < width; j++) {
                    grid[i].Add(new Cell("empty"));
                }
            }
            this.width = width;
            this.height = height;
            this.spacingAmount = spacingAmount;
            this.player = player;
            for(int row = 0; row < height; row++) {
                // grid[row] = new Cell("empty");
                for(int i = 0; i < width; i++) {
                    if(row == 0 || i == 0 || i == width-1 || row == height-1) {
                        grid[row][i].state = "wall";
                    }
                }
            }
        }

        public void render() {
            string spacing = "";
            for(int i = 0; i < spacingAmount; i++) spacing += " ";
            for(int row = 0; row < height; row++) {
                for(int i = 0; i < width; i++) {
                    if(player.x == i && player.y == row) {
                        grid[row][i].state = "player";
                    }
                    Console.Write(grid[row][i].render() + spacing);
                }
                Console.WriteLine("");
            }
        }

        public void game() {
            int[] lastpos = {player.x, player.y};
            while(true) {
                Console.Clear();
                Console.WriteLine($"Your pos: ({player.x}, {player.y})");
                this.render();
                Console.Write("Make a move (w, a, s, d) > ");
                string move = Console.ReadLine();
                if(move == "w") player.y -= 1;
                else if(move == "s") player.y += 1; 
                else if(move == "a") player.x -= 1;
                else if(move == "d") player.x += 1;
                // boundaries
                if(this.grid[player.y][player.x].state == "wall") {
                    player.x = lastpos[0];
                    player.y = lastpos[1];
                }
                this.grid[lastpos[1]][lastpos[0]].state = "empty";
                lastpos[0] = player.x;
                lastpos[1] = player.y;
            }
        }
    }
    public class Program {
        static void Main(String[] args) {
            Player player = new Player(1, 1);
            Board board = new Board(15, 15, 1, player);
            board.game();
        }
    }
}