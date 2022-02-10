import java.util.*;

public class Test3 {
    public static boolean balanceCheck(String sequence) {
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < sequence.length(); i++) {
            Character c = sequence.charAt(i);
            // if not a bracket
            if (!(c == '{' || c == '}' || c == '(' || c == ')' || c == '[' || c == ']')) {
                continue;
            }
            // opening bracket
            if (c=='{' || c=='[' || c=='(') {
                stack.push(c);
            }
            // closing bracket
            else {
                if (stack.empty()) {
                    return false;
                }
                Character p = stack.pop();
                if (c == '}') {
                    if (p != '{') {return false;}
                }
                if (c == ')') {
                    if (p != '(') {return false;}
                }
                if (c == ']') {
                    if (p != '[') {return false;}
                }
            }
        }
        return stack.empty();
    }
   
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        
        ArrayList<String> expr_arr= new ArrayList<String>();
        String inp=null;
        
        do {
            inp = s.nextLine();
            if (!inp.equalsIgnoreCase("Done"))
                expr_arr.add(inp);
        } while (!inp.equalsIgnoreCase("Done"));

        for (String expr : expr_arr) {
            if (balanceCheck(expr)) {
                System.out.println("Balanced");
            } else {
                System.out.println("Not Balanced");
            }
        }
    }
}