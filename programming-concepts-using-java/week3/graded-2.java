import java.util.*;

class Shape{
    public int area() {
        return 0;
    }
    public int volume() {
        return 0;
    }
}

class Rectangle extends Shape{
    private int w, h;
    //implement Rectangle class
    public Rectangle(int w, int h) {
        this.w = w;
        this.h = h;
    }
    public int area() {
        return this.w * this.h;
    }
}

class Cube extends Shape{
    private int a;
    //implement Cube class
    public Cube(int a) {
        this.a = a;
    }
    public int volume() {
        return (int) Math.pow(this.a, 3);
    }
}

class FClass{
    private static void caller(Shape s) {
        //check if s is of type Rectangle
        if (s instanceof Rectangle) {
            System.out.println(s.area());
        }
        //check if s is of type Cube
        if (s instanceof Cube) {
            System.out.println(s.volume());
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int w = sc.nextInt();
        int h = sc.nextInt();
        int a = sc.nextInt();
        caller(new Rectangle(w, h));
        caller(new Cube(a));
    }
}