package addition_Cycle;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String str = Integer.toString(n);
		
		int num = n;
		int count = 0;
		String ans = Integer.toString(num);
		do{
			if(num < 10) //10���� ������ �տ� 0 ����
				ans = "0"+ans;
			
			int sum = (ans.charAt(0)-'0')+(ans.charAt(1)-'0'); //�� �ڸ��� �� ���ϱ�
			String temp = Integer.toString(sum); //sum ���ڿ��� ��ȯ
			num = (ans.charAt(1)-'0')*10 + (temp.charAt(temp.length()-1)-'0'); //�־��� ���� �� ������, sum�� �� ���������� �� ����
			ans = Integer.toString(num);	//���� ������� �� ���ڿ� ��ȯ
			count++;
		} while(!str.equals(ans));
		System.out.println(count);
	}
}
