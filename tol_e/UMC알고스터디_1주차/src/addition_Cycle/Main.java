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
			if(num < 10) //10보다 작으면 앞에 0 삽입
				ans = "0"+ans;
			
			int sum = (ans.charAt(0)-'0')+(ans.charAt(1)-'0'); //각 자리의 수 더하기
			String temp = Integer.toString(sum); //sum 문자열로 변환
			num = (ans.charAt(1)-'0')*10 + (temp.charAt(temp.length()-1)-'0'); //주어진 수의 맨 오른쪽, sum의 맨 오른쪽으로 수 생성
			ans = Integer.toString(num);	//새로 만들어진 수 문자열 변환
			count++;
		} while(!str.equals(ans));
		System.out.println(count);
	}
}
