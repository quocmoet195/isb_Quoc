import java.util.Random;

public class Main {
    /*
    Сгенерировать псевдослучайные последовательности с помощью языка Java.
    */
    public static void main(String[] args) {
        Random rand = new Random();
                int size = 128;
        int[] binarySequence = new int[size];
        for (int i = 0; i < size; ++i) {
            binarySequence[i] = rand.nextInt(2); 
            System.out.print(binarySequence[i]); 
        }
        System.out.println(); 
    }
}
//10000101011100011100100010010010110101110111100101000001010110000110111100100101101100101101100000010001100001110010110011001010