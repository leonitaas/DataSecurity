package DataSecurity.Polibius;
import java.util.Scanner;

public class Polibius_Cipher {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String x = "", y;
        System.out.println("Do you want to encrypt or decrypt ? E / D");
        y = scanner.next();
        while (!y.equals("E") && !y.equals("D")) {
            System.out.println("Wrong choice");
            System.out.print("Please enter again: ");
            y = scanner.next();
        }
        char key;

        for (int i = 0; i < 5; i++) {
            System.out.print("Enter the key, it can be letters or numbers: ");
            key = scanner.next().charAt(0);
            x += key;
        }
        /*Deklarimi i nje matrice 6x6 e cila kolonen e pare dhe rreshtin
         *e pare e ka te rezervuar per celesin qe e jep useri*/
        char[][] table = {
                {' ', x.charAt(0), x.charAt(1), x.charAt(2), x.charAt(3), x.charAt(4)},
                {x.charAt(0), 'A', 'B', 'C', 'D', 'E'},
                {x.charAt(1), 'F', 'G', 'H', 'I', 'K'},
                {x.charAt(2), 'L', 'M', 'N', 'O', 'P'},
                {x.charAt(3), 'Q', 'R', 'S', 'T', 'U'},
                {x.charAt(4), 'V', 'W', 'X', 'Y', 'Z'}
        };
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                System.out.print(table[i][j] + " ");
            }
            System.out.println();
        }
        if (y.equals("E")) {
            String plain_text, cipher = "";
            int len;
            System.out.print("Enter the plain text: ");
            scanner.nextLine();
            plain_text = scanner.nextLine();
            len = plain_text.length();
            plain_text = plain_text.toUpperCase();

            for(int n=0;n<len;n++){
                for(int i = 0; i < 6; i++){
                    for (int j = 0; j < 6; j++){
                        if(plain_text.charAt(n) == table[i][j]){
                            cipher += table[i][0];
                            cipher += table[0][j];
                        }
                    }
                }
            }
            System.out.println("Cipher text: " + cipher);
        }
        if(y.equals("D")){
            String cipher_text,plain ="";
            System.out.print("Please enter the cipher text: ");
            scanner.nextLine();
            cipher_text = scanner.nextLine();
            int size = cipher_text.length();
            for(int n=0;n<size;n+=2){
                for(int i = 0; i < 6; i++){
                    for(int j = 0; j < 6; j++){
                        if(cipher_text.charAt(n) == table[i][0] && cipher_text.charAt(n+1) == table[0][j]){
                            plain += table[i][j];
                        }
                    }
                }
            }
            System.out.println("Plain text: " + plain);
        }
    }
}
