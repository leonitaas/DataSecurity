package DataSecurity;
import java.util.Scanner;

public class Polibius_Cipher {
    public static void main(String[] args) {
        Scanner scanner= new Scanner(System.in);
        String x = " ", y;
        System.out.println("Do you want to encrypt or decrypt ? E / D");
        y=scanner.next();
        while(!y.equals("E") && !y.equals("D")){
            System.out.println("Wrong choice!");
            System.out.println("Please choose again: ");
            y=scanner.next();
        }
        char key;
        for(int i=0; i < 5; i++){
            System.out.println("Enter the key please: ");
            key = scanner.next().charAt(0);
            x +=key;
        }
        char[][] table = {
                {' ', x.charAt(0), x.charAt(1), x.charAt(2), x.charAt(3), x.charAt(4)},
                {x.charAt(0), 'A', 'B', 'C', 'D', 'E'},
                {x.charAt(1), 'F', 'G', 'H', 'I', 'K'},
                {x.charAt(2), 'L', 'M', 'N', 'O', 'P'},
                {x.charAt(3), 'Q', 'R', 'S', 'T', 'U'},
                {x.charAt(4), 'V', 'W', 'X', 'Y', 'Z'}
        };
        for(int i=0;i< 6; i++){
            for(int j=0; j< 6; j++){
                System.out.print(table[i][j]+ " ");
            }
            System.out.println();
        }
        if(y.equals("E")){
            String plain_text, cipher = "";
            int len;
            System.out.println("Please enter the plain text: ");
            scanner.nextLine();
            plain_text=scanner.nextLine();
            len = plain_text.length();
            plain_text=plain_text.toUpperCase();
        }
    }
}
