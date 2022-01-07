import java.util.*;

class Employee {
    String eid;
    String ename;
    String eprojects[];
 //Define all the required methods here
    public Employee(String id, String name, String[] projects) {
        eid = id;
        ename = name;
        eprojects = projects;
    }
    public Employee(Employee other) {
        this(other.eid, other.ename, other.eprojects.clone());
    }
    public void display() {
        System.out.println("id:" + eid);
        System.out.println("name:" + ename);
        System.out.println("projects:");
        for (String s: eprojects) {
            System.out.print(s+":");
        }
    }
    public void mutator() {
            this.ename = "Mr "+ this.ename;
            this.eprojects[0] = null;
    }
    
}

public class FClass {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
    	String project[] = {"P001","P002","P003"};
        //Enter the id of employee
        String id = s.nextLine();
        //Enter the name of employee
        String name = s.nextLine();
        
        Employee e1 = new Employee(id,name,project);
        Employee e2 = new Employee(e1); 
        //The copy constructor must copy all the data members. 
       
        e1.mutator();
        
        e2.display();
    }
}