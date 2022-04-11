//�Ƹ������׳׽��� ä
package prime_LCM;
import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long ans = 1; //�� < 2^63
		int max = 0;
		int[] a = new int[n];
		for(int i = 0; i<n; i++) {
			int num = sc.nextInt();
			if(max < num) max = num;
			a[i] = num;
		}
		
		int[] arr = new int[max+1];		//�Ƹ������׳׽��� ü
		for(int i = 2; i<=max; i++) {	
			for(int j = 1; i*j<=max; j++) {
				arr[i*j]++;				//����� ������ŭ ����
			}
		}
		
		for(int i:a){
			if(arr[i]++ == 1) {			//�Ҽ��� �ѹ��̻� ������ ����
				ans *= i;
				
			}
		}
		System.out.println((ans == 1)?-1:ans);
	}
}
