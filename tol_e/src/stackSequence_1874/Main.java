package stackSequence_1874;

import java.util.*;
import java.io.*;
public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine()); //수열의 길이
		int[] arr = new int[n];
		for(int i = 0 ; i<n; i++) arr[i] = Integer.parseInt(br.readLine());
		Stack<Integer> seq = new Stack<>(); //수열
		Stack<String> sign = new Stack<>(); //+ - 사인을 저장하는 스택
		int max = n; //스택에서 빼야하는 수, 현재 수열에 남아있는 수 중 가장 큰 수
		for(int i = arr.length-1; i>=0; i--) {
			if(arr[i] == max) {
				sign.add("+\n-");
				max--;
				while(!seq.empty() && seq.peek().intValue() == max) {
					seq.pop();
					sign.add("+");
					max--;
				}
			} else {
				seq.add(arr[i]);
				sign.add("-");
			}
		}
		if(seq.empty()) 
			while(!sign.empty()) bw.write(sign.pop()+"\n");
		else
			bw.write("NO");
		bw.flush();
		br.close();
		bw.close();
	}
}
