/* 
 ���� ���� �ִ� ī�带 �ٴڿ� ������. �� ����, ���� ���� �ִ� ī�带 ���� �Ʒ��� �ִ� ī�� ������ �ű��
ī�� ��� N�� �־����� ��, ���� �������� ���� �Ǵ� ī��
 */
package card2_2164;
import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		
		Queue<Integer> q = new LinkedList<Integer>();
		for(int i = 0; i<n; i++) {
			q.add(i+1);		//1~n�� ������� ť�� ����	(����=1 / ��=n)
		}
		while(q.size() > 1) {//�� �� ���� ������ �ݺ�
			q.poll();		//ù�� ������
			q.add(q.poll());//�� ���� ù�� ���������� �ű��
		}
		bw.write(q.peek()+"");	//������ �� ���
		bw.flush();
		bw.close();
		br.close();
	}
}
