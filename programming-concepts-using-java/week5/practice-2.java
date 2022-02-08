import java.util.Scanner;


class ConvertArrays {
    public Double doubleArr[]=new Double[3];
    public Integer intArr[]=new Integer[3];
    public int x=0,y=0,z=0;
    
    public void convert(String[] arr){
        //loop through the arr and store each element 
        //in the appropriate array
        Double temp_double;
        Integer temp_int;
        for (String s : arr) {
            try {
                temp_int = Integer.parseInt(s);
                intArr[y] = temp_int;
                y++;
            } catch (Exception e) {
                temp_double = Double.parseDouble(s);
                doubleArr[x] = temp_double;
                x++;
            }
        }
    }
    
    public <T> void display(T[] arr){
        for(T elements:arr) {
        System.out.print(elements+" ");
        System.out.println();
        }
    }
}

public class Programming {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        String arr[]= new String[6];
        for (int i = 0; i < arr.length; i++) {
            arr[i]=scanner.next();
        }
        ConvertArrays conArrays=new ConvertArrays();
        conArrays.convert(arr);
        System.out.println("===After conversion Arrays===");
        conArrays.display(conArrays.doubleArr);
        conArrays.display(conArrays.intArr);        
    }
}
