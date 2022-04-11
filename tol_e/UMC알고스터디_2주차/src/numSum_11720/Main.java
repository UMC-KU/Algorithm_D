package numSum_11720;
import java.util.*;
public class Main {
    public static void main(String[] args){
        int length = 0, sum = 0;
        String numString = "";      
        Scanner scan = new Scanner(System.in);
        length = scan.nextInt();
        scan.nextLine();
        numString = scan.nextLine();
        
        for(int i = 0; i<length; i++)
            sum += (int)(numString.charAt(i)-'0');
        
        System.out.println(sum);
        scan.close();
    }
}
