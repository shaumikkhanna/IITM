import java.util.*;
public class SeriesSum {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
//Fill your code here
    int sum = 0;
    for (int i = 1; i <= n; i++) {
      sum += i*(i+1)*(2*i+1) / 6;
    }
    System.out.println(sum);
    
  }
}