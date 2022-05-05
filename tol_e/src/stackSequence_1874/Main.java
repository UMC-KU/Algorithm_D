package stackSequence_1874;

import java.util.*;
import java.io.*;
public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine()); //������ ����
		int[] arr = new int[n];
		for(int i = 0 ; i<n; i++) arr[i] = Integer.parseInt(br.readLine());
		Stack<Integer> seq = new Stack<>(); //����
		Stack<String> sign = new Stack<>(); //+ - ������ �����ϴ� ����
		int max = n; //���ÿ��� �����ϴ� ��, ���� ������ �����ִ� �� �� ���� ū ��
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
