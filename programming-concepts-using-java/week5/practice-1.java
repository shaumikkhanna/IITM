import java.lang.reflect.*;
import java.util.*;


class ClassStats {
    public static int getPubMethodCount(String cname) {
        try {
            //add code to return the count of 
            //public methods in the given class	
            Class c = Class.forName(cname);
            return c.getMethods().length;	
        } catch (Exception e) { return -1; }
    }
    public static int getAllMethodCount(String cname) {
        try {
            //add code to return the count of all 
            //declared methods in the given class
            Class c = Class.forName(cname);
            return c.getDeclaredMethods().length;	
        } catch (Exception e) { return -1; }
    }
    public static int getPubFieldCount(String cname) {
        try {
            //add code to return the count of 
            //public fields (instance variables) in the given class
            Class c = Class.forName(cname);
            return c.getFields().length;
        } catch (Exception e) { return -1; }
    }
    public static int getAllFieldCount(String cname) {
        try {
            //add code to return the count of 
            //all fields (instance variables) in the given class
            Class c = Class.forName(cname);
            return c.getDeclaredFields().length;
        } catch (Exception e) { return -1; }
    }
    public static int getPubContCount(String cname) {
        try {
            //add code to return the count of 
            //public constructors in the given class
            Class c = Class.forName(cname);
            return c.getConstructors().length;
        } catch (Exception e) { return -1; }		
    }
    public static int getAllContCount(String cname) {
        try {
            //add code to return the count of 
            //all constructors in the given class
            Class c = Class.forName(cname);
            return c.getDeclaredConstructors().length;
        } catch (Exception e) { return -1; }
    }
}

class FClass {
    public static void main(String[] args) {
        String cname;
        Scanner sc = new Scanner(System.in);
        cname = sc.nextLine();
        System.out.println("Constructor: " + 
                        ClassStats.getPubContCount(cname) + ", " + 
                        ClassStats.getAllContCount(cname));
        System.out.println("Fields: " + 
                        ClassStats.getPubFieldCount(cname) + ", " +
                        ClassStats.getAllFieldCount(cname));
        System.out.println("Methods: " + 
                        ClassStats.getPubMethodCount(cname) + ", " +
                        ClassStats.getAllMethodCount(cname));
    }
}