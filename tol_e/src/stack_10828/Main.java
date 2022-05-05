package stack_10828;

import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		Stack<Integer> stack = new Stack<Integer>();	// ������ �׾Ƴ��� ���� 
		int repeat = Integer.parseInt(br.readLine());	//�ݺ� Ƚ��

		for (int i = 0; i < repeat; i++) {
			String o = br.readLine();	//���
			String[] p = o.split(" ");	//���� ����� ���ڸ� ����
			if (p[0].equals("push")) {	//push : �߰�
				stack.push(Integer.parseInt(p[1]));
			} else if (o.equals("pop")) {	//pop : ���� (���ŵǴ� �� ����)
				try {						//try-catch�� ���� ���ÿ��� ����ó��
					bw.write(stack.pop() + "\n");
				} catch (EmptyStackException e) {
					bw.write("-1\n");
				}
			} else if (o.equals("size")) {	//size : ���� ������ ���
				bw.write(Integer.toString(stack.size()) + "\n");
			} else if (o.equals("empty")) {	//����ִ�?1:0
				if (stack.isEmpty()) {
					bw.write("1\n");
				} else {
					bw.write("0\n");
				}
			} else if (o.equals("top")) {	//���� ���� �ִ� (���������� �߰��� ��)
				try {						//try-catch�� ���� ���ÿ��� ����ó��
					bw.write(Integer.toString(stack.peek()) + "\n");
				} catch (EmptyStackException e) {
					bw.write("-1\n");
				}
			}
		}
		bw.flush();
		bw.close();
		br.close();
	}
}