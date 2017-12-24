package problems;

class Solution {
    public boolean judgeCircle(String moves) {
        int final_xloc = 0;
        int final_yloc = 0;
        for (char ch: moves.toCharArray()) {
            if (ch == 'U')
                final_yloc += 1;
            else if (ch == 'D')
                final_yloc -= 1;
            else if (ch == 'L')
                final_xloc -= 1;
            else if (ch == 'R')
                final_xloc += 1;
            else
                System.out.println("Not a valid direction.");
        }
        if (final_xloc == 0 && final_yloc == 0)
            return true;
        else
            return false;
    }
}
