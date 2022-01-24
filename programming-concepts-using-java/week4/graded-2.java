import java.util.*;

interface Iterator{
    public boolean has_next();
    public Object get_next();
}

class Sequence{
    private final int maxLimit = 80;
    private SeqIterator _iter = null;
    int[] iArr; 
    int size;

    static int current_index = 0;
    //implement the parameterized constructor to initialize size
    public Sequence(int n) {
        size = n;
        iArr = new int[n];
    }
    //implement addTo(elem) to add an int elem to the sequence 
    public void addTo(int k) {
        iArr[current_index] = k;
        current_index++;
    }

    //implement get_Iterator() to return Iterator object
    public Iterator get_Iterator() {
        _iter = new SeqIterator();
        return _iter;
    }

    private class SeqIterator implements Iterator{
        int indx;
        public SeqIterator(){
            indx = -1;
        }
        //implement has_next()
        public boolean has_next() {
            return indx < size-1;
        }
        //implement get_next()
        public Object get_next() {
            indx++;
            return iArr[indx];
        }
    }
}

class FClass{
    public static void main(String[] args) {
        Sequence sObj = new Sequence(5);
        Scanner sc = new Scanner(System.in); 
        for(int i = 0; i < 5; i++) {
            sObj.addTo(sc.nextInt());
        }
        Iterator i = sObj.get_Iterator();
        while(i.has_next())
            System.out.print(i.get_next() + ", ");
    }
}